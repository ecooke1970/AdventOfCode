# Erik Cooke
# Advent of Code 2021 10 part 2

from collections import deque

opens = {'(': ')', '[': ']', '{': '}', '<': '>'}
closes = {')': 3, ']': 57, '}': 1197, '>': 25137}
auto_closes = {')': 1, ']': 2, '}': 3, '>': 4}
stack = deque()
complete_lines = []
autocomplete_scores = []
total = 0
auto_total = 0


def autocomplete_score():
    for code in complete_lines:
        answer = 0
        for l in code:
            answer *= 5
            answer += auto_closes[l]
        autocomplete_scores.append(answer)


if __name__ == "__main__":
    # Open input file
    with open('code_input10.txt') as file:
        for j, line in enumerate(file):
            x = line.strip()
            good = True

            stack.clear()
            for i in x:
                if i in opens:
                    stack.append(i)
                elif i in closes:
                    if i != opens[stack.pop()]:
                        # print("Line: ", j + 1, " Bad character: ", i)
                        total += closes[i]
                        good = False
                        # print("stack = ", stack)
                        break
            if good:
                # print()
                # print("Stack: ", stack)
                complete = ""
                while stack:
                    complete += opens[stack.pop()]
                complete_lines.append(complete)
                # print("Line: ", j + 1)
                # print("stack = ", stack)

    # print("complete Lines: ", complete_lines)
    autocomplete_score()
    autocomplete_scores.sort()
    # print(autocomplete_scores)
    index = (int((len(autocomplete_scores) - 1) / 2))
    print(index)
    print("Answer = ", autocomplete_scores[index])
    # print("Total = ", total)

