

while True:
    # 1- input first number
    while True:
      try:
         first_number = float(input('enter first number '))
         break
      except ValueError:
            print('invalid input...please enter a numeric value ')
            


    # 2- input opreation type


    while True:
        try:
          opreation = input("enter opreation type ")
          if opreation in ("+", "-", "/", "*"):
              break
          else: 
            raise ValueError
        except ValueError:
            print("invalid opreation type....please enter (+,-,/,*)")




    # 3- input secondd number
    while True:
      try:
        second_number = float(input("enter secoend number "))
        if second_number == 0 and opreation == "/":
            raise ZeroDivisionError
        break
      except ValueError:
            print('invalid input...please enter a numeric value ')
      except ZeroDivisionError:
          print("math ERROR: cannot divide by zero....please enter a numeric value")
            
      
    # 4- print the result
    match opreation:
        case "+":
            result = first_number + second_number
        case "-":
            result = first_number - second_number
        case '/':
            result = first_number / second_number
        case "*":
            result = first_number * second_number
        case _:
            result = None

    
    if result != None:
        print("Result is:" , result)
    else:
        print("Unexpected Error")


    while True:
        try:
          repeat = input("do you want to perform another opreation ? (enter yes or no) ")
          if repeat == ("yes"):
              True
          elif repeat == ("no"):
              break
        except ValueError:
            print("invalid response...please enter ONLY yes or no")
        
    

    
    if repeat =="yes":
        True


    break

print("program exited")


            
                
        
        
