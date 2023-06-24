import os
import util

os.system("title [ 더러운 우리집 ]")

result = None
print("\033[90m[ 더러운 우리집 ]")
util.warning("이 게임은 게임 저장이 없으며, 선택지 선택을 틀리지 않도록 조심해주세요.")
util.info("이 게임은 머드 게임으로 고전 게임처럼 만들었습니다.")
result = util.gameInput(["게임 시작", "게임 종료", "정보"])
while result != None:
    result = util.gameInput(["게임 시작", "게임 종료", "정보"])
util.info("정상")