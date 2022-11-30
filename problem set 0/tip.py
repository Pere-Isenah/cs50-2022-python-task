def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    meal_cost = float(d.translate({ord('$'): None}))
    return meal_cost


def percent_to_float(p):
    tip_percent = float(p.translate({ord('%'): None}))
    return tip_percent / 100

main()