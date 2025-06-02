# # a=[6,3,4,7,1,0,89,2,5,8,9]

# # print(len(a))  # Length of the list
# # print(max(a))  # Maximum value in the list

# a={1,3,3,5,5,6,1}
# print(a)
# for element in a:
#     print(element*2)
    
# marks={'Lakshay': 90, 'Rohan': 80, 'Aman': 85}
# print(marks['Lakshay'])  # Accessing value by key 
# def average(marks):
#     total = 0
#     for mark in marks.values():
#         total += mark
#     return total / len(marks)
def greet():
    print("Hello, welcome to the function!")
    
greet()  # Calling the function    
def sum_of_list(a):
    print("calculating:")
    return sum(a)

marks=[45,66,78,435]
sum_of_marks=sum_of_list(marks)
print("Sum of marks:", sum_of_marks)