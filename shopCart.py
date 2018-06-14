from IPython.display import clear_output

shop_list = []

def shopping():
    print("Welcome!")
    print("You can add, delete, see items in list,")
    print("or even quit shopping.")
    print()
    print("please write add / del / see / quit ")


    while True:
        select = input("What will you choose - add, delete, see, quit: ")
        if select == "add":
            item = input("Type an item: ")
            shop_list.append(item)

        elif select == "delete":
            item = input("Type an item: ")
            if item in shop_list:
                shop_list.remove(item)
            else:
                print("Type again!")

        elif select == "see":
            if len(shop_list) == 0:
                print("The cart is empty!!")

            for shop in shop_list:
                print(shop)

        elif select == "quit":
            break

        else:
            print("Wrote wrong, try again!")
