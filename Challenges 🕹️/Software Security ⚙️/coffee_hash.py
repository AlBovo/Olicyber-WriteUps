from z3 import *
cfhash = "630:624:622:612:609:624:623:610:624:624:567:631:638:639:658:593:546:605:607:585:648:636:635:704:702:687:687:682:629:699:633:639:634:637:578:622:620:617:606:615:568:633:589:587:645:639:653:654:633:634".split(":")
for i in range(len(cfhash)):
    cfhash[i] = int(cfhash[i])
s = Solver()
flag = [Int("flag" + str(i)) for i in range(len(cfhash))]

for i in range(len(cfhash)):
    tot = 0
    for e in range(7):
        tot += flag[(i+e)%len(cfhash)]
    s.add(cfhash[i] == tot)
print(s.check())
m = s.model()
for i in flag:
    print(chr(m[i].as_long()), end="")
print("")
