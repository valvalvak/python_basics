prime_numbers = 0
non_prime_numbers = 0
command = input()
while command != "stop":
    isPrime = True
    number = int(command)
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    else:
        for checking in range(2, number):
            if number % checking == 0:
                isPrime = False
                break
    if isPrime:
        prime_numbers += number
    else:
        non_prime_numbers += number
    command = input()
print(f"Sum of all prime numbers is: {prime_numbers}")
print(f"Sum of all non prime numbers is: {non_prime_numbers}")