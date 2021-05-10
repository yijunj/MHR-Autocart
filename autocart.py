import serial
import time

n = 10 # Number of carting
ser = serial.Serial('COM5')

seq_register_joycon = b'LL0000RR0100ll0000rr0100AA0100aa0100LN0000RN0000'
seq_joystick_neutral = b'LN0000RN0000'
seq_walk_to_coach = b'LR1000LN0000LU1000LN0000LR1000LN0000LU2000LN0000LR0500LN0000LU0500LN0000'
seq_talk_to_coach = b'AA0100aa1000AA0100aa1000DU0100du0100DU0100du0100AA0100aa0100AA0100aa2000ZR0100zr0100AA0100aa1000LE0100le0100DU0100du0100AA0100aa0100AA0100aa0100'
seq_cart = b'LL1200LN0000LU9000LN0000LU3000LN0000'
seq_back_from_cart = b'BB0100bb0100BB0100bb0100'

seq_back_to_hub = b'MI0100mi0100DU0100du0100AA0100aa0100'
ser.write(seq_back_to_hub)

for i in range(n):
    print('Estimated time remaining: {:n} minutes'.format((n-i)*2))
    print('Going on carting {:n} of {:n}...'.format(i+1, n))
    ser.write(seq_walk_to_coach)
    ser.write(seq_talk_to_coach)
    time.sleep(31)
    ser.write(seq_cart)
    time.sleep(70)
    ser.write(seq_back_from_cart)
    time.sleep(19)
    print('Done')
