from datetime import timedelta, datetime, date

dates = []

def this_month(): # The name of the current day's month
  return date.today().strftime("%B")

def formt(date_obj): # Format the date as string
  return date_obj.strftime('%m/%d/%Y')

def convert_date(string_date): # Convert a string to date
  if (isinstance(string_date, str)):
    return datetime.strptime(string_date, '%m/%d/%Y').date()
  elif (isinstance(string_date, date)):
    return string_date
  return None

def wday(string_date):
  date_obj = convert_date(string_date)
  if (date_obj == None): return -1
  weekd = date_obj.weekday() + 1
  if (weekd == 7): weekd = 0
  return weekd

def fill_previous_days(date_list):
  prev_days = []
  earliest = min(date_list)
  for i in range(wday(earliest)):
    prev_days.append(earliest - timedelta(days=i+1))
  return prev_days

def fill_next_days(date_list):
  next_days = []
  latest = max(date_list)
  for i in range(6 - wday(latest)):
    next_days.append(latest + timedelta(days=i+1))
  return next_days

def add(string_date):
  dates.append(convert_date(string_date))

def fill_empty_dates(date_list):
  date_list.extend(fill_previous_days(date_list))
  date_list.extend(fill_next_days(date_list))
  return date_list

def sort_dates():
  if not dates: return []

  # Sort In Numerical Days.
  dates.sort()

  # Sort In Weekdays
  calendar_sort = sorted(dates, key=lambda x: wday(x))

  result = []
  u = None # The last weekday that the for statement has loaded
  each_wday = [] # Group dates by each of the weekday

  for obj in calendar_sort:
    if (u != wday(obj)): # Reset when the for statement gives it next weekday.
      each_wday = []
      u = wday(obj)
      result.append(each_wday) # Append it to the result (parent list).
    each_wday.append(obj)

  return result

# Without this function, JavaScript will receive something like this. [[datetime.date('20XX-XX-XX'), ...]]
def convert_calendar_to_text(calendar):
  result = []
  for row in calendar:
    temp = []
    for cell in row:
      temp.append(formt(cell)) # Replacing dashes to slashes
    result.append(temp)
  return result

  # [ Print Calendar ]
  # u = None
  # for obj in calendar_sort:
  #   if (u != wday(obj)):
  #     print("----")
  #     u = wday(obj)
  #   print(obj)

  # print('======')
