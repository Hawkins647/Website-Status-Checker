import requests as rq
import requests.exceptions
from colorama import Fore


def display_menu():
    global userchoice
    print(Fore.GREEN + "Welcome! Please enter an option using the numbers provided.")
    print("1: Enter a url to check the status of")
    print("2: Quit")
    userchoice = input("Enter your choice: ")

    if userchoice == "1":
        url = str(input("\nPlease enter the URL: "))
        try:
            check_status(url)
        except requests.exceptions.MissingSchema:
            print("\nPlease enter an appropriate URL.\n")


def check_status(url: str):
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


userchoice = ""
while userchoice != "2":
    display_menu()

print(Fore.WHITE + "Goodbye!")