import gspread

gc = gspread.service_account("./service_account.json")

sh = gc.open("Habit-Tracker-2023")

print(sh.sheet1.get('B1'))