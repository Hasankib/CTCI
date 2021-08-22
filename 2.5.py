from two import LinkedList,Node



ll1 = LinkedList([7,1,6])
ll2 = LinkedList([5,9,2])

def simlist(link1,link2):
    string1 = ""
    string2 = ""
    tmp = ll1.head
    while(tmp):
        string1 += str(tmp.data)
        tmp = tmp.next

    tmp = ll2.head
    while(tmp):
        string2 += str(tmp.data)
        tmp = tmp.next
    
    return LinkedList(list((str(int(string1[::-1]) + int(string2[::-1])))[::-1]))

tmp = simlist(ll1,ll2).head

while(tmp):
    print(tmp.data)
    tmp = tmp.next

