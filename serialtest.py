import serial

ctldataoff=[ord("A"),ord("0")]
ctldataon=[ord("A"),ord("1")]

if False:
    print("LED on")
    with serial.Serial('/dev/ttyUSB0',9600,timeout=1) as ser:
        ser.write(ctldataon)
    ser.close()
else:
    print("LED off")
    with serial.Serial('/dev/ttyUSB0',9600,timeout=1) as ser:
        ser.write(ctldataoff)
    ser.close()
