#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3
#!/bin/python3

import sys
from datetime import datetime, date

if (len(sys.argv) != 2):
	print("usage: " + sys.argv[0] + " [message_count]")
	exit(1)

today = datetime.today()
begin = datetime.strptime("2022-09-14", '%Y-%m-%d')
time_pourcent = (today-begin).days / (42*7) * 100;
messages_pourcent = int(sys.argv[1]) / 420
print(str(messages_pourcent) + "% of the messages has been wrote in\n" + str(time_pourcent) + "% of the given time !\n keep going folks");

