# import하면 ch08_05에서 작성한 내용이 연산되고 삭제된 리스트 값으로 나옴
# from ch08_05 import languages

languages = ['java', 'c/c++', 'c#', 'java']

print(languages)

# 개인적으로, while문으로 작성하는게 더 직관적이고 깔끔한 것 같음!!!
while ('java' in languages):
    languages.remove('java')

print(languages)