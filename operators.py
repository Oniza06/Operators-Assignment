# Arthemtic Operators 

# 1st Addition

x = 10
y = 5
print(x+y)

# 2nd Substraction
x = 15
y = 10
print(x-y)

# 3rd Modules Remainder

y = 10
print(y%2)

# 4th Exponentation 

x = 5
y = 2
print(x**y)

# 5th Multiplication *

x=5
print(x*10)

# 6th Division /

x = 8
print(x/3)

# 7th Floor Divsion //
x = 20
print(x//3)


# 2nd Assignment Operators it used to assign values to variables.

# 1st Add and Assign +=

x +=5
print(x)

# 2nd Substract and assign
y=20
x=x-y 
y-=2
print(y)

# 3rd multiplication and asign

num_num1 = 10
num_num1*=5
print(num_num1)

# 4th Divide and Assign /

num2_divide = 45
num2_divide/= 4
print(num2_divide)

# 5th Floor Divide and Assign // 

num3_fl_division = 50
num3_fl_division//=4
print(num3_fl_division)

# 6th modules remainder

num4_mod = 13
num4_mod%=2
print(num4_mod)

# 7th power and assign **

num5_pow = 10
num5_pow**=2
print(num5_pow)


# # 3rd membership operators are used to test whether a value exists in a sequence
# there are two membership operators 1-in 2-not in

names = ["Oniza", "Humaiara", "Hoorain"]
print("Sobia" not in names)

vegetables = ["Ladyfinger", "GreenChilli", "Capsicum"]
print("Ladyfinger" in vegetables)

cars_two = (1,2,3,4,5)
print(6 in cars_two)

# 4th identity operators are used to compare the meort location of two objects 
# in other words whether they are actually the same object (not just equal)
# there are two identity operators 1- is 2- is not

num1 = 100
num2 = 100
print(num1 is num2)


num3 = 2000
num4 = 2000
print(num3 is not num4)

name1 = "Oniza"
name2 = "Horrain"
print(name1 is not name2)

# 5th Comparison Operators  are used to compare two values they return a boolean
# value true or false.

# No. 01 == Checking type and value

a = 10
b = 20
print(a==b)


# nO. 02 >= checking value greater

C = 25
D = 30
print(C>=D)

# No. 03 <= checking value less than

A = 35
B = 30
print(A<=B)

# No. 4, 5  & 6  > Greater Than < Less than != not equal to

A_G =  40
A_L =  50
print(A_L>A_G)
print(A_G<A_L)
print(A_G!=A_L) 

# 5th Logical operator, are used to combine conditional statement, they also return 
# boolean

# 1 or returns True if at least one is true
# 2 not reverse the result
# 3 and returns true if both statments are true

logic_1 = 100
logic_2 = 200
print(logic_1 > 50 or logic_2 < 300)
print(not(logic_1 >  50))
print(logic_2>0 and logic_1<0)


# 6th bitwise operators, works at the binary level performing operators
# on the binary representatuibn of integar

AA = 100
BB = 100
print(AA&BB>0)
print(AA^BB<0)
print(AA<<BB<0)
print(AA>>BB>0)
print(AA|BB<0)





