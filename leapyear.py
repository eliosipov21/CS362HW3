'''
How to run the file: 
simply run the command: python ilya_osipov_hw1.py in the command line (or python3 ilya_osipov_hw1.py)
'''


x = 0
while(x == 0):
    val = input("Enter a integer: \n")
    try: 
        year = int(val)
        x += 1
    except ValueError:
        print("That's not an int!")

if(year % 4 == 0): 
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("This is a leap year")
        else: 
            print("This is not a leap year")
    else: 
        print("This is a leap year")
else: 
    print("This is not a leap year")

