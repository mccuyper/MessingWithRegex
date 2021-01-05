import pyperclip, re

protocolRegex = re.compile(r'''
    https?://           
    (?:w{3}\.)?         
    [a-zA-Z0-9._%+-]+                      
    [a-zA-Z]      
    ''', re.VERBOSE)

text = str(pyperclip.paste()) # variable contents data clipboard and converting
matches = [] # empty list for matches

for website in protocolRegex.findall(text): # finding website from text
    matches.append(website) # if find regex append to matches list

if len(matches) > 0:
    pyperclip.copy('\n'.join(map(str, matches))) # copying result to clipboard after adding newline after each match
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No website found')
