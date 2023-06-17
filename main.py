# data type

# int
int_data = 10
print(type(int_data))

# float
float_data = 1.1
print(type(float_data))

# str
str_data = "hello world"
print(type(str_data))

# bool
bool_data = True
print(type(bool_data))


# typecasting

# int 
int_a = int(5.5)
int_b = int("5")

# float
float_a = float(5)
float_b = float("5.5")

# str
str_a = str(100)

# bool
bool_a = bool("True")
bool_b = bool(0)


# arithmetic operations + - * / %

add_num = 5 + 6

sub_num = 6 - 4

mult_num = 2 * 2

div_num = 6 / 2

remin = 6 % 5  # 1

num1 = 4
num2 = 2

num1_power_num2 = num1 ** num2


# comparison operations < > == <= >=   it will return boolean

comp1 = 6 < 10 # true
comp2 = 6 > 10 # false
comp3 = 6 == 6 # true
comp4 = 4 <= 4 # true
comp5 = 5 >= 2 # false


# logical operator  -> and, or

check1 = 6 > 5 or 6 == 6
check2 = 6 == 6 and 6 < 5


# conditional statement -> if, else

num = 6
if num > 5 :
    print("number is greater than 5")
elif num < 5 :
    print("number is less than 5")
else :
    print("num is 5")


# loop -> for , while

for i in range(10) :
    print(i) # 1 2 3 4 5 6 7 8 9

start = 5
end = 10
jump = 2

for i in range(start, end, jump) :
    print(i) # 5 7 9


j = 0
while(j < 10) :
    print(j) # 0 1 2 3 4 5 6 7 8 9
    j = j + 1


# List

marks = [5,10,9,7,8,6,4]

length_of_marks = len(marks)

element_1 = marks[0]
element_2 = marks[1]
element_n = marks[length_of_marks-1]

sub_list_1 = marks[3:] # 3rd index to n
sub_list_2 = marks[:5] # oth index to 5-1 index
sub_list_3 = marks[2:4] # 2nd index to 4-1 index

# iterate throw list

sum = 0
for i in marks:
    sum = sum + i

sum_1 = 0
for i in range(length_of_marks):
    sum_1 =sum_1 + marks[i]


# Strings

first_name = "Dinesh"
last_name = "Kumar"

full_name = first_name + last_name

sub_string = full_name[:6] # 0th index to 6-1 index


# functions

def check_prime(n):
    if n<2 :
        return False
    
    if n==2:
        return True
    
    for i in range(2,int(n/2)+1,1):
        if n%i == 0:
            return False
        
    return True

print(check_prime(12))


# var args in functions

def sum_of_n_number(*numbers):
    sum = 0
    for i in numbers:
        sum += i

    return sum

print(sum_of_n_number(2,6,5,8,4,5,5))

print(sum_of_n_number(2,6,5,8,4,5,5,10))


# variable scope

# global variable & local variable

global_variable = 20

print(global_variable)

def fun(n):

    sum_till_n = 0 # local variable we are not able to access it outside this function

    for i in range(1,n,1):
        sum_till_n += i

    print(sum_till_n)


# print(sum_till_n)  here if we try to access it will give an error

# so to make local variable as a global we ca use global keyword


def fun(n):

    global sum_Of_n # here this variable is in global scope we can access it outside this function
    sum_Of_n = 0 

    for i in range(1,n,1):
        sum_Of_n += i

    print(sum_Of_n)

fun(10)

print(sum_Of_n) # now we are able to access local variable of fun function because we make it as a global.
# one thing we have to mind that to access a global variable of method we have to call that method otherwise it will give an error


# input

s = input() # it will take input as a string only
print(s)

int_input = input()
int_input = int(int_input) # to take input as a int we have to type cast it
print(type(int_input))

float_input = float(input())
print(float_input)


# split method

demo_str = "My name is Dinesh Kumar"

splited_str = demo_str.split(" ") # split method will split string with the passed argument

print(splited_str) # ['My', 'name', 'is', 'Dinesh', 'Kumar']


# map

int_in_char = ['4', '5', '9', '7']
print(int_in_char) # ['4', '5', '9', '7']

map_to_int = list(map(int, int_in_char))
print(map_to_int) # [4, 5, 9, 7]

def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5, 6]

squared_numbers = list(map(square,numbers))
print(squared_numbers) # [1, 4, 9, 16, 25, 36]


# containers
# List

li = [1,2,3,4,5,6,7,8,9]

# len
length_of_li = len(li) # it will return the length of list

# append
li.append(10) # it will add element in list

# insert
li.insert(2,3) # it will add element at specific index

# count
count_of_three = li.count(3) # it will count how many time number occurred

# pop
li.pop() # it will delete last element of list


# Set

set_of_num = set() # set will store distinct element

set_of_num.add(1)
set_of_num.add(2)
set_of_num.add(2)
set_of_num.add(3)
set_of_num.add(4)

print(set_of_num) # 1 2 3 4

# Dictionary
# it will store elements in key value pair

students_marks = {
    "Ram" : 10,
    "Shyam" : 15,
    "Ramesh" : 12
}

print(students_marks) # {'Ram': 10, 'Shyam': 15, 'Ramesh': 12}

print(students_marks["Ram"])

for key in students_marks:
    print(key)
    print(students_marks[key])

for key,value in students_marks.items():
    print(key)
    print(value)


# printing

name = "Dinesh"
age = 23

print("my name is %s and age is %d." %(name, age))

print("my name is {} and age is {}." .format(name, age))

print("my name is", name, "and age is", age , sep=" ", end=".")
