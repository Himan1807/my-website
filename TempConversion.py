# function to convert farhenheit to celsius
def far_to_cel(far):
    return (far - 32) * 5 / 9

def cel_to_far(cel):
    return ((9 / 5) * cel) + 32

while(True):
    print("Temperature Convesion Options: ")
    print("1) Farhenheit to Celsius")
    print("2) Celsius to Farhenheit")
    print("3) Exit")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            far = float(input("Enter the farhenheit value: "))
            print(f"{far} F = {far_to_cel(far)} C")
        case 2:
            cel = float(input("Enter the celsius value: "))
            print(f"{cel} C = {cel_to_far(cel)} F")
        case 3:
            print("Exiting the program")
        case _:
            print("Invalid choice, kindly try again")
    if(choice == 3):
        break