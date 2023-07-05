import social_network_ui
x=0
# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
        self.list_of_ages = []                        # you can save objects of people on the network in this list
        self.friendlist = []
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        age = input("Age: ")
        name = input("Name: ")
        
        self.list_of_people.append(name)
        self.list_of_ages.append(age)
        print("Creating ...")
        pass

    def edit_details(self):
        detail_choice = social_network_ui.editDetailsMenu()
        while True:
            if detail_choice == ("1"):
                self.id = input ("Changed name: ")
                print("name has been changed.")
                break
            elif detail_choice == ("2"):
                self.year = input ("Changed age: ")
                print("age has been changed.")
                break
            elif detail_choice == ("3"):
                break
            else:
               break
       
class Person:
    person_count = 0

    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        
    def add_friend(self, person_object):
         print("Who would you like to add as your friend?")
         print("Possible friends: " , self.id )
         self.friendlist.append(input("Friend you would like to add:"))
        #implement adding friend. Hint add to self.friendlist
         pass

    def send_message(self, friendname, message):
        #implement sending message to friend here
        pass

