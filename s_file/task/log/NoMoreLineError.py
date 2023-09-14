class NoMoreLineError(Exception):
    def __str__(self):
        return "더 이상 불러올 로그기록이 없습니다."
