# # # # # # # #Write a program that reads two no. from keyboard and gives 
# # # # # # # # their sum,addition,substraction,multiplication,division,module

# # # # # # # # def calc(n,m):
# # # # # # # #  a = int(input("Enter first digit "))
# # # # # # # #  b = int(input("Enter second digit "))
# # # # # # # #  print(a+b,a-b,a*b,a/b,a%b)
# # # # # # # # calc(4,5)

# # # # # # # #write a program to find area of triangle

# # # # # # # # def area(x,y):
# # # # # # # #  height = int(input("Enter height : "))
# # # # # # # #  base = int(input("Enter base : "))
# # # # # # # #  Area = (height*base)*0.5
# # # # # # # #  print("Area is ",Area)
# # # # # # # # area(2,4)

# # # # # # # #calculate simple interest 

# # # # # # # # def simple_interest(x,y):
# # # # # # # #     principal_amount = int(input("Enter principle amount : "))
# # # # # # # #     rate_of_interest = int(input("Enter rate of interest : "))
# # # # # # # #     No_Of_Years = int(input("Enter Number of years ; "))
# # # # # # # #     Simple_interest = (principal_amount*rate_of_interest*No_Of_Years)/100
# # # # # # # #     print("Simple interest is : ",Simple_interest)
# # # # # # # # simple_interest(2,3) 

# # # # # # # #interchange two numbers(with and without temp variable)

# # # # # # # # a = 10 
# # # # # # # # b = 20
# # # # # # # # print("A : ",a, "B : ",b)
# # # # # # # # # temp = a
# # # # # # # # # a = b
# # # # # # # # # b = temp
# # # # # # # # # print("A : ",a,"B : ",b)

# # # # # # # # #without 
# # # # # # # # b = b-a
# # # # # # # # a = a+b
# # # # # # # # print("A : ",a,"B : ",b)

# # # # # # # #write a program to find enter number is positive , negative , or Zero

# # # # # # # # number = float(input("Enter any number "))
# # # # # # # # if number > 0:
# # # # # # # #     print("number positve")
# # # # # # # # elif number < 0:
# # # # # # # #     print("Number negative")
# # # # # # # # else:
# # # # # # # #     print("number zero")

# # # # # # # #To check character is capital or small or digit and special character

# # # # # # # # def check_character(character):
# # # # # # # #     if character.isupper():
# # # # # # # #         print("Enter character is upper ")
# # # # # # # #     elif character.islower():
# # # # # # # #         print("Enter character is lower")
# # # # # # # #     elif character is not character.isupper() and character is not character.lower():
# # # # # # # #         print("special character or digit")

# # # # # # # # user_input = input("Enter character : ")
# # # # # # # # if len(user_input) == 1 and user_input.isalpha():
# # # # # # # #     check_character(user_input)
# # # # # # # # elif len(user_input) ==1 and  user_input is not user_input.isupper() and user_input is not user_input.islower():
# # # # # # # #     check_character(user_input) 
# # # # # # # # else:
# # # # # # # #     print("Please enter single alphabate character ")


# # # # # # # #write a program to sum 1+1/2+1/3+....+1/n

# # # # # # # # # n = int(input("Enter number "))
# # # # # # # # # add = 0
# # # # # # # # # for i in range(1,n+1):
# # # # # # # # #     add = add + 1/i
# # # # # # # # # print(add)

# # # # # # # # #Find Factorial of number 


# # # # # # # # def fact(n):
# # # # # # # #     Factorial = 1
# # # # # # # #     for i in range(1,n+1):
# # # # # # # #         if n == 0 or n == 1:
# # # # # # # #             return 1
# # # # # # # #         else:
# # # # # # # #             Factorial*=i
# # # # # # # #     return Factorial
        
# # # # # # # # num = int(input("Enter number "))
# # # # # # # # result = fact(num)
# # # # # # # # if num<0:
# # # # # # # #     print("Not define")
# # # # # # # # else:
# # # # # # # #     print(f"The factorial of {num} is {result}")

# # # # # # # #print series of fibbonacci series of nth term

# # # # # # # # def fib(n):
# # # # # # # #     a,b =0,1
# # # # # # # #     for _ in range(0,n):
# # # # # # # #         print(a,end=" ")

# # # # # # # #         a,b = b,a+b
  
# # # # # # # # number = int(input("enter nth term "))    
# # # # # # # # fibbo = fib(number)  


# # # # # # # # #Write a program to reverse a number

# # # # # # # # def reversse(number):
# # # # # # # #     x = str(number)
# # # # # # # #     rever = x[::-1]
# # # # # # # #     new = int(rever)
# # # # # # # #     return new  

# # # # # # # # n = int(input("Enter number to be reverse : "))
# # # # # # # # result = reversse(n)
# # # # # # # # print(f"the reverse is {result}")



# # # # # # # # taking input and check last digit is even or odd

# # # # # # # # def checknum(number):
# # # # # # # #     x = number 
# # # # # # # #     y = x%10
# # # # # # # #     print(y)
# # # # # # # #     return y
    

