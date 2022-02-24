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

        month = input("Enter the month here:\n")
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
        if int(values) <= 0:

            raise ValueError
            f'{"You may only choose from month 1 to 12"}'

    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    try:
        if int(values) > 12:

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
        
        print("\n")
        print("Retrieving savings data...\n")

        jan = int(alldata_m1_3)
        print(("Your savings for this month will be:"), jan)

        jan = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), jan)

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

        print("Retrieving total savings...\n")

        feb = int(alldata_m1_3)
        print(("Your savings for this month will be:"), feb)

        feb = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), feb)

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        feb_ts = int(alldata_m1_3) + int(alldata_m1_4)
        print(("Your total savings before expenses year to date is:"), feb_ts)

    return month


def show_alldata_month3(month):

    """
    Projects expenses,savings and balance for
    March
    """

    if month == "3":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A9')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_2 = SHEET.worksheet("alldata").get('B10')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B11')[0][0]
        print("\n")
        print("Retrieving savings data...\n")

        mar = int(alldata_m1_3)
        print(("Your savings for this month will be:"), mar)

        """
        Projects savings after deduction of expenses
        """
        mar = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), mar)

        """
        Projects overall savings for past and present month/s 
        before deduction of all monthly expenses
        """
        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        mar_ts = int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5)
        print(("Your total savings before expenses year to date is:"), mar_ts)

    return month


def show_alldata_month4(month):

    """
    Projects expenses,savings and balance for
    April
    """

    if month == "4":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A13')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_2 = SHEET.worksheet("alldata").get('B14')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B15')[0][0]
        print("\n")
        print("Retrieving savings data...\n")

        apr = int(alldata_m1_3)
        print(("Your savings for this month will be:"), apr)

        """
        Projects savings after deduction of expenses
        """
        apr = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), apr)

        """
        Projects overall savings for past and present month/s 
        before deduction of all monthly expenses
        """

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        apr_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5) +
                  int(alldata_m1_6))
        print(("Your total savings before expenses year to date is:"), apr_ts)

    return month


def show_alldata_month5(month):

    """
    Projects expenses,savings and balance for
    May
    """

    if month == "5":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A17')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_2 = SHEET.worksheet("alldata").get('B18')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B19')[0][0]
        print("\n")
        print("Retrieving savings data...\n")

        may = int(alldata_m1_3)
        print(("Your savings for this month will be:"), may)
        
        """
        Projects savings after deduction of expenses
        """
        may = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), may)

        print("\n")
        print("Retrieving total savings data...\n")

        """
        Projects overall savings for past and present month/s 
        before deduction of all monthly expenses
        """

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        may_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5) +
                  int(alldata_m1_6) + int(alldata_m1_7))
        print(("Your total savings before expenses year to date is:"), may_ts)

    return month


def show_alldata_month6(month):

    """
    Projects expenses,savings and balance for
    June
    """

    if month == "6":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A21')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_2 = SHEET.worksheet("alldata").get('B22')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        alldata_m1_3 = SHEET.worksheet("all_data").get('B23')[0][0]
        print("\n")
        print("Retrieving savings data...\n")

        jun = int(alldata_m1_3)
        print(("Your savings for this month will be:"), jun)
    
        """
        Projects savings after deduction of expenses
        """
        jun = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), jun)

        print("\n")
        print("Retrieving total savings data...\n")

        """
        Projects overall savings for past and present month/s 
        before deduction of all monthly expenses
        """

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        alldata_m1_8 = SHEET.worksheet("alldata").get('B19')[0][0]
        jun_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5) +
                  int(alldata_m1_6) + int(alldata_m1_7) +
                  int(alldata_m1_8))
        print(("Your total savings before expenses year to date is:"), jun_ts)

    return month


def show_alldata_month7(month):

    """
    Projects expenses,savings and balance for
    July
    """

    if month == "7":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A25')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_2 = SHEET.worksheet("alldata").get('B26')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B27')[0][0]
        print("\n")
        print("Retrieving savings data...\n")

        jul = int(alldata_m1_3)
        print(("Your savings for this month will be:"), jul)

        """
        Projects savings after deduction of expenses
        """

        jul = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), jul)

        print("\n")
        print("Retrieving total savings data...\n")

        """
        Projects overall savings for past and present month/s 
        before deduction of all monthly expenses
        """

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        alldata_m1_8 = SHEET.worksheet("alldata").get('B19')[0][0]
        alldata_m1_9 = SHEET.worksheet("alldata").get('B23')[0][0]
        jul_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5) +
                  int(alldata_m1_6) + int(alldata_m1_7) + int(alldata_m1_8) +
                  int(alldata_m1_9))
        print(("Your total savings before expenses year to date is:"), jul_ts)

    return month


def show_alldata_month8(month):

    """
    Projects expenses,savings and balance for
    August
    """

    if month == "8":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A29')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_2 = SHEET.worksheet("alldata").get('B30')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B31')[0][0]
        print("\n")
        print("Retrieving savings data...\n")

        aug = int(alldata_m1_3)
        print(("Your savings for this month will be:"), aug)

        """
        Projects savings after deduction of expenses
        """

        aug = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), aug)

        print("\n")
        print("Retrieving total savings...\n")

        """
        Projects overall savings for past and present month/s 
        before deduction of all monthly expenses
        """

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        alldata_m1_8 = SHEET.worksheet("alldata").get('B19')[0][0]
        alldata_m1_9 = SHEET.worksheet("alldata").get('B23')[0][0]
        alldata_m1_10 = SHEET.worksheet("alldata").get('B27')[0][0]
        aug_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5) +
                  int(alldata_m1_6) + int(alldata_m1_7) + int(alldata_m1_8) +
                  int(alldata_m1_9) + int(alldata_m1_10))
        print(("Your total savings before expenses year to date is:"), aug_ts)

    return month


