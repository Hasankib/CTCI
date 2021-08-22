from two import LinkedList,Node

ll = LinkedList(['A','B','C','D','E','C'])

def LoopDetection(circular_List):
    dictionary = {}
    tmp = circular_List.head
    while(tmp):
        print(tmp.data)
        if(tmp in dictionary.keys()):
            return tmp.data
        dictionary[tmp] = 0
        tmp = tmp.next

(LoopDetection(ll))