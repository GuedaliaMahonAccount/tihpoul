#
#  Targil 2
#
## Noam Hadad 322766064
## Guedalia Sebbah 337966659




#
# Question 1
def f1():
    # a
    def pentaNumRange(n1, n2):
        if n2 <= n1:
            raise ValueError("n2 must be greater than n1")

        getPentaNum = lambda n: (n * (3 * n - 1)) // 2
        return [getPentaNum(i) for i in range(n1, n2)]

    # b
    def part_b_pentaNumRange():
        n1 = int(input("Enter n1 (lower): "))
        n2 = int(input("Enter n2 (upper): "))

        if n1 <= 0 or n2 <= 0 or n2 <= n1:
            print("ERROR: the values must be positive integers and n2 > n1")
            return

        def getPentaNum(n):
            return (n * (3 * n - 1)) // 2

        count = 0
        for i in range(n1, n2):
            print(getPentaNum(i), end='  ')
            count += 1
            if count % 10 == 0:
                print()

        if count % 10 != 0:
            print()

    # c
    def part_c():
        n1 = int(input("Enter n1 (lower): "))
        n2 = int(input("Enter n2 (upper): "))

        if n1 <= 0 or n2 <= 0 or n2 <= n1:
            print("ERROR: the values must be positive integers and n2 > n1.")
            return

        getPentaNum = lambda n: (n * (3 * n - 1)) // 2
        numbers = list(map(getPentaNum, range(n1, n2)))
        lines = [numbers[i:i + 10] for i in range(0, len(numbers), 10)]
        list(map(lambda line: print("  ".join(map(str, line))), lines))

    # menu for question 1
    while True:
        print("\nQuestion 1: Pentagonal-number range")
        print("  b) imperative (input, validate, print 10 per line)")
        print("  c) fully functional")
        print("  x) back to main menu")
        choice = input("Choose part [b/c/x]: ").lower()

        if choice == 'b':
            part_b_pentaNumRange()

        elif choice == 'c':
            n1 = int(input("  lower bound n1: "))
            n2 = int(input("  upper bound n2: "))
            result = pentaNumRange(n1, n2)
            print("  →", result)
        elif choice == 'x':
            break

        else:
            print("  invalid choice, try again")


#
# Question 2
def f2():
    def sumDigits(n):
        # take absolute value, convert to string, map each char back to int, and sum
        return sum(map(int, str(abs(n))))

    n_str = input("Enter an integer number n (positive or negative): ")
    # manual validation instead of try/except
    if not n_str.lstrip('-').isdigit():
        print("ERROR: Input number is incorrect!")
        return

    n = int(n_str)
    result = sumDigits(n)
    print(result)



#
# Question 3
def f3():
    def reverseNumber(n):
        s = str(abs(n))
        return int(s[::-1])

    def isPalindrome(n):
        return n >= 0 and n == reverseNumber(n)

    n_str = input("Enter a non-negative integer n: ")
    if not n_str.isdigit():
        print("ERROR: Input number is incorrect!")
        return

    n = int(n_str)
    if isPalindrome(n):
        print(f"{n} is a palindrome")
    else:
        print(f"{n} is not a palindrome")



#
# Question 4
def f4():
    def m(n):
        return sum(1/(i+1) for i in range(1, n+1))

    n_str = input("Enter a positive integer n: ")
    if not n_str.isdigit() or int(n_str) <= 0:
        print("ERROR: Input number is incorrect!")
        return

    n = int(n_str)
    for i in range(1, n+1):
        print(f"{i}: {m(i)}")



#
# Question 5
def f5():
    import ast

    def add3dicts(d1, d2, d3):
        result = {}
        for d in (d1, d2, d3):
            for k, v in d.items():
                result[k] = result.get(k, 0) + v
        return result

    d1_str = input("Enter dict d1 (e.g. {'a':1, 'b':2}): ")
    d2_str = input("Enter dict d2 (e.g. {'a':3, 'c':4}): ")
    d3_str = input("Enter dict d3 (e.g. {'b':5, 'd':6}): ")

    try:
        d1 = ast.literal_eval(d1_str)
        d2 = ast.literal_eval(d2_str)
        d3 = ast.literal_eval(d3_str)
    except (ValueError, SyntaxError):
        print("ERROR: One of the inputs is not a valid dictionary!")
        return

    if not all(isinstance(d, dict) for d in (d1, d2, d3)):
        print("ERROR: All inputs must be dictionaries!")
        return

    merged = add3dicts(d1, d2, d3)
    print(merged)



if __name__ == '__main__':
    functions = {
        '1': f1,
        '2': f2,
        '3': f3,
        '4': f4,
        '5': f5,
    }
    descriptions = {
        '1': 'Pentagonal numbers range and display',
        '2': 'Sum of digits',
        '3': 'Palindrome check',
        '4': 'Series-sum calculation',
        '5': 'Merge three dictionaries',
    }

    print("Welcome to Targil 2")
    print("-------------------")

    while True:
        print("\nYour choices:")
        print("0 : exit")
        for key in sorted(functions):
            print(f"{key} : {descriptions[key]}")
        choice = input("Please enter your choice: ")
        if choice == '0':
            print("Bye!")
            break
        elif choice in functions:
            print()  # blank line before running
            functions[choice]()
        else:
            print("Invalid choice, try again.")