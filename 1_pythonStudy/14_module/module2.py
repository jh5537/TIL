'''
# calculator module을 참조하여 계산. - 같은 폴더 내에 있을 경우.
import calculator  # 모듈 전체를 참조하는 순간, 함수뿐 아니라 print()등 실행문도 같이 출력. from 형식으로 참조하면 출력되지 않음.

a = calculator.add(3, 4) # 모듈명.함수() 형식으로 호출
print(a)

# 경로가 다른 폴더에 있는 모듈을 참조할 경우. - Preferences > Project > Python Interpreter > show all > show path > +로 경로 추가
""" 또는
1) 코드로 모듈 파일 경로 설정
improt sys
from '파일명' import *

2) 폴더 경로 설정
sys.path.append('파일경로')
"""

import showInfo
"""
from showInfo import show_name
from showInfo import * # *은 import all의 의미. 
전체적으로는 import showInfo와 같은 의미이지만 모듈.함수()로 호출하지 않고 함수()로 호출함.
"""
showInfo.show_name()
'''

import moduleMain

print(moduleMain.getName())
moduleMain.main()

