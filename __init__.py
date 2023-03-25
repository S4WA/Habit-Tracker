import json
import gspread
import zcalendar
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  this_month = zcalendar.this_month()
  gc = gspread.service_account("./service_account.json")
  sh = gc.open("Habit-Tracker-2023").worksheet(this_month) # Select the worksheet of the current month

  data = sh.get_all_records()
  cl_names = sh.row_values(1)

  zcalendar.dates = [] # Reset the array everytime someone access to the index page
  math_data = {}

  # For each rows
  for x in data:
    children, parents = 0, 0
    # For each columns
    for name in cl_names: # Cells below
      # Add to the list
      if (name == "Date"):
        zcalendar.add(x[name])
      else: # Calculation
        val = x[name].split("/")
        if (len(val) < 2):
          continue # Ignore if it's empty.
        children += int(empty_check(val[0]))
        parents  += int(empty_check(val[1]))

    # Without this if statement, it will add unnecessary data.
    # Specifically when the row has only the date and doesn't have any other data in the other cells, or Simply it's 0/0.
    if (children != 0 and parents != 0): # To make sure both, denominator and numerator is not 0.
      math_data[x["Date"]] = [ children, parents ]

  # Fill the empty areas in calendar
  zcalendar.fill_empty_dates(zcalendar.dates)

  # Sort for the calendar
  sorted_dates = zcalendar.convert_calendar_to_text(zcalendar.sort_dates())
  return render_template('index.html', cl_names=cl_names, data=data, calendar=sorted_dates, math_data=math_data, this_month=this_month)

def empty_check(num):
  return 0 if not num else num

if __name__ == '__main__':
  app.run(debug=True, threaded=True)