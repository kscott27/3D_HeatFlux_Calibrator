/*
 * CPPFile1.cpp
 *
 * Created: 11/29/2017 3:12:40 PM
 *  Author: Kevin
 */ 

#include "DM542T.h"

//-------------------------------------------------------------------------------------
/** This constructor creates a DM542T motor driver object that utilizes a PWM timer pin.
 *  @param timer A pointer to a timer object used to control the PWM signal of the motor
 *  @param logic_port A pointer to the port where the motor driver logic pins are
 *  @param ena_bm A bit-mask indicating which pin on the port is used as the enable pin
 *  @param dir_bm A bit-mask indicating which pin on the port is used as the direction pin
 *  @param microstep_scaler A bit-mask indicating the factor that the default 200 steps
 *   of the motor is multiplied by
 */
DM542T::DM542T(Timer* timer, PORT_t* logic_port, uint8_t ena_bm, uint8_t dir_bm, uint8_t microstep_scaler)
:timer(timer), logic_port(logic_port), ena_bm(ena_bm), dir_bm(dir_bm), microstep_scaler(microstep_scaler)
{
	// Configure pins for specific motor driver function lines
	logic_port->DIRSET |= ena_bm;
	logic_port->DIRSET |= dir_bm;
	
	// Have motor initially disabled
	motorOff();
	
	steps = 200000;
}

//-------------------------------------------------------------------------------------
/** This constructor creates a DM542T motor driver object that utilizes interrupts to
    generate a PWM signal.
 *  @param logic_port A pointer to the port where the motor driver logic pins are
 *  @param ena_bm A bit-mask indicating which pin on the port is used as the enable pin
 *  @param dir_bm A bit-mask indicating which pin on the port is used as the direction pin
 *  @param pwm_bm A bit-mask indicating which pin on the port is used as the pwm signal pin
 *  @param microstep_scaler A bit-mask indicating the factor that the default 200 steps
 *   of the motor is multiplied by
 */
DM542T::DM542T(InterruptTimer* interrupt_timer, PORT_t* logic_port, uint8_t ena_bm, uint8_t dir_bm, uint8_t microstep_scaler)
:interrupt_timer(interrupt_timer), logic_port(logic_port), ena_bm(ena_bm), dir_bm(dir_bm), microstep_scaler(microstep_scaler)
{
	// Configure pins for specific motor driver function lines
	logic_port->DIRSET |= ena_bm;
	logic_port->DIRSET |= dir_bm;
	
	max_boundary_step_count = 100000000;
	
	// Have motor initially disabled
	motorOff();
	
	steps = 0;
}

//-------------------------------------------------------------------------------------
/** This method enables the motor driver by grounding the enable pin
 */
bool DM542T::motorOn(void)
{
	if (direction == 0)
	{
		logic_port->OUTCLR = ena_bm;
		enabled = true;
		return true;
	}
	else
	{
		logic_port->OUTCLR = ena_bm;
		enabled = true;
		return true;
	}
	
}

//-------------------------------------------------------------------------------------
/** This method enables the motor driver by grounding the enable pin
 */
//bool DM542T::motorOn(void)
//{
	//if (check_bounds())
	//{
		//logic_port->OUTCLR = ena_bm;
		//enabled = true;
		//return true;
	//}
	//else
	//{
		//return false;
	//}
	//
//}

//-------------------------------------------------------------------------------------
/** This method checks that the motor does not exceed its boundaries.
 */
bool DM542T::check_bounds(void)
{
	if (direction == 0 && max_boundary_step_count - steps > 3 * 200 * microstep_scaler)
	{
		return true;
	}
	else if (direction == 1 && steps - min_boundary_step_count > 3 * 200 * microstep_scaler)
	{
		return true;
	}
	else
	{
		return false;
	}
}

//-------------------------------------------------------------------------------------
/** This method sets the motor driver direction to clockwise
 */	
void DM542T::motorCW(void)
{
	logic_port->OUTSET = dir_bm;
	direction = 1;
}

//-------------------------------------------------------------------------------------
/** This method sets the motor driver direction to counter-clockwise
 */		
void DM542T::motorCCW(void)
{
	logic_port->OUTCLR = dir_bm;
	direction = 0;
}

//-------------------------------------------------------------------------------------
/** This method disables the motor driver by setting the enable pin high
 */	
void DM542T::motorOff(void)
{
	//logic_port->OUTSET = ena_bm;
	enabled = false;	
}

//-------------------------------------------------------------------------------------
/** This method disables the motor driver from traveling CW
 */	
void DM542T::disableCW(void)
{
	motorOff();
	disable_CW = true;
	//boundary_step_count = steps;	
}

