import os
import util

result = None
temp = None
os.system("title [ 더러운 우리집 ]")
util.clear()

print()
print("\033[90m[ 더러운 우리집 ]")

util.alart("이 게임은 게임 저장이 없으며, 이 게임은 윈도우 기반으로 만들어졌습니다.")
util.info("이 게임은 머드 게임으로 고전 게임처럼 만들었습니다.")
result = util.gameInput(["게임 시작", "게임 종료", "정보"])

class System():
    def __init__(self, money, stress, dirty, popularity, arbeit):
        self.money = money # 돈
        self.stress = stress # 스트레스
        self.dirty = dirty # 더러움
        self.popularity = popularity # 인기도
        self.arbeit = arbeit # 아르바이트(표기하지 않음)

    def firstDay(self):
        util.info("이 게임의 주인공인 당신은 어느 때와 다름없이 침대에서 일어납니다. 하지만 오늘은 무언가 다릅니다.")
        util.info("오늘은 드디어 당신이 대학교에 가는 날입니다. 당신은 대학교에 가까운 작은 원룸 월세집을 구했습니다.")
        util.info("당신은 떨리는 마음으로 강의실에 들어갑니다. 사람들은 모두 다 친절해보이고.. 아 이때 교수님이 들어와 출석을 부릅니다. 이만 여기까지 해야겠군요.")

        util.stop(10)
        util.alart("당신은 이제 드디어 집에 갑니다. 그 전에 당신은 새로운 친구를 하나 사귀었습니다. 만일 누가 물어보면 그 친구는 현수, 최현수")
        util.alart("새로 사귄 친구들이 개강 파티에 같이 가자고 합니다.")
        result = util.gameInput(["간다", "가지 않는다"])
    
        if result == "간다":
            util.info("당신은 새로 사귄 친구들과 개강 파티에 간다고 결정했습니다. 친구들은 친절했고 당신이 재미있었기에 인기도는 15상승하였습니다.")
            self.popularity += 15
            util.info("하지만 당신은 곧 처음 간 큰 파티에 스트레스가 10증가했습니다.")
            self.stress += 10
        else:
            util.info("당신은 개강 파티에 가지 않기로 결정했습니다. 당신의 인기도는 5하락하였고, 스트레스는 5감소하였습니다.")
            self.popularity -= 5
            util.info("하지만 당신은 가지 않은것을 후회하지도 원망하지도 않았습니다. 아직까지는요..")
            self.stress -= 5

            util.alart("이렇게 하루가 흘러갔습니다.")

system = System(100, 10, 10, 10, 0)

def printTotal():
    util.alart("오늘 하루의 일과입니다.")
    print()
    print(f"\033[96m[ 정보 ] : 돈 : {system.money}\033[90m")
    print(f"\033[96m[ 정보 ] : 스트레스 : {system.stress}\033[90m")
    print(f"\033[96m[ 정보 ] : 더러움 : {system.dirty}\033[90m")
    print(f"\033[96m[ 정보 ] : 인기도 : {system.popularity}\033[90m")
    print(f"\033[96m[ 정보 ] : 아르바이트 : {system.arbeit}개\033[90m")
    util.gameInput(["다음 날"])

def gamePlay():
    system.firstDay()
    printTotal()

if int(result) == 1:
    util.clear()
    gamePlay()

elif int(result) == 2:
    util.alart("게임을 종료합니다!")
    exit()

elif int(result) == 3:
    util.clear()
    util.alart("이 게임은 2023 전국 청소년 GAME 코딩대회 출품작입니다. 이 게임은 파이썬으로 작성되었으며, 세이브 파일 저장을 위해 SQLite3모듈을 사용하였습니다. 그 외에는 기본 내장 라이브러리와 직접 만든 내부 라이브러리를 사용하였으며, 윈도우 환경에서 원활하게 돌아갑니다. 타 환경에서는 작동은 합니다만, 사실상 윈도우 전용입니다. 이 게임을 만들때 아이디어는 4년전 망상으로만 구상했던 게임의 아이디어를 실제로 만든 것이라 더 애착이 갑니다. 게임은 게임이라고 할것도 없이 보잘것 없을정도로 심심하나 열심히 만들었습니다.")
    result = None
    while result == None:
        util.gameInput(["나가기"])
        exit()