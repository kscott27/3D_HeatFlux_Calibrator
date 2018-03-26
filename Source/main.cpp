//*************************************************************************************
/** \file lab1_main.cpp
 *    This file contains the main() code for a program which runs a port of the FreeRTOS
 *    for AVR devices. This port is specific to the XMEGA family.
 *
 *  Revisions:
 *    \li 09-14-2017 CTR Adapted from JRR code for AVR to be compatible with xmega 
 *
 *  License:
 *    This file is released under the Lesser GNU Public License, version 2. This 
 *    program is intended for educational use only, but it is not limited thereto. 
 */
//*************************************************************************************


#include <stdlib.h>                         // Prototype declarations for I/O functions
#include <avr/io.h>                         // Port I/O for SFR's
#include <avr/wdt.h>                        // Watchdog timer header
#include <avr/interrupt.h>
#include <string.h>                         // Functions for C string handling

#include "FreeRTOS.h"                       // Primary header for FreeRTOS
#include "task.h"                           // Header for FreeRTOS task functions
#include "queue.h"                          // FreeRTOS inter-task communication queues
#include "croutine.h"                       // Header for co-routines and such

#include "rs232int.h"                       // ME405/507 library for serial comm.
#include "time_stamp.h"                     // Class to implement a microsecond timer
#include "frt_task.h"                       // Header of wrapper for FreeRTOS tasks
#include "frt_text_queue.h"                 // Wrapper for FreeRTOS character queues
#include "frt_queue.h"                      // Header of wrapper for FreeRTOS queues
#include "frt_shared_data.h"                // Header for thread-safe shared data
#include "shares.h"                         // Global ('extern') queue declarations

#include "Timer.h"
#include "DM542T.h"
#include "LimitSwitch.h"
#include "SPI_Master.h"
#include "MAX31855.h"
#include "ADC.h"
#include "SBG01.h"

#include "task_user.h"                      // Header for user interface task
#include "task_LED.h"                      // Header for user interface task
#include "task_md.h"
#include "task_sensor.h"
#include "task_thermocouple.h"

volatile int counter;

shared_data<bool> xmotor_complete;
shared_data<bool> ymotor_complete;
shared_data<bool> zmotor_complete;
shared_data<bool> motors_ready;
shared_data<bool> sensor_complete;
shared_data<float> heat_flux;
shared_data<bool> initialization_complete;
shared_data<uint16_t> sensor_delay;
shared_data<uint16_t> microstep_scaler;

uint8_t number_of_nodes;
//uint32_t x_locs[10];
//uint32_t y_locs[10];
//uint32_t z_locs[10];

SPI_Master* spi;
MAX31855* therm1;
MAX31855* therm2;
MAX31855* therm3;
MAX31855* therm4;
MAX31855* therm5;
MAX31855* therm6;
MAX31855* therm7;
MAX31855* therm8;
ADC* adc;
SBG01* sbg01;
LimitSwitch* lim_x;
LimitSwitch* lim_y;
Timer* timer_C0;
DM542T* md_x;
DM542T* md_y;
DM542T* md_z;

frt_text_queue print_ser_queue (32, NULL, 10);

frt_queue<uint16_t> xlocations(50,NULL,10);
frt_queue<uint16_t> ylocations(50,NULL,10);
frt_queue<uint16_t> zlocations(50,NULL,10);

shared_data<bool> configuration_mode;
shared_data<bool> coordinate_mode;
shared_data<bool> direct_mode;
shared_data<bool> routine_mode;
shared_data<uint8_t> xmotor_on;
shared_data<uint8_t> ymotor_on;
shared_data<uint8_t> zmotor_on;
	

/*! \brief CCP write helper function written in assembly.
 *
 *  This function is written in assembly because of the time critical
 *  operation of writing to the registers.
 *
 *  \param address A pointer to the address to write to.
 *  \param value   The value to put in to the register.
 */
void CCPWrite( volatile uint8_t * address, uint8_t value )
{
	#if defined __GNUC__
	uint8_t volatile saved_sreg = SREG;
	cli();
	volatile uint8_t * tmpAddr = address;
	#ifdef RAMPZ
	RAMPZ = 0;
	#endif
	asm volatile(
	"movw r30,  %0"	      "\n\t"
	"ldi  r16,  %2"	      "\n\t"
	"out   %3, r16"	      "\n\t"
	"st     Z,  %1"       "\n\t"
	:
	: "r" (tmpAddr), "r" (value), "M" (0xD8), "i" (&CCP)
	: "r16", "r30", "r31"
	);

	SREG = saved_sreg;
	#endif
}


