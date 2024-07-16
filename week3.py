#name = input('who are you?')
#print('Welcome to the class,',name)


working_hour = input('how many hours did you work last week?')
weekly_working_hour = int(working_hour)

normal_hour_rate = 51.45
Overload_hour_rate = 88.9

if weekly_working_hour <= 35:
    weekly_pay = weekly_working_hour * normal_hour_rate
elif weekly_working_hour > 35:
    weekly_pay = 35 * normal_hour_rate + (weekly_working_hour-35)* Overload_hour_rate

print ('Your weekly payment is $',weekly_pay)





"""
import yfinance
start = '2020-01-01'
end = None
tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
    # Download data from yfinance
    df = yfinance.download(tic, start, end, ignore_tz=True)
    print(df)
    # Get the base name of the ticker
    # E.g. QAN.AX -> qan
    tic_base = tic.lower().split('.')[0]
    # Save data to a csv file named after tic_base
    df.to_csv(f'{tic_base}_stk_prc.csv')
numbers = [-2,3,9,1,5,7,2,11,0,3,12,3,15,10]
temp_largest = numbers (0)
print ('before', temp_largest)
for number in numbers:
    if number > temp_largest:
        temp_largest = number
    print (number, temp_largest)
print (f,'the largest number value is {temp_largest}')
for i in range(1, 4):
    for j in range(1, 4):
        if i <= j:
            print(i, j)
"""