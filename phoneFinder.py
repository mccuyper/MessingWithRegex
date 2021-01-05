import re, pyperclip

phoneRegex = re.compile(r'''(                   # group [0]
                            (\d{3}|\(\d{3}\))?  # group [1]
                            (\s|-|\.)?          # group [2]
                            (\d{3})             # group [3]
                            (\s|-|\.)           # group[4]
                            (\d{4})             # group [5]
                            )''',
                        re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3],groups[5]])

    matches.append(phoneNum)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copies to clipboard: ')
    print('\n'.join(matches))
else:
    print("No phone numbers found")