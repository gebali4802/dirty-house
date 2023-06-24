import time

def info(msg):
    print(f"\033[94m[ 정보 ] : {msg}\033[90m")

def warning(msg, type="game"):
    if type == "game":
        print(f"\033[93m[ 알림 ] : {msg}\033[90m")
    elif "system":
        print(f"\033[91m[ 경고 ]  : {msg}\033[90m")

def gameExit(msg):
    warning(f"게임에 충돌이 나 게임을 강제로 종료합니다!\n이유: {msg}", "system")
    time.sleep(3)
    exit()

def gameInput(option):
    info("선택지가 나타났습니다!")
    local = 1
    while local <= len(option):
        print(f"\033[92m[ {local} ] : {option[local-1]}\033[90m")
        local += 1
    result = input("\033[94m[ 선택 ] : \033[90m")
    for i in range(len(option)):
        if i+1 != result:
            warning("선택지를 잘못 고른것 같아요!")
            return None