def get_date():
    date_1 ="2018.06.02"
    qs = 7
    year, month, day = date_1.split(".")
    month = int(month)
    back_month = month - 1
    start_month = month - qs
    # 最后还款日期
    if back_month == 0:
        year = int(year) - 1
        last_date = str(year) + "-12-" + str(day)
    elif back_month <= 10:
        last_date = str(year) + "-0" + str(back_month) + "-" + str(day)
    else:
        last_date = str(year) + "-" + str(back_month) + "-" + str(day)
    # 借款日期
    if start_month == 0:
        year = int(year) - 1
        start_date = str(year) + "-12-" + str(day)
    elif start_month < 0:
        year = int(year) - 1
        new_month = 12 + (start_month)
        if new_month < 10:
            start_date = str(year) +"-0"+ str(new_month) +"-" + str(day)
        else:
            start_date = str(year) + "-" + str(new_month) + "-" + str(day)
    return start_date,last_date
start_date ,last_date = get_date()
print(start_date)
print(last_date)