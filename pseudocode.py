def square():
    side = int(input("Enter the side length of the square: "))
    Squarea = side * side
    print("The area of the square is:", Squarea)

def rectangle():
    length = int(input ("Enter the length of the rectangle: "))
    width = int(input ("Enter the width of the rectangle: "))
    area_of_rectangle= length * width
    print("The area of the rectangle is:", area_of_rectangle)

def circle():
    r = int(input("Enter the radius of the circle: "))
    area_of_circle = 3.14 * r ** 2
    print("The area of the circle is:", area_of_circle)
  
def triangle():
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    area_of_triangle = base * height / 2
    print("The area of the triangle is:", area_of_triangle)
  
def mainMenu():
    UserChoice = input("would you like to calculate for square (s), rectangle (r), triangle (t), or circle (c):")
    if (UserChoice == 's'):
        square()
    elif (UserChoice == 'r'):
        rectangle()
    elif (UserChoice == 'c'):
        circle()
    elif (UserChoice == 't'):
        triangle()
    else:
        print("Input choice invalid. Please choose another letter.")

mainMenu()