# # # # # # # # n = int(input("enter number : "))  
# # # # # # # # result = checknum(n)
# # # # # # # # if result % 2 == 1:
# # # # # # # #     print("odd number ")
# # # # # # # # else:
# # # # # # # #     print("Even number ")




# # # # # # # # To find sum of first and last digit of number


# # # # # # # # def sum_of_first_and_last_digit(number):
    
# # # # # # # #     number = abs(number)   # Ensure the number is non-negative by "abs"
    
# # # # # # # #     # Get the last digit of the number
# # # # # # # #     last_digit = number % 10
    
# # # # # # # #     # Get the first digit of the number
# # # # # # # #     first_digit = int(str(number)[0])
    
# # # # # # # #     # Calculate the sum of the first and last digit
# # # # # # # #     sum_result = first_digit + last_digit
    
# # # # # # # #     return sum_result

# # # # # # # # # Example usage:
# # # # # # # # input_number = int(input("Enter a number: "))
# # # # # # # # result = sum_of_first_and_last_digit(input_number)
# # # # # # # # print(f"The sum of the first and last digit is: {result}")


# # # # # # # #Second method

# # # # # # # # def sum_of_first_and_last_digit(number):
    
# # # # # # # #     number = abs(number)   # Ensure the number is non-negative by "abs"
    
# # # # # # # #     # Get the last digit of the number
# # # # # # # #     last_digit = number % 10
    
# # # # # # # #     # Get the first digit of the number
# # # # # # # #     while (number >= 10):
# # # # # # # #      number /= 10      #divide by 10 untill we don't get a single digit number
    
# # # # # # # #     first_digit = number
    
# # # # # # # #     # Calculate the sum of the first and last digit
# # # # # # # #     sum_result = int(first_digit + last_digit)
    
# # # # # # # #     return sum_result
# # # # # # # #Second method
# # # # # # # # input_number = int(input("Enter a number: "))
# # # # # # # # result = sum_of_first_and_last_digit(input_number)
# # # # # # # # print(f"The sum of the first and last digit is: {result}")




# # # # # # # # Calculate Sum and Average of numbers by entering users

# # # # # # # # def calsuav():
# # # # # # # #     list = []
# # # # # # # #     no = int(input("Enter numbers to calculate sum and average : "))
# # # # # # # #     for i in range(no):
# # # # # # # #         inp = float(input(f"Enter no {i+1}: "))
# # # # # # # #         list.append(inp)

# # # # # # # #     sumofnumber = sum(list)
# # # # # # # #     average = sumofnumber/no
# # # # # # # #     print("Sum is ",sumofnumber)
# # # # # # # #     print("Average is",average)

# # # # # # # # calsuav()


# # # # # # # #program to calculate average and total of 5 students for 3 subjects (using loops)

# # # # # # # # def calculate_average_and_total():
# # # # # # # #     num_students = 5
# # # # # # # #     num_subjects = 3

# # # # # # # #     # Initialize lists to store marks for each subject
# # # # # # # #     subjects = [[] for _ in range(num_subjects)]

# # # # # # # #     # Input marks for each student and each subject
# # # # # # # #     for student in range(num_students):
# # # # # # # #         name = input("Enter name of student  ")
# # # # # # # #         print(f"\nEnter marks for {name} :")
# # # # # # # #         for subject in range(num_subjects):
# # # # # # # #             mark = float(input(f"Enter marks for subject {subject + 1}: "))
# # # # # # # #             subjects[subject].append(mark)

# # # # # # # #     # Calculate total and average for each subject
# # # # # # # #     totals = []
# # # # # # # #     averages = []

# # # # # # # #     for subject_marks in subjects:
# # # # # # # #         total = sum(subject_marks)
# # # # # # # #         average = total / num_students
# # # # # # # #         totals.append(total)
# # # # # # # #         averages.append(average)

# # # # # # # #     # Display results
# # # # # # # #     print("\nSubject-wise results:")
# # # # # # # #     for subject in range(num_subjects):
# # # # # # # #         print(f"Subject {subject + 1} - Total: {totals[subject]}, Average: {averages[subject]}")

# # # # # # # # if __name__ == "__main__":
# # # # # # # #     calculate_average_and_total()




# # # # # # # # Read five person height and weight and count the number
# # # # # # # # of person having heightgreator than 170 and weigth less than 50



# # # # # # # # def heiwei():
# # # # # # # #     hcount = 0
# # # # # # # #     wcount = 0
# # # # # # # #     height = []
# # # # # # # #     weight = []
# # # # # # # #     number_of_person = 5
# # # # # # # #     for i in range(1,number_of_person+1):
# # # # # # # #        x = float(input(f"Enter height of person {i} : "))
# # # # # # # #        height.append(x)
    
# # # # # # # #     for j in range(1,number_of_person+1) :
# # # # # # # #         y = float(input(f"Enter the weight of person {j} : "))
# # # # # # # #         weight.append(y)
      

# # # # # # # #     for k in range(len(height)):
# # # # # # # #         if height[k]>170:
# # # # # # # #             hcount+=1
        
# # # # # # # #     for m in range(len(weight)):
# # # # # # # #         if weight[m]<50:
# # # # # # # #          wcount+=1
        

# # # # # # # #     print(hcount)
# # # # # # # #     print(wcount)        
# # # # # # # # heiwei()





# # # # # # # #Write a program to check enter number is prime or not 


# # # # # # # # def checknum(number):
# # # # # # # #     if number <= 1:
# # # # # # # #         return False
# # # # # # # #     elif number == 2:
# # # # # # # #         return True
# # # # # # # #     elif number%2==0:
# # # # # # # #         return False
# # # # # # # #     else:
# # # # # # # #         for i in range(3,int(number**0.5)+1):
# # # # # # # #             if number % i == 0:
# # # # # # # #                 return False
# # # # # # # #         return True  
    
# # # # # # # # user_input = int(input('Enter number to check : '))  
# # # # # # # # if checknum(user_input):
# # # # # # # #     print(f"{user_input} is a prime number")  
# # # # # # # # else:
# # # # # # # #     print(f"{user_input} is not a prime number"







# # # # # # # # #Write a program to evaluate series 1^2+2^2+3^2.....n^2



# # # # # # # # def square():
# # # # # # # #     n = int(input("Enter number : "))
# # # # # # # #     m=0
# # # # # # # #     for i in range(1,n+1):
# # # # # # # #         m += i**2
# # # # # # # #     print(m)    
# # # # # # # # square()  




# # # # # # # # #write a program to evaluate 1+1/2!=1/3!+....1/n!
# # # # # # # # def factorial(n):
# # # # # # # #     fact = 0
# # # # # # # #     if n == 0:
# # # # # # # #         return 1
# # # # # # # #     else:
# # # # # # # #        return n*factorial(n-1)


# # # # # # # # number = int(input("Enter number : "))
# # # # # # # # sum = 0
# # # # # # # # for i in range(1,number+1):
# # # # # # # #     sum += 1/factorial(i)

# # # # # # # # print(sum)



# # # # # # # Write a program to evaluate the series sum = 1-x+x^2/2!-x^3/3!+....+x^n/n!


# # # # # # # def series(n):
# # # # # # #     if n==0:
# # # # # # #         return 1
# # # # # # #     else:
# # # # # # #         return n*series(n-1)
    
# # # # # # # n = int(input("Enter number : "))    
# # # # # # # sum = 1
# # # # # # # sign = 1
# # # # # # # x = float(input("Enter value of x :"))

# # # # # # # for i in range(1,n+1):
# # # # # # #     sign *= -1
# # # # # # #     term = sign*(x**i)/series(i)
# # # # # # #     sum+=term
  

# # # # # # # print(sum)    


# # # # # # # #print 
# # # # # # #method 1
# # # # # # # *
# # # # # # # * * 
# # # # # # # * * * 
# # # # # # # * * * * 
# # # # # # # * * * * * 
# # # # # # # n = int(input("Enter number :"))
# # # # # # # for i in range(1,n+1):
# # # # # # #     print(i*"*")
# # # # # # # #method 2   

# # # # # # # m = int(input("Enter number : "))  
# # # # # # # for i in range(1,m+1):
# # # # # # #     for j in range(1,i+1):
# # # # # # #         print("*",end="")
# # # # # # #     print()        

# # # # # # # #pattern 2
# # # # # # # *****
# # # # # # # ****
# # # # # # # ***
# # # # # # # **
# # # # # # # *
# # # # # # #method 1
# # # # # # # n = int(input("Enter number : "))
# # # # # # # for i in range(1,n+1):
# # # # # # #     print((n-i+1)*"*")

# # # # # # #method 2
# # # # # # # n = int(input("Enter number : "))
# # # # # # # for i in range(1,n+1):
# # # # # # #     for j in range(1,n-i+2):
# # # # # # #         print("*",end="")
# # # # # # #     print()    


# # # # # # # #pattern 3
# # # # # # # *
# # # # # # # * * *
# # # # # # # * * * * *
# # # # # # # * * * * * * *

# # # # # # # #method 1
# # # # # # # n = int(input("Enter number : "))
# # # # # # # for i in range(1,n+1,2):
# # # # # # #     print(i*"*")

# # # # # # #method 2 
# # # # # # # n = int(input("Enter numer :"))
# # # # # # # k = 1
# # # # # # # for i in range(1,n+1):
# # # # # # #     for j in range(1,k+1):
# # # # # # #         print("*",end="")
# # # # # # #     k = k+2
# # # # # # #     print()    
# # # # # # # n = int(input("Enter number of n: "))

# # # # # # # for i in range(n):
# # # # # # #     # Print spaces
# # # # # # #     for j in range(n-i-1):
# # # # # # #         print(end=" ")
    
# # # # # # #     # Print stars
# # # # # # #     for j in range(i+1):
# # # # # # #         print("*", end=" ")
    
# # # # # # #     # Print spaces
# # # # # # #     for j in range(n-i-1):
# # # # # # #         print(end=" ")

# # # # # # #     print()


# # # # # # #     # Pattern 4
# # # # # # # #    *            *   (2i)
# # # # # # # #   * *         * * *
# # # # # # # #  * * *      * * * * *
# # # # # # # # * * * * 

# # # # # # # #  method 1

# # # # # # # # n = int(input("Enter number :"))
# # # # # # # # for i in range(0,n+1):
# # # # # # # #     for j in range(0,n-i+1):
# # # # # # # #         print(" ",end="")
# # # # # # # #     for j in range(0,i+1):
# # # # # # # #         print("*",end=" ")
# # # # # # # #     print()    

# # # # # # # # Method 2

# # # # # # # n = int(input("Enter number of n: "))
# # # # # # # k = 1
# # # # # # # for i in range(0,n+1):
# # # # # # #     # Print spaces
# # # # # # #     for j in range(0,n-i+2):
# # # # # # #         print(end=" ")
    
# # # # # # #     # Print stars
# # # # # # #     for j in range(1,i+1):
# # # # # # #         print("*", end=" ")
# # # # # # #     # Print spaces
# # # # # # #     for j in range(0,n-i+2):
# # # # # # #         print(end=" ")

# # # # # # #     print()



# # # # # # #Patteren 5

# # # # # # # #  * * * * * * * * * * *  
# # # # # # # #   * * * * * * * * * *   
# # # # # # # #    * * * * * * * * *    
# # # # # # # #     * * * * * * * *     
# # # # # # # #      * * * * * * *      
# # # # # # # #       * * * * * *       
# # # # # # # #        * * * * *        
# # # # # # # #         * * * *         
# # # # # # # #          * * *          
# # # # # # # #           * *           
# # # # # # # #            *            

# # # # # # # n = int(input("Enter number of n: "))
# # # # # # # k = 1
# # # # # # # for i in range(0,n+1):
# # # # # # #     # Print spaces
# # # # # # #     for j in range(0,i+1):
# # # # # # #         print(end=" ")
    
# # # # # # #     # Print stars
# # # # # # #     for j in range(1,n-i+2):
# # # # # # #         print("*", end=" ")
# # # # # # #     # Print spaces
# # # # # # #     for j in range(0,i+1):
# # # # # # #         print(end=" ")

# # # # # # #     print()



# # # # # # #Patteren 6 

# # # # # # #      1
# # # # # # #     1 2     
# # # # # # #    1 2 3    
# # # # # # #   1 2 3 4   
# # # # # # #  1 2 3 4 5 
# # # # # # # n = int(input('Enter number  : '))
# # # # # # # for i in range(1,n+1):
# # # # # # #     for j in range(1,n-i+2):
# # # # # # #         print(end=" ")
# # # # # # #     for j in range(1,i+1):
# # # # # # #         print(j,end=" ")
# # # # # # #     for j in range(1,n-i+2):
# # # # # # #         print(end=" ")    
# # # # # # #     print()    



# # # # # # #Patteren 7 

# # # # # # #  1 2 3 4 5 6 7  
# # # # # # #   1 2 3 4 5 6   
# # # # # # #    1 2 3 4 5    
# # # # # # #     1 2 3 4     
# # # # # # #      1 2 3      
# # # # # # #       1 2       
# # # # # # #        1 
# # # # # # # n = int(input('Enter number  : '))
# # # # # # # for i in range(1,n+1):
# # # # # # #     for j in range(1,i+1):
# # # # # # #         print(end=" ")
# # # # # # #     for j in range(1,n-i+2):
# # # # # # #         print(j,end=" ")
# # # # # # #     for j in range(1,i+1):
# # # # # # #         print(end=" ")    
# # # # # # #     print()    



# # # # # # #Patteren 8

# # # # # # #  7 7 7 7 7 7 7 
# # # # # # #   6 6 6 6 6 6  
# # # # # # #    5 5 5 5 5   
# # # # # # #     4 4 4 4    
# # # # # # #      3 3 3     
# # # # # # #       2 2      
# # # # # # #        1  
# # # # # # # n = int(input('Enter number  : '))
# # # # # # # for i in range(0,n+1):
# # # # # # #     for j in range(0,i+1):
# # # # # # #         print(end=" ")
# # # # # # #     for j in range(1,n-i+1):
# # # # # # #         print(n-i,end=" ")
# # # # # # #     for j in range(1,i+1):
# # # # # # #         print(end=" ")    
# # # # # # #     print()    




# # # # # # #Patteren 9

# # # # # # #       1  
# # # # # # #      2 2      
# # # # # # #     3 3 3     
# # # # # # #    4 4 4 4    
# # # # # # #   5 5 5 5 5 

# # # # # # # n = int(input("Enter n : "))  
# # # # # # # for i in range(0,n):
# # # # # # #     for j in range(0,n-i+1):
# # # # # # #         print(end=" ")
# # # # # # #     for j in range(1,i+2):
# # # # # # #         print(i+1,end=" ")   
# # # # # # #     for j in range(0,n-i+1):
# # # # # # #         print(end=" ")     
# # # # # # #     print()    



