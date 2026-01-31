
price_house = 1000000
good_credit = False

if good_credit:
    down_payment = price_house*0.1
    print(f"You would need to give out 10 % cuz of good score which is ${down_payment} " )
else:
    down_payment = price_house * 0.2
    print(f"You would need to give out 20 % cuz of bad score which is ${down_payment}")