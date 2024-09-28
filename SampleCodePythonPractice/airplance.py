# from enum import Enum
#
#
# class Company(Enum):
#     DELTA = "Delta"
#     UNITED = "United Airline"
#     AMERICAN = "American Airline"


class Airlines:
    def __init__(self, company, distance, seat_class):
        self.company = company
        self.distance = distance
        self.seat_class = seat_class

    def oper_cost(self):
        match self.seat_class:
            case "Economy":
                return 0.1 * self.distance
            case "Business":
                return 0.2 * self.distance
            case "Premium":
                return 0.5 * self.distance

    def price(self):
        pass


class United(Airlines):
    def price(self):
        return max(self.oper_cost(), 0.85 * self.distance)


class Delta(Airlines):
    def price(self):
        return 0.7 * self.distance


test1 = [
    "United 1500 Economy",
    "Delta 1300 Business"
]


def cal_price(test):
    for airline_data in test:
        company, distance, seat_class = airline_data.split()
        distance = float(distance)
        ClassReference = globals()[company]
        airline = ClassReference(company, distance, seat_class)
        print(airline.price())


cal_price(test1)
