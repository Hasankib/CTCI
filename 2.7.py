from two import LinkedList,Node

def intersection(link1,link2):
    if(link2.getlength()>link1.getlength()):
        x = link2.getlength() - link1.getlength()
        tmp = link2.head
        tmp2 = link1.head
    else:
        x = link1.getlength() - link2.getlength()
        tmp = link1.head
        tmp2 = link2.head

    y = 0

    while(y != x):
        tmp = tmp.next
        y += 1
    
    while(tmp):
        if tmp is tmp2:
            return True
        tmp = tmp.next
        tmp2 = tmp2.next
    
    return False

    
    