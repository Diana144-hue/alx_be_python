# prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter for the while loop
row = 0

#Use while loop to iterate through rows
while row < size:
    #Use for loop to print 'size' asterisks in one row
    for col in range(size):
        print("*", end=" ")
        print() #move to the next line after printing a row
        row += 1 #Increment the row counter
for i in range(1, size + 1):
    print("* " * i)
