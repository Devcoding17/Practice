# Datetime Handling
from datetime import datetime

dt = datetime.strptime("2025-06-01", "%Y-%m-%d")
print(dt.strftime("%B %Y"))
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
print(dt.strftime( "%C %A %B %d %Y %H:%M:%S"))