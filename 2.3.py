from two import LinkedList,Node

ll = LinkedList(['a','b','c','d','e'])
print(ll.head.next.data)

def remover(link,midnode):
    tmp = link.head
    while(tmp.next.data != midnode.data):
        tmp = tmp.next 

    tmp.next = tmp.next.next 

remover(ll,ll.head.next.next)
print(ll.head.next.next.data)