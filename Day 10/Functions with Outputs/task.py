def format_name(f_name,l_name):
    str1 = f_name.title()
    str2 = l_name.title()
    str = str1 + " " + str2
    return str

first_name = input("Whats your first name")
last_name = input("Whats your last name")
name = format_name(first_name,last_name)
print(name)