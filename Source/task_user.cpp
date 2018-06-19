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
#include "task_user.h"                      // Header for this file


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

task_user::task_user (const char* a_name, 
					  unsigned portBASE_TYPE a_priority, 
					  size_t a_stack_size,
					  emstream* p_ser_dev
					 )
	: frt_task (a_name, a_priority, a_stack_size, p_ser_dev), task_name(a_name)
{
	atoi_index = 0;
}

uint32_t task_user::str_to_int(void)
{
	uint32_t conv_int = 0;
	for(uint8_t i=0; i < atoi_index-1; i++)
	{
		conv_int = conv_int * 10;
		conv_int = conv_int + (atoi_buf[i]-48);		
	}
	return (conv_int);
}

void task_user::print_main_menu(void)
{
	// Tell the user how to get into command mode (state 1), where the user interface
	// task does interesting things such as diagnostic printouts
	*p_serial << PMS ("Welcome to the User Interface main menu of the 3D Heat Flux Calibrator.") << endl;
	*p_serial << PMS ("Press A for Configuration Mode.") << endl;
	*p_serial << PMS ("Press C for Coordinate Mode.") << endl;
	*p_serial << PMS ("Press D for Direct Operation Mode.") << endl;
	*p_serial << PMS ("Press R to reset the device.") << endl;
}

void task_user::print_config_mode_menu(void)
{
	*p_serial << endl << PMS ("Entering Configuration Mode.") << endl;
	*p_serial << PMS ("Press U to change the default motor microstep scaler.") << endl;
	*p_serial << PMS ("Press S to change the default sensor reading delay time.") << endl;
	*p_serial << PMS ("Press Z to return the device to the origin.") << endl;
	*p_serial << PMS ("Press R to reset the device.") << endl;
	*p_serial << PMS ("Press E to return to the main menu.") << endl;
}

void task_user::print_coord_mode_menu(void)
{
	*p_serial << endl << PMS ("Entering Coordinate Mode.") << endl;
	*p_serial << PMS ("Press X to enter X-coordinates.") << endl;
	*p_serial << PMS ("Press Y to enter Y-coordinates.") << endl;
	*p_serial << PMS ("Press Z to enter Z-coordinates.") << endl;
	*p_serial << PMS ("Press G to run the device.") << endl;
	*p_serial << PMS ("Press R to reset the device.") << endl;
	*p_serial << PMS ("Press E to return to the main menu.") << endl;
}

void task_user::print_dir_mode_menu(void)
{
	*p_serial << endl << PMS ("Entering Direct Operation Mode.") << endl;
	*p_serial << PMS ("Press Ctrl-X for X-Motor commands.") << endl;
	*p_serial << PMS ("Press Ctrl-Y for Y-Motor commands.") << endl;
	*p_serial << PMS ("Press Ctrl-Z for Z-Motor commands.") << endl;
}

void task_user::print_dir_motor_commands(void)
{
	*p_serial << PMS ("Press Ctrl-F to activate forward.") << endl;
	*p_serial << PMS ("Press Ctrl-R to activate reverse.") << endl;
	*p_serial << PMS ("Press Ctrl-S to stop.") << endl;
}

void task_user::reset_device(void)
{
	*p_serial << PMS ("Resetting device.") << endl;
	wdt_enable (WDTO_120MS);
	for (;;);
	
}


//-------------------------------------------------------------------------------------
/** This task interacts with the user by transmitting and receiving bytes over USB to 
 *  and from a computer.
 */

