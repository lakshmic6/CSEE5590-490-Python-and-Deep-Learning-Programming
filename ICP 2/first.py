def new(list):
    w_l=[]
    for n in list:
        w_l.append((len(n),n))
    w_l.sort()
    print(w_l[:])
    print(w_l[-1][1])
new(["php", "deeplearning", "python", "lakshmi"])