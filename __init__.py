import json
import gspread
import zcalendar
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  gc = gspread.service_account("./service_account.json")
  sh = gc.open("Habit-Tracker-2023").worksheet(zcalendar.this_month())

  data = sh.get_all_records()
  cl_names = sh.row_values(1)

  zcalendar.dates = []

  math_data = {}
  # For each rows
  for x in data:
    children = 0
    parents  = 0
    # For each columns
    for name in cl_names: # Cells below
      # Add to the list
      if (name == "Date"):
        # print(x[name])
        zcalendar.add(x[name])
      else: # Calculation
        val = x[name].split("/")
        if (len(val) == 0 or val[0] == ''): continue
        children += int(empty_check(val[0]))
        parents  += int(empty_check(val[1]))
    math_data[x["Date"]] = doMath(children, parents)

  # Fill the empty areas in calendar
  zcalendar.fill_empty_dates(zcalendar.dates)

  # Sort for the calendar
  sorted_dates = zcalendar.sort_dates(False)
  return render_template('index.html', cl_names=cl_names, data=data, calendar=sorted_dates, math_data=json.dumps(math_data))

def empty_check(num):
  return 0 if not num else num

def doMath(children, parents):
  return 0 if parents == 0 else round(children/parents*100, 1)

if __name__ == '__main__':
  app.run(debug=True, threaded=True)