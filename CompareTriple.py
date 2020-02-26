from array import *

def compareTriplets(a, b):
    index = 0
    score = array('i', [0, 0])
    if(len(a) >= len(b)):
        for x in a:
            if(x > b[index]):
                score[0] = score[0] + 1
            elif(x < b[index]):
                score[1] = score[1] + 1
            index += 1
    else:
        for x in b:
            if(x > a[index]):
                score[0] = score[0] + 1
            elif(x < a[index]):
                score[1] = score[1] + 1
            index += 1
    return score

if __name__ == "__main__":
    computedScore = compareTriplets(array('i',[17, 28, 30]), array('i', [99, 16, 8]))
    print("Alice fez:" + str(computedScore[0]) + " enquanto Bob fez: " + str(computedScore[1]))
