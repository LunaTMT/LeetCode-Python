emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
unique_emails = set()

for email in emails:
    local, domain = email.split('@')
    local = local.split('+')[0]
    local = local.replace('.', '')
    unique_emails.append(local + "@" + domain)
return len(unique_emails)