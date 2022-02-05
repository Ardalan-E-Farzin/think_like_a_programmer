#this is a solution in pyhton for LUHN CHECKSUM VALIDATION in Think like a programmer book!

#Taking an input from a user and turning it into a list.
inputcheck = True
while inputcheck:
    number = input("give me a 7 digit number: ")
    if len(number) != 7:
        print("just 7 digits")
    else:
        inputcheck = False

divider = list(number.strip())

#duplicate every other number in the input
values = []
for i in divider:
    if divider.index(i) == 0:
        values.append(i)
    elif divider.index(i) % 2 == 0:
        values.append(i)
    else:
        dup = int(i)*2
        if dup >= 10:
            values.append(str((dup//10)+(dup % 10)))
        else:
            values.append(str(dup))

#sumup the result
final_number = 0
for numbers in values:
    final_number += int(numbers)


#printing the result
if final_number % 10 == 0:
    print(f"THE RESULT WAS {final_number}.\nIT DID PASSED THE TEST!")
else:
    print(f"THE RESULT WAS {final_number}.\nDID NOT PASSED THE TEST!")