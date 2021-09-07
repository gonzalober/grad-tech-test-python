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


def asign_points_to_country(country, medal_result, points):
    if country in medal_result:
        medal_result[country] += points
    else:
        medal_result[country] = points


def convert_string_podium_to_position(podium):
    return int(podium.split(".")[0])


def convert_string_podium_to_country(podium):
    return podium.split(".")[1]


def get_points_by_position(position):
    BRONZE_POINT = 1
    SILVER_POINTS = 2
    GOLD_POINTS = 3
    if position == 1:
        return GOLD_POINTS
    elif position == 2:
        return SILVER_POINTS
    elif position == 3:
        return BRONZE_POINT
    else:
        return None


def create_medal_table(medal_results):
    medals_table_result = {}

    if not isinstance(medal_results, list):
        return "the input must be a list"

    for sport_podium in medal_results:
        podium = sport_podium["podium"]
        for podium_element in podium:
            position = convert_string_podium_to_position(podium_element)
            country = convert_string_podium_to_country(podium_element)
            points = get_points_by_position(position)
            if points == None:
                return "the position does not exist"
            asign_points_to_country(
                country, medals_table_result, points)

    return medals_table_result


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
