/*
 * ADC.cpp
 *
 * Created: 3/1/2018 11:39:36 PM
 *  Author: Kevin
 */ 


#include "ADC.h"

//-------------------------------------------------------------------------------------
/** This constructor creates an ADC object.
 *  @param interface A pointer to an ADC struct used to interface with the hardware
 *  @param cs_port A pointer to an ADC Channel struct used to set registers
 *   specific to a given channel
 */
ADC::ADC(ADC_t* interface, ADC_CH_t* interface_ch)
:interface(interface), interface_ch(interface_ch)
{
	// Set the enable and flush pipeline bits
	interface->CTRLA = 1 << 0 | 1 << 1 | 1 << 2;
	
	// Set the ADC for Conversion Mode, which allows signed readings. This is necessary
	// for differential input with gain mode.
	interface->CTRLB = ADC_IMPMODE_bm | ADC_CONMODE_bm;
	
	// Set the single-ended input bit
	interface->CH0.CTRL = ADC_CH_GAIN_32X_gc | ADC_CH_INPUTMODE_DIFFWGAIN_gc;

	// Set the reference voltage to be VCC/1.6
	interface->REFCTRL = ADC_REFSEL_INT1V_gc;
	
	// Declare which pins the ADC will be reading
	interface->CH0.MUXCTRL = ADC_CH_MUXPOS_PIN0_gc | ADC_CH_MUXNEG_PIN4_gc;

	voltage_ref = 1;
}

//-------------------------------------------------------------------------------------
/** This method initiates an ADC sample
 */
void ADC::start_conv (void)
{
	interface->CH0.CTRL |= ADC_CH_START_bm;
}

//-------------------------------------------------------------------------------------
/** This method reads the ADC result register
 *  @param read_sample A pointer to a word that this ADC driver can store its result in
 *  @param timeout Amount of clock cycles before this function will exit without the
     ADC Interrupt flag being raised
 */
uint8_t ADC::read (int16_t* read_sample, uint16_t timeout)
{
	volatile uint16_t counter;
	counter = timeout;
	start_conv();
	while ((--counter != 0) && ((interface->CH0.INTFLAGS & (1 << 0)) != (1 << 0))){ }
	if(counter == 0)
	{
		return 0;
	}
		
	int16_t reg_value = interface->CH0.RES;
	*read_sample = reg_value;
	return 1;
}

//-------------------------------------------------------------------------------------
/** This method returns the voltage reference member data
 */
float ADC::get_voltage_ref (void)
{
	return voltage_ref;
}
