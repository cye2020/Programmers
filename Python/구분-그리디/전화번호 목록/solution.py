def solution(phone_book):
    phone_book = sorted(phone_book)
    cur = 0
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith(phone_book[cur]):
            return False
        cur+=1
    return True