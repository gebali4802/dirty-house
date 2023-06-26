#-*-coding: utf-8-*-

import time
import os

def info(msg):
    print()
    print(f"\033[94m[ 정보 ] : {msg}\033[90m")

def alart(msg, type="game"):
    if type == "game":
        print()
        print(f"\033[93m[ 알림 ] : {msg}\033[90m")
    elif "system":
        print()
        print(f"\033[91m[ 경고 ]  : {msg}\033[90m")

def stop(sec):
    time.sleep(sec)

def clear():
    for i in ["clear", "cls"]:
        os.system(i)

def gameExit(msg):
    alart(f"게임에 충돌이 나 게임을 강제로 종료합니다!\n이유: {msg}", "system")
    time.sleep(3)
    exit()

def gameInput(option, result=None):
    while result == None:
        print()
        local = 1
        while local <= len(option):
            print(f"\033[92m[ {local} ] : {option[local-1]}\033[90m")
            local += 1
        print()
        result = input("\033[94m[ 선택 ] : \033[90m")
        try:
            if not 0 < int(result) <= len(option):
                alart("선택지 선택을 잘못 했습니다!")
                result = None
            else:
                return result
        except ValueError:
            alart("선택지 선택을 잘못 했습니다!")
            result = None