/*
 * Timer.h
 *
 * Created: 1/28/2018 1:11:49 PM
 *  Author: Kevin
 */ 


#ifndef TIMER_H_
#define TIMER_H_

#include <avr/io.h>                         // Port I/O for SFR's
#include <avr/interrupt.h>

#include <stdio.h>
#include <stdlib.h>

//class Timer
//{
	//protected:
	//
	//PORT_t* ptimer_port;
	//register16_t* pchannel; //TCD0.CCC
	//bool rising_edge;
	//int8_t duty_cycle;
	//TC0_t* timer0;
	//TC1_t* ptimer1;
	//uint8_t pin_bm;
	//
	//uint16_t pulse_period;
	//volatile uint32_t pulse_high;
	//volatile uint32_t pulse_low;
	//uint16_t freq_khz;
	//
	//
	//public:
	//
	//
	//
	//Timer(TC0_t* timer, uint8_t pin_bm);
	//
	//Timer(TC1_t* timer);
	//
	//void set_freq_khz(uint16_t ffreq_khz);
	//
	//uint16_t get_freq_khz(void);
//};

class Timer
{
	protected:
	
	PORT_t* timer_port;
	register16_t* pchannel; //TCD0.CCC
	bool rising_edge;
	int8_t duty_cycle;
	TC0_t* timer0;
	TC1_t* timer1;
	uint8_t pin_bm;
	
	uint16_t pulse_period;
	volatile uint32_t pulse_high;
	volatile uint32_t pulse_low;
	uint16_t freq_khz;
	
	
	public:
	
	
	
	Timer(PORT_t* timer_port, TC0_t* timer0, uint8_t pin_bm);
	
	Timer(PORT_t* timer_port, TC1_t* timer1, uint8_t pin_bm);
	
	void set_freq_khz(uint16_t freq_khz);
	
	uint16_t get_freq_khz(void);
};



#endif /* TIMER_H_ */