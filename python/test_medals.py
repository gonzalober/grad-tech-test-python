import pytest
from medals import createMedalTable


@pytest.fixture
def data():
    pytest.medalResults = [
        {
            "sport": "cycling",
            "podium": ["1.China", "2.Germany", "3.ROC"]
        }
    ]


def test_createMedalTable(data):
    res = createMedalTable(pytest.medalResults)
    assert res == {"China": 3, "Germany": 2, "ROC": 1}
