# 표준 모듈
'''
import sys
print(sys.builtin_module_names) # 표준 모듈 불러오기.
"""'_abc', '_ast', '_codecs', '_collections', '_functools', '_imp', '_io', '_locale', '_operator', '_peg_parser', 
'_signal', '_sre', '_stat', '_string', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'atexit', 
'builtins', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'posix', 'pwd', 'sys', 
'time', 'xxsubtype'
"""
print(dir(__builtins__)) # 로도 확인 가능.
'''
import random as rd # random 모듈을 참조. 별칭은 rd
print(rd.randint(1, 10)) # 1부터 10까지 정수 중 랜덤으로 출력.

from random import randint # random 모듈에서 randint 변수(함수)만 참조.
print(randint(1, 10)) # 1부터 10까지 정수 중 랜덤으로 출력.
