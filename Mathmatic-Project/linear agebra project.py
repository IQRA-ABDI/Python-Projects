
try:
    U = []
    V = []
    sum_of_U_and_V = []
    vector_sclar_mult = []
    dot_product_vector = []

    print()
    print("Welcome to our program")
    print("In our program you can find:")
    repeat = 1
    while repeat == 1:  
        print("1. vector addition")
        print("2. scalar vector multiplication")
        print("3. Dot Product")
        print()

        print('pls choose one')
        choise = int(input(''))
        if choise == 1:
            def vector_addition():
                print("***Vector Addition***")
                print("Enter elements of vector U: ")
                user_input_U = int(input(""))
                # this loop checks if the user entered value less than 1
                while user_input_U <= 1:
                    print("Vectors can have at least two elements")
                    user_input_U = int(input(""))
                print("Enter elements of v vector:")
                user_input_V = int(input(""))
                # this loop checks if the user entered value less than 1
                while user_input_V <= 1:
                    print("Vectors can have at least two elements")
                    user_input_V = int(input(""))
                # this loop compares the two vectors elements if they are same
                while user_input_U != user_input_V:
                    print("Please enter same vectors")
                    user_input_U = int(input(""))
                    user_input_V = int(input(""))
                # this loop stores elemts entered by the user
                for num in range(user_input_U):
                    print("Enter element", num + 1, "of U vector")
                    user_input_u_elemnt = int(input(""))
                    U.append(user_input_u_elemnt)
                # print()
                # print("You entered")
                # print("U = ",U)
                # this loop stores elemts entered by the user
                for num in range(user_input_V):
                    print("Enter element", num + 1, "of V vector")
                    user_input_v_element = int(input(""))
                    V.append(user_input_v_element)
                print()
                print("The two vectors you entered are:")
                print("U = ", U)
                print("V = ", V)

                # this loop adds the two vectors entered by the user

                for num in range(len(U)):
                    sum = U[num] + V[num]
                    sum_of_U_and_V.append(sum)

                print("The sum of the two vectors are:")
                print("U + V = ", sum_of_U_and_V)

            vector_addition()


        elif choise == 2:
            def vector_scalar_multiplication():
                print("***scalar vector multiplicaion")
                scalar = int(input("Enter the scalar number: "))
                vector = int(input("Enter elements of U vector: "))
                # this loop checks number of elements entered by the user
                while vector <= 1:
                    print("Vectors can have at least two elements: ")
                    vector = int(input("Enter elements of U vector: "))
                # this loop stores the elements entered by the user
                for num in range(vector):
                    print("Enter element", num + 1)
                    vector_elemnts = int(input(""))
                    U.append(vector_elemnts)

                print("You enetered")
                print("The scalar is:", scalar, "\t U = ", U)

                # this loop multiplies scalar by vector entered by the user

                for num in range(len(U)):
                    product = scalar * U[num]
                    vector_sclar_mult.append(product)

                print("the product of is:", vector_sclar_mult)

            vector_scalar_multiplication()

        elif choise ==  3:      #Dot prodect
            def inner_prodect():
                print('Dot prodect')
                # this loop checked if user entered less 1 element
                user_input_U_vector = int(input("Enter elements of vector U: \n"))
                while user_input_U_vector <= 1:
                    user_input_U_vector = int(input('Pls enter value two or more vector elements: \n'))
                # this loop checked if user entered less 1 element
                user_input_v_vector = int(input('Enter elements of vector V: \n'))
                while user_input_v_vector <= 1:
                    user_input_v_vector = input('Pls enter value two or more vector elements: \n')
                # this loop checking if the value vector elements are sum
                while user_input_U_vector != user_input_v_vector:
                    print('Pls enter the same vector: \n')
                    user_input_U_vector = int(input('Enter elements of vector U: \n'))
                    user_input_v_vector = int(input('Enter elements of vector V: \n'))
                # this loop holds elemts insert by the user
                for num in range(user_input_U_vector):
                    print("enter element", num + 1, "of U vector")
                    user_input_u_element = int(input(""))
                    U.append(user_input_u_element)
                # this loop holds elemts insert by the user
                for num in range(user_input_v_vector):
                    print("enter element", num + 1, "of V vector")
                    user_input_v_element = int(input(""))
                    V.append(user_input_v_element)
                print('the two vectors elements are: \n U = ', U, '\n V = ', V)
                # this loop multiplying two vectors insert user
                dot_product = 0
                for num in range(len(U)):
                    mul = U[num] * V[num]
                    dot_product_vector.append(mul)
                    dot_product += mul
                print('the two vectors multiplying are: \n U * V = ', dot_product_vector)
                print('the sum of vectors are: ', dot_product)


            inner_prodect()
        else:
            print('pls choose only 1,2 or 3')
        print()
        repeat = int(input("if you want to try again tap '1' else '0'"))
except Exception as r:
    print(r)

#copy right BCS14-B Group-C