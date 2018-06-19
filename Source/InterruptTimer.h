/*
 * InterruptTimer.h
 *
 * Created: 4/2/2018 5:49:22 PM
 *  Author: Kevin
 */ 


#ifndef INTERRUPTTIMER_H_
#define INTERRUPTTIMER_H_

#include <avr/io.h>                         // Port I/O for SFR's
#include <avr/interrupt.h>

#include <stdio.h>
#include <stdlib.h>

class InterruptTimer
{
	protected:
	
	PORT_t* timer_port;
	register16_t* pchannel; //TCD0.CCC
	bool rising_edge;
	uint8_t duty_cycle;
	TC0_t* timer0;
	TC1_t* timer1;
	uint8_t pin_bm;
	uint8_t int_lvl_bm;
	
	uint16_t pulse_period;
	uint16_t pulse_width;
	volatile uint32_t pulse_low;
	uint16_t freq_khz;
	
	public:
	
	InterruptTimer(PORT_t* timer_port, TC0_t* timer0, uint8_t pin_bm, uint8_t int_lvl_bm);
	
	InterruptTimer(PORT_t* timer_port, TC1_t* timer1, uint8_t pin_bm, uint8_t int_lvl_bm);
	
	void set_freq_khz(uint16_t freq_khz);
	
	void set_freq_hz(uint32_t freq_hz);
	
	void set_duty_cycle(uint8_t duty_cycle);
	
	uint16_t get_freq_khz(void);
	
	void high(void);
	
	void low(void);
};



#endif /* INTERRUPTTIMER_H_ */