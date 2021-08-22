from two import LinkedList,Node

ll = LinkedList([1,2,3,4,5])
print(ll.head.next.data)

def kthtolast(k,link):
    c = link.getlength()
    d = c - k
    x = 0
    tmp = link.head
    while(x != d):
        tmp = tmp.next
        x+=1
    return tmp.data

ll = LinkedList([1,2,3,4,5])
print(kthtolast(2,ll))