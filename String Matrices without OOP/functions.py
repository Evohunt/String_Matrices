# Function used to create a 2D Array of given size
# We take 2 given arguments and return the initialisation
# of a matrix with blank characters, the size of the matrix
# depending to the 2 given arguments(ints)
def create_matrix(width, heigth):
    return [[""]*heigth for _ in range(width)]

# Function used to initialize a given 2D Array with strings entered by the user
# It iterates through the matrix, and the user is promted to enter a values
# to be entered in each position in the matrix
def read_matrix(new_matrix):
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            new_matrix[i][j] = input("matrix[{}][{}]: " .format(i, j))
    print()

# Function used to print a given 2D Array
# It takes each row of the matrix and uses .join() with a " " separater
# to print the matrix in a more user-friendly way
def print_matrix(new_matrix):
    for row in new_matrix:
        print(" ".join(row))

# Function used to print the width and heigth of a given 2D Array
# It saves the required values in 2 variables and then it prints them
def print_size_of_matrix(new_matrix):
    heigth = len(new_matrix)
    width = len(new_matrix[0])

    print ("Heigth: {}" .format(heigth))
    print ("Width: {}" .format(width))

# Function used to add two 2D Arrays containing strings
# We iterate through the matrices at the same time concatenating elements with the
# same indices in a third matrix. At the end, the final matrix is returned
def add_matrix(first_matrix, second_matrix):
    res = []
    for i in range(len(first_matrix)):
        row = []
        for j in range(len(first_matrix[0])):
            row.append(first_matrix[i][j] + second_matrix[i][j])
        res.append(row)
    return res

# Function used to check if a specific element is found in a given 2D Array
# It iterates through the matrix searching for an element. If the element
# is found the function will print it and break the searching operation.
# If the searching operation is concluded without finding the element the
# function will print an error message
def search_element(element, new_matrix):
    OK = 0
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[0])):
            if (new_matrix[i][j] == element):
                OK = 1
                print ("Found at coord: {} {}" .format(i, j))
                break
    if OK == 0:
        print("Element {} not found." .format(element))

# Function used to edit a specific element from a given 2D Array
# It promts the user to enter the coordinates of the element they
# want to modify and after that to enter the new value for that elements
def modify_element(matrix):
    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    new_element = input("Enter the new value: ")
    matrix[row][column] = new_element

# Function used to multiply two given 2D Arrays
# Like normal matrix multiplication, we iterate through the lines of the
# first matrix and through the columns of the second matrix, converting the strings
# from the second matrix into ints according to the conversion rule, then we put the
# string from the first matrix multiplied by their specific numbers from the second
# matrix in a final matrix. At the end of the function we print that final matrix
def multiply_matrices(first_matrix, second_matrix, final_matrix):
    for i in range(len(first_matrix)):
        for j in range(len(second_matrix[0])):
            k = 0
            x = 0
            word = ""
            string = second_matrix[i][j]
            for k in range(len(string)):
                letter = string[k]
                x = x * 10 + (ord(letter) - 97)
            word = first_matrix[i][j]
            for p in range(x):
                final_matrix[i][j] = final_matrix[i][j] + word

    print_matrix(final_matrix)

# Function used to lexicographically compare two given 2D Arrays
# We iterate through the 2 matrices at the same time, then iterate through each string from
# those matrices at the same time to check is they differ by a letter. If that is the case
# we return 1 or -1 depending on the comparison results. If the matrices are "equal" we return 0
def compare_matrices(first_matrix, second_matrix):
    OK = 0
    for i in range(len(first_matrix)):
        for j in range(len(first_matrix[0])):
            first_element = first_matrix[i][j]
            second_element = second_matrix[i][j]
            if len(first_element) > len(second_element):
                maximum = len(first_element)
            else:
                maximum = len(second_element)
            for x in range(maximum):
                if ord(first_element[x]) > ord(second_element[x]):
                    OK = 1
                    return 1
                    break
                elif ord(first_element[x]) < ord(second_element[x]):
                    OK = 1
                    return -1
                    break
    if OK == 0:
        return 0