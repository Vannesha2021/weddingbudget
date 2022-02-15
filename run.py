import gspread
from google.oauth2.service_account import Credentials

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
    Get month from the user
    """
    print("Which month expenses are you looking for?")
    print("Please state the month in terms of a number")
    print("Example: If it is February, you should state 2\n")

    month = input("Enter the month here: ")

    validate_data(month)

def validate_data(values):
    """
    Raises an error if the month selected is not a valid number.
    """

    try:
        if int(values) >12:
            raise ValueError(
                f"You may only choose from month 1 to 12"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

get_month_data()