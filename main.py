import pyowm

owm = pyowm.OWM('a4059161b180b05d8caa7275375bdf1d')

    
city = 'Almaty'

loc = owm.weather_at_place(city)

weather = loc.get_weather()

    # wind 
wind = weather.get_wind()

    # temperature
temp = weather.get_temperature(unit='celsius')
cleaned_temp_data = (int(temp['temp']))

print ('The temperature in', city ,'is',  cleaned_temp_data, "Celcius Degree")
print (wind)


