#
#  Targil 5
#
##Noam Hadad 322766064
##Guedalia Sebbah


#
# question 1
def f1():


#
# question 2
def f2():


#
# question 3
def f3():


#
# question 4
def f4():


#
# question 5
def f5():


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

