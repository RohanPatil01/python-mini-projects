import streamlit as st
def calculate_flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    combined_length = len(name1) + len(name2)
    flames_order = ['Friends', 'Lovers', 'Affectionate', 'Marriage', 'Enemies', 'Siblings']

    while len(flames_order) > 1:
        index = (combined_length % len(flames_order)) - 1

        if index >= 0:
            right = flames_order[index + 1:]
            left = flames_order[:index]
            flames_order = right + left
        else:
            flames_order = flames_order[:-1]

    return flames_order[0]


def main():
    st.title("FLAMES Game")
    st.write("Discover the relationship between two names using the FLAMES algorithm!")

    name1 = st.text_input("Enter the first name:")
    name2 = st.text_input("Enter the second name:")

    if st.button("Calculate"):
        if name1 and name2:
            relationship = calculate_flames(name1, name2)
            st.success(f"The relationship between {name1.capitalize()} and {name2.capitalize()} will end in {relationship}!")
        else:
            st.error("Please enter both names.")


if __name__ == "__main__":
    main()
