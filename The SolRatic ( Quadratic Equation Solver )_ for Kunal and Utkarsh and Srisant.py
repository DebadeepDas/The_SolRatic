#The SolRatic

#Importing required libraries
import cmath
 
#What is cmath library?

'''This module provides access to mathematical functions for complex numbers. The functions in this module accept integers, floating-point numbers 
or complex numbers as arguments. They will also accept any Python object that has either a __complex__() or a __float__() method: these methods are 
used to convert the object to a complex or floating-point number, respectively, and the function is then applied to the result of the conversion.'''

#Introductory blocks of code
print("  Welcome to") #spacing between inverted commas for matching alignment and design scheme of the program
print(''' 'The SolRatic' ''') #spacing between inverted commas for matching alignment and design scheme of the program
print() #for creating a gap in the program

print('''The SolRatic is a program which can be used to solve simple quadratic equations in 'one variable' by implementing the mathematical method 
known as the Quadratic Formula. It is made of two words, 'Sol' taken from Solve and 'Ratic' taken from Quadratic''')

#Main Program Code

def SolRatic():
    print() #For creating a gap to format the layout
    #Displaying some standard introduction for quadratic equations
    print('''The standard form of a quadratic equation is:
ax2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0
    
The formula used to get the solutions of a quadratic equation, called the Quadratic Formula is:

x =  (-b±√(b²-4ac))/(2a)
    
The discriminant of a quadratic formula is the section under the radical. 
It tells us the number of real solutions for a given quadratic equation''')

    print() #For creating a gap to format the layout
    
    #Getting the inputs of the coefficients from the user for solving the equation

    coff_a = int(input("Give the value of a: "))
    coff_b = int(input("Give the value of b: "))
    coff_c = int(input("Give the value of c: "))

    #The block of code that does the main function of getting the roots/solutions of the equation

    #Code to calculate the discriminant
    d = (coff_b**2) - (4*coff_a*coff_c)
    
    print() #For creating a gap to format the layout
    #Displaying the discriminant of the equation
    print("The discriminant of the equation is:", d)

    #Using the Quadratc Formula using cmath library
    #Finding two solutions of the equation ( As they will be -ve and +ve )

    sol1 = (-coff_b-cmath.sqrt(d))/(2*coff_a)
    sol2 = (-coff_b+cmath.sqrt(d))/(2*coff_a)

    #Provinding information whether the roots are real, equal or imaginary/complex

    if d > 0:
        print() #For creating a gap to format the layout
        print("The roots/solutions of the equation are:", sol1,sol2)
        print("The roots/solutions are real")
    elif d == 0:
        print() #For creating a gap to format the layout
        print("The roots/solutions of the equation are:", sol1,sol2)
        print("The roots/solutions are equal")
    elif d < 0:
        print() #For creating a gap to format the layout
        print("The roots/solutions of the equation are:", sol1,sol2)
        print("The roots/solutions are imaginary")


    #Creating a conditional loop for easy continuation of the program
    
    A=input("Would you like to continue? [ y/n ]:")
    if A == "y" or A == "Y":
        SolRatic()
    elif A == "n" or A == "N":
        print() #For creating a gap to format the layout
        print("Thank You for using our Program. We hope you found it useful!")
        exit()
    else:
        print("Invalid input by User")

SolRatic()