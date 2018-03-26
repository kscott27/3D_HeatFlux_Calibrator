/*
 * SPI_Master.cpp
 *
 * Created: 1/26/2018 10:17:25 AM
 *  Author: crefvem
 */ 
#include "SPI_Master.h"

//-------------------------------------------------------------------------------------
/** This constructor creates a SPI Master object.
 *  @param interface A pointer to an SPI struct used to interface with the hardware
 *  @param cs_port A pointer to the port where the chip select pin is located
 *  @param cs_pin_bm A bit-mask indicating which pin on the port is used for the chip
 *  select line
 */
SPI_Master::SPI_Master(SPI_t* interface)
:interface(interface)
{	
	
#ifdef SPIC
	if (interface == &SPIC)
	{
		PORTC.DIRSET = PIN4_bm | PIN5_bm | PIN7_bm;
		PORTC.DIRCLR = PIN6_bm;
		PORTC.OUTSET = PIN4_bm;
		PORTC.PIN6CTRL |= PORT_OPC_PULLUP_gc;
	}
#endif		

#ifdef SPID
	if (interface == &SPID)
	{
		PORTD.DIRSET = PIN4_bm | PIN5_bm | PIN7_bm;
		PORTD.DIRCLR = PIN6_bm;
		PORTD.OUTSET = PIN4_bm;
		PORTD.PIN6CTRL |= PORT_OPC_PULLUP_gc;
	}
#endif		
	
	interface->CTRL = (SPI_ENABLE_bm | SPI_MASTER_bm | SPI_PRESCALER_DIV128_gc | SPI_MODE_0_gc);
};

//-------------------------------------------------------------------------------------
/** This method changes the SPI mode setting
 *  @param SPI_mode A bit-mask indicating the SPI mode desired (MODE 0-3)
 */
void SPI_Master::set_mode(uint8_t SPI_mode)
{
	interface->CTRL = (interface->CTRL & ~SPI_MODE_gm) | (SPI_mode & SPI_MODE_gm);
}

//-------------------------------------------------------------------------------------
/** This method begins an SPI transaction by lowering the chip select line
 */
void SPI_Master::start_transaction()
{
};


//-------------------------------------------------------------------------------------
/** This method ends an SPI transaction by raising the chip select line
 */
void SPI_Master::end_transaction()
{
};

//-------------------------------------------------------------------------------------
/** This method sends an array of bytes to the SPI device and returns the bytes received from the device
 *  @param len The number of bytes to be sent to the SPI device
 *  @param out_data A pointer to an array of bytes to be sent out
 *  @param in_data A pointer to an array of bytes to store the incoming data
 *	@param timeout 
 */
uint8_t SPI_Master::send_and_receive(uint8_t len, uint8_t* out_data, uint8_t* in_data, uint16_t timeout)
{
	volatile uint16_t counter;
	for (int i=len-1;i>=0;i--)
	{
		counter = timeout;
		interface->DATA = out_data[i];
		while ((--counter != 0) && ((interface->STATUS & SPI_IF_bm) != SPI_IF_bm)){ }
		if(counter == 0)
		{
			return 0;
		}
		
		//counter = timeout;
		in_data[i] = interface->DATA;
		//while ((counter-- != 0) && ((interface->STATUS & SPI_IF_bm) != SPI_IF_bm)){ }
	}
	
	return 1;
};