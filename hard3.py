
votes = []
vote = input("Vote (or done): ")
while vote != "done":
    votes.append(vote)
    vote = input("Vote (or done):" )

def count(items, target):
    total = 0
    for i in items:
        if i == target:
            total += 1
    return total
    
who = input("Candidate:")
print(who, "got", count(votes, who), "votes.")