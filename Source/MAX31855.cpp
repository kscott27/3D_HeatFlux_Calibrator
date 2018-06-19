/*
 * MAX31855.cpp
 *
 * Created: 2/27/2018 11:58:06 PM
 *  Author: Kevin
 */ 

#include "MAX31855.h"

//-------------------------------------------------------------------------------------
/** This constructor creates an object to use when interacting with the SPI registers on the MAX31855
    Thermocouple Analog to Digital Converter chip.
 *  @param SPIM A pointer to an SPI_master object
 */
MAX31855::MAX31855(SPI_Master* SPIM, PORT_t* cs_port, uint8_t cs_pin_bm)
         :SPIM(SPIM),cs_port(cs_port),cs_pin_bm(cs_pin_bm)
{
	cs_port->DIRSET = cs_pin_bm;
	cs_port->OUTCLR = cs_pin_bm;
};

void MAX31855::reg_write(uint8_t reg_address, uint8_t reg_data)
{
	bytes_to_send[2] = 0b01000000; // OPCODE to write
	bytes_to_send[1] = reg_address; // ADDRESS
	bytes_to_send[0] = reg_data; // DATA
	
	SPIM->set_mode(SPI_MODE_0_gc);
	
	cs_port->OUTCLR = cs_pin_bm;
	status = SPIM->send_and_receive(3,bytes_to_send,bytes_received);
	cs_port->OUTSET = cs_pin_bm;
};

void MAX31855::reg_read(void)
{
	bytes_to_send[3] = 0b10010010;
	bytes_to_send[2] = 0b01001101;
	bytes_to_send[1] = 0b01000001; // OPCODE to read
	bytes_to_send[0] = 0b11111111; // ADDRESS
	
	SPIM->set_mode(SPI_MODE_0_gc);
	
	cs_port->OUTCLR = cs_pin_bm;
	status = SPIM->send_and_receive(4,bytes_to_send,bytes_received);
	cs_port->OUTSET = cs_pin_bm;
};

uint16_t MAX31855::get_temp_cels(void)
{
	reg_read();
	temperature = (((uint16_t) bytes_received[3] << 8) | ((uint16_t) bytes_received[2])) >> 4;
	
	return temperature;
}

uint16_t MAX31855::get_temp_fahr(void)
{
	reg_read();
	temperature = (((uint16_t) bytes_received[3] << 8) | ((uint16_t) bytes_received[2])) >> 4;
	temperature = temperature * 1.8 + 32;
	
	return temperature;
}
