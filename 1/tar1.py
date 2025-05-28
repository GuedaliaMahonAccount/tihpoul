#
#  Targil 1
#
##Noam Hadad 322766064
##Guedalia Sebbah 337966659
import math
from myboolfuncs import *
import random


#
#f1
def f1():
    # triangle 3 side, and check if it s possible
    def checkTriangle(x, y, z):
        if ((x + y < z) | (x + z < y) | (y + z < x)):
            return False
        else:
            return True

    #main of f1
    print("Welcome to Triangle")
    print("Enter 3 sides of the triangle")
    x = float(input("Enter first: "))
    y = float(input("Enter second: "))
    z = float(input("Enter third: "))
    if (checkTriangle(x, y, z)):
        print("correct triangle sides lengths")
    else:
        print("not correct triangle sides lengths")

#
#f2
def f2():
    # Area calculation program
    def rectangleArea(w, h):
        return w * h

    #
    def circleArea(r):
        return math.pi * r ** 2

    #
    def triangleArea(b, h):
        return (b * h) / 2

    #
    def squereArea(w):
        return w * w

    #
    def sphereArea(r):
        return (4 / 3) * math.pi * r ** 3

    #
    def coneArea(r, h):
        return (1 / 3) * math.pi * r ** 2 * h

    #
    def pyramidArea(b, h):
        return (1 / 3) * b ** 2 * h

    #
    # printing the menu options
    def prtMenu(shapes):
        for i in range(len(shapes)):
            print(i + 1, shapes[i])
        return

    #main of f2
    print("Welcome to the Area calculation program")
    print("---------------------------------------\n")
    # Print out the menu
    shapes = ("Rectangle", "Circle", "Triangle", "Square", "Sphere", "Cone", "Pyramid")
    while True:
        print("\nPlease select a shape (press 0 to quit):")
        prtMenu(shapes)
        # Get the user's choice:
        shape = input("> ")

        # Calculate the area:
        if shape == "1":
            height = getNumber("Please enter the height: ")
            width = getNumber("Please enter the width: ")
            area = rectangleArea(width, height)
            print("The area is", area)
            continue

        elif shape == "2":
            radius = getNumber("Please enter the radius: ")
            area = circleArea(radius)
            print("The area is", area)
            continue

        elif shape == "3":
            base = getNumber("Please enter the base: ")
            height = getNumber("Please enter the height: ")
            area = triangleArea(base, height)
            print("The area is", area)

        elif shape == "4":
            height = getNumber("Please enter the height:")
            area = squereArea(height)
            print("The area is", area)

        elif shape == "5":
            radius = getNumber("Please enter the radius:")
            area = sphereArea(radius)
            print("The area is", area)

        elif shape == "6":
            radius = getNumber("Please enter the radius:")
            height = getNumber("Please enter the height:")
            area = coneArea(radius, height)

        elif shape == "7":
            base = getNumber("Please enter the base:")
            height = getNumber("Please enter the height:")
            area = pyramidArea(base, height)
            print("The area is", area)

        elif shape == "0":
            print("Bye!")
            break

        else:
            print("Invalid shape")

#
#f3
def f3():
    # — for exactly 4 numbers —
    def middle4(a, b, c, d):
        nums = [a, b, c, d]
        # sorted version
        s = sorted(nums)
        # manual version: drop min and max
        smallest, largest = min(nums), max(nums)
        mids = [x for x in nums if x not in (smallest, largest)]
        return (s[1], s[2]), (mids[0], mids[1])

    # — for more than 4 —
    def middleOfBigList(nums):
        n = len(nums)
        if n % 2:
            raise ValueError("Need an even number of elements")
        s = sorted(nums)
        m = n // 2
        # sorted and manual if all values distinct
        return (s[m - 1], s[m]), tuple(x for x in nums
                                       if sum(1 for y in nums if y < x) in (m - 1, m))

    # — helper to erase non-numbers —
    def filter_numbers(lst):
        return [x for x in lst if isinstance(x, (int, float))]

    #main of f3
    print("Welcome to Middle Calculation")
    while True:
        print("\nChoose option:")
        print("  1. Four numbers (Part Alef)")
        print("  2. Even-length list (Part Beit)")
        print("  3. Mixed list with numbers only (Part Gimel)")
        print("  0. Exit")
        choice = input("> ")

        if choice == "1":
            vals = [float(input(f"  enter number #{i}: ")) for i in range(1, 5)]
            sorted_mid, manual_mid = middle4(*vals)
            print("  middle values (with sort):", sorted_mid)
            print("  middle values (without sort):", manual_mid)

        elif choice == "2":
            raw = input("  enter numbers separated by spaces: ")
            nums = [float(x) for x in raw.split()]
            sorted_pair, manual_pair = middleOfBigList(nums)
            print("  middle values (with sorted()):", sorted_pair)
            print("  middle values (manual):", manual_pair)

        elif choice == "3":
            raw = input("  enter a Python-style list (e.g. [1, 'a', 2.5, None, 3]): ")
            data = eval(raw)  # Assuming trusted input
            nums = filter_numbers(data)
            sorted_pair, manual_pair = middleOfBigList(nums)
            print("  numeric middles (with sort):", sorted_pair)
            print("  numeric middles (manual):", manual_pair)

        elif choice == "0":
            print("Goodbye from f3!")
            break
        else:
            print("Invalid option. Try again.")

