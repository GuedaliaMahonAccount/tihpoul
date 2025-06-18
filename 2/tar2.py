#
#  Targil 2
#
## Noam Hadad 322766064
## Guedalia Sebbah 337966659

#
# Question 1: Pentagonal-number range
#   a) pure function pentaNumRange(n1, n2)
#   b) imperative version: input, validate, print 10 per line
#   c) fully functional version
def f1():
    # TODO: implement parts a, b, c of question 1 :contentReference[oaicite:0]{index=0}
    pass

#
# Question 2: sumDigits
#   pure function sumDigits(n)
#   then input, validate, print result
def f2():
    # TODO: implement question 2 :contentReference[oaicite:1]{index=1}
    pass

#
# Question 3: isPalindrome
#   pure helper to reverse digits; isPalindrome(n)
#   then input, validate, print message
def f3():
    # TODO: implement question 3 :contentReference[oaicite:2]{index=2}
    pass

#
# Question 4: series‐sum m(n)
#   pure function m(n) for ∑_{i=1}ⁿ 1/(i+1)
#   then input, validate, loop printing i and m(i)
def f4():
    # TODO: implement question 4 :contentReference[oaicite:3]{index=3}
    pass

#
# Question 5: add3dicts
#   pure function add3dicts(d1, d2, d3)
#   then input three dicts, validate, print merged dict
def f5():
    # TODO: implement question 5 :contentReference[oaicite:4]{index=4}
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
            print()   # blank line before running
            functions[choice]()
        else:
            print("Invalid choice, try again.")
