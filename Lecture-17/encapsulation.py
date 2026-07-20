class WeatherSection:
    def __init__(self, city, temperature):
        self.city = city
        self.__temperature = temperature

    def set_temperature(self, temperature):
        if -20 <= temperature <= 60:
            self.__temperature = temperature
            print("Temperature updated successfully!")
        else:
            print("Invalid temperature!")

    def get_temperature(self):
        return self.__temperature

    def show_weather(self):
        print("City:", self.city)
        print("Temperature:", self.__temperature)


print("------------------")

karachi = WeatherSection("Karachi", 35)
karachi.show_weather()

print("------------------")

lahore = WeatherSection("Lahore", 30)
lahore.show_weather()