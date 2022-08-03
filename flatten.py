l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
newl= []
def flatten(l):
    for i in l:
        if isinstance(i, list):
            flatten(i)
        else:
            newl.append(i)
    return newl

flatten(l)
print(newl)

