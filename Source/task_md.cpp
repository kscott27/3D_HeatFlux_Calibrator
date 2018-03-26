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
/** This constructor creates a new data acquisition task. Its main job is to call the
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
					  emstream* p_ser_dev, DM542T* c_md,
					  Timer* ctimer, 
					  shared_data<uint8_t>* cmotor_on,
					  shared_data<bool>* cmotor_complete,
					  uint16_t cmicrostep_scaler
					 )
	: frt_task (a_name, a_priority, a_stack_size, p_ser_dev)
{
    task_name = a_name;

	md = c_md;
	timer = ctimer;
	microstep_scaler.put(cmicrostep_scaler);
	motor_complete = cmotor_complete;
	pmotor_on = cmotor_on;
	steps = 0;
    float turns_per_inch;
    turns_per_inch = 3.22;
    inch_to_step = 200 * turns_per_inch * cmicrostep_scaler;
}


//-------------------------------------------------------------------------------------
/** This task interacts with the user for force him/her to do what he/she is told. It
 *  is just following the modern government model of "This is the land of the free...
 *  free to do exactly what you're told." 
 */

void task_md::run (void)
{
	char char_in;                           // Character read from serial device
	time_stamp a_time;                      // Holds the time so it can be displayed
	portTickType previous_ticks;
	

	// This is an infinite loop; it runs until the power is turned off. There is one 
	// such loop inside the code for each task
	for (;;)
	{
		// Run the finite state machine. The variable 'state' is kept by the parent class
		switch (state)
		{
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In state 0, the motor task is waiting for the user to enter data before 
			// proceeding to its routine.
			case (0):
			
                //*p_serial << PMS ("MD S0") << endl;
			    if(initialization_complete.get())
				{
					transition_to(3);
				}
				if(pmotor_on->get() == 1)
				{
					//*p_serial << endl << task_name << PMS (" activated forward. Press Ctrl-S to stop.") << endl;
					*p_serial << task_name << PMS ("F") << endl;
					md->motorCCW();
					md->motorOn();
					transition_to(6);
				}
				if(pmotor_on->get() == 2)
				{
					//*p_serial << endl << task_name << PMS (" activated in reverse. Press Ctrl-S to stop.") << endl;
					*p_serial << task_name << PMS ("R") << endl;
					md->motorCW();
					md->motorOn();
					transition_to(7);
				}
			
			    break;
			
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In state 1, the motor is powered CW in order to zero it at the origin in 
			// in conjunction with a limit switch.
			case (1):
				
                //*p_serial << PMS ("MD S1") << endl;
				md->motorCW();
				transition_to(2);
				
				break;
				

			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In state 2, the motor is returning to the origin and waiting for the limit 
			// switch to power it off.
			case (2):
				//*p_serial << PMS ("MD S2") << endl;
				if(steps == 0)
				{
					transition_to(3);
				}
				
				break; // End of state 1
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
			// In State 3, the motor calculates how long and in which direction it needs to
			// be activated in order to reach its next desired location.	
			case (3):
			    
				motor_complete->put(false);
				sensor_complete.put(false);
				if(task_name == "MDX" && xlocations.not_empty())
				{
					current_destination = xlocations.get();
					transition_to(4);
				}
				if(task_name == "MDY" && ylocations.not_empty())
				{
					current_destination = ylocations.get();
					transition_to(4);
				}
				if(task_name == "MDZ" && zlocations.not_empty())
				{
					current_destination = zlocations.get();
					transition_to(4);
				}
				step_diff = current_destination*inch_to_step - steps;
				travel_time_ms = abs((step_diff) / (timer->get_freq_khz()));
							
				break;
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In State 4, the motor performs its action for the calculated
			// amount of time, and then shuts off and signals that it has reached its
			// destination.	
			case (4):
			    if(step_diff < 0)
				{
					md->motorCW();
					md->motorOn();
					//*p_serial << task_name << PMS(" traveling backward to ") << current_destination << PMS(" inches: travel time = ") << travel_time_ms << PMS(" ms.") << endl;
					*p_serial << task_name << PMS ("R") << endl;
				}
				else if(step_diff > 0)
				{
					md->motorCCW();
					md->motorOn();
					//*p_serial << task_name << PMS(" traveling forward to ") << current_destination << PMS(" inches: travel time = ") << travel_time_ms << PMS(" ms.") << endl;
					*p_serial << task_name << PMS ("F") << endl;
				}
				
				previous_ticks = xTaskGetTickCount();
				delay_from_to_ms(previous_ticks, travel_time_ms);
				md->motorOff();
				
                step_diff = 0;
				steps = current_destination*inch_to_step;
				motor_complete->put(true);

				//*p_serial << task_name << PMS (" off. Steps = ") << steps << endl;
				*p_serial << task_name << PMS ("S") << endl;

				transition_to(5);
				
				break;
			
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In State 5, the motor is disabled, and awaits a signal from the sensor before
			// it begins calculating its operation parameters to reach the next destination.	
			case (5):
			    //*p_serial << task_name << motor_complete->get() << endl;
			    if(sensor_complete.get())
				{				
					node_number++;
					transition_to(3);	
				}
				
				break;
				
			case (6):
			    
			    if(pmotor_on->get() == 0)
				{
					md->motorOff();
					//*p_serial << endl << task_name << PMS (" stopped.") << endl;
					*p_serial << task_name << PMS ("S") << endl;
					transition_to(0);
				}
				
				break;
				
			case (7):
			    
			    if(pmotor_on->get() == 0)
				{
					md->motorOff();
					//*p_serial << endl << task_name << PMS (" stopped.") << endl;
					*p_serial << task_name << PMS ("S") << endl;
					transition_to(0);
				}
				
				break;


		} // End switch state

		runs++;                             // Increment counter for debugging

		// No matter the state, wait for approximately a millisecond before we 
		// run the loop again. This gives lower priority tasks a chance to run
		vTaskDelay (configMS_TO_TICKS (1));
	}
}
