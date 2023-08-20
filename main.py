import os
import time
import util
import random

result = None
os.system("title [ 더러운 우리집 ]")
util.clear()

print()
print("\033[90m[ 더러운 우리집 ]")

util.alart("이 게임은 게임 저장이 없으며, 이 게임은 윈도우 기반으로 만들어졌습니다.")
util.info("이 게임은 머드 게임으로 고전 게임처럼 만들었습니다.")
result = util.gameInput(["게임 시작", "게임 종료", "정보"])

class Game():
    def __init__(self, money, stress, dirty, popularity, arbeit):
        self.money = money # 돈
        self.stress = stress # 스트레스
        self.dirty = dirty # 더러움
        self.popularity = popularity # 인기도
        self.arbeit = arbeit # 아르바이트(표기하지 않음)

    def normalDay(self):
        util.info("오늘도 또 어김없이 다른 때와 다른것이 없이 일어난 아침입니다. 오늘은 평소보다 상쾌해진 것 같은 기분이 드네요.")
        util.info("오늘도 어김없이 등교합니다. 다른 때와 정말 달라진 것이 없군요. 평소보다도 더 격렬하게 종강을 외칩니다.")
        util.alart("앗! 교수님이 들어옵니다. 출석을 부르고 있군요. 교수님을 무시하고 폰을 볼까요?")

        result = util.gameInput(["본다", "만다"])

        if int(result) == 1:
            for i in range(random.randint(1, 3))
                util.info("당신은 폰을 쳐다보기 시작합니다.")
                time.sleep(random.randint(3, 15))

                clock = [time.time(), 0]
                util.alart("교수님이 당신 옆을 지나갑니다. 당신의 이름을 알고 있는 듯 하군요.")
                util.gameInput(["끈다"])
                clock[1] = time.time()

                if clock[1] - clock[2] > 3:
                    util.info("당신은 교수님에게 들켰습니다. 당신은 모두가 보는 앞에서 혼났고, 당신의 인기도는 \033[91m10감소\033[94m했습니다.")
                    uitl.alart("TIP. 3초 이내에 폰을 끄세요.")
                else:
                    util.info("당신은 다행이 빨리 폰을 끈 결과, 교수님에게 들킬 뻔 했습니다.")
        else:
            util.info("당신은 절제하는 마음으로 열심히 교수님의 강의를 듣기 시작했습니다..")

        time.sleep(5)
        util.info("당신의 강의는 이제 모두 끝났습니다. 이제 집으로 돌아가도 됩니다.")

        if len(self.arbeit) < 2 and money < 80:
            util.alart("당신은 돈이 없는 나머지 아르바이트를 하기로 결정했습니다. 아르바이트를 하시겠습니까?")

            result = util.gameInput(["네", "아니오"])

            if int(result) == 1:
                util.info("당신은 아르바이트를 하기로 결정했습니다. 무슨 알바를 하시겠습니까?")

                result = util.gameInput(["편의점", "카페", "상하차"])

                if int(result) == 1 and self.arbeit[0] != "편의점":
                    util.info("당신은 편의점 알바를 하기로 결정했습니다.")
                    util.alart("당신은 편의점 면접을 보러 갑니다..")
                    time.sleep(3)

                    if random.randint(1, 3) == 1:
                        util.alart("당신은 극적으로 편의점 알바에 붙었습니다!")
                        util.info("편의점 알바는 가장 쉬운 알바이며 월급은 150만원입니다. 사장님이 다음날부터 나오라고 하시는군요.")
                    else:
                        util.alart("당신은 아쉽게도 편의점 알바에서 탈락했습니다.")
                        util.info("TIP. 다음 날에도 도전할 수 있으니 너무 낙심하지 마세요!")
                else:
                    util.info("앗! 당신은 이미 편의점 알바를 하고있는것 같아요!")
                    util.alart("알바 면접은 다음 날에 도전해주세요.")

                elif int(result) == 2 and self.arbeit[1] != "카페":
                    util.info("당신은 편의점 알바를 하기로 결정했습니다.")
                    util.alart("당신은 편의점 면접을 보러 갑니다..")
                    time.sleep(3)

                    if random.randint(1, 5) == 1:
                        util.alart("당신은 극적으로 카페 알바에 붙었습니다!")
                        util.info("카페 알바는 어려운 알바이며 월급은 180만원입니다. 사장님이 다음날부터 나오라고 하시는군요.")
                    else:
                        util.alart("당신은 아쉽게도 카페 알바에서 탈락했습니다.")
                        util.info("TIP. 다음 날에도 도전할 수 있으니 너무 낙심하지 마세요!")
                else:
                    util.info("앗! 당신은 이미 카페 알바를 하고있는것 같아요!")
                    util.alart("알바 면접은 다음 날에 도전해주세요.")

                elif int(result) == 3:
                    pass # 상하차

    def firstDay(self):
        util.info("이 게임의 주인공인 당신은 어느 때와 다름없이 침대에서 일어납니다. 하지만 오늘은 무언가 다릅니다.")
        util.info("오늘은 드디어 당신이 대학교에 가는 날입니다. 당신은 대학교에 가까운 작은 원룸 월세집을 구했습니다.")
        util.info("당신은 떨리는 마음으로 강의실에 들어갑니다. 사람들은 모두 다 친절해보이고.. 아 이때 교수님이 들어와 출석을 부릅니다. 이만 여기까지 해야겠군요.")

        time.sleep(10)
        util.alart("당신은 이제 드디어 집에 갑니다. 그 전에 당신은 새로운 친구를 하나 사귀었습니다. 만일 누가 물어보면 그 친구는 현수, 최현수")
        util.alart("새로 사귄 친구들이 개강 파티에 같이 가자고 합니다.")
        result = util.gameInput(["간다", "가지 않는다"])
    
        if int(result) == 1:
            util.info("당신은 새로 사귄 친구들과 개강 파티에 간다고 결정했습니다. 친구들은 친절했고 당신이 재미있었기에 인기도는 \033[92m20상승\033[94m하였습니다.")
            self.popularity += 15
            util.info("하지만 당신은 곧 처음 간 큰 파티에 스트레스가 \033[91m15증가\033[94m했습니다.")
            self.stress += 10
        else:
            util.info("당신은 개강 파티에 가지 않기로 결정했습니다. 당신의 인기도는 \033[91m5감소\033[94m하였고, 스트레스는 \033[92m5감소\033[94m하였습니다.")
            self.popularity -= 5
            util.info("하지만 당신은 가지 않은것을 후회하지도 원망하지도 않았습니다. 아직까지는요..")
            self.stress -= 5

        util.alart("이렇게 하루가 흘러갔습니다.")
        time.sleep(10)

