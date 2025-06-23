#
#  Targil 2
#
## Noam Hadad 322766064
## Guedalia Sebbah 337966659



from functools import reduce

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
    def part_b():
        n1 = int(input("Enter n1 (lower): "))
        n2 = int(input("Enter n2 (upper): "))

        if n1 <= 0 or n2 <= 0 or n2 <= n1:
            print("ERROR: the values must be positive integers and n2 > n1")
            return

        numbers = pentaNumRange(n1, n2)
        # print all the numbers, but go to next line, every 10
        count = 0
        for i in numbers:
            print(i , end='  ')
            count += 1
            if ((count%10) == 0):
                print()

    # c
    def part_c():
        n1 = int(input("  lower bound n1: "))
        n2 = int(input("  upper bound n2: "))

        if n1 <= 0 or n2 <= 0 or n2 <= n1:
            print("ERROR: the values must be positive integers and n2 > n1.")
        else:
            result = pentaNumRange(n1, n2)

            chunk_list = lambda lst, size: list(map(lambda i: lst[i:i + size], range(0, len(lst), size)))

            list(map(lambda line: print("  ".join(map(str, line))), chunk_list(result, 10)))


    # menu for question 1
    while True:
        print("\nQuestion 1: Pentagonal-number range")
        print("  b) imperative (input, validate, print 10 per line)")
        print("  c) fully functional")
        print("  x) back to main menu")
        choice = input("Choose part [b/c/x]: ").lower()

        if choice == 'b':
            part_b()
        elif choice == 'c':
            part_c()
        elif choice == 'x':
            break

        else:
            print("  invalid choice, try again")


#
# question 2
def f2():
    def Positivenumber(n):
        return abs(n)

    def sumDigits(n):
        if n < 0:
            y = Positivenumber(n)
            return sum(int(digit) for digit in str(y))
        else:
            return sum(int(digit) for digit in str(n))
        pass

    try:
       n=int(input("Enter an integer number n (positive or negative): "))
    except ValueError:
        print("ERROR: Input number is incorrect!")
        return
    print(sumDigits(n))



#
# question 3
def f3():
    def Positivenumber(n):
        return abs(n)
    def isPalindrom(n):
        y = Positivenumber(n)
        reversed_n = int(str(y)[::-1])
        if n == reversed_n:
            return "It is a palindrome"
        else:
            return "It is not a palindrome"

    pass

    try:
     n = int(input("Enter an integer number n (positive or negative): "))
    except ValueError:
         print("ERROR: Input number is incorrect!")
         return
    print(isPalindrom(n))



#
# question 4
def f4():
    def m(n):
        get_term = lambda i: i / (i + 1)
        return sum(map(get_term, range(1, n + 1)))

    try:
        n = int(input("Enter a Natural number n: "))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("ERROR: Input number is incorrect!")
        return
    for i in range(1, n + 1):
        print(i, m(i))
    pass



#
# question 5
def f5():
    # Helper: Get the union of all keys from a list of dictionaries
    get_all_keys = lambda dicts: reduce(lambda acc, d: acc | set(d), dicts, set())

    # Helper: Collect all values for a given key from all dictionaries
    get_values_for_key = lambda k, dicts: list({d[k] for d in dicts if k in d})

    # Pure function: Merge three dictionaries as specified
    def add3dicts(d1, d2, d3):
        dicts = (d1, d2, d3)
        all_keys = get_all_keys(dicts)
        merge_value = lambda vals: vals[0] if len(vals) == 1 else tuple(vals)
        return dict(map(lambda k: (k, merge_value(get_values_for_key(k, dicts))), all_keys))

    # Read dictionary input and validate it
    def read_dict_eval():
        try:
            d = eval(input("Enter a dictionary: "))
            if not isinstance(d, dict):
                raise ValueError
            return d
        except:
            print("ERROR: Input is incorrect!")
            exit()

    d1 = read_dict_eval()
    d2 = read_dict_eval()
    d3 = read_dict_eval()
    print(add3dicts(d1, d2, d3))
    pass







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