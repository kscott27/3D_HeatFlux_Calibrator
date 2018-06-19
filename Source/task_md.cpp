//**************************************************************************************
/** \file task_user.cpp
 *    This file contains source code for a user interface task for a ME405/FreeRTOS
 *    test suite. 
 *
 *  Revisions:
 *    \li 09-30-2012 JRR Original file was a one-file demonstration with two tasks
 *    \li 10-05-2012 JRR Split into multiple files, one for each task
 *    \li 10-25-2012 JRR Changed to a more fully C++ version with class task_user
 *    \li 11-04-2012 JRR Modified from the data acquisition example to the test suite
 *
 *  License:
 *    This file is copyright 2012 by JR Ridgely and released under the Lesser GNU 
 *    Public License, version 2. It intended for educational use only, but its use
 *    is not limited thereto. */
/*    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
 *    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
 *    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
 *    ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
 *    LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUEN-
 *    TIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS 
 *    OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
 *    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
 *    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
 *    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. */
//**************************************************************************************

#include <avr/io.h>                         // Port I/O for SFR's
#include <avr/wdt.h>                        // Watchdog timer header

#include "shared_data_sender.h"
#include "shared_data_receiver.h"
#include "task_md.h"                      // Header for this file


/** This constant sets how many RTOS ticks the task delays if the user's not talking.
 *  The duration is calculated to be about 5 ms.
 */
const portTickType ticks_to_delay = ((configTICK_RATE_HZ / 1000) * 5);


//-------------------------------------------------------------------------------------
/** This constructor creates a new motor driver task. Its main job is to call the
 *  parent class's constructor which does most of the work.
 *  @param a_name A character string which will be the name of this task
 *  @param a_priority The priority at which this task will initially run (default: 0)
 *  @param a_stack_size The size of this task's stack in bytes 
 *                      (default: configMINIMAL_STACK_SIZE)
 *  @param p_ser_dev Pointer to a serial device (port, radio, SD card, etc.) which can
 *                   be used by this task to communicate (default: NULL)
 */

task_md::task_md (const char* a_name,
unsigned portBASE_TYPE a_priority,
size_t a_stack_size,
emstream* p_ser_dev, DM542T* md,  
LimitSwitch* LS_min, LimitSwitch* LS_max,
frt_queue<uint32_t>* locations,
frt_queue<uint32_t>* max_velocity,
shared_data<uint8_t>* motor_operator,
shared_data<bool>* motor_complete,
uint16_t microstep_scaler
)
: frt_task (a_name, a_priority, a_stack_size, p_ser_dev),
task_name(a_name), md(md),
LS_min(LS_min), LS_max(LS_max),
locations(locations),
max_velocity(max_velocity),
motor_operator(motor_operator),
motor_complete(motor_complete),
microstep_scaler(microstep_scaler)
{
	float turns_per_inch;
	turns_per_inch = 3;
	inch_to_step = 200 * turns_per_inch * microstep_scaler;
	step_to_inch = 1 / inch_to_step;
}


//-------------------------------------------------------------------------------------
/** This task interacts with the motor driver object in order to control the motors
 *  in ways specified by the user.
 */