//-------------------------------------------------------------------------------------
/** This method disables the motor driver from traveling CCW
 */	
void DM542T::disableCCW(void)
{
	motorOff();
	disable_CCW = true;	
	//boundary_step_count = steps;
}

//-------------------------------------------------------------------------------------
/** This method allows the motor driver to operate in either direction
 */	
void DM542T::free_motion(void)
{
	disable_CCW = false;	
	disable_CW = false;
}

//-------------------------------------------------------------------------------------
/** This method returns the direction of the motor
 */	
uint8_t DM542T::get_direction(void)
{
	return direction;
}

//-------------------------------------------------------------------------------------
/** This method resets the motor's steps to 0
 */	
void DM542T::reset_steps(void)
{
	steps = 0;
}

//-------------------------------------------------------------------------------------
/** This method adds or subtracts one step from the motor driver's step count depending
    on its direction.
 */
void DM542T::update_step(void)
{
	if (enabled)
	{
		if (!direction)
		{
			++steps;
		}
		else
		{
			--steps;
		}
	}
	
}

//-------------------------------------------------------------------------------------
/** This method returns the number of steps that the driver has taken relative to the origin.
 */
int32_t DM542T::get_steps(void)
{
	return steps;
}

//-------------------------------------------------------------------------------------
/** This method is meant to be called during an interrupt service routine in order to 
    set the PWM signal pin, thereby causing the motor to take a step.
 */
void DM542T::take_step(void)
{
	if (enabled)
	{
		interrupt_timer->high();
		update_step();
	}
}

//-------------------------------------------------------------------------------------
/** This method is meant to be called during an interrupt service routine in order to 
    clear the PWM pin, thereby preparing the pin for the next rising edge.
 */
void DM542T::set_signal_low(void)
{
	interrupt_timer->low();
}

//-------------------------------------------------------------------------------------
/** This method is meant to be called during an interrupt service routine in order to 
    record the number of steps at the motor boundary. It is used to prohibit the motor
	from moving past the boundary of a limit switch.
 */
void DM542T::set_step_boundary(void)
{
	if (direction == 0)
	{
		max_boundary_step_count = steps;
	}
	else
	{
		min_boundary_step_count = steps;
	}
	
}

//-------------------------------------------------------------------------------------
/** This method is meant to be called during an interrupt service routine in order to 
    record the number of steps at the motor boundary. It is used to prohibit the motor
	from moving past the minimum boundary of a limit switch.
 */
void DM542T::set_min_step_boundary(void)
{
	reset_steps();
	min_boundary_step_count = steps;
}

//-------------------------------------------------------------------------------------
/** This method is meant to be called during an interrupt service routine in order to 
    record the number of steps at the motor boundary. It is used to prohibit the motor
	from moving past the maximum boundary of a limit switch.
 */
void DM542T::set_max_step_boundary(void)
{
	max_boundary_step_count = steps;
}

//-------------------------------------------------------------------------------------
/** This method returns the enable-status of the motor.
 */
bool DM542T::get_status(void)
{
	return enabled;
}

//-------------------------------------------------------------------------------------
/** This method sets the controls for the acceleration of the motor.
 */
void DM542T::set_ramp_ctrl(uint32_t init_freq_hz, uint32_t final_freq_hz, uint32_t run_span)
{
	ramp_ctrl_init_freq_hz = init_freq_hz;
	ramp_ctrl_final_freq_hz = final_freq_hz;
	ramp_ctrl_run_span = run_span;
	ramp_run_count = 0;
	interrupt_timer->set_freq_hz(init_freq_hz);	
}

//-------------------------------------------------------------------------------------
/** This method controls the acceleration of the motor.
 */
uint32_t DM542T::ramp_ctrl(void)
{
	
	if (ramp_run_count <= ramp_ctrl_run_span)
	{
		ramp_run_count++;
		ramp_ctrl_freq_hz = ramp_ctrl_init_freq_hz + (ramp_ctrl_final_freq_hz - ramp_ctrl_init_freq_hz) * ramp_run_count / ramp_ctrl_run_span;
		interrupt_timer->set_freq_hz(ramp_ctrl_freq_hz);
		return ramp_ctrl_freq_hz;
	}
	else
	{
		return ramp_ctrl_freq_hz;
	}
}

void DM542T::min_bound_interrupt_handler(void)
{
	if (get_direction() == 1)
	{
		motorOff();
		reset_steps();
	}
}

void DM542T::max_bound_interrupt_handler(void)
{
	if (get_direction() == 0)
	{
		motorOff();
	}
}

	


