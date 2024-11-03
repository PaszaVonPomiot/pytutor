from datetime import datetime, timezone

input_seconds = datetime.now(tz=timezone.utc).timestamp()  # epoch

days, remainder = divmod(input_seconds, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