void task_md::run (void)
{
	char char_in;                           // Character read from serial device
	time_stamp a_time;                      // Holds the time so it can be displayed
	portTickType previous_ticks;
	uint16_t delay_counter = 0;
	uint16_t state_delay_counter = 0;
	

	// This is an infinite loop; it runs until the power is turned off. There is one 
	// such loop inside the code for each task
	for (;;)
	{
		//if (++state_delay_counter == 75)
		//{
			//*p_serial << task_name << state << endl;
			//state_delay_counter = 0;
		//}
		
		// Run the finite state machine. The variable 'state' is kept by the parent class
		switch (state)
		{
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In state 0, the motor task is powered CW back to the origin location in order
			// to get a starting location for all subsequent steps.
			case (0):
			
				motor_operator->put(2);
				transition_to(3);
			
			    break;
			
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In state 1, the motor is returning to the origin and waiting for the limit
			// switch to power it off.
			case (1):
				
				md->ramp_ctrl();
				
                if (md->get_status())
				{
					motor_operator->put(0);
					*p_serial << PMS ("S2") << endl;
					transition_to(2);
				}
				
				break;
				

			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In state 2, the motor is idle - waiting for a command to switch it into 
			// a certain mode.
			case (2):
				//*p_serial << task_name << PMS ("S2") << endl;
				if(direct_mode.get())
				{
					transition_to(3);
				}
				else if(coordinate_mode.get())
				{
					transition_to(5);
				}
				else if(incremental_mode.get())
				{
					transition_to(5);
				}
				break;
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
			// In State 3, the motor is in the off state of direct operation mode.	
			case (3):
			    
				if (motor_operator->get() == 1)
				{
					md->motorCCW();
					md->set_ramp_ctrl(500, gen_max_v.get(), ramp_run_span.get());
					motor_on = motorOn();
					if (motor_on)
					{
						transition_to(4);
					}
					else
					{
						motor_operator->put(0);
						transition_to(2);
					}
				}
				else if (motor_operator->get() == 2)
				{
					md->motorCW();
					md->set_ramp_ctrl(500, gen_max_v.get(), ramp_run_span.get());
					motor_on = motorOn();
					if (motor_on)
					{
						transition_to(4);
					}	
					else
					{
						motor_operator->put(0);
						transition_to(2);
					}	
				}
				else
				{
					transition_to(2);
				}
							
				break;
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In State 4, the motor is enabled, waiting for a stop command.
			case (4):
								
				md->ramp_ctrl();
				
				if(md->get_status() == false)
				{
					motor_operator->put(0);
				}
				
			    if(motor_operator->get() == 0)
				{
					md->motorOff();
					*p_serial << task_name << PMS ("loc:") << md->get_steps() << endl;
					*p_serial << task_name << PMS ("S") << endl;
					transition_to(2);
				}
				
				if (++delay_counter == 5)
				{
					*p_serial << task_name << PMS ("loc:") << md->get_steps() << endl;
					delay_counter = 0;
				}
				
				break;
			
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In State 5, the motor is disabled, and awaits a signal from the sensor before
			// it begins calculating its operation parameters to reach the next destination.	
			case (5):
							
				if (!(coordinate_mode.get()) && !(incremental_mode.get()))
				{
					transition_to(2);
				}	
				else if(next_node.get())
				{
					transition_to(6);
				}
				 
				break;
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In State 6, the motor is calculating how many steps it must take to reach 
			// the desired node.
			case (6):
			    
				steps = md->get_steps();
				step_destination = locations->get();
				
				//*p_serial << max_velocity->get() << endl;
							
				if (steps < step_destination)
				{
					md->motorCCW();
					md->set_ramp_ctrl(500, max_velocity->get(), ramp_run_span.get());
					//if (drawing_mode.get())
					//{
						//md->set_ramp_ctrl(500, max_velocity->get(), ramp_run_span.get());
					//}
					//else
					//{
						//md->set_ramp_ctrl(500, gen_max_v.get(), ramp_run_span.get());
					//}		
					motorOn();
				}
				else if (steps > step_destination)
				{
					md->motorCW();
					md->set_ramp_ctrl(500, max_velocity->get(), ramp_run_span.get());
					//if (drawing_mode.get())
					//{
						//md->set_ramp_ctrl(500, max_velocity->get(), ramp_run_span.get());
					//}
					//else
					//{
						//md->set_ramp_ctrl(500, gen_max_v.get(), ramp_run_span.get());
					//}
					motorOn();
				}
				
				transition_to(7); 
				
				break;
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In State 7, the motor is enabled until it reaches its destination.
			case (7):
			
				if (pause.get())
				{
					md->motorOff();
					transition_to(8);
				}
				
				md->ramp_ctrl();
			    
			    if(md->get_direction() == 0)
				{
					if(md->get_steps() >= step_destination)
					{
						md->motorOff();
						*p_serial << task_name << PMS ("S") << endl;
						*p_serial << task_name << PMS ("loc:") << md->get_steps() << endl;
						motor_complete->put(true);
						next_node.put(false);
						transition_to(5);
					}
				}
				else if(md->get_direction() == 1)
				{
					if(md->get_steps() <= step_destination)
					{
						md->motorOff();
						*p_serial << task_name << PMS ("S") << endl;
						*p_serial << task_name << PMS ("loc:") << md->get_steps() << endl;
						motor_complete->put(true);
						next_node.put(false);
						transition_to(5);

					}
				}
				
				if (++delay_counter == 5)
				{
					*p_serial << task_name << PMS ("loc:") << md->get_steps() << endl;
					delay_counter = 0;
				}
				
				break;	
				
			case (8):
			
				if(!(pause.get()))
				{
					motorOn();
					transition_to(7);
				}
				
				break;


		} // End switch state

		runs++;                             // Increment counter for debugging

		// No matter the state, wait for approximately a millisecond before we 
		// run the loop again. This gives lower priority tasks a chance to run
		vTaskDelay (configMS_TO_TICKS (20));
	}
}

void task_md::take_step (void)
{
	md->take_step();
}

void task_md::set_signal_low(void)
{
	md->set_signal_low();
}

void task_md::motorOff(void)
{
	md->motorOff();
	if(coordinate_mode.get() && (LS_min->get_status() || LS_max->get_status()))
	{
		reset_device();
	}
}

bool task_md::motorOn(void)
{
	if (md->get_direction() == 0)
	{
		if (!(LS_max->get_status()))
		{
			md->motorOn();
			*p_serial << task_name << PMS ("F") << endl;
			return true;
		}
		else
		{
			return false;
		}
	}
	else
	{
		if (!(LS_min->get_status()))
		{
			md->motorOn();
			*p_serial << task_name << PMS ("R") << endl;
			return true;
		}
		else
		{
			return false;
		}
	}
}

//bool task_md::motorOn(void)
//{
	//if (md->get_direction() == 0)
	//{
		//md->motorOn();
		//*p_serial << task_name << PMS ("F") << endl;
		//return true;
	//}
	//else
	//{
		//md->motorOn();
		//*p_serial << task_name << PMS ("R") << endl;
		//return true;
	//}
//}

void task_md::reset_device(void)
{
	*p_serial << PMS ("Resetting device.") << endl;
	wdt_enable (WDTO_120MS);
	for (;;);	
}

