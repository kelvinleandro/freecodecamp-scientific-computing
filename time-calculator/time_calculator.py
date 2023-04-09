def add_time(start, duration, starting_day=None):
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    new_time = ''

    # Separates the start string into time and period
    start_time, period = start.split()

    # Splits the start time into hours and minutes
    start_hr = int(start_time.split(':')[0])
    start_min = int(start_time.split(':')[1])

    # Splits the duration time into hours and minutes
    duration_hr = int(duration.split(':')[0])
    duration_min = int(duration.split(':')[1])
    n_days = int(duration_hr / 24)

    end_min = start_min + duration_min
    if end_min >= 60:
        start_hr += 1
        end_min %= 60

    n_flips = int((start_hr + duration_hr) / 12)
    end_hr = (start_hr + duration_hr) % 12

    # Formatting the ending hour and period
    end_min = end_min if end_min > 9 else '0' + str(end_min)
    end_hr = 12 if end_hr == 0 else end_hr
    if period == 'PM' and start_hr + (duration_hr % 12) >= 12:
        n_days += 1

    if n_flips % 2 == 1:
        period = 'AM' if period == 'PM' else 'PM'
    
    # The final hour and period formatted
    new_time = f"{end_hr}:{end_min} {period}"

    # If a starting day is given (e.g. Tuesday)
    if starting_day:
        index = (week_days.index(starting_day.capitalize()) + n_days) % 7
        end_day = week_days[index]
        new_time += f", {end_day}"
    
    # Showing how many days have passed since the starting hour
    if n_days == 1:
        new_time += " (next day)"
    elif n_days > 1:
        new_time += f" ({n_days} days later)"

    return new_time
