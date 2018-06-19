//**************************************************************************************
/** \file task_sensor.cpp
 *    This file contains source code for a heat flux gauge task for a ME405/FreeRTOS
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
}


//-------------------------------------------------------------------------------------
/** This task interacts with the heat flux sensor in order to capture readings and relay
 *  that data to the user interface task.
 */

void task_sensor::run (void)
{
	char char_in;                           // Character read from serial device
	time_stamp a_time;                      // Holds the time so it can be displayed
	portTickType previous_ticks;
	//float sensor_readings[sensor_sample_number.get()];
	samples_taken = 0;
	sample_sum = 0;
	sensor_complete.put(false);
	

	// This is an infinite loop; it runs until the power is turned off. There is one 
	// such loop inside the code for each task
	for (;;)
	{
		// Run the finite state machine. The variable 'state' is kept by the parent class
		switch (state)
		{
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In state 0, the sensor task is waiting for the device to enter a certain mode.
			case (0):
		
				//*p_serial << sbg01->get_voltage_mv() <<  endl;
				if (sensor_reading.get())
				{
					sample_sum = 0;
					samples_taken = 0;
					transition_to(3);
				}
				else if(coordinate_mode.get() || incremental_mode.get())
				{
					sample_sum = 0;
					samples_taken = 0;
					current_node = 0;
					transition_to(1);
				}
			
			    break;			

			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In state 1, the device is in coordinate mode, so the sensor will only take readings
			// after the set delay time has elapsed while the sensor is in the proper position.
			case (1):
			
			if(xmotor_complete.get() && ymotor_complete.get() && zmotor_complete.get())
			{
				if (incremental_mode.get())
				{
					incremental_mode.put(false);
					next_node.put(true);
					sensor_reading.put(false);
					xmotor_complete.put(false);
					ymotor_complete.put(false);
					zmotor_complete.put(false);
					transition_to(0);
				}
				else if (drawing_mode.get())
				{
					next_node.put(true);
					sensor_reading.put(false);
					xmotor_complete.put(false);
					ymotor_complete.put(false);
					zmotor_complete.put(false);
				}
				else
				{
					sensor_reading.put(true);
					*p_serial <<  PMS ("Sensor Reading ") << ++current_node << " (Delay = " << sensor_delay.get() << " ms)" << endl;
					node++;
					previous_ticks = xTaskGetTickCount();
					delay_from_to_ms(previous_ticks, sensor_delay.get());
					transition_to(2);
				}	
			}
			//if (!coordinate_mode.get())
			//{
				//transition_to(0);
			//}
			
			break;
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In state 3, the device has waited for the heat flux gage to get a steady reading, and will
			// now take a number of samples to be averaged and then sent back to the interface.
			case (2):
									
			if(samples_taken < sensor_sample_number.get())
			{
				//sensor_readings[samples_taken] = sbg01->get_voltage_mv();
				sample_sum += sbg01->get_voltage_mv();
				samples_taken++;
			}
			else
			{
				heat_flux.put(sample_sum/sensor_sample_number.get());
				*p_serial << PMS ("HF:") << heat_flux.get()*6.289 << endl;
				*p_serial << PMS ("mV:") << heat_flux.get() << endl;
				//*p_serial << PMS ("Sample std dev: ") << get_std_dev(heat_flux.get(), sensor_sample_number.get(), sensor_readings) << endl;
				sample_sum = 0;
				samples_taken = 0;
				if (current_node < total_nodes.get())
				{
					next_node.put(true);
					sensor_reading.put(false);
					xmotor_complete.put(false);
					ymotor_complete.put(false);
					zmotor_complete.put(false);
					transition_to(1);
				}
				else
				{
					*p_serial << PMS ("Routine complete.") << endl;	
					transition_to(0);
					coordinate_mode.put(false);
					*p_serial << PMS ("C") << endl;
					next_node.put(false);
					sensor_reading.put(false);
					xmotor_complete.put(false);
					ymotor_complete.put(false);
					zmotor_complete.put(false);
					//previous_ticks = xTaskGetTickCount();
					//delay_from_to_ms(previous_ticks, 3000);
					//reset_device();
				}
				
			}
			
			break;
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In state 4, the interface has requested a sensor reading. The ADC will sample
			// a set number of readings and then take the average and send the result back
			// over serial.
			case (3):
			
			if(samples_taken < sensor_sample_number.get())
			{
				sample_sum += sbg01->get_voltage_mv();
				samples_taken++;
			}
			else
			{
				heat_flux.put(sample_sum/sensor_sample_number.get());
				*p_serial << PMS ("HF:") << heat_flux.get()*6.289 << endl;
				*p_serial << PMS ("mV:") << heat_flux.get() << endl;
				//*p_serial << PMS ("Sample std dev: ") << get_std_dev(heat_flux.get(), sensor_sample_number.get(), sensor_readings) << endl;
				sample_sum = 0;
				samples_taken = 0;
				sensor_reading.put(false);
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

float task_sensor::get_std_dev(float mean, uint32_t n, float* data)
{
	float variance = 0;
	float std_dev = 0;
	for (uint16_t i=0; i<n; i++)
	{
		variance += pow((data[i] - mean), 2);
	}
	std_dev = pow((variance / (n - 1)), 0.5);
	return std_dev;
}

void task_sensor::reset_device(void)
{
	*p_serial << PMS ("Resetting device.") << endl;
	wdt_enable (WDTO_120MS);
	for (;;);
}
