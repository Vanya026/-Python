#todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.

import calendar
free_days = []
for i in range(1, 13):
    c = calendar.monthcalendar(2023, i)
    first_week = c[0]
    third_week = c[2]
    fourth_week = c[3]
    if first_week[calendar.THURSDAY]:
        free_day = third_week[calendar.THURSDAY]
    else:
        free_day = fourth_week[calendar.THURSDAY]
    s = '{0} {1}'.format(free_day, calendar.month_name[i]) 
    free_days.append(s)

print(", ".join(free_days))       
