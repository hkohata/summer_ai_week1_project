#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui




#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()
    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            while True:
                if inner_menu_choice == "1":
                    print ("You are now in the edit my details menu.")
                    ai_social_network.edit_details()
                    break
                elif inner_menu_choice == "2":
                    print ("You are now in the add friends menu")
                    Person.add_friend()
                elif inner_menu_choice == "3":
                    print("Your friends:")
                    print(ai_social_network.friendlist)
                    break
                elif inner_menu_choice == "4":
                    print("Your current friends:")
                    print(ai_social_network.friendlist)
                    ai_social_network.friendlist.clear(input("Friend you would like to block:"))
                    break
                elif inner_menu_choice == "5":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break
        elif choice == "4":
            print(ai_social_network.list_of_people)

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
