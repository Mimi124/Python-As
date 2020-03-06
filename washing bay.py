class sales:
    def __init__(self,vehicle_type,reg_no,attendant_id,charge,date):
        self.vehicle_type = vehicle_type
        self.reg_no = reg_no
        self.attendant_id = attendant_id
        self.charge = charge
        self.date = date

class attendant:
    def __init__(self,attendant_id,attendant_name):
        self.attendant_id = attendant_id
        self.attendant_name = attendant_name

class vehicle_type:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


daysoftheweek = {}
def enterDailySales(daysoftheweek):
    dailySales = []

    for currentDay in daysoftheweek:
        print("Pleas enter sales for", currentDay + ": ")
        dailySale = float(input())
        dailySales.append(dailySale)

    return dailySales

def TotalSales(dailySales):
    total = 0

    for currentdailySale in range (len(dailySales)):
        total = total
