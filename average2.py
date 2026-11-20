scores = []
total = 0
for i in range(5):
    score = int(input("Score:"))
    scores.append(score)
    total += score
    
print("Total:", total)
print("Average:", total / len(scores))

