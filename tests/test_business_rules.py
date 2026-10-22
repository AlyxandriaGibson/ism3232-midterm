from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    get_event_discount,
)


def test_calculate_food_cost():
    assert round(calculate_food_cost(18.00, 20), 2) == 360.00


def test_calculate_food_costs_zero_guests():
    assert round(calculate_food_cost(18.00, 0), 2) == 0.00


def test_discount_below_25_guests():
    assert get_event_discount(24) == 0.00


def test_discount_at_25_guests():
    assert get_event_discount(25) == 0.05


def test_discount_at_99_guests():
    assert get_event_discount(99) == 0.05


def test_discount_at_100_guests():
    assert get_event_discount(100) == 0.05


def test_nonprofit_gets_12_percent_discount():
    assert get_event_discount(100, nonprofit=True) == 0.12


def test_nonprofit_changes_discount():
    assert get_event_discount(100, nonprofit=True) != get_event_discount(100)


def test_event_total_no_discount():
    assert round(calculate_event_total(18.00, 20), 2) == 435.00


def test_event_total_nonprofit_discount():
    assert round(calculate_event_total(22.00, 40, True), 2) == 836.00


def test_service_fee_at_500_discount_cost():
    assert round(calculate_event_total(25.00, 20), 2) == 575.00


def test_no_service_fee_above_500_discount_cost():
    assert round(calculate_event_total(25.05, 20), 2) == 501.00
