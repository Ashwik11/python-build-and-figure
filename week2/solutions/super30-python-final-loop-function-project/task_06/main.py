def salary_analysis(salaries):
    """Return payroll, averages, salary extremes, and above-average employees."""
    if not salaries:
        return {"total": 0, "average": None, "highest": [], "lowest": [], "above_average": []}
    if any(salary < 0 for salary in salaries.values()):
        raise ValueError("Salary cannot be negative")
    total = 0
    for salary in salaries.values():
        total += salary
    average = total / len(salaries)
    highest = max(salaries.values())
    lowest = min(salaries.values())
    return {"total": total, "average": average, "highest": [(name, salary) for name, salary in salaries.items() if salary == highest], "lowest": [(name, salary) for name, salary in salaries.items() if salary == lowest], "above_average": [(name, salary) for name, salary in salaries.items() if salary > average]}


print(salary_analysis({"Asha": 50000, "Ben": 70000, "Cara": 70000, "Dev": 60000}))
