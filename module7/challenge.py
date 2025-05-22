from traceback import print_tb

from module7.ExampleTypeCasting import resultati


def calculate(nr1,nr2,operator):
    if operator=="+":
        return nr1+nr2
    elif operator=="-":
        return nr1-nr2
    elif operator=="*":
        return nr1*nr2
    elif operator=="/":
        return nr1/nr2
    else:
        raise ValueError("Invalid operation")


try:
    num1=float(input("Enter the first number:"))
    num2= float(input("Enter the second"))
    operator=input("Enter an operation:+,-,*,/")
    resultati=calculate(num1,num2,operator)
    print(f"The result of {num1} {operator} {num2}:{resultati}")

except ValueError as e:
    print(f"Invalid {e}")

except ZeroDivisionError as e:
    print(f"Cannot devide by zero {e}")

except Exception as e:
    print(f"Error: {e}")

finally:
    print("End of program")