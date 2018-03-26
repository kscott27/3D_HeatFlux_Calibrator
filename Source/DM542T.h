/*
 * MotorDriver.h
 *
 * Created: 11/29/2017 3:09:50 PM
 *  Author: Kevin
 */ 


#ifndef DM542T_H_
#define DM542T_H_

#include <avr/io.h>                         // Port I/O for SFR's
#include <avr/interrupt.h>

#include <stdio.h>
#include <stdlib.h>

#include "Timer.h"

class DM542T
{
	protected:
	
	Timer* timer;
	PORT_t* logic_port;
	PORT_t* pwm_port;
	uint8_t ena_bm;
	uint8_t dir_bm;
	uint8_t pwm_bm;	
	bool rising_edge;
	int8_t duty_cycle;
	uint8_t microstep_scaler;
	volatile uint32_t pulse_high;
	volatile uint32_t pulse_low;
	int32_t pulse_period;
	int32_t steps;
	bool enabled;
	uint8_t direction;
	
	
	public:
	
	DM542T(Timer* timer, PORT_t* logic_port, uint8_t ena_bm, uint8_t dir_bm, uint8_t microstep_scaler);
	
	DM542T(PORT_t* pwm_port, PORT_t* logic_port, uint8_t ena_bm, uint8_t dir_bm, uint8_t pwm_bm, uint8_t microstep_scaler);
	
	void motorOn(void);
	
	void motorCW(void);
	
	void motorCCW(void);
	
	void motorOff(void);
	
	void update_step(void);
	
	int32_t get_steps(void);
	
	void operatePWM(void);
};




#endif /* DM542T_H_ */