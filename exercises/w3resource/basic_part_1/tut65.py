from datetime import datetime, timezone

input_seconds = datetime.now(tz=timezone.utc).timestamp()  # epoch

days, day_remainder = divmod(input_seconds, 86400)
hours, hour_remainder = divmod(day_remainder, 3600)
minutes, seconds = divmod(hour_remainder, 60)

print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
