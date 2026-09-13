import re

log = input("Service log: ")

pattern = r"^(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2}) (?P<time>[0-9]{2}:[0-9]{2}:[0-9]{2}) (?P<level>[a-z]+) (?P<message>.+)$"

match = re.match(pattern, log, re.IGNORECASE)

print(match.groupdict())
