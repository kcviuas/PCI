from librec.cf import similarity as sim
from librec.cf import userCF

def calculateItemsSimilarityDict(dict2dim, n=10, similarity=sim.sim_pearson):
    result = {}
    trans = userCF.transformDict2dim(dict2dim)

    count = 0
    for i in trans:
        count += 1
        if count %100 ==0:
            print("%d / %d" % (count,len(trans)))
        topSim = sim.topMatch(trans,i,n=n,similarity=similarity)
        result[i] = topSim

    return result


def getRecommendations(dict2dim, itemSimilarityDict, name):
    scores = {}
    for i in dict2dim[name]:
        for (sim,item) in itemSimilarityDict[i]:
            scores.setdefault(item,{"sim":0,"total":0})
            scores[item]["sim"] += sim
            scores[item]["total"] += sim*dict2dim[name][i]

    result = []
    for item in scores:
        if item not in dict2dim[name]:
            result.append((scores[item]["total"]/scores[item]["sim"], item))

    return result




