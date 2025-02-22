l1=[]
def insertstck(x):
    l1.append(x)
    print(f"Elements of Stack : {l1}")
def popStck():
    l1.pop()
    print(f"Elements of Stack : {l1}")

insertstck(12)
insertstck(13)
insertstck(14)
insertstck(15)
print("\nAfter deletion")
popStck()