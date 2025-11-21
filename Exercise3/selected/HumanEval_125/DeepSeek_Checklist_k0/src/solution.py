def split_words(txt):
    if " " in txt:
        return txt.split()

    if "," in txt:
        return txt.split(",")

    # count lowercase letters whose position is odd
    return sum(
        1 for c in txt
        if c.islower() and ((ord(c) - ord('a')) % 2 == 1)
    )
