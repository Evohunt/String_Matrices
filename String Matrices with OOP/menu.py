from functions import *

dimension = int(input("Enter the size of the 2 matrices: "))
new_class = StringMatrices(dimension)
new_class.create_matrices()
new_class.read_matrices()

def menu():

    print("==================================================")
    print("\t1. Print matrix/matrices")
    print("\t2. Print dimension of matrices")
    print("\t3. Add matrices")
    print("\t4. Multiply matrices")
    print("\t5. Compare matrices")
    print("\t6. Search element")
    print("\t7. Edit element")
    print("==================================================")
    choice = int(input("Enter your option: "))

    if choice == 1: # Menu option #1
        print("1. First matrix")
        print("2. Second matrix")
        print("3. Both matrices")
        temp_choice = int(input("Option: "))

        if temp_choice == 1:
            print()
            new_class.print_matrix(1)
        elif temp_choice == 2:
            print()
            new_class.print_matrix(2)
        elif temp_choice == 3:
            print()
            new_class.print_matrix(3)
        else:
            print("Invalid option.")

        print()
        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()

    elif choice == 2: # Menu option #2
        print()
        new_class.print_size_of_matrices()

        print()
        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()

    elif choice == 3: # Menu option #3
        print()
        new_class.add_matrices()

        print()
        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()

    elif choice == 4: # Menu option #4
        print()
        new_class.multiply_matrices()

        print()
        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()

    elif choice == 5: # Menu option #5
        print()
        print("Comparison result: {}" .format(new_class.compare_matrices()))

        print()
        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()

    elif choice == 6: # Menu option #6
        print()
        string_to_search = input("String to search: ")
        print("1. Search in first matrix")
        print("2. Search in second matrix")
        temp_choice = int(input("Option: "))

        if temp_choice == 1:
            print()
            new_class.search_element(string_to_search, 1)
        elif temp_choice == 2:
            print()
            new_class.search_element(string_to_search, 2)
        else:
            print()
            print("Invalid option.")

        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()

    elif choice == 7: # Menu option #7
        print()
        print("1. Edit an element from the first matrix")
        print("2. Edit an element from the second matrix")
        temp_choice = int(input("Option: "))

        if temp_choice == 1:
            print()
            new_class.modify_element(1)
        elif temp_choice == 2:
            print()
            new_class.modify_element(2)

        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()

    else:
        print()
        print("Invalid option.")

        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()
