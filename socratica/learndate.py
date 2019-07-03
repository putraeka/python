import datetime

# fungsi datetime ga bisa
# Eh ternyata karena nama filenya ga boleh sama dengan nama module
define_date = datetime.date(2019, 7, 1)
today = datetime.datetime.today()
print(define_date)
print(today)
print(today.hour,":",today.minute)

mill = datetime.date(2000, 1, 1)
# Untuk menghitung berapa hari kedepan/kebelakang
dt = datetime.timedelta(100)
print(mill + dt)

#Parse tanggal dari data
moon_landing = "7/20/1969"
moon_landing_date_time = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_date_time)