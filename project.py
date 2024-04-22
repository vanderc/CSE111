import math

def main():
    """Get the users input"""
    print("""
          Welcome To My Calculator""")

    print("""
          To calculate the perimeter of a triangle (enter 1)
          To calculate the area of a triangle (enter2)
          To calculate the volume of a triangel (enter 3)
          To calculate the area of a circle (enter 4)
          To calculate the circumference of a circle (enter 5)
          To calculate the perimeter of a square (enter 6)
          To calculate the area of a square (enter 7)
          To calculate the perimeter of a rectangle (enter 8)
          To calculate the area of a rectangle (enter 9)
          To calculate the square root of a number (enter 10)
          To convert fahrenheit to celsius (enter 11)
          To convert celsius to fahrenheit (enter 12)
          To convert celsius to kelvin (enter 13)""")
    try:
        user_choice = float


        while user_choice != 0:
            user_choice = int(input('\nEnter your choice of calculations (1-13) enter 0 to end the program: '))

            if user_choice == 1:
                side_a = float(input('Enter the first side of the triangele: '))
                base_c = float(input('Enter the base: '))
                side_b = float(input('Enter the second side of the triangle: '))
                
                perimeter_tri = perimeter_triangle(side_a, base_c, side_b)

                print(f'Perimeter = {perimeter_tri:.2f}')


            elif user_choice == 2:
                base_t = float(input('Enter the base of the triangle: '))
                triangle_height = float(input('Enter the height of the triangle: '))

                area_tri = area_triangle(base_t, triangle_height)

                print(f'Area = {area_tri:.2f}')

            
            elif user_choice == 3:
                   vol_base = float(input('Enter the triangle base: '))
                   vol_height = float(input('Enter the triangle height: '))
                   length =float(input('Enter the triangle length: '))

                   volume_tri = volume_triangle(vol_base, vol_height, length)

                   print(f'Volume = {volume_tri:.2f}')



            elif user_choice == 4:
                 radius_a = float(input('Enter the radius of the circle: '))

                 circle_area = area_circle(radius_a)

                 print(f'Area = {circle_area:.2f}')

            
            elif user_choice == 5:
                   radius = float(input('Enter the radius of the circle: '))

                   circumference_circ = circumference_circle(radius)

                   print(f'Circumference = {circumference_circ:.2f}')



            elif user_choice == 6:
                 side = float(input('Enter the side of the square: '))

                 perimeter_square = p_square(side)

                 print(f'Perimeter = {perimeter_square:.2f}')



                      
            elif user_choice == 7:
                 sides = float(input('Enter the side of the square: '))

                 square_area = area_square(sides)

                 print(f'Area = {square_area:.2f}')


                      
            elif user_choice == 8:
                 rect_length = float(input('Enter the length of the rectangle: '))
                 width = float(input('Enter the width of the rectangle: '))

                 rectangle_p = p_rectangle(rect_length, width)

                 print(f'Perimeter = {rectangle_p:.2f}')

                      
            
            elif user_choice == 9:
                 area_length = float(input('Enter the length of the rectangle: '))
                 area_width = float(input('Enter the width of the rectangle: '))

                 rectangle_area = area_rectangle(area_length, area_width)

                 print(f'Area = {rectangle_area:.2f}')

                      
            
            elif user_choice == 10:
                 number = float(input('Enter the desired number to square root: '))

                 square_number = square_root(number)

                 print(f'Square root = {square_number:.2f}')


            elif user_choice == 11:
               
                 f_temp = float(input('Enter in \u00b0Farenheit: '))

                 c_temperature = c_conversion(f_temp)

                 print(f'Celsius = {c_temperature:.2f}\u00b0C')


            elif user_choice == 12:
                 
                 c_temp = float(input('Enter in \u00b0Celsius: '))

                 f_temperature = conversion(c_temp)

                 print(f'Fahrenheit = {f_temperature:.2f}\u00b0F')


            elif user_choice == 13:
                 print('Enter the temperature in Celsius: ')
                 cel_temp = float(input('Enter in \u00b0Celsius: '))

                 cel_temperature = k_conversion(cel_temp)

                 print(f'Kelvin = {cel_temperature:.2f}\u00B0K')



            elif user_choice > 13 or user_choice < 0:
                 print('\nYou entered an invalid option choose between (1-13) Enter 0  to exit program.')
    
    except ValueError as val_err:
         # This will happen if the user enters an invalid integer
         print()
         print(type(val_err).__name__, val_err, sep=": ")
         print('You entered an invalid integer or decimal for the section to input a value.')
         print("Run the program again and enter an integer or decimal" \
               " as prompted.")
    
    except Exception as excep:
         # This will happen if other type of execution occurs
         print()
         print(type(excep).__name__, excep, sep=": ")


def perimeter_triangle(side_a, base_c, side_b):
     # Computes and returns the perimeter of a triangle
     perimeter = side_a + base_c + side_b

     return perimeter

def area_triangle(base_t, triangle_height):
     # Computes and returns the area of a triangle
     area = (base_t * triangle_height) / 2

     return area

def volume_triangle(vol_base, vol_height, length):
     # Computes and returns the volume of a triangle
     vol = 0.5 * vol_base * vol_height * length

     return vol

def circumference_circle(radius):
     # Computes and returns the circumference of a circle
     c = 2 * (math.pi * radius)

     return c

def area_circle(radius_a):
     # Computes and returns the area of a circle
     area = math.pi * (radius_a ** 2)

     return area

def p_square(side):
     # Computes and returns the perimeter of a square
     perimeter = 4 * side

     return perimeter

def area_square(sides):
     # Computes and returns the area of a square
     area = sides ** 2

     return area

def p_rectangle(rect_length, width):
     # Computes and returns the perimeter of a rectangle
     perimeter = 2 * (rect_length) + 2 * (width)

     return perimeter

def area_rectangle(area_length, area_width):
     # Computes and returns the area of a rectangle
     area = area_width * area_length

     return area

def square_root(number):
     # Compustes and returns the square root of a number
     square_root = math.sqrt(number)

     return square_root

def c_conversion(f_temp):
     # Converts fahrenheit into celcius
     celsius = (f_temp - 32) * (5/9)

     return celsius

def conversion(c_temp):
     # Converts celcius into fahrenheit
     fahrenheit = c_temp * (9/5) + 32

     return fahrenheit

def k_conversion(cel_temp):
     # Converts celcius into kelvin
     kelvin = (cel_temp + 273.15)

     return kelvin


if __name__ == "__main__":
     main()