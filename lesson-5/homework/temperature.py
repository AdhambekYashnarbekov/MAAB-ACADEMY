def convert_cel_to_far(celsius):
	return celsius*1.8+32


def convert_far_to_cel(fahrenheit):
	return (fahrenheit-32)*(5/9)


int_fahrenheit=float(input("Enter a temperature in degrees F: "))
print(f"{int_fahrenheit} degrees F = {convert_far_to_cel(int_fahrenheit):.2f} degrees C" )

int_celsius=int(input("Enter a temperature in degrees C: "))
print(f"{int_celsius} degrees C = {convert_cel_to_far(int_celsius):.2f} degrees F")