//=====================================================================================
/** The main function sets up the RTOS.  Some test tasks are created. Then the 
 *  scheduler is started up; the scheduler runs until power is turned off or there's a 
 *  reset.
 *  @return This is a real-time microcontroller program which doesn't return. Ever.
 */

int main (void)
{
	cli();
	// Configure the system clock
	{	
		// Enable the 32MHz internal RC oscillator and the external 32KHz oscillator
		OSC.CTRL |= (1 << OSC_RC32MEN_bp);
		do {} while((OSC.STATUS & (1 << OSC_RC32MRDY_bp)) != (1 << OSC_RC32MRDY_bp));

		// Select the clock
		CCPWrite(&(CLK.CTRL),((CLK.CTRL & ~CLK_SCLKSEL_gm) | (1 << CLK_SCLKSEL0_bp)));
		
		// Disable the 2MHz internal RC oscillator
		OSC.CTRL &= ~(1 << OSC_RC2MEN_bp);
	}
	
	// Disable the watchdog timer unless it's needed later. This is important because
	// sometimes the watchdog timer may have been left on...and it tends to stay on	 
	wdt_disable ();


	// Configure a serial port which can be used by a task to print debugging infor-
	// mation, or to allow user interaction, or for whatever use is appropriate.  The
	// serial port will be used by the user interface task after setup is complete and
	// the task scheduler has been started by the function vTaskStartScheduler()
	rs232 ser_dev(0,&USARTE0); // Create a serial device on USART E0
	ser_dev << clrscr << "FreeRTOS Xmega Testing Program" << endl << endl;
		
	
	
	
	// Create driver objects
	
	//spi = new SPI_Master(&SPID);
	//therm1 = new MAX31855(spi, &PORTC, PIN4_bm);
	adc = new ADC(&ADCA, &(ADCA.CH0));
	sbg01 = new SBG01(adc, 0.225);
	//lim_x = new LimitSwitch (&PORTA, 6);
	//lim_y = new LimitSwitch (&PORTA, 7);
	//timer_C0 = new Timer (&PORTC, &TCC0, PIN4_bm);
	//timer_C0->set_freq_khz(5);
	//md_x = new DM542T (timer_C0, &PORTA, PIN1_bm, PIN0_bm, 8);
	//md_y = new DM542T (timer_C0, &PORTA, PIN3_bm, PIN2_bm, 8);
	//md_z = new DM542T (timer_C0, &PORTA, PIN5_bm, PIN4_bm, 8);
	
	
	
	
	
	// The user interface is at low priority; it could have been run in the idle task
	// but it is desired to exercise the RTOS more thoroughly in this test program
	new task_user ("UserInt", task_priority (0), 128, &ser_dev);
	
	//new task_md ("MDX", task_priority(8), 128, &ser_dev, md_x, timer_C0,
	//&xmotor_on, &xmotor_complete, 8);
	//
	//new task_md ("MDY", task_priority(8), 128, &ser_dev, md_y, timer_C0,
	//&ymotor_on, &ymotor_complete, 8);
	//
	//new task_md ("MDZ", task_priority(8), 128, &ser_dev, md_z, timer_C0,
	//&zmotor_on, &zmotor_complete, 8);
	
	new task_sensor ("Gardon_Gauge", task_priority(9), 128, &ser_dev, sbg01);

    //new task_thermocouple ("Therm1", task_priority(6), 128, &ser_dev, therm1);

    //new task_thermocouple ("Therm2", task_priority(6), 260, &ser_dev);
//
	//new task_thermocouple ("Therm3", task_priority(6), 260, &ser_dev);
//
	//new task_thermocouple ("Therm4", task_priority(6), 260, &ser_dev);
//
	//new task_thermocouple ("Therm5", task_priority(6), 260, &ser_dev);
	
	// Enable high level interrupts and global interrupts
	PMIC_CTRL = (1 << PMIC_HILVLEN_bp | 1 << PMIC_MEDLVLEN_bp | 1 << PMIC_LOLVLEN_bp);
	sei();

    initialization_complete.put(false);
	
	// Here's where the RTOS scheduler is started up. It should never exit as long as
	// power is on and the microcontroller isn't rebooted
	vTaskStartScheduler ();
}

ISR(PORTA_INT0_vect)
{
	md_x->motorOff();
}

ISR(PORTA_INT1_vect)
{
	md_y->motorOff();
}
