import csv
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

banks = []
with open('new_banks.csv') as newBanks:
    banks = list(csv.DictReader(newBanks))

    for entry in banks:
        entry.pop('2010_Deposits')
        entry.pop('2011_Deposits')
        entry.pop('2012_Deposits')
        entry.pop('2013_Deposits')
        entry.pop('2014_Deposits')
        entry.pop('2015_Deposits')
        entry.pop('2016_Deposits')

print("banks:\n", banks[0].keys())

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2010, 1, 1)
end_date = date(2050, 1, 1)
day = daterange(start_date, end_date)

with open('bank_deposits.csv', 'r') as file:
    deposits = csv.DictReader(file)
    deposits = list(deposits)
    new_deposits = []
    for bank in banks:
        print("New Bank: ", bank)
        #print("firstdeposits:",deposits[1])
        bank_year = deposits[:365]
        #print("abankyear:", bank_year[0].keys())
        deposits = deposits[:365]
        #print(len(bank_year))
        if len(bank_year) == 365:
            # This loop makes a year of entries for 1 of the 14 new bank locations
            # For each day in bank year, assign data to one bank
            for row in bank_year:
                date = next(day).strftime("%m/%d")

                # Day of the year for the current bank location
                bank['Day_of_Year'] = date
                row['Day_of_Year'] = date
                # Change the old bank location to the current bank location of the 14 total
                for column, value in bank.items():
                    row[column] = value
                #print(row)
                #input()
            
            # Start building the new list of day rows
            for row in bank_year:
                # Pop off random None: [
                # None key is view only
                # print("inRowPop",row[None])
                new_deposits.append(row)


    # We have used up all year-sized data sets
    print("yo", len(bank_year))
    with open('new_deposits_data.csv', 'w') as f:
        headers = list(new_deposits[0].keys())
        print(headers)
        writer = csv.DictWriter(f, headers)
        writer.writeheader()
        writer.writerows(new_deposits)


print("Complete.")
input()
