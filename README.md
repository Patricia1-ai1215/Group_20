# 🏋️ Gym Membership Management System

A Python project managing gym memberships using all 4 OOP principles.

---

## 📁 Project Structure

```
gym_membership/
├── part1_member.py          
├── part2_premium_member.py  
├── gym_final.py             
└── README.md
```

---

## 📄 Files

| File | Description |
|---|---|
| `part1_member.py` | `Person` and `Member` — basic membership logic, public attributes |
| `part2_premium_member.py` | `GymMember` and `PremiumMember` — premium logic, disconnected from Part 1 |
| `gym_final.py` | Unified final version — all 4 OOP principles applied |

---

## 🏗️ Class Hierarchy

```
GymEntity  ← ABCMeta — enforces display_summary(), calculate_total()
    └── Person        — name, age, city
        └── Member    — fee, months, sessions, student discount
            └── PremiumMember — training sessions and cost
```

---

## 🎯 OOP Principles

| Principle | Where | What it does |
|---|---|---|
| **Abstraction** | `GymEntity` | Forces all subclasses to implement `display_summary()` and `calculate_total()` |
| **Encapsulation** | All classes | `ValidatedProperty` stores attributes privately and validates every assignment |
| **Inheritance** | Full chain | Each class calls `super().__init__()` and only adds what is new |
| **Polymorphism** | `calculate_total()`, `display_summary()` | Overridden at each level — `process_member()` works on any type |

---

## 🔄 What Changed

| | Part 1 & 2 | Final |
|---|---|---|
| Attributes | Public | Private via `ValidatedProperty` |
| Abstraction | None | `GymEntity` ABC |
| Premium class | Separate file | Subclass of `Member` |
| Polymorphism | None | `process_member()` on any type |

---

## 📋 Sample Output

### Standard Member
```
=== Welcome to the Gym Membership Management System ===
  1. Standard Member
  2. Premium Member
Enter 1 or 2: 1

=== Register a new Member ===
First Name: John
Last Name: Doe
Age: 25
City: Ouagadougou
Member ID: M001
Membership type ('Basic', 'Standard', 'Premium'): Standard
Monthly fee (XOF): 15000
Months paid (1-12): 3
Sessions per week (1-7): 4
Student? (yes/no): yes

====== MEMBERSHIP SUMMARY ======
Member      : John Doe  |  ID: M001
Age         : 25  |  City: Ouagadougou
Student     : True  |  Active: True
--------------------------------
Type              : Standard
Monthly Fee       : 15000.00 XOF
Months Paid       : 3
Total Paid        : 45000.00 XOF
Annual Fee        : 180000.00 XOF
Discounted Annual : 162000.00 XOF
Est. Sessions     : 48

Welcome John Doe! Membership active. Keep it up!

>>> Total cost calculated: 45000.00 XOF

=== Thank you for using our Gym Membership Management System ===
```

### Premium Member
```
=== Welcome to the Gym Membership Management System ===
  1. Standard Member
  2. Premium Member
Enter 1 or 2: 2

=== Register a new Premium Member ===
First Name: Aisha
Last Name: Traore
Age: 30
City: Bobo-Dioulasso
Member ID: P002
Monthly fee (XOF): 25000
Months paid (1-12): 6
Sessions per week (1-7): 5
Student? (yes/no): no
Training sessions (0-10): 4
Fee per session (XOF): 10000

====== MEMBERSHIP SUMMARY ======
Member      : Aisha Traore  |  ID: P002
Age         : 30  |  City: Bobo-Dioulasso
Student     : False  |  Active: True
--------------------------------
Type              : Premium
Monthly Fee       : 25000.00 XOF
Months Paid       : 6
Total Paid        : 150000.00 XOF
Annual Fee        : 300000.00 XOF
Est. Sessions     : 120

Welcome Aisha Traore! Membership active. Keep it up!
------- Premium Details --------
Training Sessions : 4
Fee per Session   : 10000.00 XOF
Training Cost     : 40000.00 XOF
Total with Train. : 190000.00 XOF
Premium Benefits  :
  - Access to premium equipment
  - Priority booking for classes
  - Personal training sessions
  - Free monthly fitness assessment

>>> Total cost calculated: 190000.00 XOF

=== Thank you for using our Gym Membership Management System ===
```

---

## ▶️ How to Run

```bash
python gym_final.py
```

## 🛠️ Requirements

- Python 3.8+
- No external libraries — built-in `abc` module only
