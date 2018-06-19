/*
 * LimitSwitch.cpp
 *
 * Created: 2/19/2018 2:54:43 PM
 *  Author: Kevin
 */ 

#include "LimitSwitch.h"

LimitSwitch::LimitSwitch(DM542T* md, PORT_t* port, uint8_t input_bm, uint8_t EVENTCHnMUX, uint8_t INTnMASK, uint8_t EVSYS_CHMUX_PORTx_PINn_gc)
:md(md), port(port), input_bm(input_bm), EVENTCHnMUX(EVENTCHnMUX), INTnMASK(INTnMASK), EVSYS_CHMUX_PORTx_PINn_gc(EVSYS_CHMUX_PORTx_PINn_gc)
{
	port->DIRCLR = input_bm;
	
	engaged = false;
	
	switch(input_bm)
	{
		case(PIN0_bm):
		port->PIN0CTRL = PORT_ISC_RISING_gc;
		break;
		
		case(PIN1_bm):
		port->PIN1CTRL = PORT_ISC_RISING_gc;
		break;
		
		case(PIN2_bm):
		port->PIN2CTRL = PORT_ISC_RISING_gc;
		break;
		
		case(PIN3_bm):
		port->PIN3CTRL = PORT_ISC_RISING_gc;
		break;
		
		case(PIN4_bm):
		port->PIN4CTRL = PORT_ISC_RISING_gc;
		break;
		
		case(PIN5_bm):
		port->PIN5CTRL = PORT_ISC_RISING_gc;
		break;
		
		case(PIN6_bm):
		port->PIN6CTRL = PORT_ISC_RISING_gc;
		break;
		
		case(PIN7_bm):
		port->PIN7CTRL = PORT_ISC_RISING_gc;
		break;
	}
	
	if (EVENTCHnMUX == 0)
	{
		EVSYS.CH0MUX |= EVSYS_CHMUX_PORTx_PINn_gc;
	}
	else if (EVENTCHnMUX == 1)
	{
		EVSYS.CH1MUX |= EVSYS_CHMUX_PORTx_PINn_gc;
	}
	else if (EVENTCHnMUX == 2)
	{
		EVSYS.CH2MUX |= EVSYS_CHMUX_PORTx_PINn_gc;
	}
	else if (EVENTCHnMUX == 3)
	{
		EVSYS.CH3MUX |= EVSYS_CHMUX_PORTx_PINn_gc;
	}
	else if (EVENTCHnMUX == 4)
	{
		EVSYS.CH4MUX |= EVSYS_CHMUX_PORTx_PINn_gc;
	}
	else if (EVENTCHnMUX == 5)
	{
		EVSYS.CH5MUX |= EVSYS_CHMUX_PORTx_PINn_gc;
	}
	
	if(INTnMASK == 0)
	{
		port->INT0MASK |= input_bm;
		port->INTCTRL |= PORT_INT0LVL1_bm | PORT_INT0LVL0_bm;
	}
	else
	{
		port->INT1MASK |= input_bm;
		port->INTCTRL |= PORT_INT1LVL1_bm | PORT_INT1LVL0_bm;
	}
}

//LimitSwitch::LimitSwitch(PORT_t* port, uint8_t input_bm, uint8_t EVENTCHnMUX, uint8_t INTnMASK, uint8_t EVSYS_CHMUX_PORTx_PINn_gc)
//:port(port), input_bm(input_bm), EVENTCHnMUX(EVENTCHnMUX), INTnMASK(INTnMASK), EVSYS_CHMUX_PORTx_PINn_gc(EVSYS_CHMUX_PORTx_PINn_gc)
//{
	//port->DIRCLR = input_bm;
	//
	//engaged = false;
	//
	//switch(input_bm)
	//{
		//case(PIN0_bm):
		//port->PIN0CTRL = PORT_ISC_RISING_gc;
		//break;
		//
		//case(PIN1_bm):
		//port->PIN1CTRL = PORT_ISC_RISING_gc;
		//break;
		//
		//case(PIN2_bm):
		//port->PIN2CTRL = PORT_ISC_RISING_gc;
		//break;
		//
		//case(PIN3_bm):
		//port->PIN3CTRL = PORT_ISC_RISING_gc;
		//break;
		//
		//case(PIN4_bm):
		//port->PIN4CTRL = PORT_ISC_RISING_gc;
		//break;
		//
		//case(PIN5_bm):
		//port->PIN5CTRL = PORT_ISC_RISING_gc;
		//break;
		//
		//case(PIN6_bm):
		//port->PIN6CTRL = PORT_ISC_RISING_gc;
		//break;
		//
		//case(PIN7_bm):
		//port->PIN7CTRL = PORT_ISC_RISING_gc;
		//break;
	//}
	//
	//if (EVENTCHnMUX == 0)
	//{
		//EVSYS.CH0MUX |= EVSYS_CHMUX_PORTx_PINn_gc;
	//}
	//else if (EVENTCHnMUX == 1)
	//{
		//EVSYS.CH1MUX |= EVSYS_CHMUX_PORTx_PINn_gc;
	//}
	//else if (EVENTCHnMUX == 2)
	//{
		//EVSYS.CH2MUX |= EVSYS_CHMUX_PORTx_PINn_gc;
	//}
	//else if (EVENTCHnMUX == 3)
	//{
		//EVSYS.CH3MUX |= EVSYS_CHMUX_PORTx_PINn_gc;
	//}
	//else if (EVENTCHnMUX == 4)
	//{
		//EVSYS.CH4MUX |= EVSYS_CHMUX_PORTx_PINn_gc;
	//}
	//else if (EVENTCHnMUX == 5)
	//{
		//EVSYS.CH5MUX |= EVSYS_CHMUX_PORTx_PINn_gc;
	//}
	//
	//if(INTnMASK == 0)
	//{
		//port->INT0MASK |= input_bm;
		//port->INTCTRL |= PORT_INT0LVL1_bm | PORT_INT0LVL0_bm;
	//}
	//else
	//{
		//port->INT1MASK |= input_bm;
		//port->INTCTRL |= PORT_INT1LVL1_bm | PORT_INT1LVL0_bm;
	//}
//}

//void LimitSwitch::interrupt_handler(void)
//{
//
	//md->motorOff();
	//md->set_step_boundary();
	//engaged = true;
//}
//
//void LimitSwitch::min_bound_interrupt_handler(void)
//{
	//if (md->get_direction() == 1)
	//{
		//md->motorOff();
		//md->set_min_step_boundary();
		//engaged = true;
	//}
//}
//
//void LimitSwitch::max_bound_interrupt_handler(void)
//{
	//if (md->get_direction() == 0)
	//{
		//md->motorOff();
		//md->set_max_step_boundary();
		//engaged = true;
	//}	
//}

bool LimitSwitch::get_status(void)
{
	if (port->IN & input_bm)
	{
		set_status();
	}
	else
	{
		clr_status();
	}
	return engaged;

}

void LimitSwitch::clr_status(void)
{
	engaged = false;
}

void LimitSwitch::set_status(void)
{
	engaged = true;
}
