
def testRBlist():
    import random
    print "--- Testing RBList ---"
    print "    Basic tests..."

    initList = [5,3,6,7,2,4,21,8,99,32,23]
    rbList = RBList (initList)
    initList.sort()
    assert rbList.values() == initList
    initList.reverse()
    assert rbList.reverseValues() == initList
    #
    rbList = RBList ([0,1,2,3,4,5,6,7,8,9])
    for i in range(10):
        assert i == rbList.index (i)

    # remove odd values
    for i in range (1,10,2):
        rbList.remove (i)
    assert rbList.values() == [0,2,4,6,8]

    # pop tests
    assert rbList.pop() == 8
    assert rbList.values() == [0,2,4,6]
    assert rbList.pop (1) == 2
    assert rbList.values() == [0,4,6]
    assert rbList.pop (0) == 0
    assert rbList.values() == [4,6]

    # Random number insertion test
    rbList = RBList()
    for i in range(5):
        k = random.randrange(10) + 1
        rbList.insert (k)
    print "    Random contents:", rbList

    rbList.insert (0)
    rbList.insert (1)
    rbList.insert (10)

    print "    With 0, 1 and 10:", rbList
    n = rbList.findNode (0)
    print "    Forwards:",
    while n is not None:
        print "(" + str(n) + ")",
        n = rbList.nextNode (n)
    print

    n = rbList.findNode (10)
    print "    Backwards:",
    while n is not None:
        print "(" + str(n) + ")",
        n = rbList.prevNode (n)

    if rbList.nodes() != rbList.nodesByTraversal():
        print "node lists don't match"
    print

def testRBdict():
    import random
    print "--- Testing RBDict ---"

    rbDict = RBDict()
    for i in range(10):
        k = random.randrange(10) + 1
        rbDict[k] = i
    rbDict[1] = 0
    rbDict[2] = "testing..."

    print "    Value at 1", rbDict.get (1, "Default")
    print "    Value at 2", rbDict.get (2, "Default")
    print "    Value at 99", rbDict.get (99, "Default")
    print "    Keys:", rbDict.keys()
    print "    values:", rbDict.values()
    print "    Items:", rbDict.items()

    if rbDict.nodes() != rbDict.nodesByTraversal():
        print "node lists don't match"

    # convert our RBDict to a dictionary-display,
    # evaluate it (creating a dictionary), and build a new RBDict
    # from it in reverse order.
    revDict = RBDict(eval(str(rbDict)),lambda x, y: cmp(y,x))
    print "    " + str(revDict)
    print


if __name__ == "__main__":

    import sys

    if len(sys.argv) <= 1:
        testRBlist()
        testRBdict()
    else:

        from distutils.core import setup, Extension

    sys.exit(0)