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
	
	steps = 0;
}

//-------------------------------------------------------------------------------------
/** This constructor creates a DM542T motor driver object that utilizes interrupts to
    generate a PWM signal.
 *  @param pwm_port A pointer to the port where the PWM signal pin is
 *  @param logic_port A pointer to the port where the motor driver logic pins are
 *  @param ena_bm A bit-mask indicating which pin on the port is used as the enable pin
 *  @param dir_bm A bit-mask indicating which pin on the port is used as the direction pin
 *  @param pwm_bm A bit-mask indicating which pin on the port is used as the pwm signal pin
 *  @param microstep_scaler A bit-mask indicating the factor that the default 200 steps
 *   of the motor is multiplied by
 */
DM542T::DM542T(PORT_t* pwm_port, PORT_t* logic_port, uint8_t ena_bm, uint8_t dir_bm, uint8_t pwm_bm, uint8_t microstep_scaler)
:pwm_port(pwm_port), logic_port(logic_port), ena_bm(ena_bm), dir_bm(dir_bm), pwm_bm(pwm_bm), microstep_scaler(microstep_scaler)
{
	// Configure pins for specific motor driver function lines
	logic_port->DIRSET |= ena_bm;
	logic_port->DIRSET |= dir_bm;
	pwm_port->DIRSET |= pwm_bm;
	
	// Have motor initially disabled
	motorOff();
	
	steps = 0;
}

//-------------------------------------------------------------------------------------
/** This method enables the motor driver by grounding the enable pin
 */
void DM542T::motorOn(void)
{
	logic_port->OUTCLR = ena_bm;
	enabled = true;
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
	logic_port->OUTSET = ena_bm;
	enabled = false;	
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
    toggle the PWM signal pin, thereby creating a PWM signal.
 */
void DM542T::operatePWM(void)
{
	if(rising_edge)
	{
		pwm_port->OUTSET = pwm_bm;
		update_step();
		rising_edge = false;
	}
	else
	{
		pwm_port->OUTCLR = pwm_bm;
		rising_edge = true;
	}
}

	


