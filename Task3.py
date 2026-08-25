# Task 3: Filter Generator for Employees

def high_earners(employees, threshold):
    for name, salary in employees:
        if salary >= threshold:
            yield (name, salary)


if __name__ == '__main__':
    employees = [
        ('Ali', 3000),
        ('Mona', 8000),
        ('Omar', 5000),
        ('Sara', 12000),
    ]

    count = 0
    for name, salary in high_earners(employees, 5000):
        print(f"{name} {salary}")
        count += 1

    print(f"Count = {count}")