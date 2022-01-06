# Alt-Ctrl-L to reformat code

print(print)
print(print())

f = print
f("test")


def send_mail(from_name, to_name, old):
    text = '''
    Dear {}, I am sending you this email from {}.
    I am sorry to inform you that your {} is old.'''
    print(text.format(to_name, from_name, old))


send_mail("John", "Jane", "44")
