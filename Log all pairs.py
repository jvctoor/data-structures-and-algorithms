
boxes = [1, 2, 3, 4]

def logAllPairs():
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            print(f"{boxes[i]}{boxes[j]}")

logAllPairs()
