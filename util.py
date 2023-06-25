import time
import os

def info(msg):
    print()
    print(f"\033[94m[ 정보 ] : {msg}\033[90m")

def warning(msg, type="game"):
    if type == "game":
        print()
        print(f"\033[93m[ 알림 ] : {msg}\033[90m")
    elif "system":
        print()
        print(f"\033[91m[ 경고 ]  : {msg}\033[90m")

def clear():


def gameExit(msg):
    warning(f"게임에 충돌이 나 게임을 강제로 종료합니다!\n이유: {msg}", "system")
    time.sleep(3)
    exit()

def gameInput(option):
    print()
    local = 1
    while local <= len(option):
        print(f"\033[92m[ {local} ] : {option[local-1]}\033[90m")
        local += 1
    print()
    result = input("\033[94m[ 선택 ] : \033[90m")
    try:
        if not 0 < int(result) <= len(option):
            warning("선택지 선택을 잘못 했습니다!")
            return None
        else:
            return result
    except ValueError:
        warning("선택지 선택을 잘못 했습니다!")
        return None