import datetime as dt


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, new_record):
        self.new_record = new_record
        self.records.append(self.new_record)

    def get_today_stats(self):
        today_stats = [record.amount for record in self.records
                       if record.date == dt.datetime.now().date()]
        total = sum(today_stats)
        return total

    def get_week_stats(self):
        today = dt.datetime.now().date()
        seven_days_ago = today - dt.timedelta(days=7)
        week_stats = [record.amount for record in self.records
                      if record.date <= today and record.date > seven_days_ago]
        total_week = sum(week_stats)
        return total_week


class Record:

    def __init__(self, amount, comment, date=dt.datetime.now().date()):
        self.amount = amount
        date_format = '%d.%m.%Y'
        if date == dt.datetime.now().date():
            self.date = date
        else:
            date_right = dt.datetime.strptime(date,
                                              date_format)
            self.date = date_right.date()
        self.comment = comment


class CashCalculator(Calculator):
    EURO_RATE = 70.00
    USD_RATE = 60.00
    currencies = {
        'usd': {'rate': USD_RATE, 'name': 'USD'},
        'eur': {'rate': EURO_RATE, 'name': 'Euro'},
        'rub': {'rate': 1, 'name': 'руб'}
    }

    def get_today_cash_remained(self, currency):
        cash_remained = self.limit - self.get_today_stats()
        if currency in self.currencies.keys():
            rate = self.currencies[currency]['rate']
            name_currency = self.currencies[currency]['name']
            uni_cash = round(cash_remained/rate, 2)
            if uni_cash > 0:
                return f'На сегодня осталось {uni_cash} {name_currency}'
            elif uni_cash == 0:
                return 'Денег нет, держись'
            else:
                debt = -uni_cash
                return f'Денег нет, держись: твой долг - {debt} {name_currency}'
        else:
            return f"введите название валюты (eur, rub, usd)"


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        total_calories = self.get_today_stats()
        calories_remained = self.limit - total_calories
        if total_calories < self.limit:
            string_calories = (
                f"Сегодня можно съесть что-нибудь ещё, "
                f"но с общей калорийностью не более {calories_remained} кКал"
            )
            return string_calories
        else:
            return 'Хватит есть!'