void task_user::run (void)
{
	char char_in;							// Character read from serial device                         
	time_stamp a_time;                      // Holds the time so it can be displayed
    portTickType previous_ticks;
	uint16_t state_delay_counter = 0;

	//print_main_menu();

	// This is an infinite loop; it runs until the power is turned off. There is one 
	// such loop inside the code for each task
	for (;;)
	{
		//if (++state_delay_counter == 150)
		//{
			//*p_serial << task_name << state << endl;
			//state_delay_counter = 0;
		//}
		
		//if (reset.get())
		//{
			//*p_serial << PMS ("interrupt reset") << endl;
			//reset_device();
		//}
		
		// Run the finite state machine. The variable 'state' is kept by the parent class
		switch (state)
		{
			// In Case 0, the interface is in the main menu.
			case (0):
			
				if (p_serial->check_for_char ())        // If the user typed a
				{                                       // character, read
					char_in = p_serial->getchar ();     // the character
					atoi_buf[atoi_index] = char_in;
					atoi_index++;
					switch(char_in)
					{
						case('a'):
						
							//print_config_mode_menu();
							configuration_mode.put(true);
							*p_serial << PMS ("Entering config mode") << endl;
							transition_to(3);
							break;
							
						//case('e'):
							//drawing_mode.put(true);
							//transition_to(1);
							
						case('i'):
							if (!(incremental_mode.get()))
							{
								incremental_mode.put(true);
								transition_to(1);
							}
							
							break;
							
						case('c'):
						
							if (!(coordinate_mode.get()))
							{
								coordinate_mode.put(true);
								transition_to(1);
							}
							
							break;
						
						case('d'):
						
							//print_dir_mode_menu();
							direct_mode.put(true);
							transition_to(2);
							break;
							
						case('r'):
							
							*p_serial << PMS ("r reset") << endl;
							reset_device();
							break;
							
						case('s'):
						
							sensor_reading.put(true);
							break;
							
						case('p'):
							
							if(!(pause.get()))
							{
								pause.put(true);
							}
							else
							{
								pause.put(false);
							}
							break;
							
					}
				}
			
                break;
				
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// In Case 1, the UI is in Coordinate Mode. It waits for the user to specify the x, y, z 
			// coordinates of the device and then activates the device upon the user's command.
            case (1):
				if (p_serial->check_for_char ())        // If the user typed a
				{                                       // character, read
					char_in = p_serial->getchar ();     // the character
					atoi_buf[atoi_index] = char_in;
					atoi_index++;
					switch (char_in)
					{
						case('r'):
						
							reset_device();
							break;
						
						case ('e'):
						//print_main_menu();
						//coordinate_mode.put(false);
						if (xlocations.num_items_in() == ylocations.num_items_in() && xlocations.num_items_in() == zlocations.num_items_in())
						{
							total_nodes.put(xlocations.num_items_in());
							*p_serial << PMS ("Total nodes: ") << total_nodes.get() << endl;
							next_node.put(true);
						}
						else
						{
							*p_serial << PMS ("Error: Unequal axis coordinate vectors.") << endl;
						}
						atoi_index = 0;
						transition_to(0);
						break;
						
						// This character acts as an enter which the python file can more easily send.
						case('a'):
						conv_int = str_to_int();
						location_queue->put(conv_int);
						atoi_index = 0;
						//*p_serial << endl << PMS ("Locations stored in memory location: ") << location_queue << endl;
						break;
						
						case ('x'):
						atoi_index = 0;
						*p_serial << endl << PMS ("Receiving X-locations.") << endl;
						location_queue = &xlocations;
						break;
						
						case ('y'):
						atoi_index = 0;
						*p_serial << endl << PMS ("Receiving Y-locations.") << endl;
						location_queue = &ylocations;
						break;
						
						case ('z'):
						atoi_index = 0;
						*p_serial << endl << PMS ("Receiving Z-locations.") << endl;
						location_queue = &zlocations;
						break;
						
						case ('g'):
						initialization_complete.put(true);
						*p_serial << endl;
						break;
						
						case (','):
						*p_serial << char_in;
						conv_int = str_to_int();
						location_queue->put(conv_int);
						atoi_index = 0;

						break;
						
						case('0'):
						
						*p_serial << char_in;
						break;

						case('1'):
						
						*p_serial << char_in;
						break;

						case('2'):
						
						*p_serial << char_in;
						break;

						case('3'):
						
						*p_serial << char_in;
						break;

						case('4'):
						
						*p_serial << char_in;
						break;

						case('5'):
						
						*p_serial << char_in;
						break;

						case('6'):
						
						*p_serial << char_in;
						break;

						case('7'):
						
						*p_serial << char_in;
						break;

						case('8'):
						
						*p_serial << char_in;
						break;

						case('9'):
						
						*p_serial << char_in;
						break;
					}
				}

				// Check the print queue to see if another task has sent this task
				// something to be printed
				else if (print_ser_queue.check_for_char ())
				{
					p_serial->putchar (print_ser_queue.getchar ());
				}
            
				break;
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
			// State 2 is Direct Operation Mode. Here, the user can enter commands that directly turn the motors on
			// and off, as well as control their direction.
				
			case (2):
				if (p_serial->check_for_char ())        // If the user typed a
				{                                       // character, read
					char_in = p_serial->getchar ();     // the character
					atoi_buf[atoi_index] = char_in;
					atoi_index++;
					switch (char_in)
					{
						case ('x'):
							pmotor_operator = &xmotor_on;
							//*p_serial << endl << PMS ("Press Ctrl-E to return to the main menu.") << endl << endl;
							//*p_serial << PMS ("X-Motor Controls:") << endl;
							
							break;
						case ('y'):
							pmotor_operator = &ymotor_on;
							//*p_serial << endl << PMS ("Press Ctrl-E to return to the main menu.") << endl << endl;
							//*p_serial << PMS ("Y-Motor Controls:") << endl;
							//*p_serial << PMS ("Press Ctrl-F to activate forward.") << endl;
							//*p_serial << PMS ("Press Ctrl-R to activate reverse.") << endl;
							//*p_serial << PMS ("Press Ctrl-S to stop.") << endl;
							break;
						case ('z'):
							pmotor_operator = &zmotor_on;
							//*p_serial << endl << PMS ("Press Ctrl-E to return to the main menu.") << endl << endl;
							//*p_serial << PMS ("Z-Motor Controls:") << endl;
							//*p_serial << PMS ("Press Ctrl-F to activate forward.") << endl;
							//*p_serial << PMS ("Press Ctrl-R to activate reverse.") << endl;
							//*p_serial << PMS ("Press Ctrl-S to stop.") << endl;
							break;
							
						case('e'):
							//*p_serial << endl << PMS ("Press Ctrl-A for Command Mode") << endl;
							//*p_serial << PMS ("Press Ctrl-B for Coordinate Mode") << endl;
							//*p_serial << PMS ("Press Ctrl-D for Direct Operation Mode") << endl;
							//*p_serial << PMS ("Press Ctrl-R for Routine Operation Mode") << endl;
						
							direct_mode.put(false);
							transition_to(0);
							break;
						
						case ('f'):
							if(pmotor_operator == &xmotor_on || pmotor_operator == &ymotor_on || pmotor_operator == &zmotor_on)
							{
								pmotor_operator->put(1);
								
							}
							else
							{
								*p_serial << PMS ("Please choose the motor you would like to control.") << endl;
							}
							
							break;
							
						case ('r'):
							if(pmotor_operator == &xmotor_on || pmotor_operator == &ymotor_on || pmotor_operator == &zmotor_on)
							{
								pmotor_operator->put(2);
								
							}
							else
							{
								*p_serial << PMS ("Please choose the motor you would like to control.") << endl;
							}
							
							break;
							
						case ('s'):
							if(pmotor_operator == &xmotor_on || pmotor_operator == &ymotor_on || pmotor_operator == &zmotor_on)
							{
								pmotor_operator->put(0);
								
							}
							else
							{
								*p_serial << PMS ("Please choose the motor you would like to control.") << endl;
							}
							
							break;
							
						
					}
					
				}
			
                break;
			
			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
			/** In State 3, the interface task is in configuration mode. In this mode, it has the ability to change the
			 *	default values of certain system parameters.
			 */			
				
			case (3):
				if (p_serial->check_for_char ())        // If the user typed a
				{                                       // character, read
					char_in = p_serial->getchar ();     // the character
					atoi_buf[atoi_index] = char_in;
					atoi_index++;
					switch (char_in)
					{
						//case ('r'):
							//*p_serial << PMS ("Set the ramp run span below:") << endl;
							//atoi_index = 0;
							//data_config = &ramp_run_span;
							//break;
							
						case ('v'):
							*p_serial << PMS ("Max velocity set to:") << endl;
							atoi_index = 0;
							data_config = &gen_max_v;
							break;
							
						case ('x'):
							*p_serial << PMS ("X-axis max velocity set to:") << endl;
							atoi_index = 0;
							v_config = &x_max_velocity;
							queue_indicator = true;
							break;
							
						case ('y'):
							*p_serial << PMS ("Y-axis max velocity set to:") << endl;
							atoi_index = 0;
							v_config = &y_max_velocity;
							queue_indicator = true;
							break;
						
						case ('z'):
							*p_serial << PMS ("Z-axis max velocity set to:") << endl;
							atoi_index = 0;
							v_config = &z_max_velocity;
							queue_indicator = true;
							break;
						
						case ('e'):
							*p_serial << PMS ("Leaving config mode") << endl;
							configuration_mode.put(false);
							transition_to(0);
							break;
							
						case('a'):
							conv_int = str_to_int();
							if (queue_indicator)
							{
								conv_int = 1000 * conv_int;
								v_config->put(conv_int);
								queue_indicator = false;
							}
							else
							{
								if (data_config == &ramp_run_span)
								{
									conv_int = 100 / conv_int;
								}
								else if (data_config == &gen_max_v)
								{
									conv_int = 1500 * conv_int;
								}
								data_config->put(conv_int);
							}
									
							atoi_index = 0;
							*p_serial << PMS ("Config entered:") << conv_int << endl;
							break;
							
						case (','):
							*p_serial << char_in;
							
							conv_int = str_to_int();
							conv_int = conv_int * 1000;
							v_config->put(conv_int);
							atoi_index = 0;
							break;
							
						case ('u'):
							*p_serial << PMS ("Microstep scaler set to:") << endl;
							atoi_index = 0;
							data_config = &microstep_scaler;
							break;
							
						case ('s'):
							*p_serial << PMS ("Sensor delay set to:") << endl;
							atoi_index = 0;
							data_config = &sensor_delay;
							break;
							
						case ('n'):
							*p_serial << PMS ("Sensor sample size set to:") << endl;
							atoi_index = 0;
							data_config = &sensor_sample_number;
							break;
							
						case('0'):
						
						*p_serial << char_in;
						break;

						case('1'):
						
						*p_serial << char_in;
						break;

						case('2'):
						
						*p_serial << char_in;
						break;

						case('3'):
						
						*p_serial << char_in;
						break;

						case('4'):
						
						*p_serial << char_in;
						break;

						case('5'):
						
						*p_serial << char_in;
						break;

						case('6'):
						
						*p_serial << char_in;
						break;

						case('7'):
						
						*p_serial << char_in;
						break;

						case('8'):
						
						*p_serial << char_in;
						break;

						case('9'):
						
						*p_serial << char_in;
						break;
					}
				}
				break;

			// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
			// We should never get to the default state. If we do, complain and restart
			default:
				*p_serial << PMS ("Illegal state! Resetting AVR") << endl;
				wdt_enable (WDTO_120MS);
				for (;;);
				break;

		} // End switch state

		runs++;                             // Increment counter for debugging

		// No matter the state, wait for approximately a millisecond before we 
		// run the loop again. This gives lower priority tasks a chance to run
		vTaskDelay (configMS_TO_TICKS (1));
	}
}


