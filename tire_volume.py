import math
from datetime import datetime
current_date_and_time = datetime.now()

width = float(input('Enter the width of the tire in mm (ex 205): '))
ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))


volume = math.pi * width**2 * ratio *(width * ratio + 2540 * diameter) /10000000000



print(f'The approximate volume is {volume:.2f} liters')

today = datetime.now()
today = f"{today: %Y-%m-%d}"

tires = input('Would you like to purchase tires with these dimensions?(yes or no) ')
if tires.lower() == 'yes':
    phone_number = float(input('What is your phone number so we can contact you? '))
    with open('volumes.txt', 'a') as volumes_file:
        volumes_file.write(f"\n{str(today)}, {width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume:.2f}, {phone_number:.0f}")
if tires.lower() == 'no':
    with open('volumes.txt', 'a') as volumes_file:
        volumes_file.write(f"\n{str(today)}, {width:.0f}, {ratio:.0f}, {diameter:.0f}, {volume:.2f}")