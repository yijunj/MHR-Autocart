import serial

ser = serial.Serial('COM5')

seq_register_joycon = b'LL0000RR0100ll0000rr0500AA0100aa0100LN0000RN0000'

ser.write(seq_register_joycon)
