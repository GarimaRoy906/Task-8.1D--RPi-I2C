#Garima Roy
#2110994840

#Importing the libraries
import smbus
import time

##I2C address for BH1750 sensor

# Default device I2C address
Address = 0x23

# Power On
Start = 0x01

# No active state
Stop = 0x00

# Reset data register value
Reset = 0x07

Sensor = 0x23
# To initiate the smbus library bus is used as a variable
bus = smbus.SMBus(1)

# Method to read the sensor's value
def light():
	address = bus.read_i2c_block_data(Address, Sensor)
	result = light_Convert(address)
	return result
	
def light_Convert(address):
	#convert 2 bytes of data to decimal
	convert = ((address[1] + (256 * address[0])) / 1.2)
	return int (convert)

#Main conditions and overall output
try:
	while 1:
		#To display the value
		intensity = light()
		
		print(f"Reading: {intensity}")
		
		#Printing instensity status
		print("Status:")
		if(intensity >= 400):           
			print("Too bright")
		elif(intensity >= 200 and intensity < 400):
			print("Bright")
		elif(intensity >= 50 and intensity < 200):
			print("Medium")
		elif(intensity > 20 and intensity < 50):
			print("Dark")
		elif(intensity < 20):
			print("Too dark")
			
		#Delay of 1 second
		time.sleep(1)

except KeyboardInterrupt:
	print("Quit")
