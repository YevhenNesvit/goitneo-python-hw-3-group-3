from datetime import datetime, date
from collections import defaultdict

def get_birthdays_per_week(users) :
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()
    users.sort(key=lambda x: x['birthday'])

    for user in users :
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today :
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days
        if delta_days < 7 :
            if birthday_this_year.strftime('%A') in ('Saturday', 'Sunday') :
                if delta_days > 5 :
                    continue
                else :
                    birthdays_per_week['Monday'].append(name)
            else :
                birthdays_per_week[birthday_this_year.strftime('%A')].append(name)
    
    for k, v in birthdays_per_week.items() :
        if v :
            if len(v) > 1 :
                print(f"{k} : {', '.join(v)}")
            else :
                print(f"{k} : {''.join(v)}")