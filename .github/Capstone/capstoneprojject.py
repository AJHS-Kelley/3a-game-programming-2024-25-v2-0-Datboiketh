from datetime import datetime, timedelta

# --- Bonus Date Functions ---
def get_start_date():
    return (datetime.now() - timedelta(days=13)).strftime("%m/%d/%Y")

def get_end_date():
    return (datetime.now() - timedelta(days=7)).strftime("%m/%d/%Y")

def get_pay_date():
    return datetime.now().strftime("%m/%d/%Y")

# --- Main Payroll Program ---
connon = "Yes"

while connon == "Yes":
    # Input section
    name = input("Enter your name: ")
    try:
        hrsworked = int(input("Enter the number of work hrs: "))
    except ValueError:
        print("** Invalid number for hours worked **")
        continue

    occupation = input("Enter the Employee occupation (cashier, clerk, manager): ").lower()

    # Determine pay rate
    if occupation == "cashier":
        payrate = 17.25
    elif occupation == "clerk":
        payrate = 18
    elif occupation == "manager":
        payrate = 25.25
    else:
        print("**Invalid Occupation Code** Program stopped*** Check your data *****")
        exit()

    # Set normal and overtime hours
    if occupation == "manager":
        normal_hrsworked = 40
        overtime_hrsworked = 0
    else:
        if hrsworked > 40:
            normal_hrsworked = 40
            overtime_hrsworked = hrsworked - 40
        else:
            normal_hrsworked = hrsworked
            overtime_hrsworked = 0

    # Calculate pay
    base40pay = normal_hrsworked * payrate
    over40pay = overtime_hrsworked * (payrate * 1.5)
    gross_pay = base40pay + over40pay

    # Calculate taxes
    fed_tax = gross_pay * 0.10
    state_tax = gross_pay * 0.03
    net_pay = gross_pay - fed_tax - state_tax

    # Output
    print("\n---------- BoxMart Pay Stub ----------------")
    print(f"Employee Name: {name}")
    print(f"Normal Hours Worked:          {normal_hrsworked} hrs")
    print(f"Overtime Hours Worked:        {overtime_hrsworked} hrs")
    print(f"Hourly Wage:            $ {payrate:.2f}/hr")
    print(f"Normal Pay:             $ {base40pay:.2f}")
    print(f"Overtime Pay:           $ {over40pay:.2f}")
    print(f"Gross Pay:              $ {gross_pay:.2f}")
    print(f"Federal Tax:            $ {fed_tax:.2f}")
    print(f"State Tax:              $ {state_tax:.2f}")
    print(f"Net Pay:                $ {net_pay:.2f}")
    print("\nBox Mart, Inc.                ", get_pay_date())
    print(f"Pay to: {name:25} $ {net_pay:.2f}")
    print("\nPay Period:    ", get_start_date(), "to", get_end_date())
    print("===========================================================\n")

    connon = input("Do you wish to continue? (Yes/No): ").capitalize()