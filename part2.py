class GymMember:

    def __init__(self, first_name, last_name, age, city,
                 membership_type, monthly_fee, months_paid,
                 sessions_per_week):
        self.first_name        = first_name
        self.last_name         = last_name
        self.age               = age
        self.city              = city
        self.membership_type   = membership_type
        self.monthly_fee       = monthly_fee
        self.months_paid       = months_paid
        self.sessions_per_week = sessions_per_week

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_active(self):
        return self.months_paid >= 1

    def total_paid(self):
        return self.monthly_fee * self.months_paid

    def estimated_sessions(self):
        return self.sessions_per_week * self.months_paid * 4

    def membership_summary(self):
        return (
            f"Member: {self.full_name}\n"
            f"Type: {self.membership_type}\n"
            f"Monthly Fee: {self.monthly_fee:.2f} XOF\n"
            f"Months Paid: {self.months_paid}\n"
            f"Total Paid: {self.total_paid():.2f} XOF\n"
            f"Estimated Sessions: {self.estimated_sessions()}\n"
            f"Active: {self.is_active}"
        )


class PremiumMember(GymMember):

    def __init__(self, first_name, last_name, age, city,
                 membership_type, monthly_fee, months_paid,
                 sessions_per_week, personal_training_sessions,
                 training_fee_per_session):

        super().__init__(first_name, last_name, age, city,
                         membership_type, monthly_fee, months_paid,
                         sessions_per_week)

        self.personal_training_sessions = personal_training_sessions
        self.training_fee_per_session = training_fee_per_session

    def training_cost(self):
        return self.personal_training_sessions * self.training_fee_per_session

    def total_paid_with_training(self):
        return self.total_paid() + self.training_cost()

    def premium_benefits(self):
        return [
            "Access to premium equipment",
            "Priority booking for classes",
            "Personal training sessions"
        ]

    def __str__(self):
        lines = [
            "\n****** PREMIUM MEMBER SUMMARY ******",
            f"Member: {self.full_name}",
            f"Age: {self.age}",
            f"City: {self.city}",
            f"Membership Type: {self.membership_type}",
            f"Monthly Fee: {self.monthly_fee:.2f} XOF",
            f"Months Paid: {self.months_paid}",
            f"Sessions per Week: {self.sessions_per_week}",
            f"Total Paid: {self.total_paid():.2f} XOF",
            f"Training Sessions: {self.personal_training_sessions}",
            f"Training Cost: {self.training_cost():.2f} XOF",
            f"Total Paid with Training: {self.total_paid_with_training():.2f} XOF",
            f"Estimated Sessions: {self.estimated_sessions()}",
            f"Active: {self.is_active}",
            "Premium Benefits:",
        ]
        lines.extend(f"- {benefit}" for benefit in self.premium_benefits())
        return "\n".join(lines)


def get_int(prompt, low, high):
    while True:
        try:
            value = int(input(prompt))
            if low <= value <= high:
                return value
            print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Value cannot be negative. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    print("=== Premium Gym Member Registration ===")
    first_name = input("First name: ")
    last_name = input("Last name: ")
    age = get_int("Age: ", 1, 120)
    city = input("City: ")
    membership_type = input("Membership type (Basic/Standard/Premium): ")
    monthly_fee = get_float("Monthly fee (XOF): ")
    months_paid = get_int("Months paid (1-12): ", 1, 12)
    sessions_per_week = get_int("Sessions per week (1-7): ", 1, 7)
    personal_training_sessions = get_int("Personal training sessions this month: ", 0, 10)
    training_fee_per_session = get_float("Training fee per session (XOF): ")

    premium_member = PremiumMember(
        first_name, last_name, age, city,
        membership_type, monthly_fee, months_paid,
        sessions_per_week, personal_training_sessions,
        training_fee_per_session
    )

    print(premium_member)


if __name__ == "__main__":
    main()
