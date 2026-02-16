import datetime

import requests
from bs4 import BeautifulSoup

class Wheather:
    def __init__(self, date:str, temp:str, fells_like:str, pressure:str, wind:str, humidity:str ):
        self.date = date
        self.temp = temp
        self.fells_like = fells_like
        self.pressure = pressure
        self.wind = wind
        self.humidity = humidity

    def to_dict(self):
        return {
            'date': self.date,
            'temp': self.temp,
            'fells_like': self.fells_like,
            'pressure': self.pressure,
            'wind': self.wind,
            'humidity': self.humidity
        }


class Parser:
    def __init__(self, url:str):
        self.url = url
        self._soup = None
        self.headers = {
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
        }

    def get_soup(self):
        if self._soup is None:
            response = requests.get(self.url, headers=self.headers, timeout=15)
            self._soup = BeautifulSoup(response.content, 'html.parser')


    def parse_weather_table(self):
        self.get_soup()
        tables = self._soup.find_all("div", class_="weather-short")
        weather_today = tables[0]
        if len(tables)<1 or weather_today is None:
            return {}
        periods = ['night', 'morning', 'day', 'evening']
        weather_data = {}

        for period in periods:
            period_row = weather_today.find("tr", class_=f"{period}")

            if period_row:
                cells = period_row.find_all("td")

                if len(cells) >= 7:
                    period_data = {
                        'period': cells[0].text.strip(),
                        'temperature': cells[1].text.strip(),
                        'felling': cells[2].text.strip(),
                        'probability': cells[3].text.strip(),
                        'pressure': cells[4].text.strip(),
                        'wind': cells[5].text.strip(),
                        'humidity': cells[6].text.strip(),
                    }

                    weather_data[period] = period_data
        return weather_data

    def parse(self):
        self.get_soup()
        date = self._soup.find("div", class_="dates").text
        if date:
            print("Погода сегодня: " + date)
        print("-"*60)
        weather_data = self.parse_weather_table()
        if weather_data:
            for period, data in weather_data.items():
                print(f"\n{period.upper()}")
                print(f"Период: {data['period']}")
                print(f"Температура: {data['temperature']}")
                print(f"Ощущается как: {data['felling']}")
                print(f"Вероятность осадков: {data['probability']}")
                print(f"Давление: {data['pressure']}")
                print(f"Ветер: {data['wind']}")
                print(f"Влажность: {data['humidity']}")
        else:
            print("Не удалось получить данные о погоде")

if __name__ == "__main__":
    base_url = "https://world-weather.ru/pogoda/russia/saint_petersburg/"
    parser = Parser(base_url)
    parser.parse()
