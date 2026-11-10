def total_cal(bill_amout,tip_per):
    total = bill_amout*(1 + 0.01*tip_per)
    total + round(total,2)
    print(f"Please pay{total}")\

total_cal(150,20)