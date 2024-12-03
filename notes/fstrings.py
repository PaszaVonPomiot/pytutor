# format_spec  ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
# {value:fill align width , sign # 0 width . precision type}

from datetime import datetime

number = 1234567.1234567
date = datetime.now()
space = 30
time = 10

# limit the number of decimal places
print(f"Formatted number: {number:.2f}")

# add underscores as thousands separators
print(f"Formatted number: {number:_}")

# add spaces as thousands separators
print(f"Formatted number: {number:,}".replace(",", " "))

# add spaces as thousands separators
format(1234567890, ",d").replace(",", " ")

print(f"Formatted date: {date:%Y-%m-%d %H:%M:%S}")

print(f"Left aligned {"100 zł":<20} xxx")  # with spaces
print(f"Right aligned {"100 zł":>20} xxx")  # with spaces
print(f"Right aligned {"100 zł":.>20} xxx")  # with dots
print(f"Center aligned {"100 zł":.^20} xxx")  # with dots

print(f"Center aligned {"100 zł":.^{space}} xxx")  # with dynamic length

print(f"{number=}, {date=}, {space + time=}")
