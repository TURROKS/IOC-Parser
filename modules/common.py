# File is used to store global variables

# Variables

IPs = []
Hashes = []
URLs = []
Files = []
Emails = []
Domains = []

domain_re = "([a-zA-Z0-9-_]+\.[a-zA-Z]{2,})$"
file_re = "^[\w,\s-]+\.[A-Za-z0-9]{3}$"
email_re = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"