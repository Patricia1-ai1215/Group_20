from abc import ABCMeta, abstractmethod


class ValidatedProperty:

    def __init__(self, min_val=None, max_val=None, non_empty=False):
        self.min_val   = min_val
        self.max_val   = max_val
        self.non_empty = non_empty

    def __set_name__(self, owner, name):
        self.private = f"_{owner.__name__}__{name}"

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private, None)

    def __set__(self, obj, value):
        if self.non_empty and isinstance(value, str) and not value.strip():
            raise ValueError(f"{self.private} cannot be empty.")
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"{self.private} must be >= {self.min_val}.")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"{self.private} must be <= {self.max_val}.")
        setattr(obj, self.private, value)


class GymEntity(metaclass=ABCMeta):

    @abstractmethod
    def display_summary(self):
        pass

    @abstractmethod
    def calculate_total(self):
        pass


class Person(GymEntity):

    first_name = ValidatedProperty(non_empty=True)
    last_name  = ValidatedProperty(non_empty=True)
    age        = ValidatedProperty(min_val=1, max_val=120)
    city       = ValidatedProperty(non_empty=True)

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age
        self.city       = city

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def display_summary(self):
        return f"Name : {self.full_name}\nAge  : {self.age}\nCity : {self.city}"

    def calculate_total(self):
        return 0.0

    def __str__(self):
        return self.display_summary()


class Member(Person):

    VALID_TYPES     = ("Basic", "Standard", "Premium")
    monthly_fee     = ValidatedProperty(min_val=0)
    months_paid     = ValidatedProperty(min_val=1, max_val=12)
    sessions_per_week = ValidatedProperty(min_val=1, max_val=7)

    def __init__(self, first_name, last_name, age, city,
                 member_id, membership_type, monthly_fee,
                 months_paid, sessions_per_week, is_student):
        super().__init__(first_name, last_name, age, city)
        if membership_type not in self.VALID_TYPES:
            raise ValueError(f"Type must be one of {self.VALID_TYPES}.")
        self.member_id         = member_id
        self.membership_type   = membership_type
        self.monthly_fee       = monthly_fee
        self.months_paid       = months_paid
        self.sessions_per_week = sessions_per_week
        self.is_student        = is_student

    @property
    def is_active(self):
        return self.months_paid >= 1

    @staticmethod
    def get_float(prompt):
        while True:
            try:
                value = float(input(prompt))
                if value >= 0:
                    return value
                print("Value cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    @staticmethod
    def get_int(prompt, low, high):
        while True:
            try:
                value = int(input(prompt))
                if low <= value <= high:
                    return value
                print(f"Enter a number between {low} and {high}.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    @classmethod
    def from_input(cls):
        print("\n=== Register a new Member ===")
        return cls(
            first_name        = input("First Name: "),
            last_name         = input("Last Name: "),
            age               = cls.get_int("Age: ", 1, 120),
            city              = input("City: "),
            member_id         = input("Member ID: "),
            membership_type   = input(f"Membership type {cls.VALID_TYPES}: "),
            monthly_fee       = cls.get_float("Monthly fee (XOF): "),
            months_paid       = cls.get_int("Months paid (1-12): ", 1, 12),
            sessions_per_week = cls.get_int("Sessions per week (1-7): ", 1, 7),
            is_student        = input("Student? (yes/no): ").lower() == "yes",
        )

    def annual_fee(self):         return self.monthly_fee * 12
    def estimated_sessions(self): return self.sessions_per_week * self.months_paid * 4
    def calculate_total(self):    return self.monthly_fee * self.months_paid
    def discounted_annual(self):  return self.annual_fee() * (0.90 if self.is_student else 1.0)

    def display_summary(self):
        lines = [
            "\n====== MEMBERSHIP SUMMARY ======",
            f"Member      : {self.full_name}  |  ID: {self.member_id}",
            f"Age         : {self.age}  |  City: {self.city}",
            f"Student     : {self.is_student}  |  Active: {self.is_active}",
            "--------------------------------",
            f"Type              : {self.membership_type}",
            f"Monthly Fee       : {self.monthly_fee:.2f} XOF",
            f"Months Paid       : {self.months_paid}",
            f"Total Paid        : {self.calculate_total():.2f} XOF",
            f"Annual Fee        : {self.annual_fee():.2f} XOF",
        ]
        if self.is_student:
            lines.append(f"Discounted Annual : {self.discounted_annual():.2f} XOF")
        lines.append(f"Est. Sessions     : {self.estimated_sessions()}")
        lines.append(
            f"\nWelcome {self.full_name}! Membership active. Keep it up!"
            if self.is_active else
            f"\nHello {self.full_name}. Please renew your membership."
        )
        return "\n".join(lines)

    def __str__(self):
        return self.display_summary()


class PremiumMember(Member):

    personal_training_sessions = ValidatedProperty(min_val=0, max_val=10)
    training_fee_per_session   = ValidatedProperty(min_val=0)

    def __init__(self, first_name, last_name, age, city,
                 member_id, membership_type, monthly_fee,
                 months_paid, sessions_per_week, is_student,
                 personal_training_sessions, training_fee_per_session):
        super().__init__(first_name, last_name, age, city,
                         member_id, membership_type, monthly_fee,
                         months_paid, sessions_per_week, is_student)
        self.personal_training_sessions = personal_training_sessions
        self.training_fee_per_session   = training_fee_per_session

    @classmethod
    def from_input(cls):
        print("\n=== Register a new Premium Member ===")
        return cls(
            first_name                 = input("First Name: "),
            last_name                  = input("Last Name: "),
            age                        = cls.get_int("Age: ", 1, 120),
            city                       = input("City: "),
            member_id                  = input("Member ID: "),
            membership_type            = "Premium",
            monthly_fee                = cls.get_float("Monthly fee (XOF): "),
            months_paid                = cls.get_int("Months paid (1-12): ", 1, 12),
            sessions_per_week          = cls.get_int("Sessions per week (1-7): ", 1, 7),
            is_student                 = input("Student? (yes/no): ").lower() == "yes",
            personal_training_sessions = cls.get_int("Training sessions (0-10): ", 0, 10),
            training_fee_per_session   = cls.get_float("Fee per session (XOF): "),
        )

    def training_cost(self):   return self.personal_training_sessions * self.training_fee_per_session
    def calculate_total(self): return super().calculate_total() + self.training_cost()

    def premium_benefits(self):
        return [
            "Access to premium equipment",
            "Priority booking for classes",
            "Personal training sessions",
            "Free monthly fitness assessment",
        ]

    def display_summary(self):
        lines = [
            super().display_summary(),
            "------- Premium Details --------",
            f"Training Sessions : {self.personal_training_sessions}",
            f"Fee per Session   : {self.training_fee_per_session:.2f} XOF",
            f"Training Cost     : {self.training_cost():.2f} XOF",
            f"Total with Train. : {self.calculate_total():.2f} XOF",
            "Premium Benefits  :",
        ]
        lines.extend(f"  - {b}" for b in self.premium_benefits())
        return "\n".join(lines)

    def __str__(self):
        return self.display_summary()


def process_member(entity: GymEntity):
    print(entity.display_summary())
    print(f"\n>>> Total cost calculated: {entity.calculate_total():.2f} XOF")


def main():
    print("=== Welcome to the Gym Membership Management System ===")
    print("  1. Standard Member\n  2. Premium Member")
    choice = Member.get_int("Enter 1 or 2: ", 1, 2)
    process_member(PremiumMember.from_input() if choice == 2 else Member.from_input())
    print("\n=== Thank you for using our Gym Membership Management System ===")


if __name__ == "__main__":
    main()
