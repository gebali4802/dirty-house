import os
import util

os.system("title [ 더러운 우리집 ]\033[95m")

print("\033[90m[ 더러운 우리집 ]")
util.info("이 게임은 머드 게임으로 고전 게임처럼 만들었습니다.")
util.warning("이 게임은 게임 저장이 없으며, 선택지 선택을 틀리지 않도록 조심해주세요.")
result = util.gameInput([[1, 2, 3], ["게임 시작", "게임 종료", "정보"]])
if result == None:
    while result != None:
        result = util.gameInput([[1, 2, 3], ["게임 시작", "게임 종료", "정보"]])
else:
    util.info("정상적작동")