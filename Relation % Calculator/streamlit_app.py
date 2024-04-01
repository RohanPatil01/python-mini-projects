import streamlit as st

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


def main():
    st.title("Relationship % Calculator Game")
    st.write("Discover the relationship between two names!")

    name1 = st.text_input("Enter the first name:")
    relation = st.text_input("Enter the relation you want to choose:")
    name2 = st.text_input("Enter the second name:")

    if st.button("Calculate"):
        l = list(name1.lower().replace(" ", "") + relation.lower().replace(" ", "") + name2.lower().replace(" ", ""))
        li = {}

        for i in l:
            li[i] = l.count(i)

        lis = list(li.values())
        a = [i for i in lis if i != 1] + [i for i in lis if i == 1]

        if name1 and relation and name2:
            result = check(a)
            st.success(f"{name1} and {name2} have {result}% of relation of {relation}")
        else:
            st.error("Please enter both names.")


if __name__ == "__main__":
    main()
