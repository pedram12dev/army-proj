def determine_disability_level(score):
    if score >= 0 and score <= 4:
        return "no disability"
    elif score >= 5 and score <= 14:
        return "mid disability"
    elif score >= 15 and score <= 24:
        return "moderate disability"
    elif score >= 25 and score <= 34:
        return "severe disability"
    elif score >= 35 and score <= 50:
        return "completely disability"


# score = 27
# result = determine_disability_level(score)
# print(result)


def determine_stress_level(score):
    if score >= 0 and score <= 14:
        return "normal"
    elif score >= 15 and score <= 18:
        return "mild"
    elif score >= 19 and score <= 25:
        return "moderate"
    elif score >= 26 and score <= 33:
        return "severe"
    elif score > 33:
        return "extremely severe"


# score = 28
# result = determine_stress_level(score)
# print(result)

def determine_anxiety_level(score):
    if score >= 0 and score <= 7:
        return "normal"
    elif score >= 8 and score <= 9:
        return "mild"
    elif score >= 10 and score <= 14:
        return "moderate"
    elif score >= 15 and score <= 19:
        return "severe"
    elif score >= 20:
        return "extremely severe"


# score = 12
# result = determine_anxiety_level(score)
# print(result)

def determine_depression_level(score):
    if score >= 0 and score <= 9:
        return "normal"
    elif score >= 10 and score <= 13:
        return "mild"
    elif score >= 14 and score <= 20:
        return "moderate"
    elif score >= 21 and score <= 27:
        return "severe"
    elif score >= 28:
        return "extremely severe"

# score = 29
# result = determine_depression_level(score)
# print(result)
