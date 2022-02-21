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
            show_alldata_month3(month)
            show_alldata_month4(month)
            show_alldata_month5(month)
            show_alldata_month6(month)
            show_alldata_month7(month)
            show_alldata_month8(month)
            show_alldata_month9(month)
            show_alldata_month10(month)
            show_alldata_month11(month)
            show_alldata_month12(month)
            break


def validate_data(values):

    """
    Raises an error if the month
    selected is not a valid number or not an integer.
    """
    try:
        if int(values) > 12:

            raise ValueError
            f'{"You may only choose from month 1 to 12"}'

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def validate_data2(values):

    """
    Raises an error if the month selected is less than 1.
    """
    try:
        if int(values) < 1:

            raise ValueError
            f'{"You may only choose from month 1 to 12"}'

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
        print(("The month you have chosen : "), alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B3')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        jan = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings for this month should be:"), jan)

    return month


def show_alldata_month2(month):

    """
    Projects expenses,savings and balance for
    February
    """

    if month == "2":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A5')[0][0]
        alldata_m1_2 = SHEET.worksheet("alldata").get('B6')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B7')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        feb_savings = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings for this month should be:"), feb_savings)
        print("\n")

        print("Retrieving total savings...\n")

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        feb_ts = int(alldata_m1_3) + int(alldata_m1_4)
        print(("Your total savings including past months is:"), feb_ts)

    return month


def show_alldata_month3(month):

    """
    Projects expenses,savings and balance for
    March
    """

    if month == "3":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A9')[0][0]
        alldata_m1_2 = SHEET.worksheet("alldata").get('B10')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B11')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        mar_savings = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings for this month should be:"), mar_savings)
        print("\n")

        print("Retrieving total savings...\n")

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        mar_ts = int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5)
        print(("Your total savings including past months is:"), mar_ts)

    return month


def show_alldata_month4(month):

    """
    Projects expenses,savings and balance for
    April
    """

    if month == "4":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A13')[0][0]
        alldata_m1_2 = SHEET.worksheet("alldata").get('B14')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B15')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        apr_savings = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings for this month should be:"), apr_savings)
        print("\n")

        print("Retrieving total savings...\n")

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        apr_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5)
                  + int(alldata_m1_6))
        print(("Your total savings including past months is:"), apr_ts)

    return month


def show_alldata_month5(month):

    """
    Projects expenses,savings and balance for
    May
    """

    if month == "5":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A17')[0][0]
        alldata_m1_2 = SHEET.worksheet("alldata").get('B18')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B19')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        may_savings = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings for this month should be:"), may_savings)
        print("\n")

        print("Retrieving total savings...\n")

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        may_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5)
                  + int(alldata_m1_6) + int(alldata_m1_7))
        print(("Your total savings including past months is:"), may_ts)

    return month


def show_alldata_month6(month):

    """
    Projects expenses,savings and balance for
    June
    """

    if month == "6":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A21')[0][0]
        alldata_m1_2 = SHEET.worksheet("alldata").get('B22')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B23')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        jun_savings = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings for this month should be:"), jun_savings)
        print("\n")

        print("Retrieving total savings...\n")

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        alldata_m1_8 = SHEET.worksheet("alldata").get('B19')[0][0]
        jun_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5)
                  + int(alldata_m1_6) + int(alldata_m1_7)
                  + int(alldata_m1_8))
        print(("Your total savings including past months is:"), jun_ts)

    return month


def show_alldata_month7(month):

    """
    Projects expenses,savings and balance for
    July
    """

    if month == "7":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A25')[0][0]
        alldata_m1_2 = SHEET.worksheet("alldata").get('B26')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B27')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        jul_savings = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings for this month should be:"), jul_savings)
        print("\n")

        print("Retrieving total savings...\n")

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        alldata_m1_8 = SHEET.worksheet("alldata").get('B19')[0][0]
        alldata_m1_9 = SHEET.worksheet("alldata").get('B23')[0][0]
        jul_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5)
                  + int(alldata_m1_6) + int(alldata_m1_7) + int(alldata_m1_8)
                  + int(alldata_m1_9))
        print(("Your total savings including past months is:"), jul_ts)

    return month


def show_alldata_month8(month):

    """
    Projects expenses,savings and balance for
    August
    """

    if month == "8":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A29')[0][0]
        alldata_m1_2 = SHEET.worksheet("alldata").get('B30')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B31')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        aug_savings = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings for this month should be:"), aug_savings)
        print("\n")

        print("Retrieving total savings...\n")

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        alldata_m1_8 = SHEET.worksheet("alldata").get('B19')[0][0]
        alldata_m1_9 = SHEET.worksheet("alldata").get('B23')[0][0]
        alldata_m1_10 = SHEET.worksheet("alldata").get('B27')[0][0]
        aug_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5)
                  + int(alldata_m1_6) + int(alldata_m1_7) + int(alldata_m1_8)
                  + int(alldata_m1_9) + int(alldata_m1_10))
        print(("Your total savings including past months is:"), aug_ts)

    return month


