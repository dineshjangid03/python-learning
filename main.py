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
else :
    print("number less than or equal to 5")


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