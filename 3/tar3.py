#
#  Targil 3
#
##Noam Hadad 322766064
##Guedalia Sebbah 337966659






#
# question 1
def f1():

    # a
    getPentaNum = lambda x: 0.5 * x * (3 * x - 1)

    def pentaNumRangewithtail(n1, n2):
        def halper(n1, n2, nums):
            if n1 >= n2:
                return nums
            nums.append(getPentaNum(n1))
            return halper(n1 + 1, n2, nums)

        return (halper(n1, n2, []))

    # non-tail recursion
    def pentaNumRange(n1, n2):
        if n1 >= n2:
            return []
        return [getPentaNum(n1)] + pentaNumRange(n1 + 1, n2)

    # with for loop
    def pentaNumRange1(n1, n2):
        nums = []
        for i in range(n1, n2):
            nums.append(getPentaNum(i))
        return nums

    def printnums(nums):
        if not nums:
            return
        for i, num in enumerate(nums):
            print(num, end=' ')
            if (i + 1) % 10 == 0:
                print()  # New line after every 10 numbers

    try:
      n1 = int(input("enter the value of n1: "))
      n2 = int(input("enter the value of n2: "))
      if isinstance(n1, int) and isinstance(n2, int) and n2 > n1:
          x=input("Please select the function you would like to use.\n""1: Recursive function \n""2: For loop function\n""3: Recursive function with tail recursion\n")
          if x == '1':
              nums = pentaNumRange(n1, n2)
              printnums(nums)
          elif x == '2':
              nums = pentaNumRange1(n1, n2)
              printnums(nums)
          elif x == '3':
              nums = pentaNumRangewithtail(n1, n2)
              printnums(nums)
          else:
              print("you must choose 1 or 2")
      else:
          print("ERROR: the values must be positive integers and n2 > n1")
    except ValueError:
        print("Invalid input. Please enter integers.")




#
# question 2
def f2():

    def reverseNumwithtail(n):
        sign = -1 if n < 0 else 1

        def helper(x, rev):
            if x == 0:
                return rev
            return helper(x // 10, rev * 10 + x % 10)

        return sign * helper(abs(n), 0)

    getunitsdigit = lambda n: abs(n) % 10

    def reverseNum(n):
        def helper(n):
            if n < 10:
                return str(n)
            return str(n % 10) + helper(n // 10)

        if n < 0:
            return int("-" + helper(-n))
        return int(helper(n))


    try:
     n=int(input("Enter an integer number n (positive or negative): "))
     x = input("Please select the function you would like to use.\n""1: Recursive function \n""2: Recursive function with tail recursion\n")
     if x == '1':
        print(reverseNum(n))
     elif x == '2':
        print(reverseNumwithtail(n))
     else:
        print("you must choose 1 or 2")

    except ValueError:
        print("ERROR: Input number is incorrect!")



#
# question 3
def f3():

    def pi(n):
        if n == 0:
            return 0
        return ((-1) ** (n + 1)) * (4 / (2 * n - 1)) + pi(n - 1)

    # Tail recursive
    def pi_tail(n):
        def helper(i, acc):
            if i == 0:
                return acc
            return helper(i - 1, acc + ((-1) ** (i + 1)) * (4 / (2 * i - 1)))

        return helper(n, 0)


    try:
        n = int(input("Enter a Natural number n: "))
        if n <= 0:
            print("ERROR: Input number is incorrect!")
            return

        choice = input("Choose implementation:\n1: Recursion\n2: Tail Recursion\n")

        if choice == '1':
            for i in range(1, n + 1):
                print(i, pi(i))
        elif choice == '2':
            for i in range(1, n + 1):
                print(i, pi_tail(i))
        else:
            print("ERROR: You must choose 1 or 2")
    except ValueError:
        print("ERROR: Input number is incorrect!")




#
# question 4
def f4():

    # Helper to check prime
    isPrime = lambda n, d=2: False if n < 2 else True if d * d > n else False if n % d == 0 else isPrime(n, d + 1)

    # Non-tail version
    def twinp(n):
        def primes(i):
            if i >= n:
                return []
            return [i] + primes(i + 1) if isPrime(i) else primes(i + 1)

        def build_twin(p_list):
            if len(p_list) < 2:
                return {}
            head, tail = p_list[0], p_list[1:]
            rest = build_twin(tail)
            if tail[0] - head == 2:
                rest[head] = tail[0]
            return rest

        return build_twin(primes(2))

    # Tail-recursive version
    def twinp_tail(n):
        def primes(i, acc):
            if i >= n:
                return acc
            return primes(i + 1, acc + [i] if isPrime(i) else acc)

        def build_twin(p_list, acc):
            if len(p_list) < 2:
                return acc
            head, tail = p_list[0], p_list[1:]
            if tail[0] - head == 2:
                acc[head] = tail[0]
            return build_twin(tail, acc)

        return build_twin(primes(2, []), {})


    try:
        n = int(input("Enter a Natural number n: "))
        if n <= 0:
            print("ERROR: Input number is incorrect!")
            return

        choice = input("Choose implementation:\n1: Recursion\n2: Tail Recursion\n")

        if choice == '1':
            result = twinp(n)
        elif choice == '2':
            result = twinp_tail(n)
        else:
            print("ERROR: You must choose 1 or 2")
            return

        for k, v in result.items():
            print(k, v)
    except ValueError:
        print("ERROR: Input number is incorrect!")




#
# question 5
def f5():

    def dicts3add(d1, d2, d3):
        keys1, keys2, keys3 = set(d1.keys()), set(d2.keys()), set(d3.keys())
        all_keys = keys1 | keys2 | keys3

        def build(keys):
            if not keys:
                return {}
            k = keys.pop()
            vals = tuple(
                x[k] for x in (d1, d2, d3) if k in x and x[k] not in (None,)
            )
            if len(vals) == 1:
                return {k: vals[0]} | build(keys)
            return {k: vals} | build(keys)

        return build(all_keys)


    try:
        d1 = eval(input("Enter a dictionary: "))
        d2 = eval(input("Enter a dictionary: "))
        d3 = eval(input("Enter a dictionary: "))

        if not all(isinstance(d, dict) for d in (d1, d2, d3)):
            raise ValueError

        res = dicts3add(d1, d2, d3)
        print(res)

    except:
        print("ERROR: Input is incorrect!")









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

