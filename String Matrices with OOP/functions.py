class StringMatrices:

    dimension = 0
    first_matrix = []
    second_matrix = []

    # Constructor of class. It takes an int as parameter that will become the
    # dimension of the matrices
    def __init__ (self, dimension):
        self.dimension = dimension

    # Instance that creates 2 2D Arrays with a size depending of the dimension
    # member of the class. The default initialisation is with blank spaces
    def create_matrices (self):
        self.first_matrix = [[""]*self.dimension for _ in range(self.dimension)]
        self.second_matrix = [[""] * self.dimension for _ in range(self.dimension)]

    # Instance used to initialise the matrix members of the class with strings
    # entered by the user. It iterates through the matrices, one at a time,
    # and prompts the user to enter a string for each position
    def read_matrices (self):
        print()
        print("First matrix:")
        for i in range(len(self.first_matrix)):
            for j in range(len(self.first_matrix[0])):
                self.first_matrix[i][j] = input("matrix[{}][{}]: ".format(i, j))
        print()
        print("Second matrix:")
        for i in range(len(self.second_matrix)):
            for j in range(len(self.second_matrix[0])):
                self.second_matrix[i][j] = input("matrix[{}][{}]: ".format(i, j))

    # Instance that prints matrices of the class
    # It takes each row of the matrix and uses .join() with a " " separator
    # to print the matrix in a more user-friendly way
    def print_matrix (self, check):
        if check == 1:
            for row in self.first_matrix:
                print(" ".join(row))
        elif check == 2:
            for row in self.second_matrix:
                print(" ".join(row))
        elif check == 3:
            for row in self.first_matrix:
                print(" ".join(row))
            print()
            for row in self.second_matrix:
                print(" ".join(row))

    # Instance used print the size of the two member matrices of the class
    def print_size_of_matrices (self):
        print("Size of matrices: {} x {}" .format(self.dimension, self.dimension))

    # Instance used to add the two matrix members of the class.
    # It iterates through the matrices at the same time
    # concatenating elements with the same indices in a result matrix.
    # In the end, the result matrix is printed
    def add_matrices (self):
        res = []
        for i in range(len(self.first_matrix)):
            row = []
            for j in range(len(self.first_matrix[0])):
                row.append(self.first_matrix[i][j] + self.second_matrix[i][j])
            res.append(row)
        for row in res:
            print(" ".join(row))

    # Instance used to check if a given string is found in a selected matrix
    # member of the class
    # If found, it's coordinates are printed out, else, an error message will
    # be printed out instead
    def search_element (self, element, check):
        if check == 1:
            OK = 0
            for i in range(len(self.first_matrix)):
                for j in range(len(self.first_matrix[0])):
                    if (self.first_matrix[i][j] == element):
                        OK = 1
                        print("Found at coord: {} {}".format(i, j))
                        break
            if OK == 0:
                print("Element {} not found.".format(element))
        elif check == 2:
            OK = 0
            for i in range(len(self.second_matrix)):
                for j in range(len(self.second_matrix[0])):
                    if (self.second_matrix[i][j] == element):
                        OK = 1
                        print("Found at coord: {} {}".format(i, j))
                        break
            if OK == 0:
                print("Element {} not found.".format(element))

    # Instance used to edit a certain element from either the first
    # matrix member or the second one.
    # It prompts the user to enter the coordinates of the element they
    # want to modify and after that to enter the new value for that elements
    def modify_element (self, check):
        if check == 1:
            row = int(input("Enter row: "))
            column = int(input("Enter column: "))
            new_element = input("Enter the new value: ")
            self.first_matrix[row][column] = new_element
        elif check == 2:
            row = int(input("Enter row: "))
            column = int(input("Enter column: "))
            new_element = input("Enter the new value: ")
            self.second_matrix[row][column] = new_element

    # Instance used to multiply the two matrix members of the class.
    # Like normal matrix multiplication, we iterate through the lines of the
    # first matrix and through the columns of the second matrix, converting the strings
    # from the second matrix into ints according to the conversion rule, then we put the
    # string from the first matrix multiplied by their specific numbers from the second
    # matrix in a final matrix. At the end of the function we print that final matrix
    def multiply_matrices (self):
        final_matrix = [[""]*self.dimension for _ in range(self.dimension)]
        for i in range(len(self.first_matrix)):
            for j in range(len(self.second_matrix[0])):
                k = 0
                x = 0
                word = ""
                string = self.second_matrix[i][j]
                for k in range(len(string)):
                    letter = string[k]
                    x = x * 10 + (ord(letter) - 97)
                word = self.first_matrix[i][j]
                for p in range(x):
                    final_matrix[i][j] = final_matrix[i][j] + word

        for row in final_matrix:
            print(" ".join(row))

    # Instance used to lexicographically compare the two matrix
    # members of the class
    # We iterate through the 2 matrices at the same time, then iterate through each string from
    # those matrices at the same time to check is they differ by a letter. If that is the case
    # we return 1 or -1 depending on the comparison results. If the matrices are "equal" we return 0
    def compare_matrices (self):
        OK = 0
        for i in range(len(self.first_matrix)):
            for j in range(len(self.first_matrix[0])):
                first_element = self.first_matrix[i][j]
                second_element = self.second_matrix[i][j]
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