#ATBS MoreFinders
---
Experimenting with other regexs.

1. Web finder
..* looks for https, www., .com, or other common website names and then copies it to the clipboard

2. Date Cleaner
..* looks for dates and then puts the years in front.
..* the problem with this one is not being able to tell the difference between days and months

3. Sensitive info
..* replaces all Credit card numbers and SSNs with asterisks using re.sub
