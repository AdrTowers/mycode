#!/usr/binpython3

def fetcher():
    with open("numfile.txt", "r") as numfile:
        numlist = []
        for line in numfile:
            numlist.append(int(line))
        return numlist


def main():
    fizz = 0
    buzz = 0
    fizzbuzz = 0
    for num in fetcher():
        if num % 3 != 0 and num % 5 != 0:
            print("FizzBuzz")
            fizzbuzz += 1
        elif num % 3 != 0:
            print("Fizz")
            fizz += 1
        elif num % 5 == 0:
            print("Buzz")
            buzz += 1
        else:
            print(num)

    print(
        f"There are this many Fizzes: {fizz}, Buzzes: {buzz}, Fizzbuzzes: {fizzbuzz}")


if __name__ == "__main__":
    main()

