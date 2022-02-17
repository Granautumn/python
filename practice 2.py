my_text = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

text = []

for i in str:
    if i.isdigit()
        text.append(f'"{int(i):02}"')
    else:
        try:
            text.append(f'"+{int(i):02}"')
        except:
            text.append(i)
print(*text)
