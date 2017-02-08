def Hanoi(disks, src, dest, aux):
    if(disks == 0):
        return
    else:
        Hanoi(disks-1, src, aux, dest)
        print("%s -> %s" %(src, dest))
        Hanoi(disks-1, aux, dest, src )

Hanoi(3,1,3,2)
