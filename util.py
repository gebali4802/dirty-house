def info(msg):
    print(f"\033[94m[정보] : {msg}\033[95m")

def warning(msg, type="game"):
    if type == "game":
        print(f"\033[93m[알림] : {msg}\033[95m")
    else:
        print(f"\033[91m[경고]  : {msg}\033[95m")

def inputer(option):
    info("선택지가 나타났습니다!")
    for i in range(len(option)):
        for j in range(option):
            print(f"\033[93m[{i}] : {j}\033[95m")
    return input("\033[93m[선택] : \033[95m")