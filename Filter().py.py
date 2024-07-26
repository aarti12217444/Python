marks = [90, 67, 47, 78, 100]

def failing(score):
    return score < 50
result = filter(failing,marks)
print("failing scores:",list(result))