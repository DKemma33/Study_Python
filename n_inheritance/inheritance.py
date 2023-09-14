class TV:
    def __init__(self):
        self.power = False
        self.channel = 1
        self.volume = 1

    def display_info(self):
        print("전원: " + str(self.power))
        print("채널: " + str(self.channel))
        print("볼륨: " + str(self.volume))


tv = TV()

tv.power = True
tv.channel = 24
tv.volume = 14

tv.display_info()


class SmartTV(TV):
    def __init__(self):
        # 부모 생성자 호출
        super().__init__()
        self.ip ="192.168.1.1"

    def display_info(self):
        super().display_info()
        print("IP: " + self.ip)


smart_tv = SmartTV()

smart_tv.power = True
smart_tv.channel = 24
smart_tv.volume = 14

smart_tv.display_info()













