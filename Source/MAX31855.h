/*
 * MAX31855.h
 *
 * Created: 2/27/2018 11:57:36 PM
 *  Author: Kevin
 */ 


#ifndef MAX31855_H_
#define MAX31855_H_

#include "SPI_Master.h"

class MAX31855
{
	private:
	SPI_Master* SPIM;
	uint8_t bytes_to_send[4] = {0};
	uint8_t bytes_received[4] = {0};
	PORT_t* cs_port;
	uint8_t cs_pin_bm;
	uint8_t status = 0;
	uint16_t temperature;
	uint16_t ref_temperature;
	
	protected:

	public:
	MAX31855(SPI_Master*, PORT_t* cs_port, uint8_t cs_pin_bm);
	
	void reg_write(uint8_t reg_address, uint8_t reg_data);
	
	void reg_read(void);
	
	uint16_t get_temp_cels(void);
	
	uint16_t get_temp_fahr(void);
	
};


#endif /* MAX31855_H_ */