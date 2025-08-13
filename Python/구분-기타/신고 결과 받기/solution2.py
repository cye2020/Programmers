class User:
    def __init__(self, id) -> None:
        self.id = id  # 유저 아이디
        self.report = set()  # 자신이 신고한 유저
        self.reported = set()  # 자신을 신고한 유저

    def ban_check(self, k):  # ban 당했는지 확인
        if len(self.reported) >= k:
            return True
        else:
            return False
    
    def email_check(self, k):
        email = 0
        for user in self.report:
            if user.ban_check(k):
                email += 1
        return email

        
def reports(user1: User, user2: User):
    user1.report.add(user2)
    user2.reported.add(user1)

def solution(id_list, report, k):
    report = set(report)
    users = {id: User(id) for id in id_list}
    for r in report:
        user1, user2 = map(lambda x: users[x], r.split())
        reports(user1, user2)
    
    answer = list(map(lambda i: users[i].email_check(k), id_list))
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2

print(solution(id_list, report, k))