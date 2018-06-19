//**************************************************************************************
/** \file task_user.h
 *    This file contains header stuff for a user interface task for a ME507/FreeRTOS
 *    test suite. 
 *
 *  Revisions:
 *    \li 09-30-2012 JRR Original file was a one-file demonstration with two tasks
 *    \li 10-05-2012 JRR Split into multiple files, one for each task
 *    \li 10-25-2012 JRR Changed to a more fully C++ version with class task_user
 *    \li 11-04-2012 JRR Modified from the data acquisition example to the test suite
 *
 *  License:
 *    This file is copyright 2012 by JR Ridgely and released under the Lesser GNU 
 *    Public License, version 2. It intended for educational use only, but its use
 *    is not limited thereto. */
/*    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
 *    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
 *    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
 *    ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
 *    LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUEN-
 *    TIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS 
 *    OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
 *    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
 *    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
 *    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. */
//**************************************************************************************

// This define prevents this .h file from being included multiple times in a .cpp file
#ifndef _TASK_MD_H_
#define _TASK_MD_H_

#include <stdlib.h>                         // Prototype declarations for I/O functions

#include "FreeRTOS.h"                       // Primary header for FreeRTOS
#include "task.h"                           // Header for FreeRTOS task functions
#include "queue.h"                          // FreeRTOS inter-task communication queues

#include "ansi_terminal.h"

#include "rs232int.h"                       // ME405/507 library for serial comm.
#include "time_stamp.h"                     // Class to implement a microsecond timer
#include "frt_task.h"                       // Header for ME405/507 base task class
#include "frt_queue.h"                      // Header of wrapper for FreeRTOS queues
#include "frt_text_queue.h"                 // Header for a "<<" queue class
#include "frt_shared_data.h"                // Header for thread-safe shared data

#include "shares.h"                         // Global ('extern') queue declarations

#include "DM542T.h"
#include "Timer.h"
#include "InterruptTimer.h"
#include "LimitSwitch.h"

/// This macro defines a string that identifies the name and version of this program. 
#define PROGRAM_VERSION		PMS ("ME405 base radio program V0.4 ")


//-------------------------------------------------------------------------------------
/** This task interacts with the user for force him/her to do what he/she is told. What
 *  a rude task this is. Then again, computers tend to be that way; if they're polite
 *  with you, they're probably spying on you. 
 */

class task_md : public frt_task
{
private:
	// No private variables or methods for this class

protected:

    DM542T* md;
	LimitSwitch* LS_min;
	LimitSwitch* LS_max;
	uint32_t travel_time_ms;
    int32_t steps;
	int32_t step_diff;
	uint16_t current_node;
	frt_queue<uint32_t>* locations;
    float inch_to_step;
	float step_to_inch;
    uint16_t current_destination;
	shared_data<bool>* motor_complete;
	Timer* timer;
	shared_data<uint8_t>* motor_operator;
	bool limit_switch;
	uint16_t microstep_scaler;
	int32_t step_destination;
	bool motor_on;
	frt_queue<uint32_t>* max_velocity;
	
	// This method displays a simple help message telling the user what to do. It's
	// protected so that only methods of this class or possibly descendents can use it
	void print_help_message (void);

	// This method displays information about the status of the system
	void show_status (void);

public:

    const char* task_name;
	
	// This constructor creates a motor driver task object
	task_md (const char*, unsigned portBASE_TYPE, size_t, emstream*, DM542T* md, LimitSwitch* LS_min, LimitSwitch* LS_max,
	frt_queue<uint32_t>* locations, frt_queue<uint32_t>* max_velocity, shared_data<uint8_t>* motor_operator, shared_data<bool>* motor_complete,
	uint16_t microstep_scaler);

	/** This method is called by the RTOS once to run the task loop for ever and ever.
	 */
	void run (void);
	
	void take_step (void);
	
	void set_signal_low (void);
	
	void reset_device(void);
	
	bool motorOn(void);
	
	void motorOff(void);
};

#endif // _TASK_MD_H_
