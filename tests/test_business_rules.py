from business_rules import (
    calculate_event_total,
    calculate_food_cost,
    get_event_discount,
    needs_second_chef,
    needs_signoff,
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


def test_signoff_over_2500():
    assert needs_signoff(2500.01) is True


def test_signoff_below_2500():
    assert needs_signoff(2499.99) is False


def test_signoff_at_2500():
    assert needs_signoff(2500.00) is False


def test_second_chef_above_80_guests():
    assert needs_second_chef(81, 100.00) is True


def test_no_second_chef_at_80_guests():
    assert needs_second_chef(80, 100.00) is False


def test_second_chef_at_3000_total():
    assert needs_second_chef(80, 3000.00) is True


def test_no_second_chef_below_3000_total():
    assert needs_second_chef(80, 2999.99) is False