def show_alldata_month9(month):

    """
    Projects expenses,savings and balance for
    September
    """

    if month == "9":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A33')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_2 = SHEET.worksheet("alldata").get('B34')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B35')[0][0]
        print("\n")
        print("Retrieving savings data...\n")

        sep = int(alldata_m1_3)
        print(("Your savings for this month will be:"), sep)

        """
        Projects savings after deduction of expenses
        """
        sep = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), sep)

        print("\n")
        print("Retrieving total savings...\n")

        """
        Projects overall savings for past and present month/s 
        before deduction of all monthly expenses
        """

        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        alldata_m1_8 = SHEET.worksheet("alldata").get('B19')[0][0]
        alldata_m1_9 = SHEET.worksheet("alldata").get('B23')[0][0]
        alldata_m1_10 = SHEET.worksheet("alldata").get('B27')[0][0]
        alldata_m1_11 = SHEET.worksheet("alldata").get('B27')[0][0]
        sep_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5) +
                  int(alldata_m1_6) + int(alldata_m1_7) + int(alldata_m1_8) +
                  int(alldata_m1_9) + int(alldata_m1_10) +
                  int(alldata_m1_11))
        print(("Your total savings before expenses year to date is:"), sep_ts)

    return month


def show_alldata_month10(month):

    """
    Projects expenses,savings and balance for
    October
    """

    if month == "10":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A37')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_2 = SHEET.worksheet("alldata").get('B38')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B39')[0][0]
        print("\n")
        print("Retrieving savings data...\n")

        oct = int(alldata_m1_3)
        print(("Your savings for this month will be:"), oct)

        """
        Projects savings after deduction of expenses
        """
        oct = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), oct)

        print("\n")
        print("Retrieving total savings...\n")

        """
        Projects overall savings for past and present month/s 
        before deduction of all monthly expenses
        """
        alldata_m1_4 = SHEET.worksheet("alldata").get('B3')[0][0]
        alldata_m1_5 = SHEET.worksheet("alldata").get('B7')[0][0]
        alldata_m1_6 = SHEET.worksheet("alldata").get('B11')[0][0]
        alldata_m1_7 = SHEET.worksheet("alldata").get('B15')[0][0]
        alldata_m1_8 = SHEET.worksheet("alldata").get('B19')[0][0]
        alldata_m1_9 = SHEET.worksheet("alldata").get('B23')[0][0]
        alldata_m1_10 = SHEET.worksheet("alldata").get('B27')[0][0]
        alldata_m1_11 = SHEET.worksheet("alldata").get('B27')[0][0]
        alldata_m1_12 = SHEET.worksheet("alldata").get('B35')[0][0]
        oct_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5) +
                  int(alldata_m1_6) + int(alldata_m1_7) +
                  int(alldata_m1_8) + int(alldata_m1_9) +
                  int(alldata_m1_10) + int(alldata_m1_11) +
                  int(alldata_m1_12))
        print(("Your total savings before expenses year to date is:"), oct_ts)

    return month


def show_alldata_month11(month):

    """
    Projects expenses,savings and balance for
    November
    """

    if month == "11":
        alldata_m1_1 = SHEET.worksheet("alldata").get('A41')[0][0]
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_2 = SHEET.worksheet("alldata").get('B42')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B43')[0][0]
        print("\n")
        print("Retrieving savings data...\n")

        nov = int(alldata_m1_3)
        print(("Your savings for this month will be:"), nov)

        """
        Projects savings after deduction of expenses
        """

        nov = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), nov)

        print("\n")
        print("Retrieving total savings...\n")

        """
        Projects overall savings for past and present month/s 
        before deduction of all monthly expenses
        """

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
        nov_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5) +
                  int(alldata_m1_6) + int(alldata_m1_7) + int(alldata_m1_8) +
                  int(alldata_m1_9) + int(alldata_m1_10) + int(alldata_m1_11) +
                  int(alldata_m1_12) + int(alldata_m1_13))
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
        print(("The month you have chosen :"), alldata_m1_1)

        alldata_m1_2 = SHEET.worksheet("alldata").get('B46')[0][0]
        print(("Your expenses for this month will be:"), alldata_m1_2)

        alldata_m1_3 = SHEET.worksheet("alldata").get('B47')[0][0]
        print("\n")
        print("Retrieving savings data...\n")

        dec = int(alldata_m1_3)
        print(("Your savings for this month will be:"), dec)

        """
        Projects savings after deduction of expenses
        """

        dec = int(alldata_m1_3) - int(alldata_m1_2)
        print(("Your savings after expenses will be:"), dec)

        print("\n")
        print("Retrieving total savings...\n")

        """
        Projects overall savings for past and present month/s 
        before deduction of all monthly expenses
        """

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
        dec_ts = (int(alldata_m1_3) + int(alldata_m1_4) + int(alldata_m1_5) +
                  int(alldata_m1_6) + int(alldata_m1_7) +
                  int(alldata_m1_8) + int(alldata_m1_9) +
                  int(alldata_m1_10) + int(alldata_m1_11) +
                  int(alldata_m1_12) + int(alldata_m1_13) +
                  int(alldata_m1_14))
        print(("Your total savings before expenses for the year is:"), dec_ts)

    return month


def main():

    """
    Run all program functions
    """
    get_month_data()


main()

