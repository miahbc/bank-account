import csv

class Owner():
    def __init__(self):
        pass

    def all_owners(self):
        owners_array = []
        owners_file = csv.DictReader(open("support/owners.csv"))
        for row in owners_file:
            owners_array.append(row)
        return owners_array

    
    # def all_owners(self):
    #     owners_array = []
    #     owners_file = csv.DictReader(open("support/owners.csv"))
    #     for row in owners_file:
    #         owners_array.append(row)    

    #     return owners_array


print(Owner.all_owners())