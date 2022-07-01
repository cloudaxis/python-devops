from devopslib.randomfruit import fruit

def test_fruit():
    fruit_choice = fruit()
    assert fruit_choice in ["apple", "cherry", "strawberry"]

def test_meal():
    result = meal("beer")
    assert "beer" in result