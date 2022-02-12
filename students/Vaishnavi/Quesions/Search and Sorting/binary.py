from pytz import country_timezones, timezone
def find_city(query):
    for country, cities in country_timezones.items():
        for city in cities:
            if query in city:
                yield timezone(city)


a = input("Enter the city : ")
for tz in find_city(a):
    print(tz)