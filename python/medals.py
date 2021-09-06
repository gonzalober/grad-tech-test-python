medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]


def createMedalTable(results):
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    result_country = {}
    FIRST_POSITION = 1
    SECOND_POSITION = 2
    THIRD_POSITION = 3
    for x in results:
        for key, value in x.items():
            if key == "podium":
                for y in value:
                    country_name = y.split(".")[1]
                    country_position = int(y.split(".")[0])
                    if country_position == FIRST_POSITION:
                        if country_name in result_country:
                            result_country[country_name] += 3
                        else:
                            result_country[country_name] = 3
                    elif country_position == SECOND_POSITION:
                        if country_name in result_country:
                            result_country[country_name] += 2
                        else:
                            result_country[country_name] = 2
                    elif country_position == THIRD_POSITION:
                        if country_name in result_country:
                            result_country[country_name] += 1
                        else:
                            result_country[country_name] = 1
                    else:
                        return
    return result_country


def test_function():
    # This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable
