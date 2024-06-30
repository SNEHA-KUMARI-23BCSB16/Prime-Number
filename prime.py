# to display prime numbers in a given range

num1=int(input("Enter the first number:"))                                                  # taking first number as input from user

num2=int(input("Enter the second number:"))                                                 # taking second number as input from user

def prime_number_range(n1,n2):                                                              # a user defined function to display range of prime number

    for i in range(n1,n2+1):                                                                # a loop to run from first number till second number

        flag=0                                                                              # counter variable to check whether number is prime or not
        if( i==1):
            continue                                                                               

        for j in range(2,int(i/2)+1):                                                      # loop to check whether the number is prime or not

            if( i%j == 0 ):
                flag=1
                break

        if( flag==0 ):
            print(i)
        else:
            continue

prime_number_range(num1,num2)