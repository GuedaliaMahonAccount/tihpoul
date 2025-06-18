#
#  Targil 2
#
## Noam Hadad 322766064
## Guedalia Sebbah 337966659





#
# question 1
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
# question 2
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
# question 3
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
        print(f" is a palindrome")
    else:
        print(f" is not a palindrome")





#
# question 4
def f4():
    def m(n):
        return sum(map(lambda i: i/(i+1), range(1, n+1)))

    n_str = input("Enter a positive integer n: ")
    if not n_str.isdigit() or int(n_str) <= 0:
        print("ERROR: Input number is incorrect!")
        return

    n = int(n_str)
    for i in range(1, n+1):
        print(i, m(i))








#
# question 5
def f5():
    def add3dicts(d1, d2, d3):
        all_keys = set(d1) | set(d2) | set(d3)
        merged = {}
        for k in all_keys:
            vals = []
            if k in d1: vals.append(d1[k])
            if k in d2: vals.append(d2[k])
            if k in d3: vals.append(d3[k])
            seen = []
            for v in vals:
                if v not in seen:
                    seen.append(v)
            merged[k] = seen[0] if len(seen) == 1 else tuple(seen)
        return merged

    try:
        d1 = eval(input("Enter a dictionary: "))
        d2 = eval(input("Enter a dictionary: "))
        d3 = eval(input("Enter a dictionary: "))
    except Exception:
        print("ERROR: Input is incorrect!")
        return

    if not all(isinstance(d, dict) for d in (d1, d2, d3)):
        print("ERROR: Input is incorrect!")
        return

    result = add3dicts(d1, d2, d3)
    print(result)











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
            print()
            functions[choice]()
        else:
            print("Invalid choice, try again.")