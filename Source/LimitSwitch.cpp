/*
 * LimitSwitch.cpp
 *
 * Created: 2/19/2018 2:54:43 PM
 *  Author: Kevin
 */ 

#include "LimitSwitch.h"

LimitSwitch::LimitSwitch(PORT_t* port, uint8_t input_bp)
{
	uint8_t input_bm;
	input_bm = 2^input_bp;
	
	//Configure Port C bits for input capture
	port->DIRCLR = input_bm;
	
	//Set input sense configuration for PC3
	switch(input_bp)
	{
		case(6):
			port->PIN6CTRL = PORT_OPC_PULLUP_gc | PORT_ISC_FALLING_gc;
			//Link event Channel 2 to PC2
			EVSYS.CH2MUX = EVSYS_CHMUX_PORTA_PIN6_gc;
			break;
			
		case(7):
			port->PIN7CTRL = PORT_OPC_PULLUP_gc | PORT_ISC_FALLING_gc;
			//Link event Channel 3 to PC3
			EVSYS.CH3MUX = EVSYS_CHMUX_PORTA_PIN7_gc;
			break;
	}
	
	//Set Lim Switch pins for specific port interrupt
	port->INTCTRL = PORT_INT0LVL1_bm | PORT_INT0LVL0_bm;
	port->INT0MASK = 1 << input_bp;
	
	//Enable interrupts for all priority levels
	PMIC.CTRL = PMIC_HILVLEN_bm | PMIC_MEDLVLEN_bm | PMIC_LOLVLEN_bm;
}
