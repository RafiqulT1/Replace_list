# print value_list at the beginning 
def display_list(value_list):
    print("Here is current list: ", value_list)

# Check user's input 
def check_input():
    while True:
        try:
            index = int(input("Type number between 1-5 to select index for replacement: "))
        except ValueError:
            print("Sorry worng value! :(")
        else:
            if index >= 1 and index <= 5:
                return index
            else:
                print("Value out of range")

# Replace list word/position with user's desired word
def replacement(value_list, index):
    value = input("Type a word to replace index: ")
    value_list[index - 1] = value
    return value_list

# Ask user if they want to continue replacing
def doplay():
    y_n = "wrong"
    while y_n not in ["Y", "N"]:
        y_n = input("Do you want to keep replacing words? (Y/y or N/n): ")
        y_n = y_n.capitalize()

        if y_n not in ["Y", "N"]:
            print("Please choose (Y/y or N/n)")

    if y_n == "Y":
        return True
    else:
        y_n == "N"
        return False

# List to begain with 
value_list = [1, 2, 3, 4, 5]

go_on = True

# Game logic
while go_on:
    display_list(value_list)
    position = check_input()
    value_list = replacement(value_list,position)
    print("Current list: ", value_list)
    go_on = doplay()

