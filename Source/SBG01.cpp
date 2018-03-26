/*
 * SBG01.cpp
 *
 * Created: 3/2/2018 6:07:01 PM
 *  Author: Kevin
 */ 

#include "SBG01.h"

//-------------------------------------------------------------------------------------
/** This constructor creates an SBG01 heat flux sensor object.
 *  @param adc A pointer to an ADC object used to interface with the hardware
 *  @param sensitivity A constant value which represents the linear correlation between
     sensor output voltage and the heat flux input
 */
SBG01::SBG01(ADC* adc, float sensitivity)
      :adc(adc), sensitivity(sensitivity)
{
	amplification_ratio = 67.1;
}

//-------------------------------------------------------------------------------------
/** This method calls the ADC read method and passes it a memory location to store the
    sample in
 */
void SBG01::reg_read (void)
{
	adc->read(&read_word);	
}

//-------------------------------------------------------------------------------------
/** This method returns the result of reg_read after converting it to volts
 */
float SBG01::get_voltage (void)
{
	reg_read();
	uint16_t voltage_bits = read_word;
	float voltage_ref = adc->get_voltage_ref();
	voltage = voltage_bits * voltage_ref / (4096 * amplification_ratio);
	
	return voltage;
}

//-------------------------------------------------------------------------------------
/** This method returns the result of reg_read
 */
uint16_t SBG01::get_voltage_bits (void)
{
	reg_read();
	return read_word;
}

//-------------------------------------------------------------------------------------
/** This method returns the result of get_voltage after converting it to millivolts
 */
float SBG01::get_voltage_mv (void)
{
	get_voltage();
	return voltage*1000;
}

//-------------------------------------------------------------------------------------
/** This method returns the result of get_voltage after converting it to heat flux
 */
float SBG01::get_heat_flux(void)
{
	voltage = get_voltage();
	
	heat_flux = voltage / sensitivity;
	return heat_flux;
}