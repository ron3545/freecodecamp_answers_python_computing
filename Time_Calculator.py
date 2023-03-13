
def add_time(start, duration, start_day = None):
  start_time_parts = start.split()
  start_hour, start_min = map(int, start_time_parts[0].split(':'))

  is_pm = start_time_parts[1] == 'PM'
  if is_pm and start_hour != 12:
    start_hour += 12
  elif not is_pm and start_hour == 12:
    start_hour =0

  duration_parts = duration.split(':')
  duration_hour, duration_min = map(int, duration_parts)

  end_hour = start_hour + duration_hour
  end_min = start_min + duration_min
  end_day_offset = 0
  while end_min >= 60:
    end_min -= 60
    end_hour += 1
  while end_hour >= 24:
    end_hour -=24
    end_day_offset += 1

  end_time_parts = []
  if end_hour == 0:
    end_time_parts.append('12:')
  elif end_hour <= 12:
    end_time_parts.append(str(end_hour) + ':')
  else:
    end_time_parts.append(str(end_hour -12) + ':')
  end_time_parts.append(f'{end_min:02d}')
  end_time_parts.append(' PM' if end_hour >= 12 else ' AM')
  end_time_str = ''.join(end_time_parts)

  if start_day is not None:
    start_day = start_day.lower()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    start_day_index = days.index(start_day)
    end_day_index = (start_day_index + end_day_offset) % 7
    end_day = days[end_day_index]
    end_time_str += f', {end_day.capitalize()}'

  if end_day_offset == 1:
    end_time_str += ' '
    end_time_str += '(next day)'
  elif end_day_offset > 1:
    end_time_str += ' '
    end_time_str += f'({end_day_offset} days later)'

  return end_time_str

print(add_time("2:59 AM", "24:00", "saturDay"))