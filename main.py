import random


def main():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    number3 = random.randint(0, 100)
    """
    ########################################
    Code Your Program here
    """
    # Prints out statements, number1, number2, number3
    print(f'{number1}')
    print(f'{number2}')
    print(f'{number3}')
    
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
