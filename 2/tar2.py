#
#  Targil 2
#
##Noam Hadad 322766064
##Guedalia Sebbah 337966659



#
#f1
def f1():

#
#f2



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

