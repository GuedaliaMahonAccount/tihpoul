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
    print("Hello world!")









if __name__ == '__main__':
    # map menu choices to your functions
    functions = {
        '1': f1,
        '2': f2,
        '3': f3,
        #'4': f4,
        # '5': f5,
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