def show_alldata_month9(month):

    """
    Projects expenses,savings and balance for
    September
    """

    if month == "9":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A33')[0][0]
        alldata_m1_2 = SHEET.worksheet("alldata").get('B34')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B35')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        sep_savings = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings for this month should be:"), sep_savings)
        print("\n")

        print("Retrieving total savings...\n")

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        alldata_m1_8 = SHEET.worksheet("alldata").get('B19')[0][0]
        alldata_m1_9 = SHEET.worksheet("alldata").get('B23')[0][0]
        alldata_m1_10 = SHEET.worksheet("alldata").get('B27')[0][0]
        alldata_m1_11 = SHEET.worksheet("alldata").get('B27')[0][0]
        sep_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5)
                  + int(alldata_m1_6) + int(alldata_m1_7) + int(alldata_m1_8)
                  + int(alldata_m1_9) + int(alldata_m1_10)
                  + int(alldata_m1_11))
        print(("Your total savings including past months is:"), sep_ts)

    return month


def show_alldata_month10(month):

    """
    Projects expenses,savings and balance for
    October
    """

    if month == "10":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A37')[0][0]
        alldata_m1_2 = SHEET.worksheet("alldata").get('B38')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B39')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        oct_savings = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings for this month should be:"), oct_savings)
        print("\n")

        print("Retrieving total savings...\n")

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        alldata_m1_8 = SHEET.worksheet("alldata").get('B19')[0][0]
        alldata_m1_9 = SHEET.worksheet("alldata").get('B23')[0][0]
        alldata_m1_10 = SHEET.worksheet("alldata").get('B27')[0][0]
        alldata_m1_11 = SHEET.worksheet("alldata").get('B27')[0][0]
        alldata_m1_12 = SHEET.worksheet("alldata").get('B35')[0][0]
        oct_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5)
                  + int(alldata_m1_6) + int(alldata_m1_7)
                  + int(alldata_m1_8) + int(alldata_m1_9)
                  + int(alldata_m1_10) + int(alldata_m1_11)
                  + int(alldata_m1_12))
        print(("Your total savings including past months is:"), oct_ts)

    return month


def show_alldata_month11(month):

    """
    Projects expenses,savings and balance for
    November
    """

    if month == "11":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A41')[0][0]
        alldata_m1_2 = SHEET.worksheet("alldata").get('B42')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B43')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        nov_savings = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings for this month should be:"), nov_savings)
        print("\n")

        print("Retrieving total savings...\n")

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        alldata_m1_8 = SHEET.worksheet("alldata").get('B19')[0][0]
        alldata_m1_9 = SHEET.worksheet("alldata").get('B23')[0][0]
        alldata_m1_10 = SHEET.worksheet("alldata").get('B27')[0][0]
        alldata_m1_11 = SHEET.worksheet("alldata").get('B27')[0][0]
        alldata_m1_12 = SHEET.worksheet("alldata").get('B35')[0][0]
        alldata_m1_13 = SHEET.worksheet("alldata").get('B39')[0][0]
        nov_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5)
                  + int(alldata_m1_6) + int(alldata_m1_7) + int(alldata_m1_8)
                  + int(alldata_m1_9) + int(alldata_m1_10) + int(alldata_m1_11)
                  + int(alldata_m1_12) + int(alldata_m1_13))
        print(("Your total savings including past months is:"), nov_ts)

    return month


def show_alldata_month12(month):

    """
    Projects the chosen month. The data will show the expenses
    and savings for December.
    The end calaculations shows the total savings from Janauary
    until December.
    """

    if month == "12":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A45')[0][0]
        alldata_m1_2 = SHEET.worksheet("alldata").get('B46')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B47')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        nov_savings = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings for this month should be:"), nov_savings)
        print("\n")

        print("Retrieving total savings...\n")

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        alldata_m1_8 = SHEET.worksheet("alldata").get('B19')[0][0]
        alldata_m1_9 = SHEET.worksheet("alldata").get('B23')[0][0]
        alldata_m1_10 = SHEET.worksheet("alldata").get('B27')[0][0]
        alldata_m1_11 = SHEET.worksheet("alldata").get('B27')[0][0]
        alldata_m1_12 = SHEET.worksheet("alldata").get('B35')[0][0]
        alldata_m1_13 = SHEET.worksheet("alldata").get('B39')[0][0]
        alldata_m1_14 = SHEET.worksheet("alldata").get('B43')[0][0]
        dec_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5)
                  + int(alldata_m1_6) + int(alldata_m1_7)
                  + int(alldata_m1_8) + int(alldata_m1_9)
                  + int(alldata_m1_10) + int(alldata_m1_11)
                  + int(alldata_m1_12) + int(alldata_m1_13)
                  + int(alldata_m1_14))
        print(("Congratulations! Your total savings for the year is:"), dec_ts)

    return month


def main():

    """
    Run all program functions
    """
    get_month_data()


main()
