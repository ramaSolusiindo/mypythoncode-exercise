import re
text = 'string 7 asuuu 5 string'
angka = str(re.search(r'\d+', text).group())
print(angka)

text2 = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', text2)
# If-statement after search() tests if it succeeded
if match:
  print('found', match.group()) ## 'found word:cat'
else:
  print('did not find')