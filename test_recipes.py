# создаем тесты для класса Ingredient

import pytest

def test_ingredient_creation():
    all_ingredients = Ingredient("клубничное мороженое", 4, "шт")
    assert all_ingredients.name == "клубничное мороженое"
    assert all_ingredients.quantity == 4.0
    assert all_ingredients.unit == "шт"

def test_ingredient_str():
    all_ingredients = Ingredient("Мука", 500, "г")
    assert str(all_ingredients) == "Мука: 500.0 г"

def test_ingredient_eq():
    all_ingredients1 = Ingredient("лед", 20, "шт")
    all_ingredients2 = Ingredient("варенье из клубники", 1120, "шт")
    all_ingredients3 = Ingredient("лед", 67, "шт")
    all_ingredients4 = Ingredient("Сахар", 7, "кг")
    assert all_ingredients1 == all_ingredients3
    assert all_ingredients2 != all_ingredients3
    assert all_ingredients1 != all_ingredients4

# создали тест для класса Ingredient и все сделали
