def to_seconds(days = 0, hours = 0, minutes = 0):
    t_days = days * 3600 * 24
    t_hours = hours * 3600
    t_minutes = minutes * 60
    return t_days + t_hours + t_minutes

print(to_seconds(days=0, hours=2, minutes=1))



