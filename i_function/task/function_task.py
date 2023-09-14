# 조회수
def 수정하기(게시글번호):
    게시글들 = {1: 0, 2: 2, 3: 204, 4: 324}
    게시글들[게시글번호] += 1

def 조회하기(게시글번호):
    게시글들 = {1: 0, 2: 2, 3: 204, 4: 324}
    return 게시글들[게시글번호]

수정하기(1)
조회하기(1)

# def 골막기(축구공):
#     결과 = "공잡음"
#     if 결과 == "미끄러짐":
#         return False
#     if 결과 == "공잡음":
#         return True
#
# result = 골막기("축구공")
# print(result)
#
# def 공칠게(공):
#     data = 2
#     result = None
#     if data == 1:
#         result = "홈런"
#     elif data == 2:
#         result = "파울"
#     else:
#         result = "아웃"
#     return result
#
#
# print(공칠게("야구공"))
#
# def 굽자(제육볶음):
#     후라이팬 = 제육볶음
#     제육볶음 = "요리"
#     return 제육볶음
#
# def 제육볶음만들어(고기):
#     제육볶음 = 고기 + "양파" + "마늘" + "소스"
#     return 제육볶음
#
#
# print(굽자(제육볶음만들어("돼지고기")))
