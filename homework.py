import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self, new_record):
        self.new_record = new_record
        self.records.append(self.new_record)
    def get_today_stats(self):
        today_stats = [record.amount for record in self.records if record.date == dt.datetime.now().date()]
        total = sum(today_stats)
        return total
    pass

class Record:
    def __init__(self, amount, comment, date=dt.datetime.now().date()):
        self.amount = amount
        date_format = '%d.%m.%Y'
        if date == dt.datetime.now().date():
            self.date = date
        else:
            date_right = dt.datetime.strptime(date,date_format)
            self.date = date_right.date()
        self.comment = comment
    pass

class cash_calc(Calculator):
    def __init__(self,limit):
        super().__init__(limit)
        self.USD_RATE = 75.09
        self.EURO_RATE = 89.29
    def get_today_cash_remained(self, currency):
        currencies = {
            'usd':[{'rate':self.USD_RATE, 'name':'USD'}], 'eur':[{'rate':self.EURO_RATE, 'name':'Euro'}], 'rub':[{'rate':1,'name':'руб'}]
            }
        cash_remained = self.limit - self.get_today_stats()
        if currency in currencies.keys():
            rate = currencies[currency][0]['rate']
            name_currency = currencies[currency][0]['name']
            uni_cash = cash_remained/rate
        if cash_remained > 0:
            return f'На сегодня осталось {uni_cash} {name_currency}'
        elif cash_remained == 0:
            return 'Денег нет, держись'
        else:
            return f'Денег нет, держись: твой долг - {abs(cash_remained)} {name_currency}'

class calories_calc(Calculator):
    def get_calories_remained(self):
        total_calories = self.get_today_stats()
        calories_remained = self.limit - total_calories
        if total_calories < self.limit:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_remained} кКал'
        else:
            return 'Хватит есть!'
    def get_week_stats(self):
        today = dt.datetime.now().date()
        seven_days_ago = today - dt.timedelta(days=6)
        week_stats = [record.amount for record in self.records if record.date <= today and record.date > seven_days_ago]
        total = sum(week_stats)
        return total

cash_calculator = cash_calc(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др', date='08.11.2019'))

print(cash_calculator.get_today_cash_remained('rub'))
