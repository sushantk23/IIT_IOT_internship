
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:
            return False
    return True
def print_primes_in_range(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
    print()  
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print_primes_in_range(start, end)