# # # # # # #Patteren 10



# # # # # # #   A A A A A      A ascii value = 65
# # # # # # #   B B B B   
# # # # # # #   C C C C
# # # # # # #   D D D
# # # # # # #   E E
# # # # # # #   F
# # # # # # # A = 65
# # # # # # # n = int(input("Enter n : "))  
# # # # # # # for i in range(0,n):
# # # # # # #     for j in range(1,n-i+1):
# # # # # # #         print(chr(A),end=" ")
# # # # # # #     A = A+1   
     
# # # # # # #     print()  


# # # # # # #Patteren 11

# # # # # # #   A 
# # # # # # # # A B 
# # # # # # # # A B C 
# # # # # # # # A B C D 
# # # # # # # # A B C D E

# # # # # # # n = int(input("Enter n : "))  
# # # # # # # for i in range(1,n+1):
# # # # # # #     for j in range(65,65+i):
# # # # # # #         print(chr(j),end=" ")
      
     
# # # # # # #     print()    



# # # # # # #patteren 12

# # # # # # # A B C D E 
# # # # # # # A B C D 
# # # # # # # A B C 
# # # # # # # A B 
# # # # # # # A 

# # # # # # # n = int(input("Enter n : "))  
# # # # # # # for i in range(1,n+1):
# # # # # # #     for j in range(65,65+n-i+1):
# # # # # # #         print(chr(j),end=" ")
      

# # # # # # #     print()    









# # # # # #Complex patteren 1



# # # # # # #    
# # # # # # #        * * * * *
# # # # # # #         * * * *
# # # # # # #          * * *
# # # # # # #           * *
# # # # # # #            * 
# # # # # # #            * 
# # # # # # #           * *         
# # # # # # #          * * *    
# # # # # # #         * * * *  
# # # # # # #        * * * * *

# # # # # # n = int(input("Enter number of rows :"))
# # # # # # x = int(n/2)
# # # # # # y = int(n-n/2)
# # # # # # z=1
# # # # # # for i in range(1,n+1):
# # # # # #     if i<=x:
# # # # # #         for j in range(0,i):
# # # # # #          print(end=" ")
    
# # # # # #         for j in range(1,x-i+2):
# # # # # #          print("*", end=" ")
  
# # # # # #         for j in range(0,i+1):
# # # # # #          print(end=" ")
# # # # # #     elif i>x:
# # # # # #        for k in range(0,n-i+1):
# # # # # #         print(end=" ")
# # # # # #        for k in range(0,i-x):
# # # # # #         print("*",end=" ")
# # # # # #        for k in range(0,n-i+1):
# # # # # #         print(end=" ")   
# # # # # #     z = z+1
# # # # # #     print() 





# # # # # #Complex Patteren 2



# # # # # # # * 
# # # # # # # * * 
# # # # # # # * * * 
# # # # # # # * * * * 
# # # # # # # * * * * * 
# # # # # # # * * * * * *
# # # # # # # * * * * * 
# # # # # # # * * * * 
# # # # # # # * * * 
# # # # # # # * * 
# # # # # # # * 

# # # # # # n = int(input("Enter number : "))
# # # # # # k = int(n//2)
# # # # # # for i in range(0,n+1):
# # # # # #     if i <k:
# # # # # #       for j in range(0,i+1):
# # # # # #         print("*",end=" ")  
# # # # # #     elif i==k:
# # # # # #       for j in range(0,k+1):
# # # # # #        print("*",end=" ")     
# # # # # #     else:    
# # # # # #       for j in range(0,n-i+1):
# # # # # #        print("*",end=" ")

# # # # # #     print()  
    




# # # # # #       ***  ##List accessing MEthod ****


# # # # # #using index number direct or [1:4] = "(1,2,3)" index number count.
# # # # # #reverse list = [::-1]
# # # # # #access element both positive and negative [2] other [-2]

# # # # # #Remove Element from list 

# # # # # #list.pop(index)    //when no index number is passed means remove last element
# # # # # #list.remove(element)
# # # # # #list.clear() to clear a list
# # # # # #  del list[2(index number)]
# # # # # #  del list //delete entire list

# # # # # #List Comprehension


# # # # # # Creating a list of squares:

# # # # # # squares = [x**2 for x in range(1, 6)]
# # # # # # # Output: [1, 4, 9, 16, 25]


# # # # # # Filtering even numbers:

# # # # # # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # # # # evens = [x for x in numbers if x % 2 == 0]
# # # # # # # Output: [2, 4, 6, 8]


# # # # # # Creating a list of tuples with pairs of numbers:
# # # # # # pairs = [(x, x*2) for x in range(1, 4)]
# # # # # # # Output: [(1, 2), (2, 4), (3, 6)]


# # # # # # #Flattening a nested list:
# # # # # # nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # # # # # flattened = [item for sublist in nested_list for item in sublist]
# # # # # # # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]



