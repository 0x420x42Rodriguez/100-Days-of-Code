# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Don't use the sum() or len() functions
#Write your code below this row 👇

sum_of_height = 0
number_of_students = 0

for i in student_heights:
    number_of_students += 1  # Count the number of students in the provided list
    sum_of_height += int(i)

average_height = round(sum_of_height / number_of_students) 
print(average_height)