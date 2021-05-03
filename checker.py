import requests as rq
import requests.exceptions
from colorama import Fore


class WebsiteChecker:
    """A class that creates a loop, allowing a user to check the status of a domain through the requests library."""

    def __init__(self):
        self.main_logic()

    def display_menu(self):
        print(Fore.GREEN + "Welcome! Please enter an option using the numbers provided.")
        print("1: Enter a url to check the status of")
        print("2: Quit")

    def check_status(self, url: str):
        response = rq.get(url)
        status = response.status_code
        if status == 200:
            print(url + " Has responded and there are no issues.\n")
        if status == 301:
            print(url + " Has permanently redirected to another domain.\n")
        if status == 302:
            print(url + " Has temporarily changed domain, maybe due to site maintenance.\n")
        if status == 404:
            print(url + "The page may have been removed, or a client side error has occured.\n")
        if status == 500:
            print(url + " Has had an internal server error.\n")

    def main_logic(self):
        user_input = ""
        while user_input != "2":
            self.display_menu()
            user_input = input("Enter your choice: ")

            if user_input == "1":
                url = str(input("\nPlease enter the URL: "))
                try:
                    self.check_status(url)
                except requests.exceptions.MissingSchema:
                    print("\nPlease enter an appropriate URL.\n")

        print(Fore.WHITE + "Goodbye!")

    def __str__(self):
        return "A class that will initialise a loop until the user exits, allowing them to check the status of a " \
               "domain through the requests library."


WebsiteChecker()
