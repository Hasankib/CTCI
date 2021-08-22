from two import LinkedList,Node

ll = LinkedList([3,5,8,5,10,2,1])
tmp = ll.head


while(tmp):
    print(tmp.data)
    tmp = tmp.next
    
    

def partition(link,part):
    list2 = []
    list3 = []
    tmp = link.head
    while(tmp):
        if(tmp.data<part):
            list2.append(tmp.data)
        else:
            list3.append(tmp.data)
        tmp = tmp.next
    ll2 = LinkedList(list2)
    ll3 = LinkedList(list3)
    tmp = ll2.head
    while(tmp.next):
        tmp = tmp.next
    tmp.next = ll3.head
    
    tmp = ll2.head
    print(ll2.head.data)
    while(tmp):
        print(tmp.data)
        tmp = tmp.next

partition(ll,5)