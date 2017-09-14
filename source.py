import re

fin = open('./data/mbox.txt', 'r')

"""
In each separate letter from the beginning there is a line of format:
From <email> <name of a day> <name of a month> <day of the month> <time> <year>
and in the middle of the letter the line "Subject".
Regular expression (which located above) describes one string:
    - subject
    - email and date
"""
pattern = re.compile(r"^From\s+"
                     r"(?P<email>[\w_\-\.]+@[\w_\-]+(?:\.[\w_\-]+)+)\s+"
                     r"(?:[A-Z]{1}[a-z]{2})\s+(?P<month>[A-Z]{1}[a-z]{2})\s+"
                     r"(?P<num_day>\d+)\s+"
                     r"\d+:\d+:\d+\s+"
                     r"(?P<year>\d+)\s*\n"
                     r"|^Subject: (?P<subject>.+)", re.U|re.M)

parse_result = pattern.findall(fin.read())

"""
In result, pattern.findall() returned list of tuple such as:
        (email, month, num_day, year, subject)
Subject-string is always lower than  email-date-string.
This means that the tuple on the even position (in parse_result) contains the date and email:
        ('mail@mail.com', 'Jun', '5', '2007', '')
The tuple on the odd position (in parse_result) contains the subject:
        ('','','','','any subject')
"""
quantity_dict = {}
for i in range(len(parse_result) // 2):
    email = parse_result[2*i][0]
    date = "%s %s %s" % (parse_result[2*i][2], parse_result[2*i][1], parse_result[2*i][3])
    subject = parse_result[2*i+1][4]
    print("%s (%s): %s" % (email, date, subject))
    if email in quantity_dict:
        quantity_dict[email] += 1
    else:
        quantity_dict[email] = 1

for key, value in quantity_dict.items():
    print("%s: %d" %(key, value))
