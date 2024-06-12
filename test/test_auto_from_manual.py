import allure


@allure.id("32833")
@allure.title("Ручной тест-кейс")
@allure.label("owner", "allure8")
def test_example():
    with allure.step("Проснуться"):
        pass
    with allure.step("Улыбнуться"):
        assert 1 == 0, 'Проснулся в плохом настроении'
    with allure.step("Потянуться"):
        pass
