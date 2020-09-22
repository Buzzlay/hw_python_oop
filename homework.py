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
    pass


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
    pass


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
            debt = uni_cash*-1
            return f'Денег нет, держись: твой долг - {debt} {name_currency}'


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


cash_calculator = CashCalculator(2500)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))
cash_calculator.add_record(Record(amount=500,
                                  comment=',бургер',
                                  date='19.09.2020'))
cash_calculator.add_record(Record(amount=500,
                                  comment=',бургер',
                                  date='19.09.2020'))
cash_calculator.add_record(Record(amount=500,
                                  comment=',бургер',
                                  date='19.09.2020'))
cash_calculator.add_record(Record(amount=500,
                                  comment=',бургер',
                                  date='19.09.2020'))
cash_calculator.add_record(Record(amount=500,
                                  comment=',бургер',
                                  date='19.09.2020'))
cash_calculator.add_record(Record(amount=500,
                                  comment=',бургер',
                                  date='14.09.2020'))
cash_calculator.add_record(Record(amount=500,
                                  comment=',бургер',
                                  date='13.09.2020'))
print(cash_calculator.get_today_cash_remained('usd'))
