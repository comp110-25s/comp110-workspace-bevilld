"""Our third coding exercise"""

__author__: str = "730509911"


def invert(invertee: dict[str, str]) -> dict[str, str]:
    inverted: dict[str, str] = {}
    for i in invertee:
        inverted[invertee[i]] = i
    if len(invertee) != len(inverted):
        raise KeyError("Values must not repeat!")
    return inverted


def count(countee: list[str]) -> dict[str, int]:
    counted: dict[str, int] = {}
    idx: int = 0
    while idx < len(countee):
        if countee[idx] in counted:
            counted[countee[idx]] += 1
            idx += 1
        else:
            counted[countee[idx]] = 1
            idx += 1
    return counted


def favorite_color(colors: dict[str, str]) -> str:
    clean: list[str] = []
    max: int = 0
    word: str = ""
    for i in colors:
        clean.append(colors[i])
    counted: dict[str, int] = count(clean)
    for n in counted:
        if counted[n] > max:
            max = counted[n]
            word = n
    return word


def bin_len(words: list[str]) -> dict[int, set[str]]:
    idx: int = 0
    binned: dict[int, set[str]] = {}
    while idx < len(words):
        word_len = len(words[idx])
        if word_len not in binned:
            binned[word_len] = set()
        binned[word_len].add(words[idx])
        idx += 1
    return binned


print(favorite_color({"Howard": "red", "Chuck": "blue", "Saul": "blue"}))
