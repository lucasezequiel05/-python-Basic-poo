import time

def factorial_loop(number):

    result = 1

    while(number > 1):
        result *= number
        number -= 1

    return result

def factorial_recursivity(number):

    if number > 1:
        number = number*factorial_recursivity(number-1)

    return number

def main():

    number = 500
    start = time.time()
    factorial_loop(number)
    end = time.time()
    print(end-start)

    start = time.time()
    factorial_recursivity(number)
    end = time.time()
    print(end-start)

if __name__ == '__main__':
    main()