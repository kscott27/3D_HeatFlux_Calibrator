/*
 * SPI_Master.h
 *
 * Created: 1/26/2018 10:17:12 AM
 *  Author: crefvem
 */ 


#ifndef SPI_MASTER_H_
#define SPI_MASTER_H_

#include <avr/io.h>

typedef union SPI_packet
{
	uint8_t buffer[2];
	uint16_t data;
} SPI_packet_t;

class SPI_Master
{
	private:
	
	protected:
	SPI_t* interface;
	
	public:
	SPI_Master(SPI_t* interface);
	void set_mode(uint8_t SPI_mode);
	void start_transaction();
	void end_transaction();
	uint8_t send_and_receive(uint8_t len, uint8_t* out_data, uint8_t* in_data, uint16_t timeout=1000);
};


#endif /* SPI_MASTER_H_ */