//-------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------
/** This method prints a simple help message.
 */

void task_user::print_help_message (void)
{
	*p_serial << ATERM_BKG_CYAN << ATERM_TXT_BLACK << clrscr;
	*p_serial << PROGRAM_VERSION << PMS (" help") << endl;
	*p_serial << PMS ("  Ctl-C: Reset the AVR") << endl;
	*p_serial << PMS ("  Ctl-A: Enter command mode") << endl;
	*p_serial << PMS ("  In command mode only:") << endl;
	*p_serial << PMS ("    n:   Show the time right now") << endl;
	*p_serial << PMS ("    v:   Version and setup information") << endl;
	*p_serial << PMS ("    s:   Stack dump for tasks") << endl;
	*p_serial << PMS ("    e:   Exit command mode") << endl;
	*p_serial << PMS ("    h:   HALP!") << endl;
}


//-------------------------------------------------------------------------------------
/** This method displays information about the status of the system, including the
 *  following: 
 *    \li The name and version of the program
 *    \li The name, status, priority, and free stack space of each task
 *    \li Processor cycles used by each task
 *    \li Amount of heap space free and setting of RTOS tick timer
 */

void task_user::show_status (void)
{
	time_stamp the_time;					// Holds current time for printing

	// Show program vesion, time, and free heap space
	*p_serial << endl << PROGRAM_VERSION << PMS (__DATE__) << endl 
			  << PMS ("Time: ") << the_time.set_to_now ()
			  << PMS (", Heap free: ") << heap_left() << PMS ("/") 
			  << configTOTAL_HEAP_SIZE;

	// Show how the timer/counter is set up to cause RTOS timer ticks
	*p_serial << PMS (", TCC0CCA=") << TCC0.CCA << endl << endl;

	// Have the tasks print their status
	print_task_list (p_serial);
}

