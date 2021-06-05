import mypack.pack1.module11 # 경로 불러오기 전에 경로참조설정.
mypack.pack1.module11.func11()

import mypack.pack1.module11 as mm1 # 경로를 전부 치는 번거로움을 피하기 위해 별칭 이용.
mm1.func111()

from mypack.pack1.module11 import * # 또는 from을 이용.
func111()

