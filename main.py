import os
import util

result = None
os.system("title [ 더러운 우리집 ]")
util.clear()

print()
print("\033[90m[ 더러운 우리집 ]")

util.warning("이 게임은 게임 저장이 없으며, 이 게임은 윈도우 기반으로 만들어졌습니다.")
util.info("이 게임은 머드 게임으로 고전 게임처럼 만들었습니다.")

while result == None:
    result = util.gameInput(["게임 시작", "게임 종료", "정보"])

def gamePlay():
    util.info("이 게임의 주인공인 당신은 어느 때와 다름없이 침대에서 일어납니다.\n하지만 오늘은 무언가 다릅니다.")
    util.info("오늘은 드디어 당신이 대학교에 가는 날입니다.")

if int(result) == 1:
    util.clear()
    gamePlay()

elif int(result) == 2:
    util.warning("게임을 종료합니다!")
    exit()

elif int(result) == 3:
    util.clear()
    util.warning("이 게임은 2023 전국 청소년 GAME 코딩대회 출품작입니다. 이 게임은 파이썬으로 작성되었으며, 세이브 파일 저장을 위해 SQLite3모듈을 사용하였습니다. 그 외에는 기본 내장 라이브러리와 직접 만든 내부 라이브러리를 사용하였으며, 윈도우 환경에서 원활하게 돌아갑니다. 타 환경에서는 작동은 합니다만, 사실상 윈도우 전용입니다. 이 게임을 만들때 아이디어는 4년전 망상으로만 구상했던 게임의 아이디어를 실제로 만든 것이라 더 애착이 갑니다. 게임은 게임이라고 할것도 없이 보잘것 없을정도로 심심하나 열심히 만들었습니다.")
    result = None
    while result == None:
        result = util.gameInput(["나가기"])
        exit()