#
#f4
def f4():
    def shiftL(binNr, N):
        # drop leftmost N bits, pad N zeros on right
        return binNr[N:] + "0" * N

    def shiftR(binNr, N):
        # drop rightmost N bits, pad N zeros on left
        return "0" * N + binNr[:-N]

    def shiftCL(binNr, N):
        # rotate left by N (wrap the dropped bits to the end)
        L = len(binNr)
        N %= L
        return binNr[N:] + binNr[:N]

    def shiftCR(binNr, N):
        # rotate right by N (wrap the dropped bits to the front)
        L = len(binNr)
        N %= L
        return binNr[-N:] + binNr[:-N]

    #main of f4
    print("Welcome to the binary program")
    print("---------------------------------------\n")
    while True:
        print("\nChoose shift function:")
        print("  1. shiftL  (logical left)")
        print("  2. shiftR  (logical right)")
        print("  3. shiftCL (circular left)")
        print("  4. shiftCR (circular right)")
        print("  0. Exit")
        choice = input("> ")

        if choice == "0":
            print("Goodbye from f4!")
            break

        binNr = input("Enter binary string (e.g. 11000110): ")
        N = int(input("Enter number of places to shift: "))

        if choice == "1":
            print("Result:", shiftL(binNr, N))
        elif choice == "2":
            print("Result:", shiftR(binNr, N))
        elif choice == "3":
            print("Result:", shiftCL(binNr, N))
        elif choice == "4":
            print("Result:", shiftCR(binNr, N))
        else:
            print("Invalid option. Try again.")

#
#f5
def f5():
    # count function
    def count_lists(data):
        count = 0
        for x in data:
            if isinstance(x, list):
                count += 1
        return count

    def count_ints(data):
        count = 0
        for x in data:
            # bool is subclass of int; exclude booleans
            if isinstance(x, int) and not isinstance(x, bool):
                count += 1
        return count

    def count_floats(data):
        count = 0
        for x in data:
            if isinstance(x, float):
                count += 1
        return count

    def count_strs(data):
        count = 0
        for x in data:
            if isinstance(x, str):
                count += 1
        return count

    def count_tuples(data):
        count = 0
        for x in data:
            if isinstance(x, tuple):
                count += 1
        return count

    # main of f5
    print("Welcome to Type Counter")
    raw = input("Enter a Python-style list (e.g. [1,2,'a',(3,),[4]]): ")
    data = eval(raw)  # assuming input is always correct
    type_dict = {
        'list': count_lists(data),
        'int': count_ints(data),
        'float': count_floats(data),
        'str': count_strs(data),
        'tuple': count_tuples(data)
    }
    print("Type-count dictionary:", type_dict)
    total_records = type_dict['tuple']
    total_lists = type_dict['list']
    total_numbers = type_dict['int'] + type_dict['float']
    total_strings = type_dict['str']
    print(
        f"סה\"כ הרשומות: {total_records}, סה\"כ הרשימות: {total_lists}, סה\"כ המספרים: {total_numbers}, סה\"כ המחרוזות: {total_strings}")

#
#f6
def f6():
    def nihushTest(target_tuple, *guesses):
        N = len(target_tuple)
        result = []
        for i, g in enumerate(guesses):
            if i < N and g == target_tuple[i]:
                result.append(g)
            else:
                result.append("X")
        return tuple(result)

    # 1) Choose N
    while True:
        try:
            N = int(input("Enter the number of elements to guess (3–9): "))
        except ValueError:
            print("  ✗ please enter an integer.")
            continue
        if 3 <= N <= 9:
            break
        print("  ✗ N must be between 3 and 9.")

    # 2) Generate the hidden tuple
    hidden = tuple(random.randint(1, 9) for _ in range(N))
    maxpct = 0.0

    # 3) Main guess loop
    while True:
        line = input(f"\nEnter your guess of {N} numbers (space-separated), or -1 to quit: ")
        if line.strip() == "-1":
            print("You chose to exit.")
            break

        parts = line.split()
        if len(parts) != N:
            print(f"  ✗ Please enter exactly {N} numbers.")
            continue

        try:
            guess = [int(p) for p in parts]
        except ValueError:
            print("  ✗ All entries must be integers.")
            continue

        if any((g < 1 or g > 9) for g in guess):
            print("  ✗ Numbers must be in 1–9.")
            continue

        # 4) Test the guess
        result = nihushTest(hidden, *guess)
        print("Result:        ", result)

        # 5) Compute success %
        correct = sum(1 for x in result if x != "X")
        pct = correct / N * 100
        print(f"Success rate:  {pct:.2f}%")
        if pct > maxpct:
            maxpct = pct

        # 6) Check for perfect guess
        if correct == N:
            print("You’ve guessed all numbers.")
            break

    # 7) Game over – reveal and highest %
    print("\nGame over.")
    print("The hidden numbers were:", hidden)
    print(f"Your highest success rate was: {maxpct:.2f}%")


if __name__ == '__main__':
    # map menu choices to your functions
    functions = {
        '1': f1,
        '2': f2,
        '3': f3,
        '4': f4,
        '5': f5,
        '6': f6,
    }

    print("Welcome to Targil 1")
    print("---------------------------------------")

    while True:
        # print menu
        print("\nyour choices:")
        print("0 : exit")
        for num in sorted(functions):
            print(f"{num} : function {num}")

        # get choice
        choice = input("please enter your choice ")

        # dispatch
        if choice == '0':
            print("Bye!")
            break
        elif choice in functions:
            print()           # extra line before function runs
            functions[choice]()
        else:
            print("Invalid choice, try again.")

