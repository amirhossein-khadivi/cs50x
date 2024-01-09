# TODO
import string
from cs50 import get_string

comment = get_string('Text: ')
letter = 0
for a in comment:
    if (a.isalpha()):
        letter = letter + 1

word = len(comment.split())
sen = 0
for a in comment:
    if (a == '!' or a == '.' or a == '?'):
        sen = sen + 1

wordsen = word / 100
L = letter / wordsen; S = sen / wordsen

index = round(0.0588 * L - 0.296 * S - 15.8)

if (index >= 16):
    print('Grade 16+')
elif (index < 1):
    print('Before Grade 1.')
else:
    print('Grade '+str(index))