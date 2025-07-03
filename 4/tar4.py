#
#  Targil 4
#
# Noam Hadad 322766064
# Guedalia Sebbah 337966659

import ast


#
#f1
def f1():
    # fake data for testing
    def info_proj_get(name_file):
        return [
            [["a1", 10, 12], []],
            [["a2", 13, 18], [
                [["a21", 6, 8], []],
                [["a22", 7, 10], []]
            ]],
            [["a3", 3, 7], []]
        ]

    # seif a
    def proj_times(file_name):
        def diff_tree(tree):
            return [
                [[step[0], abs(step[1] - step[2])], diff_tree(subs)]
                for [step, subs] in tree
            ]

        result = diff_tree(info_proj_get(file_name))
        print("Difference tree:")
        print(result)

    # seif b
    def proj_time_cost(file_name, cost_per_time_unit):
        data = info_proj_get(file_name)

        def sum_times(tree):
            planned_total = sum(step[1] for [step, _] in tree)
            actual_total = sum(step[2] for [step, _] in tree)
            return planned_total, actual_total

        planned, actual = sum_times(data)
        planned_cost = planned * cost_per_time_unit
        actual_cost = actual * cost_per_time_unit

        diff_time = actual - planned
        diff_cost = actual_cost - planned_cost

        result = (
            (planned, planned_cost),
            (actual, actual_cost),
            (diff_time, diff_cost)
        )

        print("Project cost and timing summary:")
        print(result)

    # main menu to f1
    while True:
        print("1 : Show difference tree")
        print("2 : Show project cost and timing summary")
        print("0 : Return to main menu")
        choice = input("Enter choice: ").strip()

        if choice == '0':
            break
        elif choice == '1':
            # You can ask for file name if you want; here we just use a dummy name
            proj_times("dummy_file")
        elif choice == '2':
            cost_str = input("Enter cost per time unit (number): ").strip()
            try:
                cost = float(cost_str)
                proj_time_cost("dummy_file", cost)
            except ValueError:
                print("Invalid number for cost.")
        else:
            print("Invalid choice, try again.")


#
#f2
def f2():
    def reverseList(n):
        if isinstance(n, str):
            return n[::-1]
        elif isinstance(n, list):
            if not n:
                return []
            return [reverseList(n[-1])] + reverseList(n[:-1])
        elif isinstance(n, tuple):
            return tuple(reverseList(elem) for elem in n)
        else:
            return n

    while True:
        try:
            x = (input("Enter a Python list literal (or '0' to exit): "))
            if x == '0':
                break
            y = ast.literal_eval(x)
            print("Reversed list:", reverseList(y))
        except Exception as e:
            print("Invalid input. Please enter a valid Python list literal.")


#
#f3
def f3():
    def reverseList(n):
        if isinstance(n, str):
            return n[::-1]
        elif isinstance(n, list):
            return [reverseList(elem) for elem in n[::-1]]
        elif isinstance(n, tuple):
            return tuple(reverseList(elem) for elem in n[::-1])
        else:
            return n

    def isPalindrome(seq):
        return seq == reverseList(seq)

    while True:
        x = input("Enter a Python list literal (or '0' to exit): ").strip()
        if x == '0':
            break
        try:
            lst = ast.literal_eval(x)
            if not isinstance(lst, list):
                raise ValueError
            if isPalindrome(lst):
                print("It is a palindrome")
            else:
                print("It is not a palindrome")
        except Exception:
            print("Invalid input. Please enter a valid Python list literal.")


#
#f4
def f4():

    def twinp(n):
        def sieve(lst):
            if not lst:
                return []
            p = lst[0]
            return [p] + sieve([x for x in lst[1:] if x % p != 0])

        primes = sieve(list(range(2, n)))
        return {p: p + 2 for p in primes if (p + 2) in primes}


    while True:
        x = input("Enter a Natural number n (or '-1' to exit): ").strip()
        if x == '-1':
            break
        try:
            n = int(x)
            if n <= 0:
                print("ERROR: Input number is incorrect!")
            else:
                twins = twinp(n)
                for a, b in sorted(twins.items()):
                    print(a, b)
        except ValueError:
            print("ERROR: Input number is incorrect!")


#
#f5
def f5():

    def dicts3add(d1, d2, d3):
        keys1, keys2, keys3 = set(d1), set(d2), set(d3)
        all_keys = keys1 | keys2 | keys3
        multi = {k for k in all_keys
                 if sum(k in s for s in (keys1, keys2, keys3)) > 1}
        result = {}
        for k in multi:
            vals = ()
            if k in d1: vals += (d1[k],)
            if k in d2: vals += (d2[k],)
            if k in d3: vals += (d3[k],)
            vals = tuple(dict.fromkeys(vals).keys())
            result[k] = vals
        for k in all_keys - multi:
            if k in d1:
                result[k] = d1[k]
            elif k in d2:
                result[k] = d2[k]
            else:
                result[k] = d3[k]
        return result

    while True:
        s1 = input("Enter a dictionary (or '0' to exit): ").strip()
        if s1 == '0':
            break
        s2 = input("Enter a dictionary (or '0' to exit): ").strip()
        if s2 == '0':
            break
        s3 = input("Enter a dictionary (or '0' to exit): ").strip()
        if s3 == '0':
            break

        try:
            try:
                d1 = ast.literal_eval(s1)
            except (ValueError, SyntaxError):
                d1 = eval(s1,
                          {'__builtins__': None},
                          {'dict': dict})
            try:
                d2 = ast.literal_eval(s2)
            except (ValueError, SyntaxError):
                d2 = eval(s2,
                          {'__builtins__': None},
                          {'dict': dict})
            try:
                d3 = ast.literal_eval(s3)
            except (ValueError, SyntaxError):
                d3 = eval(s3,
                          {'__builtins__': None},
                          {'dict': dict})

            if not all(isinstance(d, dict) for d in (d1, d2, d3)):
                raise ValueError

            merged = dicts3add(d1, d2, d3)
            print(sorted(merged.items()))

        except Exception:
            print("ERROR: Input is incorrect!")








if __name__ == '__main__':
    # map menu choices to your functions
    functions = {
        '1': f1,
        '2': f2,
        '3': f3,
        '4': f4,
        '5': f5,
    }

    print("Welcome to Targil 4")
    print("---------------------------------------")

    while True:
        # print menu
        print("\nYour choices:")
        print("0 : exit")
        for num in sorted(functions):
            print(f"{num} : function {num}")

        # get choice
        choice = input("Please enter your choice: ")

        # dispatch
        if choice == '0':
            print("Bye!")
            break
        elif choice in functions:
            print()           # extra line before function runs
            functions[choice]()
        else:
            print("Invalid choice, try again.")