# # # # # #TO count element how often a element come in list 
# # # # # #use list.count(element)

# # # # # #Implement a function that returns a list of squares of even numbers from a given list using list comprehension

# # # # # def square_of_evens(input_list):
# # # # #     # Using list comprehension to create a new list of squares of even numbers
# # # # #     even_squares = [x**2 for x in input_list if x % 2 == 0]
# # # # #     return even_squares

# # # # # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # # # # result = square_of_evens(my_list)

# # # # # print("Original List:", my_list)
# # # # # print("Squares of Even Numbers:", result)

# # # # Write a Python program to sort a list of tuples based on the second element of each tuple.

# # # # #Method 1 to sort second index 
# # # # a = [(7, 5), (2, 1), (11, 7), (4, 3)]
# # # # a.sort(key=lambda x:x[0])
# # # # print(a)

# # # # #method 2
# # # # def sortt(a):
# # # #     return a[0]

# # # # a = [(7, 5), (2, 1), (11, 7), (4, 3)]
# # # # a.sort(key=sortt)
# # # # print(a)   

# # # #Use of Lamda function
# # # #it's work like a function

# # # # def ope(a,b):
# # # #     return a+b
# # # # r = ope(2,3)   //call function 
# # # # print(r)

# # # # z = lambda x,y : x+y
# # # # k = z(4,5)    //call lambda function
# # # # print(k)


# # # Implement a Python function to filter out all the strings from a list of mixed data types.
# # def filter_strings(input_list):
# #     # Using list comprehension to filter out strings
# #     non_strings = [x for x in input_list if not isinstance(x, str)]
# #     return non_strings

# # # Example usage
# # mixed_list = [1, 'apple', 3.14, 'banana', 'orange', True, 'grape', 'kiwi', False]
# # result = filter_strings(mixed_list)

# # print("Original List:", mixed_list)
# # print("List without Strings:", result)

# # Another Example

# # def filter_out(input_string):
# # #     z = [x for x in input_string if not isinstance(x,str) ]    //if str replace by int it give us only string
# # #     return z #non string

# # # original = [1,3,False,4,"Pawan","kumar",7,9,True]
# # # z =filter_out(original)
# # # print(z)

#         ##unpack tupple

# # fruits= ("banana","mango","apple","kiwi","lichi")

# # #in this code we can print elements like this
# # we pass at least two argument first element  represent first item in tupple and second same as first if we put * infront of second 
# # the second print remaining element in list.
# # (a,*b) = fruits
# # print(a)   # output = banana
# # print(b)   #output = [mango,apple,kiwi,lichi]

# # example 2 
# # (a,b,*c,d) = fruits
# # print(a)   #output = banana
# # print(b)   #output = mango
# # print(c)   #output = [apple,kiwi]
# # print(d)   #output = lichi

# ##SET
# #set is a collection which is unordered and unindexed.   True and 1 both are same in set
# # print random value in  sets because sets don't have index value
# # ADD two sets
# # using update function same as extend function in tupple

# # fruit = {"Apple","Mango","Banana","Orange"}
# # vegetable = {"Tomato","Potato","Cabbage","Onion"}
# # fruit.update(vegetable)
# # print(fruit)  

# # Add element in sets using add() function
# #Remove item in set 
# # using remove , pop(remove random item) ,discard, clear

# #Set join method
# # union,intersection,difference,symmetric_difference(print all value but not same value),update
# print only duplicate value in set using intersection_update



# #PYTHON DICTIONARY     duplicates don't allow,unordered
# pawan = {
#     "s" : "pawa",
#     "k" : 98,
#     "n" : 67.87
#     "l" : (3,5,7,"kumar",True)
# }
# Second Method to create dictionary
# # car = dict(name="pawan",model="newAI",age=18)
# print(car)

# print values using pawan["s"]   //pawa
# also use get function pawan.get("k") //98
# to print only keys like "s","k","n" use keys()
# for print only values use values()
# print(pawan.values())

# ADD item in dictionary
# pawan = {
#     "s" : "pawa",
#     "k" : 98,
#     "n" : 67.87,
#     "l" : (3,5,7,"kumar",True)
# }
# ## Add new item in dictonary 

# pawan["class"] = 12     also similiar change value 
# print(pawan)


# The items() method will return each item in a dictionary, as tuples in a list.
# pawan.items() output == dict_items([('s', 'pawa'), ('k', 98), ('n', 67.87), ('l', 'Noob'), ('class', 12), ('age', 19)])
# we can update values using pawan.update({"year": 2020})
# REMOVE ITEM FROM DICT using pop(name of keyword),popitem(//remove last key and value),clear,del


# Loop in dict 
# print keys 
#   for x in pawan:     //for x in pawan.keys()
#       print(x)        //   print(x)

# print values
#   for x in pawan:           // for x in pawan.values()
#       print(pawan[x])       //    print(x)


# Print both keys and value
# for x,y in pawan.items():
#     print(x,y)


