/*
 * Timer.cpp
 *
 * Created: 1/28/2018 1:21:33 PM
 *  Author: Kevin
 */ 

#include "Timer.h"

Timer::Timer(PORT_t* timer_port, TC0_t* timer0, uint8_t pin_bm)
:timer_port(timer_port), timer0(timer0), pin_bm(pin_bm)
{
	timer_port->DIRSET = pin_bm;
	
	// Configure timer prescaler
	timer0->CTRLA = TC_CLKSEL_DIV1_gc;
	
	set_freq_khz(5);
	
	if(pin_bm == PIN0_bm)
	{
		timer0->CTRLB = TC0_WGMODE0_bm | TC0_WGMODE1_bm | TC0_CCAEN_bm;
		timer0->CCA = pulse_period / 2;
	}
	else if(pin_bm == PIN1_bm)
	{
		timer0->CTRLB = TC0_WGMODE0_bm | TC0_WGMODE1_bm | TC0_CCBEN_bm;
		timer0->CCB = pulse_period / 2;
	}
	else if(pin_bm == PIN2_bm)
	{
		timer0->CTRLB = TC0_WGMODE0_bm | TC0_WGMODE1_bm | TC0_CCCEN_bm;
		timer0->CCC = pulse_period / 2;
	}
	else if(pin_bm == PIN3_bm)
	{
		timer0->CTRLB = TC0_WGMODE0_bm | TC0_WGMODE1_bm | TC0_CCDEN_bm;
		timer0->CCD = pulse_period / 2;
	}
}

Timer::Timer(PORT_t* timer_port, TC1_t* timer1, uint8_t pin_bm)
:timer_port(timer_port), timer1(timer1), pin_bm(pin_bm)
{
	timer_port->DIRSET = pin_bm;
	
	// Configure timer prescaler
	timer1->CTRLA = TC_CLKSEL_DIV1_gc;
	
	if(pin_bm == PIN0_bm)
	{
		timer1->CTRLB = TC1_WGMODE0_bm | TC1_WGMODE1_bm | TC1_CCAEN_bm;
		timer1->CCA = pulse_period / 2;
	}
	else if(pin_bm == PIN1_bm)
	{
		timer1->CTRLB = TC1_WGMODE0_bm | TC1_WGMODE1_bm | TC1_CCBEN_bm;
		timer1->CCB = pulse_period / 2;
	}
}

void Timer::set_freq_khz(uint16_t freq_khz)
{
	// Convert freq (KHz) to the timer period, considering a
	// 32 MHz clock speed.
	pulse_period = 32000 / freq_khz;
	
	if(timer0 == &TCC0 || timer0 == &TCD0 || timer0 == &TCE0)
	{
		timer0->PER = pulse_period; //set for appropriate duty cycle denominator
	}
	if(timer1 == &TCC1 || timer1 == &TCD1)
	{
		timer1->PER = pulse_period; //set for appropriate duty cycle denominator
	}
}

uint16_t Timer::get_freq_khz(void)
{
	return freq_khz;
}