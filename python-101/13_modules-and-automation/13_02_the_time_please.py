# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

from datetime import datetime

now = datetime.now()

pretty_date = now.strftime("%A, %B %d, %Y - %H:%M")

print(pretty_date)
