def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, temp = s.split('@')
        website, extension = temp.split('.')
    except ValueError:
        return False
    username_validity = all(list(map(lambda x: x.isalnum() or x in ['-','_'],username))) and (len(username) > 0)
    website_validity = all(list(map(lambda x: x.isalnum(),website)))
    extension_validity = all(list(map(lambda x: x.isalpha(),extension))) and (len(extension) <= 3)

    return (username_validity) and (website_validity) and (extension_validity)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)