from recommendation import rating
from math import sqrt

def euclidiana(base, user1, user2):
    movies = {}
    for item in base[user1]:
       if item in base[user2]: movies[item] = 1

    if len(movies) == 0: return 0
    soma = sum([pow(base[user1][item] - base[user2][item], 2)
                for item in base[user1] if item in base[user2]])
    return 1/(1 + sqrt(soma))

def getSimilar(base, user):
    similar = [(euclidiana(base, user, other), other)
                    for other in base if other != user]
    similar.sort()
    similar.reverse()
    return similar[0:30]

result = getSimilar(rating, 'Ana')
print(result)