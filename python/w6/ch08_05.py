languages = ['java', 'c/c++', 'c#', 'java']
print(languages)

for str in languages:
    if str == 'java':
        languages.remove('java')

print(languages)