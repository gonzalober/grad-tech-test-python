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


@pytest.fixture
def mock_four_country_data():
    return [
        {
            "sport": "cycling",
            "podium": ["1.China", "2.Germany", "3.ROC", "4.Russia"]
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


def test_create_medal_table_error_for_more_than_three_countries(mock_four_country_data):
    """""
    Where more than 3 countries are given in the podium
    then returns an error that the maximum is three countries in the podium
    """""
    res = create_medal_table(mock_four_country_data)
    assert res == "podium must be maximum 3 countries"


def test_create_medal_table_error_if_input_is_not_list():
    """""
    Where input is not a list type object
    """""
    mock_type_error_input_country_data = "I am not a list type"
    res = create_medal_table(mock_type_error_input_country_data)
    assert res == "the input must be a list of dictionaries"
