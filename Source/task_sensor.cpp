//**************************************************************************************
/** \file task_sensor.cpp
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
#include "task_sensor.h"                      // Header for this file


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

task_sensor::task_sensor (const char* a_name, 
					  unsigned portBASE_TYPE a_priority, 
					  size_t a_stack_size,
					  emstream* p_ser_dev,
					  SBG01* sbg01
					 )
	: frt_task (a_name, a_priority, a_stack_size, p_ser_dev), sbg01(sbg01)
{
	task_name = a_name;
	sensor_delay.put(3000);
    node = 0;
	
}


//-------------------------------------------------------------------------------------
/** This task interacts with the user for force him/her to do what he/she is told. It
 *  is just following the modern government model of "This is the land of the free...
 *  free to do exactly what you're told." 
 */

void task_sensor::run (void)
{
	char char_in;                           // Character read from serial device
	time_stamp a_time;                      // Holds the time so it can be displayed
	portTickType previous_ticks;
	sensor_complete.put(false);
	transition_to(2);
	

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
			    //*p_serial << task_name << PMS ("S0") << endl;
			
			    if(initialization_complete.get())
				{
					*p_serial << PMS ("Sensor initialized.") << endl;
					transition_to(1);
				}
			
			    break;
			
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In state 1, the motor is powered CW in order to zero it at the origin in 
			// in conjunction with a limit switch.
			case (1):
				
				if(xmotor_complete.get() && ymotor_complete.get() && zmotor_complete.get())
				{
                    *p_serial <<  "Sensor Reading " << node+1 << " (Delay = " << sensor_delay.get() << " ms)" << endl;
					transition_to(2);
				}
				
				break;
				

			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In state 2, the motor is returning to the origin and waiting for the limit 
			// switch to power it off.
			case (2):
				
				//tsensor_delay = sensor_delay.get();
				//previous_ticks = xTaskGetTickCount();
				//delay_from_to_ms(previous_ticks, sensor_delay.get());
				
				//heat_flux.put(sbg01->get_heat_flux());
				//heat_flux.put(sbg01->get_voltage_bits());
				
				//sensor_complete.put(true);
				//xmotor_complete.put(false);
				//ymotor_complete.put(false);
				//zmotor_complete.put(false);

				*p_serial << PMS ("Sensor Reading: ")  << sbg01->get_voltage() << PMS (" kW/m^2") <<  endl;
                //*p_serial << PMS ("Sensor Reading: ")  << heat_flux.get() << PMS (" kW/m^2") <<  endl;
				//node++;
				//transition_to(1);
				
				break; // End of state 1
			

		} // End switch state

		runs++;                             // Increment counter for debugging

		// No matter the state, wait for approximately a millisecond before we 
		// run the loop again. This gives lower priority tasks a chance to run
		vTaskDelay (configMS_TO_TICKS (1000));
	}
}
