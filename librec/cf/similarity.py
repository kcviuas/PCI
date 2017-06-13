from math import sqrt

def sim_euclid(dict2dim, name1, name2):
    '''
    :param dict2dim: two dimension dictionary: dict2dim[name1][name2]=rating
    :param name1: pass
    :param name2: pass
    :return: similarity
    '''
    same = {}
    for item in dict2dim[name1]:
        if item in dict2dim[name2]:
            same[item] = 1

    if len(same) == 0:
        return 0

    sum = 0
    for item in same:
        sum = sum + pow((dict2dim[name1][item] - dict2dim[name2][item]),2)

    sum = sqrt(sum) / len(same)
    return 1 / (1 + sum)


def sim_pearson(dict2dim, name1, name2):
    same = {}
    for item in dict2dim[name1]:
        if item in dict2dim[name2]:
            same[item] = 1

    if same == 0:
        return 0

    avg1 = 0
    avg2 = 0
    for item in same:
        avg1 = avg1 + dict2dim[name1][item]
        avg2 = avg2 + dict2dim[name2][item]

    avg1 = avg1 / len(same)
    avg2 = avg2 / len(same)

    var1 = 0
    var2 = 0
    for item in same:
        var1 = var1 + pow(dict2dim[name1][item] - avg1,2)
        var2 = var2 + pow(dict2dim[name2][item] - avg2,2)

    std1 = sqrt(var1/len(same))
    std2 = sqrt(var2/len(same))

    cov = 0
    for item in same:
        cov = cov + (dict2dim[name1][item] - avg1)*(dict2dim[name2][item] - avg2)

    cov = cov/len(same)

    return cov / (std1*std2)


def topMatch(dict2dim, name, n=5, similarity=sim_pearson):
    '''
    return the top n similarity items/users of name
    :param dict2dim:
    :param name:
    :param n:
    :param similarity:
    :return: list of (score,name)
    '''
    score = []
    for i in dict2dim:
        if i != name:
            score.append((similarity(dict2dim,name,i),i))

    score.sort()
    score.reverse()
    return score[0:n]


