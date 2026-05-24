
# Gym Membership Management System — Part 1

## About

Small interactive Python program to register a gym member, collect their personal details and membership information, compute fees and session estimates, and display a formatted membership summary.

## Files

part1.py — main program. The Member class handles all input collection, validation, fee calculations, and formatted output.

## Classes

**Person** (parent class)
- Attributes : first_name, last_name, age, city
- Property   : full_name → returns "First Last"

**Member** (child of Person)
- Extra attributes : member_id, membership_type, monthly_fee, months_paid, sessions_per_week, is_student, is_active
- Methods          : total_paid(), annual_fee(), estimated_sessions(), discounted_annual()
- Magic method     : __str__() for formatted summary output
- Static methods   : get_float(), get_int() for input validation
- Class method     : from_input() to create a Member interactively

## How to run

Open PowerShell and change to the project folder:

    cd "path\to\your\project"
    python part1.py

The program is interactive: it asks for first name, last name, age, city, member ID, membership type, monthly fee, months paid, sessions per week, and student status. If you enter a non-number or a value outside the expected range, it will ask again until a valid value is entered.

## Example output

    === Welcome to our Gym Membership Management System ===
    === Register a new Member ===
    Enter your First Name: Alice
    Enter your Last Name: Ouedraogo
    Enter your age: 22
    Enter your city: Ouagadougou
    Enter your Member ID: M001

    Membership types: Basic / Standard / Premium
    Enter your membership type: Premium
    Enter the monthly fee (XOF): 15000
    Enter number of months paid (1-12): 6
    Enter sessions per week (1-7): 4
    Are you a student? (yes/no): yes

    ******MEMBERSHIP SUMMARY******
    Member      : Alice Ouedraogo
    ID          : M001
    Age         : 22
    City        : Ouagadougou
    Student     : True
    Active      : True
    -----Membership Details-----
    Type              : Premium
    Monthly Fee       : 15000.00 XOF
    Months Paid       : 6
    Total Paid        : 90000.00 XOF
    Annual Fee        : 180000.00 XOF
    Student Discount  : -18000.00 XOF
    Discounted Annual : 162000.00 XOF
    Est. Sessions     : 96

    Welcome Alice Ouedraogo! Your membership is active. Keep it up!

    === Thank you for using our Gym Membership Management System ===
