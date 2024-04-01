name1 = input("Enter your name: ")
relation = input("Enter your relation: ")
name2 = input("Enter second name: ")

l = list(name1.lower().replace(" ", "") + relation.lower().replace(" ", "") + name2.lower().replace(" ", ""))

li = {}
for i in l:
    li[i] = l.count(i)

lis = list(li.values())
a = [i for i in lis if i != 1] + [i for i in lis if i == 1]


def add_ends(a):
    new = []
    while a:
        if len(a) > 1:
            n1 = a[0]
            n2 = a[-1]
            n3 = n1 + n2
            a.remove(n1)
            a.remove(n2)
            if n3 > 9:
                new_n3 = [int(i) for i in list(str(n3))]
                new += new_n3
            else:
                new.append(n3)
        else:
            new.append(a[0])
            a.remove(a[0])
    return check(new)


def check(a):
    a_str = [str(i) for i in a]
    ans = int("".join(a_str))
    if ans <= 100:
        return ans
    else:
        return add_ends(a)


result = check(a)

print(f"{name1} and {name2} have {result}% of relation of {relation}")