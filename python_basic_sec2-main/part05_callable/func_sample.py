def split_name(username, delimiter):
    familiy_name, last_name = username.split(delimiter)
    return familiy_name, last_name


myoji, namae = split_name('山田_太郎', '_')
print(myoji)
print(namae)
