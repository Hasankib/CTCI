from two import LinkedList,Node

ll1 = LinkedList([1,2,3,4,5,4,3,2,1])
ll2 = LinkedList(['a','b','b','a'])

def ispalindrome(link):
    length = link.getlength()
    midnode = length//2
    list1 = []
    x = 1
    tmp = link.head
    while(x <= midnode):
        list1.append(tmp.data)
        tmp = tmp.next 
        x += 1
    
    list2 = list1[::-1]

    if(length//2 == 1):
        tmp = tmp.next 

    y = 0
    
    while(tmp and y < len(list2)):
        if(tmp.data!=list2[y]):
            return False
        tmp = tmp.next
        y += 1
    return True

print(ispalindrome(ll2))