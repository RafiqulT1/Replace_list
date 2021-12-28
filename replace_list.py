def display_list():
    print("Here is current list: ", value_list)
value_list = [1, 2, 3, 4, 5]

def check_input():
    while True:
        try:
            index = int(input("Type number between 1-5 to select position for replacement: "))
        except ValueError:
            print("Sorry worng value! :(")
        else:
            return index


display_list()
print(check_input())

#testing