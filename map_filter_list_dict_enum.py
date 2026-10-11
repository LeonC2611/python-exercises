import re

# Used Map to create a list of numbers to turn each string into the sum of its two numbers.
rows = ["3,4", "10,20", "7,8"]


def add(rows):
    a, b = rows.split(",")
    return int(a) + int(b)


total = list(map(add, rows))
print(total)


# Used Filter to create a list of emails that matched with the regex pattern I specified.
emails = ["a@x.com", "bad-email", "b@y.org", "c@"]

correct_emails = list(filter(lambda e: re.search(r"@\w+", e), emails))

print(correct_emails)


# Used list comprehension to create a list to add the pairs of numbers in a list
rows = ["3,4", "10,20", "7,8"]
total = [int(row.split(",")[0]) + int(row.split(",")[1]) for row in rows]
print(total)

# Used list comprehension and regex to create a list of emails that matched a certain criteria
emails = ["a@x.com", "bad-email", "b@y.org", "c@"]
correct_emails = [email for email in emails if re.search(r"@\w+", email)]
print(correct_emails)


# Used dictionary comprehension and regex to create a dictionary of the names and the position they were in the list.
names = ["ana", "ben", "cy"]

name_index = {name: position for (position, name) in enumerate(names)}

print(name_index)
