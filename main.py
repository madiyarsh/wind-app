import pyowm

owm = pyowm.OWM('a4059161b180b05d8caa7275375bdf1d')

mgr = owm.weather_manager()

city = 'Almaty'

loc = mgr.weather_at_place(city)

weather = loc.weather

    # wind
wind = weather.wind()

    # temperature
#temp = weather.get_temperature(unit='celsius')
#cleaned_temp_data = (int(temp['temp']))

#print ('The temperature in', city ,'is',  cleaned_temp_data, "Celcius Degree")
print (wind)
