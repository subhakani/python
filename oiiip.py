from datetime import datetime

o = datetime.strptime("01:05:00.000", "%H:%M:%S.%f")
p= datetime.strptime("00:50:00.000", "%H:%M:%S.%f")

print (o-p)