# #Create Nested Dictionary  //Method 1
# dict3 = {
#     "child1" : {
#         "k" : 34,
#         "y" : 45,
#         "l" : ("pawan",3,True)
#     },

#     "child2" : {
#         "Name" : "Pawan",
#         "Age" : 19,
#         "Cast" : "prajapati"
#     },

#     "child3" : {
#      "Name" : "Bawan",
#      "Age" : 12,
#      "Cast" : "prajapat"

#     }

# }

# print(dict3)

# child1 = {
#         "k" : 34,
#         "y" : 45,
#         "l" : ("pawan",3,True)
#     }
# child2 = {
#         "Name" : "Pawan",
#         "Age" : 19,
#         "Cast" : "prajapati"
#     }

# child3 = {
#      "Name" : "Bawan",
#      "Age" : 12,
#      "Cast" : "prajapat"
   
#     }

# myfamily = {
#     "child1" : child1,
#     "child2" : child2,
#     "child3" : child3


# }

# print(myfamily)

# Access item in nested dictionary
# print(myfamily["child1"]["l"])


# Python Classes/Objects
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# class pawan:
#     y = 10

# p1 = pawan()    #Create object of class pawan
# print(p1.y)    #access item from class through object
# print(pawan)



# class pawan:
#  def __init__(self,name,age):
#   self.name = name
#   self.age = age 
  
# p2 = pawan("PAWAN",98) //create object
# print(p2.name,p2.age)


# The __str__ () 
# The __str__ () function is used to return a string representation of the object.
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"    

# p1 = Person("John", 36)

# print(p1)


# class new:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name},{self.age}"    
# p1 = new("john",67)
# p1.age = 40 //change value     //p1.age and p1.name is called properties
# print(p1)     //output = john,40
# delete properties using del p1.age

# # Object Methods
# # Objects can also contain methods. Methods in objects are functions that belong to the object.

# # Let us create a method in the Person class:

# # Example
# # Insert a function that prints a greeting, and execute it on the p1 object:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()    //output = Hello my name is John


#      Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


# #Python inheritance 
# class pwan:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def myfu(self):
#         x = 98
#         y = 102
#         print("sum is ",x+y,"Name of parents is " + self.name )
    
# class wt(pwan):   //create a child class of parents class, name of child class is wt
#   pass

# p1 = wt("Pawan",18)  //create object to access parents class methods by child class
# p1.myfu()


#    // If we want to use __init__ function in child class 
# #     //    The way is like  this..

# class pawan:
#     def __init__(self,name,kumar):
#         self.name = name
#         self.kumar = kumar

#     def func(self):
#         print(self.name) 

# class child_class(pawan):
#     def __init__(self,name,kumar):
#         pawan.__init__(self,name,kumar)       //also we can use here super().__init__(name,kumar)


# p1 = child_class("John",67)       
# p1.func()    //output =  John


 
# class mn(pawan):
#      def __init__(self,name,kumar):
#       super().__init__(name,kumar)     #we can add properties here 
#       self.newage = 19
# p1 = mn("John",67)
# p1.func()
# print(p1.newage)    output = john , 19



# In the example below, the newage 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:

# Example
# Add a year parameter, and pass the correct year when creating objects:

# class Student(Person):
#   def __init__(self, fname, lname, age):
#     super().__init__(fname, lname)
#     self.newage = age

# x = Student("Mike", "Olsen", 2019)
# print(x.newage)

# output = 2019


# class pawan:
#     def __init__(self,branch,course):
#         self.brance = branch
#         self.corse = course

#     def func(self):
#         print(5+9)    

# class rahul(pawan):
#     def __init__(self,branch,course,code):
#         super().__init__(branch,course)
#         self.subject_code = code

#     def newfun(self):
#         print(self.subject_code,self.brance,self.corse)    

# p1 = rahul("BTECH","Data Science",46)     
# p1.newfun()     //output = 46 Data Science BTECH

     

#           Python iterators   

# class Mynumber:
#     def __iter__(self):   // like for loop initialize from 1
#         self.a = 1
#         return self
    
#     def __next__(self):
#         if self.a <= 20:     ///write condition 
#           x = self.a
#           self.a += 1         //it's like i++
#           return x
#         else:
#             raise StopIteration     ///to stop iteration
# myclass = Mynumber()    
# myiter = iter(myclass)

# for x in myiter:
#     print(x)


# # ## access single like 

# # def __next__(self):
# #     x = self.a
# #     self.a+=1
# #     return x

# # myclass = Mynumber()
# # myiter =  iter(myclass)

# # print(next(myclass))    //1
# # print(next(myclass))    //2
# # print(next(myclass))    //3


# #    Inheritance with PolyMorphism 

# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()
   
# Output
# Ford
# Mustang
# Move!
# Ibiza
# Touring 20
# Sail!
# Boeing
# 747
# Fly!


#   Local variable v/s Global variale

# x = 200
 
# def myfunc():
#     print(x)   //here x global variable and all function can access it but we want any change inside the function 

# def myfunc():
#     x = 200
#     print(x)  //x = 200 became value inside the function only not 200 same for everyone
# // if we want to make x is same for all function use "global" keyward


