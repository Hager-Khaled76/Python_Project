# Task 3: Company Salary Chain
#------------------------------------
# Base Class
class Employee:

    def __init__(self, name, base):
        self.name = name
        self.base = base

    def total(self):
        return self.base


# Multilevel Inheritance: Level 1
class TeamLead(Employee):

    def __init__(self, name, base, team_size):
        super().__init__(name, base)
        self.team_size = team_size

    def total(self):
        return super().total() + (self.team_size * 200)


# Multilevel Inheritance: Level 2
class Manager(TeamLead):

    def __init__(self, name, base, team_size, allowance):
        super().__init__(name, base, team_size)
        self.allowance = allowance

    def total(self):
        return super().total() + self.allowance


if __name__ == '__main__':
    # Create instances
    staff = [
        Employee('Ali', 5000),
        TeamLead('Mona', 7000, 4),
        Manager('Omar', 9000, 6, 3000),
    ]

    payroll = 0
    for emp in staff:
        salary = emp.total()
        payroll += salary
        print(f"{emp.name} = {salary}")

    print(f"Payroll = {payroll}")

    # Find the top earner using sorted + lambda
    sorted_staff = sorted(staff, key=lambda x: x.total(), reverse=True)
    top_earner = sorted_staff[0]

    print(f"Top = {top_earner.name}")