"""EX06 is good practice for data manipulation and organization."""
__author__ = "730402747"


def invert(dictt: dict[str, str]) -> dict[str, str]:
    """This invers the values given to give a new dictionary."""
    final = dict()
    for x in dictt:
        if dictt[x] in final:
            raise KeyError("KeyError: Duplicate")
        final[dictt[x]] = x
    return final


def favorite_color(namesColors: dict[str, str]) -> str:
    """Figures out what the favorite color is based on the dict."""
    count: dict[str, int] = {}
    for x in namesColors:
        if namesColors[x] in count:
            count[namesColors[x]] = count[namesColors[x]] + 1
        else:
            count[namesColors[x]] = 1
    pop: int = 0
    mostPop: str = ""
    for x in count:
        if count[x] == pop:
            mostPop = "purple"
        if count[x] > pop:
            pop = count[x]
            mostPop = x
    return mostPop


def count(val: list[str]) -> dict[str, int]:
    """This counts stuff."""
    final: dict[str, int] = dict()
    for x in val:
        if x in final:
            final[x] += 1
        else:
            final[x] = 1
    return final


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """This takes stringd and ordres them based on first letter."""
    final: dict[str, list[str]] = dict()
    word: bool = True
    for word in words:
        wordL = word.lower()
        if len(wordL) >= 1:
            if wordL[0] in final: 
                final[wordL[0]].append(str(word))
            else:
                final[wordL[0]] = [word]
        else:
            word = False
    if word is False:
        return "Error: One item is empty"
    else:
        return final


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """This updates the attendence log when given the prior dict and new date one day and student at a time."""
    if day in attendance_log:
        if student not in attendance_log[day]:
            attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]
    return attendance_log