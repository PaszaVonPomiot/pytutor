def to_seconds(days = None, hours = None, minutes = None):
    if not days:
        days = 0
    if not hours:
        hours = 0
    if not minutes:
        minutes = 0

    t_days = days * 3600 * 24
    t_hours = hours * 3600
    t_minutes = minutes * 60
    return t_days + t_hours + t_minutes

print(to_seconds(1, hours=2))




