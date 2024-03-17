first_number= input('Enter your first number')
second_number= input('enter your second  number ')
operator= input('enter your operator (+,-,%,*,/)')
first= int(first_number)
second= int(second_number)

if operator == "+" :
    print(first + second )

elif operator == "-" :
    print(first - second)

elif  operator == "/"  :
    print(first / second)

elif operator == "*" :
    print(first *second )
    
elif operator == "%" :
    print(first % second)

else:
    print("Invalid operand")