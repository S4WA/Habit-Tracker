import gspread
from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello_world():
  gc = gspread.service_account("./service_account.json")
  sh = gc.open("Habit-Tracker-2023").worksheet(get_date())

  data = sh.get_all_records()
  cl_names = sh.row_values(1)

  for x in data:
    for name in cl_names:
      print(x[name])
  return render_template('index.html', cl_names=cl_names, data=data)

def get_date():
  return date.today().strftime("%B")

if __name__ == '__main__':
  app.run(debug=True)