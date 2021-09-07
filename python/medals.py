medal_results = [
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


def create_medal_table(results):
    # Use the results object above to create a medal table
    # The winner gets 3 points, second place 2 points and third place 1 point
    if not isinstance(results, list):
        return "the input must be a list of dictionaries"
    result_country = {}
    BRONZE_POINT = 1
    SILVER_POINTS = 2
    GOLD_POINTS = 3
    for x in results:
        for key, value in x.items():
            if key == "podium":
                for y in value:
                    country_name = y.split(".")[1]
                    country_position = int(y.split(".")[0])
                    if country_position == 1:
                        if country_name in result_country:
                            result_country[country_name] += GOLD_POINTS
                        else:
                            result_country[country_name] = GOLD_POINTS
                    elif country_position == 2:
                        if country_name in result_country:
                            result_country[country_name] += SILVER_POINTS
                        else:
                            result_country[country_name] = SILVER_POINTS
                    elif country_position == 3:
                        if country_name in result_country:
                            result_country[country_name] += BRONZE_POINT
                        else:
                            result_country[country_name] = BRONZE_POINT
                    else:
                        return "podium must be maximum 3 countries"
    return result_country


create_medal_table(medal_results)


def test_function():
    # This it the test function, please don't change me
    medal_table = create_medal_table(medal_results)
    expected_table = {
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
    assert medal_table == expected_table
