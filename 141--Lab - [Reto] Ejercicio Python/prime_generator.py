def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def generate_primes(limit):
    primes = []

    for num in range(1, limit + 1):
        if is_prime(num):
            primes.append(num)

    return primes


def save_results(primes):
    with open("results.txt", "w") as file:
        for prime in primes:
            file.write(str(prime) + "\n")


def main():
    limit = 250
    primes = generate_primes(limit)

    save_results(primes)

    print("Prime numbers saved in results.txt")


if __name__ == "__main__":
    main()