import pytest
from medals import create_medal_table


@pytest.fixture
def mock_one_country_data():
    return [
        {
            "sport": "cycling",
            "podium": ["1.USA"]
        }
    ]


@pytest.fixture
def mock_three_country_data():
    return [
        {
            "sport": "cycling",
            "podium": ["1.China", "2.Germany", "3.ROC"]
        }
    ]


def test_create_medal_table_for_one_country(mock_one_country_data):
    """""
    Given a sport where only 1 country is in the podium
    when calculating the medals
    then returns the medales for that country
    """""
    result = create_medal_table(mock_one_country_data)
    assert result == {"USA": 3}


def test_create_medal_table_for_three_countries(mock_three_country_data):
    """""
    Given a sport where three countries are in the podium
    when calculating the medals
    then returns the medales each of them
    """""
    res = create_medal_table(mock_three_country_data)
    assert res == {"China": 3, "Germany": 2, "ROC": 1}
