def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

my_numbers = [1, 5, 12, 11, 10, 9, 3, 4 ,17, 18]

prime_numbers = list(filter(lambda x: is_prime(x), my_numbers))

print("prime numb:", prime_numbers) 