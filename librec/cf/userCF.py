from librec.cf import similarity

def getRecommendations(dict2dim, name, n=5, similarity=similarity.sim_pearson):
    items = {}
    for i in dict2dim:
        sim = similarity(dict2dim,name,i)
        if sim < 0:
            continue

        for j in dict2dim[i]:
            items.setdefault(j,{"total":0,"sim":0})
            items[j]["total"] += sim * dict2dim[i][j]
            items[j]["sim"] += sim

    scores = []
    for i in items:
        if i not in dict2dim[name]:
            scores.append((items[i]["total"] / items[i]["sim"], i))

    scores.sort()
    scores.reverse()
    return scores[0:n]


def transformDict2dim(dict2dim):
    result = {}
    for i in dict2dim:
        for j in dict2dim[i]:
            result.setdefault(j,{})
            result[j][i] = dict2dim[i][j]
    return result
