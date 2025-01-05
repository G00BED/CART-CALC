main = True
while main:
    print("/////////////////////////////////////////////////////////////")
    print("                 CART-CALC")
    print("/////////////////////////////////////////////////////////////")
    user_input_one = input("WOULD YOU LIKE TO CALCULATE DAYS OR MONTHS: ").strip().lower()
    print("/////////////////////////////////////////////////////////////")

    price_of_cart = 20.0

    if user_input_one in ["month", "months"]:
        print("         You selected MONTHS!")
        print("/////////////////////////////////////////////////////////////")
        user_input_two = float(input("ENTER THE NUMBER OF MONTHS: "))
        print("/////////////////////////////////////////////////////////////")
        days_to_months = user_input_two * 30.0
        month_calc = days_to_months * price_of_cart
        print(round(days_to_months * 0.5), "CARTS ARE NEEDED FOR", round(user_input_two), "MONTHS.")
        print("$", round(month_calc * 0.5), "USD")
    elif user_input_one in ["day", "days"]:
        print("           You selected DAYS!")
        print("/////////////////////////////////////////////////////////////")
        user_input_two = float(input("ENTER THE # OF DAYS: "))
        day_num = user_input_two / 2.0
        day_calc = day_num * price_of_cart
        print(round(day_num), "CARTS ARE NEEDED FOR", round(user_input_two), "DAYS.")
        print("$", round(day_calc), "USD")
    else:
        print("                      ERROR!")
        continue

    print("/////////////////////////////////////////////////////////////")
    user_input_three = input("WOULD YOU LIKE TO CALCULATE AGAIN? (Y/N): ").strip().lower()
    if user_input_three in ["n", "no"]:
        main = False
        print("/////////////////////////////////////////////////////////////")
        print("                        BYE!")
        print("/////////////////////////////////////////////////////////////")
    elif user_input_three not in ["y", "yes"]:
        print("                     ERROR!")
