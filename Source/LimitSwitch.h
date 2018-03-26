/*
 * LimitSwitch.h
 *
 * Created: 2/19/2018 2:54:23 PM
 *  Author: Kevin
 */ 


#ifndef LIMITSWITCH_H_
#define LIMITSWITCH_H_

#include <avr/io.h>                         // Port I/O for SFR's
#include <avr/interrupt.h>

#include <stdio.h>
#include <stdlib.h>

class LimitSwitch
{
	protected:
	
	
	public:
	
	LimitSwitch(PORT_t* port, uint8_t input_bp);
	
};




#endif /* LIMITSWITCH_H_ */