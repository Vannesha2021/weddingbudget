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
        print("Please state the month in terms of a number")
        print("Example: If it is February, you should state 2\n")

        month = input("Enter the month here: ")
        if validate_data(month):
            print("Month has been noted, thank you.\n")
            show_alldata_month1(month)
            show_alldata_month2(month)

            break

    
def validate_data(values):

    """
    Raises an error if the month 
    selected is not a valid number or not an integer.
    """
    try:
        if int(values) > 12:

            raise ValueError
            (f"You may only choose from month 1 to 12")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def show_alldata_month1(month):

    """
    Projects expenses,savings and balance for
    January
    """
    print("Retrieving data...\n")

    if month == "1":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A1')[0][0]
        alldata_m1_2 = SHEET.worksheet("alldata").get('B2')[0][0]
        print(("The month you have chosen :"),alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B3')[0][0]
        print(("Your expenses for this month will be:"),alldata_m1_2)

        jan = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings for this month should be:"),jan)
        
    return month



def show_alldata_month2(month):

    """
    Projects expenses,savings and balance for
    February
    """

    if month == "2":
        print("Retrieving data...\n")
        alldata_m2 = SHEET.worksheet("alldata").get('A6:B9')
        print(alldata_m2)
        
    return month


def main():
    """
    Run all program functions
    """
    get_month_data()
    
main()

