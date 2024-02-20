from utils import is_prime
from utils import is_power_of_five

def main():
    number = int(input("Введіть число: "))
    if is_power_of_five(number):
        print(f"{number} є степенем числа 5.")
    else:
        print(f"{number} не є степенем числа 5.")

if __name__ == "__main__":
    main()

number = 7
if is_prime(number):
    print(f'{number} is a prime number')
else:
    print(f'{number} is not a prime number')
