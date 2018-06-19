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

#include "DM542T.h"

class LimitSwitch
{
	protected:
	
	DM542T* md;
	PORT_t* port;
	uint8_t input_bp;
	uint8_t input_bm;
	uint8_t EVENTCHnMUX;
	uint8_t INTnMASK;
	uint8_t EVSYS_CHMUX_PORTx_PINn_gc;
	bool engaged;
	
	public:
	
	LimitSwitch(DM542T* md, PORT_t* port, uint8_t input_bm, uint8_t EVENTCHnMUX, uint8_t PORT_INTnMASK, uint8_t EVSYS_CHMUX_PORTx_PINn_gc);
	
	//LimitSwitch(PORT_t* port, uint8_t input_bm, uint8_t EVENTCHnMUX, uint8_t INTnMASK, uint8_t EVSYS_CHMUX_PORTx_PINn_gc);
	
	//void interrupt_handler (void);
	//
	//void min_bound_interrupt_handler (void);
	//
	//void max_bound_interrupt_handler (void);
	
	bool get_status (void);
	
	void clr_status (void);
	
	void set_status (void);
	
};




#endif /* LIMITSWITCH_H_ */