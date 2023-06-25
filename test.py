import random

class Room:
    def __init__(self, name, description, npc=None, quest=None):
        self.name = name
        self.description = description
        self.npc = npc
        self.quest = quest

class NPC:
    def __init__(self, name, dialogues):
        self.name = name
        self.dialogues = dialogues

class Quest:
    def __init__(self, name, description, completed=False):
        self.name = name
        self.description = description
        self.completed = completed

class Player:
    def __init__(self, name):
        self.name = name
        self.current_room = self.get_starting_room()
        self.inventory = []
        self.quests = []

    def get_starting_room(self):
        starting_rooms = [
            Room("방 1", "어둡고 으스스한 방입니다."),
            Room("방 2", "깨끗하고 환한 방입니다."),
            Room("방 3", "돌로 만들어진 방입니다.")
        ]
        return random.choice(starting_rooms)

    def move(self, direction):
        if direction == "n":
            self.current_room = Room("북쪽으로 이동", "북쪽 방향으로 이동했습니다.")
        elif direction == "s":
            self.current_room = Room("남쪽으로 이동", "남쪽 방향으로 이동했습니다.")
        elif direction == "e":
            self.current_room = Room("동쪽으로 이동", "동쪽 방향으로 이동했습니다.")
        elif direction == "w":
            self.current_room = Room("서쪽으로 이동", "서쪽 방향으로 이동했습니다.")
        else:
            print("잘못된 방향입니다.")

    def talk(self, npc):
        if npc.dialogues:
            print(f"{npc.name}: {random.choice(npc.dialogues)}")
        else:
            print(f"{npc.name}: 대화할 내용이 없습니다.")

    def take_quest(self, quest):
        if quest.completed:
            print("이미 완료된 퀘스트입니다.")
        elif quest in self.quests:
            print("이미 퀘스트를 수행 중입니다.")
        else:
            self.quests.append(quest)
            print(f"{quest.name} 퀘스트를 받았습니다!")

    def complete_quest(self, quest):
        if quest.completed:
            print("이미 완료된 퀘스트입니다.")
        elif quest in self.quests:
            quest.completed = True
            self.quests.remove(quest)
            self.inventory.append(quest)
            print(f"{quest.name} 퀘스트를 완료하였습니다!")
        else:
            print("해당 퀘스트를 수행 중이 아닙니다.")

def start_game():
    print("어서오세요! TRPG 스타일의 머드 게임에 오신 것을 환영합니다.")
    print("당신은 어둠의 세계에서 모험을 시작합니다.")

    player_name = input("플레이어 이름을 입력하세요: ")
    player = Player(player_name)

    while True:
        print("\n------------------------------------")
        print("당신은 " + player.current_room.name + "에 있습니다.")
        print(player.current_room.description)

        command = input("무엇을 하시겠습니까? (이동하려면 방향을 입력하세요, 대화하려면 'talk [NPC 이름]', 퀘스트를 받으려면 'take [퀘스트 이름]', 퀘스트를 완료하려면 'complete [퀘스트 이름]', 'q'를 입력하면 게임이 종료됩니다.): ")

        if command == "q":
            print("게임을 종료합니다. 감사합니다!")
            break

        if command.startswith("talk"):
            npc_name = command.split(" ")[1]
            npc = NPC(npc_name, ["안녕하세요!", "무엇을 도와드릴까요?"])
            player.talk(npc)

        elif command.startswith("take"):
            quest_name = command.split(" ")[1]
            quest = Quest(quest_name, "어떤 퀘스트에 대한 설명입니다.")
            player.take_quest(quest)

        elif command.startswith("complete"):
            quest_name = command.split(" ")[1]
            quest = Quest(quest_name, "어떤 퀘스트에 대한 설명입니다.", completed=True)
            player.complete_quest(quest)

        elif command in ["n", "s", "e", "w"]:
            player.move(command)

        else:
            print("잘못된 명령입니다.")

start_game()
