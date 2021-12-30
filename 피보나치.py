n=int(input("몇 번째 항까지 구할까요? "))
_curr=0
_next=1
i=0
while i<n-1:
    if i==0:
        print(i, end=" ")
    _curr, _next = _next, _curr + _next
    print(_curr,end=" ")
    i=i+1

