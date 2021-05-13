"""
This program will display student grades on a final exam. The first option will display the number of grades. 
The second option will display the average grade. And the third option will display the percentage of grades 
that are above average. There will be three functions total. The first function will initialize the application. 
The second function will calculate the percentage above average. The third function will calculate the percentage 
of grades above average.

Funtion 1 will initialize the application
Function 2 will sum all the grades/ number of grades
Function 3 will sum all grades above average.

It will output the percentage above average. After the code has ran, it will output the percentage of grades that
are above average.
"""

"""
# function1
  add total number of grades

# function2 
  add sum of all grades / total number of grades

# function3
  n*100 / len(grades)

#main
"""
infile = open("Final (1).txt")
grades = [line.rstrip() for line in infile]
infile.close()
for i in range(len(grades)): 
  grades[i] = int(grades[i])
average = sum(grades) / len(grades)
num = 0
for grade in grades:
  if grade > average:
    num += 1
print("Number of grades:", len(grades)) 
print("Average grade:", average)
print("Percentage of grades above average: {0:.2f}%" 
                    .format(100 * num / len(grades)))


