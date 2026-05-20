try:
    number = int(input("Enter a number: "))
    print(f"Your number doubled is: {number * 2}")
    number = int(input("Enter a number: "))
    print(10 / number)
except ValueError:
    print("This does not work. Please only enter digits")
except ZeroDivisionError:
    print("Can't divide by zero!")