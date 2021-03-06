from functions import *

width = int(input("Width: "))
heigth = int(input("Heigth: "))
first_matrix = create_matrix(width, heigth)
second_matrix = create_matrix(width, heigth)

read_matrix(first_matrix)
read_matrix(second_matrix)

# Function used to promt the user to choose an option for the 2 matrices
def menu():

    print ("==================================================")
    print ("\t1. Print matrix/matrices")
    print ("\t2. Print dimension of matrix/matrices")
    print ("\t3. Add matrices")
    print ("\t4. Multiply matrices")
    print ("\t5. Compare matrices")
    print ("\t6. Search element")
    print ("\t7. Edit element")
    print ("==================================================")
    choice = int(input("Enter your option: "))

    if choice == 1:
        print("1. First matrix")
        print("2. Second matrix")
        print("3. Both matrices")
        temp_choice = int(input("Option: "))
        if temp_choice == 1:
            print()
            print_matrix(first_matrix)
        elif temp_choice == 2:
            print()
            print_matrix(second_matrix)
        elif temp_choice == 3:
            print ()
            print_matrix(first_matrix)
            print ()
            print_matrix(second_matrix)
        else:
            print ("Invalid option.")
        print ()
        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()
    elif choice == 2:
        print("1. First matrix")
        print("2. Second matrix")
        print("3. Both matrices")
        temp_choice = int(input("Option: "))
        if temp_choice == 1:
            print ()
            print_size_of_matrix(first_matrix)
        elif temp_choice == 2:
            print ()
            print_size_of_matrix(second_matrix)
        elif temp_choice == 3:
            print ()
            print_size_of_matrix(first_matrix)
            print ()
            print_size_of_matrix(second_matrix)
        else:
            print ("Invalid option.")
        print ()
        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()
    elif choice == 3:
        final_matrix = add_matrix(first_matrix, second_matrix)
        print ()
        print_matrix(final_matrix)
        print ()
        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()
    elif choice == 4:
        final_matrix = create_matrix(width, heigth)
        print ()
        multiply_matrices(first_matrix, second_matrix, final_matrix)
        print ()
        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()
    elif choice == 5:
        result = compare_matrices(first_matrix, second_matrix)
        if result == 0:
            print ()
            print("They are equal.")
            print ()
        elif result == 1:
            print ()
            print("The first matrix is bigger.")
            print ()
        elif result == -1:
            print ()
            print("The first matrix is smaller.")
            print ()
        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()
    elif choice == 6:
        string_to_search = input("String to search: ")
        print ("1. Search in first matrix")
        print ("2. Search in second matrix")
        temp_choice = int(input("Option: "))
        if temp_choice == 1:
            print ()
            search_element(string_to_search, first_matrix)
            print ()
        elif temp_choice == 2:
            print()
            search_element(string_to_search, second_matrix)
            print ()
        else:
            print ("Invalid option.")
            print()
        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()
    elif choice == 7:
        print ("1. Edit an element from the first matrix")
        print ("2. Edit an element from the second matrix")
        temp_choice = int(input("Option: "))
        if temp_choice == 1:
            modify_element(first_matrix)
        elif temp_choice == 2:
            modify_element(second_matrix)
        else:
            print("Invalid option.")
        print ()
        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()
    else:
        print ("Invalid option.")
        print ()
        continue_input = input("Continue? Y / N ")
        if continue_input == 'Y' or continue_input == 'y':
            menu()