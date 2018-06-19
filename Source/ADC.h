/*
 * ADC.h
 *
 * Created: 3/1/2018 11:39:19 PM
 *  Author: Kevin
 */ 


#ifndef ADC_H_
#define ADC_H_

#include <avr/io.h>

class ADC
{
	protected:
	
	uint16_t voltage_readout;
	float voltage_ref;
	ADC_t* interface;
	ADC_CH_t* interface_ch;
	
	public:
	
	ADC (ADC_t* interface, ADC_CH_t* interface_ch);
	
	void start_conv (void);
	
	uint8_t read (int16_t* read_sample, uint16_t timeout=1000);
	
	float get_voltage_ref (void);
};




#endif /* ADC_H_ */