import numbers
import requests


class Money(object):
    def __init__(self, amount, currency="USD"):
        if amount < 0:
            raise ValueError("The amount of money should be positive.")
        self.amount = amount
        self.currency = currency

    def convert_to(self, currency):
        """Currency converter

        :param currency: resulting currency
        :return: converted amount

        """
        if self.currency == "USD":
            return self.amount * self.exchange_rate(currency)
        else:
            return self.amount / self.exchange_rate(currency)

    def exchange_rate(self, base_currency):
        """Get exchange rate from API relatively to USD

        :param base_currency:
        :return:

        """
        params = {'access_key': '847ebf28d9825567493742e4b0fc2d46',
                  'currencies':
                      '{}, {}'.format(self.currency, base_currency)}
        r = requests.get('http://apilayer.net/api/live',
                         params=params)
        exchange_dict = r.json()['quotes']
        if self.currency == "USD":
            rate = exchange_dict['USD' + base_currency]
        else:
            prime_curr_rate = exchange_dict['USD' + self.currency]
            sec_curr_rate = exchange_dict['USD' + base_currency]
            rate = prime_curr_rate / sec_curr_rate
        return rate

    def __str__(self):
        return "{} {}".format(self.amount, self.currency)

    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return Money(self.amount + other, self.currency)
        elif isinstance(other, Money):
            if self.currency != other.currency:
                other.amount = other.convert_to(self.currency)
            return Money(self.amount + other.amount, self.currency)
        else:
            raise TypeError

    __radd__ = __add__

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Money(self.amount * other, self.currency)
        elif isinstance(other, Money):
            if self.currency != other.currency:
                other.amount = other.convert_to(self.currency)
            return Money(self.amount * other.amount, self.currency)
        else:
            raise TypeError

    __rmul__ = __mul__

    def __sub__(self, other):
        if isinstance(other, numbers.Number):
            return Money(self.amount - other, self.currency)
        elif isinstance(other, Money):
            if self.currency != other.currency:
                other.amount = other.convert_to(self.currency)
            return Money(self.amount - other.amount, self.currency)
        else:
            raise TypeError

    def __rsub__(self, other):
        if isinstance(other, numbers.Number):
            return Money(other - self.amount, self.currency)
        elif isinstance(other, Money):
            if self.currency != other.currency:
                other.amount = other.convert_to(self.currency)
            return Money(other.amount - self.amount, self.currency)
        else:
            raise TypeError
