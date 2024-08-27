def solution(cards1, cards2, goal):
    index1 = 0
    index2 = 0
    index_goal = 0

    while index_goal < len(goal):
        if index1 < len(cards1) and cards1[index1] == goal[index_goal]:
            index1 += 1
            index_goal += 1
        elif index2 < len(cards2) and cards2[index2] == goal[index_goal]:
            index2 += 1
            index_goal += 1
        else:
            return "No"

    return "Yes"


# 테스트 케이스 1
cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))  # Expected: "Yes"

# 테스트 케이스 2
cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))  # Expected: "No"