game = Game(100, 10, 10, 10, 0)

def printTotal():
    util.alart("오늘 하루의 일과입니다.")
    print()
    print(f"\033[96m[ 정보 ] : 돈 : {game.money}\033[90m")
    print(f"\033[96m[ 정보 ] : 스트레스 : {game.stress}\033[90m")
    print(f"\033[96m[ 정보 ] : 더러움 : {game.dirty}\033[90m")
    print(f"\033[96m[ 정보 ] : 인기도 : {game.popularity}\033[90m")
    print(f"\033[96m[ 정보 ] : 아르바이트 : {game.arbeit}개\033[90m")
    util.gameInput(["다음 날"])

def gamePlay():
    game.firstDay()
    printTotal()

    while True:
        pass # 클래스로 일반적인 날의 게임 구문

if int(result) == 1:
    util.clear()
    gamePlay()

elif int(result) == 2:
    util.alart("게임을 종료합니다!")
    exit()

elif int(result) == 3:
    util.clear()
    util.alart("2023 전국 청소년 GAME 코딩대회 출품작으로 개발될 예정이였지만 부득이하게 대회를 취소하게 되어 버려진 비운의 작품입니다. 이 게임은 파이썬으로 작성되었으며, 기본 내장 라이브러리와 직접 만든 내부 라이브러리를 사용하였습니다. 윈도우 환경에서 원활하게 돌아갑니다. 타 환경에서는 작동은 합니다만, 사실상 윈도우 전용입니다. 이 게임을 만들때 아이디어는 4년전 망상으로만 구상했던 게임의 아이디어를 실제로 만든 것이라 더 애착이 갑니다. 게임은 게임이라고 할것도 없이 보잘것 없을정도로 심심하나 열심히 만들었습니다.")
    result = None
    while result == None:
        util.gameInput(["나가기"])
        exit()
