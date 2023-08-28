def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def isitprime(numbers):
    return list(map(is_prime, numbers))

def main():
    input_numbers = []
    
    while True:
        try:
            num = int(input("masukkan angka atau tekan enter jika selesai: "))
            input_numbers.append(num)
        except ValueError:
            break
    
    if input_numbers:
        output = isitprime(input_numbers)
        print("Output:", output)
    else:
        print("tidak ada angka yang dimasukkan.")

if __name__ == "__main__":
    main()
