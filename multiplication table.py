def multiplication_table():
    number= int(input("Enter the number to display the multiplication table: "))

    print("\nUsing for loop:")
    for i in range(1,11):
        print(f"{number} X {i} = {number * i} ")

    print("\nUsing while loop:")
    i=1
    while i <= 10:
        print(f"{number} X {i} = {number * i} ")
        i+=1

multiplication_table()