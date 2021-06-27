def manager(houses):
    if houses==1:
        worker()
        return
    elif houses==2:
        worker()
        worker()
        return
    elif houses%2!=0:
        manager(houses//2 +1)
        manager(houses//2)
    else:
        manager(houses//2)
        manager(houses//2)
def worker ():
    name=input()
    print("delevering presents to ",name )
    return;
houses=int(input())
manager(houses)

