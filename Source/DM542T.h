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
#include "InterruptTimer.h"

class DM542T
{
	protected:
	
	Timer* timer;
	InterruptTimer* interrupt_timer;
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
	int32_t min_boundary_step_count;
	int32_t max_boundary_step_count;
	bool enabled;
	uint8_t direction;
	bool disable_CW;
	bool disable_CCW;
	uint32_t ramp_run_count = 0;
	uint32_t ramp_ctrl_init_freq_hz = 0;
	uint32_t ramp_ctrl_final_freq_hz = 0;
	uint32_t ramp_ctrl_run_span = 0;
	uint32_t ramp_ctrl_freq_hz = 0;
	
	
	public:
	
	DM542T(Timer* timer, PORT_t* logic_port, uint8_t ena_bm, uint8_t dir_bm, uint8_t microstep_scaler);
	
	DM542T(InterruptTimer* interrupt_timer, PORT_t* logic_port, uint8_t ena_bm, uint8_t dir_bm, uint8_t microstep_scaler);
	
	bool motorOn(void);
	
	bool check_bounds(void);
	
	void motorCW(void);
	
	void motorCCW(void);
	
	void motorOff(void);
	
	void disableCW(void);
	
	void disableCCW(void);
	
	void free_motion(void);
	
	uint8_t get_direction(void);
	
	void reset_steps(void);
	
	void update_step(void);
	
	int32_t get_steps(void);
	
	void take_step(void);
	
	void set_signal_low(void);
	
	void set_step_boundary(void);
	
	void set_min_step_boundary(void);
	
	void set_max_step_boundary(void);
	
	bool get_status(void);
	
	void set_ramp_ctrl(uint32_t init_freq_hz, uint32_t final_freq_hz, uint32_t run_span);
	
	uint32_t ramp_ctrl(void);
	
	void min_bound_interrupt_handler(void);
	
	void max_bound_interrupt_handler(void);
};




#endif /* DM542T_H_ */