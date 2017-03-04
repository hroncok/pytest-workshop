def fizzbuzz(num):
    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"
    if num % 15 == 0:
        return "fizzbuzz"
    return str(num)
