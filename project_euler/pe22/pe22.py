import json
import string

with open('pe22_names.json') as nfile:
    names = json.load(nfile)
    
names.sort()
    
sum_scores = 0
    
for i in range(len(names)):
    score = 0
    
    for c in names[i]:
        score += ord(c) - ord('A') + 1
    
    score *= i + 1
    sum_scores += score
    
    
print(sum_scores)
print(names[936:940])
print(len(names))
