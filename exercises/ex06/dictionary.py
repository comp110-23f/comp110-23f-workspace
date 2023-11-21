"""Dictionary Exercise!"""

__author__ = "730664874"


def invert(orig_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of an inputted dictionary."""
    inverted_dict: dict[str, str] = dict()
    for key in orig_dict:
        if orig_dict[key] in inverted_dict:
            raise KeyError("The values of your dictionary are not unique!")
        else:
            inverted_dict[orig_dict[key]] = key
    return inverted_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Returns the color that occurs most frequently in the inputted dictionary."""
    freq_dict: dict[str, int] = dict()
    max_freq: int = 0
    most_popular_color: str = ""
    for name in color_dict:
        if (color_dict[name] in freq_dict):
            freq_dict[color_dict[name]] += 1
        else:
            freq_dict[color_dict[name]] = 1
    for color in freq_dict:
        if (freq_dict[color] > max_freq):
            max_freq = freq_dict[color]
            most_popular_color = color
    return most_popular_color


def count(str_list: list[str]) -> dict[str, int]:
    """Returns a dictionary where the keys are the values of str_list and the values are their frequency in the list."""
    count_dict: dict[str, int] = dict()
    for item in str_list:
        if (item in count_dict):
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary where each value is a letter and each value is a list of words from word_list that start with that letter."""
    alpha_dict: dict[str, list[str]] = dict()
    for word in word_list:
        lowered_word: str = word.lower()
        if (lowered_word[0] in alpha_dict):
            alpha_dict[lowered_word[0]].append(word)
        else:
            alpha_dict[lowered_word[0]] = [word]
    return alpha_dict


def update_attendance(attendence_dict: dict[str, list[str]], day_of_week: str, student: str) -> dict[str, list[str]]:
    """Returns updated attendence_dict with the student in attendence of a certain day of the week."""
    if ((day_of_week in attendence_dict) and (student not in attendence_dict[day_of_week])):
        attendence_dict[day_of_week].append(student)
    elif (day_of_week not in attendence_dict):
        attendence_dict[day_of_week] = [student]
    return attendence_dict