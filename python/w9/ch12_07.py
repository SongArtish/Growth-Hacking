import ex03.module01
import ex03.module02
import ex03.module03

print('실행 파일입니다.')

# module을 이렇게 설계하면 오류는 아니지만
# 함수가 자동으로 실행되므로 설계가 문제가 있음
# => 실행 파일과 모듈 파일을 구분!!!

# __name__
# python에는 기본적으로 이 전역변수에 파일 이름이 저장됨
print(f'__name__: {__name__}')