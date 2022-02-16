import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('planning_doc')

def get_month_data():
    """
    Get month from the user.
    Run a while loop to collect the valid month from the user via the terminal, 
    which must be from month 1 to 12. The loop will repeatedly request a valid 
    data until the data collected is correct.
    """
    while True:
        print("Welcome to Wedding Budget Planner.\n")
        print("Here is the your wedding planning budget at the moment.")

        month = input("Enter the month here: ")
        if validate_data(month):
           print("Month has been noted, thank you.\n")
           break

def validate_data(values):
    """
    Raises an error if the month selected is not a valid number or not an integer.
    """
    try:
        if int(values) >12:
            raise ValueError(
                f"You may only choose from month 1 to 12"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def show_expenses_month1(month):
    if month(input) == "1":
        print("Retrieving data")
        expenses_data_m1 = SHEET.worksheet("expenses").cell(col=6 ,row=2)
        print(expenses_data_m1)
        
    return month


def main():
    """
    Run all program functions
    """
    data = get_month_data()
    month = show_expenses_month1()
main()