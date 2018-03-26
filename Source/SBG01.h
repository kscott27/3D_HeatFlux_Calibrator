/*
 * SBG01.h
 *
 * Created: 3/2/2018 6:06:37 PM
 *  Author: Kevin
 */ 


#ifndef SBG01_H_
#define SBG01_H_

#include <avr/io.h>
#include "ADC.h"

class SBG01
{
	protected:
	
	ADC* adc;
	float voltage;
	uint8_t bytes_to_read[2];
	uint16_t read_word;
	float heat_flux;
	float amplification_ratio;
	float sensitivity;
	
	public:
	
	SBG01 (ADC* adc, float sensitivity);
	
	void reg_read (void);
	
	uint16_t get_voltage_bits (void);
	
	float get_voltage_mv (void);
	
	float get_voltage (void);
	
	float get_heat_flux(void);
};
	



#endif /* SBG01_H_ */