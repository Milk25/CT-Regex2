
import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Regular expression to extract emails, excluding those from 'exclude.com'
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

print(emails)
