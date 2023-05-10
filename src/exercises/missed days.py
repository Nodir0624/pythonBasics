def get_full_name(firstname: str, lastname: str, middlename: str = '') -> str:
    if middlename !='':
        return f"{firstname} {middlename} {lastname}".title()
    else:
        return f"{firstname} {lastname}".title()

print(get_full_name('john', 'doe'))
print(get_full_name('john', 'doe', 'brown'))
print(get_full_name('jane', 'doe', 'rogers'))
print(get_full_name('john', 'doe'))

print(get_full_name(firstname='jane', middlename='rogers', lastname='doe'))
print(get_full_name('anne', 'doe', 'marie'))


