# Calculation steps
# 1. Input number under the square root for this initial version I just worked with whole numbers (if you put in a negative it just makes it positive and puts i)
# 2. Subtract from the input number the largest square of a number that is <= it. This is the number before the decimal in the solution (38 > 36 -> 6 is the number)
# 3. Multiply the difference from step 2 by 100
# 4. Double the current value of the square root disgegarding the decimal (6.16 -> 616) and multiply by 10
# 5. Find the largest digit that can be added to the answer from step 4 and then multiplied by that same number
#    so that it is <= than the number from step 3 (if step 3 = 300 and the step 4 = 25 then 25 -> 250 -> 251 * 1 = 251 which is <= 300)
# 6. The digit found in step 5 is the next digit of the square root
# 7. Now subtract the answer from step 5 from the answer from step 4
# 8. Start the process over from step 3


import cmath

print("Input a number to find the square root manually:")

rootnum = 0
negflag = False

while True:
    try:
        rootnum = int(input())
        if(rootnum < 0):
            rootnum = -1 * rootnum
            negflag = True
        break
    except:
        print("\nInput must be an integer.")

print("Input the number of decimal places you want the root calculated to:")

# If the number reaches a point where it is perfect before it reaches the precision value the program will stop
precision = 0

while True:
    try:
        precision = int(input())
        break
    except:
        print("\nInput must be an integer.")

# rootstring holds a string representation of the final value so that it can be printed
rootstring = ""

precisioncount = 0

# Finding value before the decimal

x = 1

# represents the value of the sqrt without a decimal
currentsqrt = 0

while True:

    if x**2 == rootnum:
        currentsqrt = x
        print("You input a perfect square. Good job!")
        break

    elif x**2 > rootnum:
        currentsqrt = x-1
        break

    else:
        x += 1

rootstring = str(currentsqrt) + '.'

subvalue = rootnum - currentsqrt**2

while precision > precisioncount:

    subvalue *= 100

    comparevalue = currentsqrt * 20

    for i in range(9,-1,-1):
        
        x = (comparevalue + i) * i

        if(x <= subvalue):
            rootstring += str(i)
            currentsqrt = currentsqrt * 10 + i
            subvalue = subvalue - x
            break

    precisioncount += 1

    # Uncomment this and watch it build the square root digit by digit
    # print(currentsqrt)

rootstring += 'i' if negflag else ''

print(f"The square root of {rootnum} is:")

print(rootstring)

# This is weak in comparison
print(cmath.sqrt(-rootnum)) if negflag else print(cmath.sqrt(rootnum))

