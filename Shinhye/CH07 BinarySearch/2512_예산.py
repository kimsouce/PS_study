n = int(input())
budgets = list(map(int, input().split()))
total_budget = int(input())

# 예산들 중 가장 큰 값 이상으로 상한액이 나오지 않음
start, end = 0, max(budgets)

while start <= end:
    mid = (start+end) // 2  # 상한액
    total = 0
    for budget in budgets:
        # 상한액보다 높은 금액 -> 상한액만큼 더하기
        if budget >= mid:
            total += mid
        else:
            # 상한액보다 낮은 금액 -> 예산만큼 더하기
            total += budget
    if total > total_budget:
        end = mid - 1
    else:
        start = mid + 1
print(end)
