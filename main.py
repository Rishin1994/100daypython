# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import drinks


#toDo  Update the resources once the input is succesful added the latest
print("testing")
def update_resource():

    for key in drinks.MENU[answer]["ingredients"]:
        drinks.resources[key]  -= drinks.MENU[answer]["ingredients"][key]
    drinks.resources["money"] += drinks.MENU[answer]["cost"]

#ToDO create a report that returns the quantity of the items left
def report():
    print(drinks.resources)
#toDo based on drink check if resource is sufficient if the option is incoorect print wrong option
def report_check():
    for key in drinks.MENU[answer]["ingredients"]:
        if drinks.MENU[answer]["ingredients"][key] > drinks.resources[key]:
            print (f"Not Enough {key}\n")
            return False
    return True
def money_check(quaters,dimes,nikel,pennies):
    dollar = 0.25*quaters + 0.1*dimes + 0.05*nickel + 0.01*pennies
    if dollar > drinks.MENU[answer]["cost"] :
        return dollar- drinks.MENU[answer]["cost"]
    else:
        print("The Money is not sufficient. Money refunded")
        return -1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    answer=''

    while answer!= "off":
        answer = input("What would you like ? (expresso/latte/cappuccino)").lower()
        if answer not in drinks.MENU and answer not in ["off","report"]:
            print("incorrect option , try again")
            continue
        if answer=='report':
            report()
        elif answer =="off":
            exit()
        else:
            if report_check():
                print(f'''The cost of the drink is {drinks.MENU[answer]["cost"]}''')
                print("Please provide the coins")
                quaters=int(input("How Many Quaters?  "))
                dimes= int( input("How Many dimes ? "))
                nickel= int (input("How many Nickels ?"))
                pennies= int (input("How many pennies ? "))
                change = money_check(quaters,dimes,nickel,pennies)
                if change>=0 :
                    print(f"Here is your change {change}")
                    print(f"Here is your {answer} . Enjoy!")
                    update_resource()









# See PyCharm help at https://www.jetbrains.com/help/pycharm/