#  // Module is like library (having in-built function)


# Print Random Number 
# using Random library

# import random 
# num = random.randint(1,10)
# for i in range (1,10):
#     print(num)
#     num = random.randint(1,10)


# Print all prime number


# lower = int(input("Enter starting "))
# upper = int(input("Enter ending "))
# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if (num%i==0):
#              break
#         else:
#          print(num)

#  Second method

# y = list()
# for num in range(2,20):
#     for j in range(2,num):
#         if num%j==0:
#             break
#     else:
#         y.append(num)             
# print(y) 




# #  Aremstrong Number 

# def checkArm(number):
#     sum_of_power = 0
#     originl = number
#     order = len(str(number))          
#     new = 0
#     while number>0:
#         new = number%10
#         sum_of_power += new**order
#         number //=10
#     return sum_of_power == originl  

# for num in range(1,10000):
#     if checkArm(num):
#         print(num)



# Power of 2 using anonymous function

# number = int(input("Enter number : "))

# result = list(map(lambda x : 2**x,  range(1,number+1)))   ///map is like loop
# print(result)

# using filter function with lambda


# Convert number in binary, octal and hexadecimal


# number = int(input("Enter number : "))
# print(number)
# print(bin(number),"binary")
# print(oct(number),"octal")
# print(hex(number),"hexadecimal")

# Convert Decimal to Binarary with recursion
# def code(number):
#     if number>1:
#      code(number//2)
#     print(number%2)

# code(15)



# Find HCF of any number


# x = 30
# y = 12
# hcf = 0
# for i in range(2,30):
#     if x%i==0 and y%i==0:
#      hcf = i
     
# print(hcf)


# Program to suffle deck Card  //Tash ke patte

# import random,itertools
# values = range(1,14)
# suits = ['spade','diamond','club','heart']
# deck = list(itertools.product(values,suits))

# for i in range(1,5):
#  random.shuffle(deck)
#  print("number ; ",deck[i][0],"deck is ", deck[i][1])


# #   Matrix   ##

# # Additon of matrix

# A = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# B = [[1,8,3],
#      [4,7,6],
#      [7,8,2]]
# c = [[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(A)):
#     for j in range(len(A)):
#           c[i][j] = A[i][j]+B[i][j]
          
# for i in c:
#      print(i)



##   Matrix   ##

# # multiplication of matrix

# A = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# B = [[1,8,3],
#      [4,7,6],
#      [7,8,2]]
# c = [[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(A)):
#     for j in range(len(A)):
#           c[i][j] = A[i][j]*B[j][i]
          
# for i in c:
#      print(i)


##   Matrix   ##

# # Transpose  of matrix

# A = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# c = [[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(A)):
#     for j in range(len(A)):
#         c[i][j] = A[j][i]
# for i in c:          
#  print(i)        


#    Check palandrome

# def pal():
#    x = input("Enter string to check palandrome : ")
#    y  = 0
#    z = len(x)-1
#    while y<z:
#       if x[y]!=x[z]:    
#         return False
    
#       y+=1
#       z-=1
       
#    return True    

# n = input("Enter string ")
# result = pal()
# print("palandrome : ",result)




# #    Count string 

# String = "Hello guys my Name is Pawan"
# h = "aeiou"
# String = String.casefold()
# print(String)
# count = {}.fromkeys(h,0)  # //create dictionary and store each vowel as a key
# print(count)
# for char in String:
#     if char in count:
#         count[char]+=1
# print(count)       

# Second Method

# String = "Hello guys my Name is Pawan"
# h = "aeiou"
# String = String.casefold()
# print(String)
# count = {key:sum([1 for char in String if char == key])for key in h}
# print(count)       


#  Print Value of index and item from list


# l = [34,67,32,56,70]
# for index,value in enumerate(l,start=1) :
#     print(index,value)

# values sort in dictionary

# dict1 = {"a":5,"b": 3,"c":9,"d":4}
# v = sorted(dict1.values()) #//3,4,5,9
# print(v)
# #Print values and key both after getting sorted
# w = sorted(dict1.items(),key = lambda x:x[1])
# print(w)

# Check List is empty

# x = list()
# if x == []:
#     print("Empty")


# Fix errors in my code


# # When errors occurs in particular part and if want to skip that errors and reun next part of our code
# # using try and except

# i = input("Enter number :")
# y = 23
# z = 89
# try:
#  num = "karan"
#  print(num+y)
# except(TypeError) as a:
#  print(a)
   

# print(y,z)
# print("Thank you")



#  Check Python keyword


# import keyword
# words = ["break","John","Lisa","else"]
# print(keyword.kwlist)  # Print all python keyword
# for i in range(len(words)):
#     if keyword.iskeyword(words[i]):
#         print(words[i],"is a keyword")
#     else:
#         print(words[i],"is not a keyword")


##  use of iter keyword

# l = [2,4,6,8,9]

# iterator = iter(l)
# for i in range(len(l)):
#  print(next(iterator),end=" ")

