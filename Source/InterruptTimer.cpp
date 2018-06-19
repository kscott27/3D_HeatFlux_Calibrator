/*
 * InterruptTimer.cpp
 *
 * Created: 4/2/2018 5:49:57 PM
 *  Author: Kevin
 */ 


#include "InterruptTimer.h"

InterruptTimer::InterruptTimer(PORT_t* timer_port, TC0_t* timer0, uint8_t pin_bm, uint8_t int_lvl_bm)
:timer_port(timer_port), timer0(timer0), pin_bm(pin_bm), int_lvl_bm(int_lvl_bm)
{
	timer_port->DIRSET |= pin_bm;
	
	// Configure timer prescaler
	timer0->CTRLA |= TC_CLKSEL_DIV1_gc;
	
	set_freq_hz(1);
	set_duty_cycle(50);
		
	if(pin_bm == PIN0_bm)
	{
		timer0->CTRLB |= TC0_CCAEN_bm;
		timer0->INTCTRLB |= TC_CCAINTLVL_HI_gc;
		//timer0->CCA = pulse_period / 2;
	}
	else if(pin_bm == PIN1_bm)
	{
		timer0->CTRLB |= TC0_CCBEN_bm;
		timer0->INTCTRLB |= TC_CCBINTLVL_HI_gc;
		//timer0->CCB = pulse_period / 2;
	}
	else if(pin_bm == PIN2_bm)
	{
		timer0->CTRLB |= TC0_CCCEN_bm;
		timer0->INTCTRLB |= TC_CCCINTLVL_HI_gc;
		//timer0->CCC = pulse_period / 2;
	}
	else if(pin_bm == PIN3_bm)
	{
		timer0->CTRLB |= TC0_CCDEN_bm;
		timer0->INTCTRLB |= TC_CCDINTLVL_HI_gc;
		//timer0->CCD = pulse_period / 2;
	}
	
	timer0->INTCTRLA |= TC_OVFINTLVL_HI_gc;
}

InterruptTimer::InterruptTimer(PORT_t* timer_port, TC1_t* timer1, uint8_t pin_bm, uint8_t int_lvl_bm)
:timer_port(timer_port), timer1(timer1), pin_bm(pin_bm), int_lvl_bm(int_lvl_bm)
{
	timer_port->DIRSET |= pin_bm;
	
	// Configure timer prescaler
	timer1->CTRLA |= TC_CLKSEL_DIV1_gc;
	
	set_freq_khz(5);
	set_duty_cycle(50);
	
	if(pin_bm == PIN4_bm)
	{
		timer1->CTRLB |= TC1_CCAEN_bm;
		timer1->INTCTRLB |= TC_CCAINTLVL_HI_gc;
		//timer1->CCA = pulse_period / 2;
	}
	else if(pin_bm == PIN5_bm)
	{
		timer1->CTRLB |= TC0_CCBEN_bm;
		timer1->INTCTRLB |= TC_CCBINTLVL_HI_gc;
		//timer1->CCB = pulse_period / 2;
	}
	
	timer1->INTCTRLA |= TC_OVFINTLVL_HI_gc;
}

void InterruptTimer::set_freq_khz(uint16_t freq_khz)
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

void InterruptTimer::set_freq_hz(uint32_t freq_hz)
{
	// Convert freq (Hz) to the timer period, considering a
	// 32 MHz clock speed.
	pulse_period = 32000000 / freq_hz;
	
	if(timer0 == &TCC0 || timer0 == &TCD0 || timer0 == &TCE0)
	{
		timer0->PER = pulse_period; //set for appropriate duty cycle denominator
	}
	if(timer1 == &TCC1 || timer1 == &TCD1)
	{
		timer1->PER = pulse_period; //set for appropriate duty cycle denominator
	}
}

void InterruptTimer::set_duty_cycle(uint8_t duty_cycle)
{
	pulse_width = pulse_period * duty_cycle / 100;
	
	if(pin_bm == PIN0_bm)
	{
		timer0->CCA = pulse_width;
	}
	if(pin_bm == PIN1_bm)
	{
		timer0->CCB = pulse_width;
	}
	if(pin_bm == PIN2_bm)
	{
		timer0->CCC = pulse_width;
	}
	if(pin_bm == PIN3_bm)
	{
		timer0->CCD = pulse_width;
	}
	if(pin_bm == PIN4_bm)
	{
		timer1->CCA = pulse_width;
	}
	if(pin_bm == PIN5_bm)
	{
		timer1->CCB = pulse_width;
	}
}

uint16_t InterruptTimer::get_freq_khz(void)
{
	return freq_khz;
}

void InterruptTimer::high(void)
{
	timer_port->OUTSET = pin_bm;
}

void InterruptTimer::low(void)
{
	timer_port->OUTCLR = pin_bm;
}