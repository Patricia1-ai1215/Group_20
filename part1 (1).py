class Person:

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age
        self.city       = city

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Member(Person):

    def __init__(self, first_name, last_name, age, city,
                 member_id, membership_type, monthly_fee,
                 months_paid, sessions_per_week, is_student):

        super().__init__(first_name, last_name, age, city)

        self.member_id         = member_id
        self.membership_type   = membership_type
        self.monthly_fee       = monthly_fee
        self.months_paid       = months_paid
        self.sessions_per_week = sessions_per_week
        self.is_student        = is_student
        self.is_active         = months_paid >= 1

    @staticmethod
    def get_float(prompt):
        while True:
            try:
                value = float(input(prompt))
                if value >= 0:
                    return value
                print("Value cannot be negative. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    @staticmethod
    def get_int(prompt, low, high):
        while True:
            try:
                value = int(input(prompt))
                if low <= value <= high:
                    return value
                print(f"Please enter a number between {low} and {high}.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    @classmethod
    def from_input(cls):
        print("=== Register a new Member ===")

        first_name        = input("Enter your First Name: ")
        last_name         = input("Enter your Last Name: ")
        age               = cls.get_int("Enter your age: ", 1, 120)
        city              = input("Enter your city: ")
        member_id         = input("Enter your Member ID: ")

        print("\nMembership types: Basic / Standard / Premium")
        membership_type   = input("Enter your membership type: ")

        monthly_fee       = cls.get_float("Enter the monthly fee (XOF): ")
        months_paid       = cls.get_int("Enter number of months paid (1-12): ", 1, 12)
        sessions_per_week = cls.get_int("Enter sessions per week (1-7): ", 1, 7)
        is_student        = input("Are you a student? (yes/no): ").lower() == "yes"

        return cls(first_name, last_name, age, city,
                   member_id, membership_type, monthly_fee,
                   months_paid, sessions_per_week, is_student)

    def total_paid(self):
        return self.monthly_fee * self.months_paid

    def annual_fee(self):
        return self.monthly_fee * 12

    def estimated_sessions(self):
        return self.sessions_per_week * self.months_paid * 4

    def discounted_annual(self):
        discount = self.annual_fee() * 0.10 if self.is_student else 0.0
        return self.annual_fee() - discount

    def __str__(self):
        discount = self.annual_fee() * 0.10 if self.is_student else 0.0

        lines = [
            "\n******MEMBERSHIP SUMMARY******",
            f"Member      : {self.full_name}",
            f"ID          : {self.member_id}",
            f"Age         : {self.age}",
            f"City        : {self.city}",
            f"Student     : {self.is_student}",
            f"Active      : {self.is_active}",
            "-----Membership Details-----",
            f"Type              : {self.membership_type}",
            f"Monthly Fee       : {self.monthly_fee:.2f} XOF",
            f"Months Paid       : {self.months_paid}",
            f"Total Paid        : {self.total_paid():.2f} XOF",
            f"Annual Fee        : {self.annual_fee():.2f} XOF",
        ]

        if self.is_student:
            lines.append(f"Student Discount  : -{discount:.2f} XOF")
            lines.append(f"Discounted Annual : {self.discounted_annual():.2f} XOF")

        lines.append(f"Est. Sessions     : {self.estimated_sessions()}")

        if self.is_active:
            lines.append(f"\nWelcome {self.full_name}! Your membership is active. Keep it up!")
        else:
            lines.append(f"\nHello {self.full_name}. Please renew your membership to continue.")

        return "\n".join(lines)


print("=== Welcome to our Gym Membership Management System ===")

member = Member.from_input()

print(member)

print("\n=== Thank you for using our Gym Membership Management System ===")
