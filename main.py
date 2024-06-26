import random


def main():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    number3 = random.randint(0, 100)
    """
    ########################################
    Code Your Program here
    """
    # print statement, number1, number2, number3
    print(f'{number1} {number2} {number3}')
    
    # determines whether number1 is less than number2 and number3, outputs number 1 if less 
    if number1 < number2 and number1 < number3:
        min_value = number1
    
    # determines wheter number2 is less than 3, outputs number 2 if less
    elif number2 < number3:
        min_value = number2
    
    # determines wheter number 3 is less than number1 and number2 in previous if and elif statements
    else:
        min_value = number3
    
    # print 'smallest number statement' and the smallest number produced by the random generator
    print(f'smallest number : {min_value}')
    """"
    ########################################
    """

    ########################################
    # Do not delete the return statement
    ########################################
    return number1, number2, number3, min_value


if __name__ == '__main__':
    main()
