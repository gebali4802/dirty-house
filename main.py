import os
import util

os.system("title [ 더러운 우리집 ]")

result = None
print()
print("\033[90m[ 더러운 우리집 ]")
util.warning("이 게임은 게임 저장이 없으며, 이 게임은 윈도우 기반으로 만들어졌습니다.")
util.info("이 게임은 머드 게임으로 고전 게임처럼 만들었습니다.")
while result == None:
    result = util.gameInput(["게임 시작", "게임 종료", "정보"])
util.info("정상")