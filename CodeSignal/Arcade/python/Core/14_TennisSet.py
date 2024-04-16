'''
two int : score1 and score2
determine if it is possible for a tennis set to be finished with a final score of score1:score2
'''

def solution(score1, score2):
    mins, maxs = min(score1,score2), max(score1, score2)
    return (maxs==6 and mins<5) or (maxs==7 and mins in (5,6))