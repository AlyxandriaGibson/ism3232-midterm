# business_rules.py
# Author: Alyxandria Gibson

GUESTS_TIER_LOW = 25
GUESTS_TIER_HIGH = 100
STANDARD_DISCOUNT = 0.05
NONPROFIT_DISCOUNT = 0.12
NO_DISCOUNT = 0.0
SERVICE_FEE_THRESHOLD = 500.00
SERVICE_FEE = 75.00
MANAGER_SIGNOFF_THRESHOLD = 2500.00
SECOND_CHEF_GUEST_THRESHOLD = 80
SECOND_CHEF_TOTAL_THRESHOLD = 3000.00


def calculate_food_cost(guest_price: float, guests: int) -> float:
    """Calculate the food cost before any discount."""
    return guest_price * guests


def get_event_discount(guests: int, nonprofit: bool = False) -> float:
    """Return the discount rate as a decimal."""
    if guests < GUESTS_TIER_LOW:
        return NO_DISCOUNT
    elif guests >= GUESTS_TIER_HIGH and nonprofit:
        return NONPROFIT_DISCOUNT
    else:
        return STANDARD_DISCOUNT


def calculate_event_total(
    guest_price: float, guests: int, nonprofit: bool = False
) -> float:
    """Return the total cost for one event including any discounts and service fees."""
    food_cost = calculate_food_cost(guest_price, guests)
    discount = get_event_discount(guests, nonprofit)
    discounted_cost = food_cost * (1 - discount)
    if discounted_cost <= SERVICE_FEE_THRESHOLD:
        return discounted_cost + SERVICE_FEE
    return discounted_cost


def needs_signoff(total: float) -> bool:
    """Return True if the event total requires a manager's sign-off."""
    return total > MANAGER_SIGNOFF_THRESHOLD


def needs_second_chef(guests: int, total: float) -> bool:
    """Return True when the event needs a second chef."""
    return guests > SECOND_CHEF_GUEST_THRESHOLD or total >= SECOND_CHEF_TOTAL_THRESHOLD


def total_booked(events: list) -> float:
    """Calculate sum of total events for every event in the list."""
    Total = 0.0
    for event in events:
        Total += calculate_event_total(
            event["guest_price"], event["guests"], event.get("nonprofit", False)
        )
        return Total


def largest_event(events: list) -> str:
    """Return the client of the event with the largest event total."""
    largest_client = ""
    largest_total = 0.0
    for event in events:
        event_total = calculate_event_total(
            event["guest_price"], event["guests"], event.get("nonprofit", False)
        )
        if event_total > largest_total or largest_client == "":
            largest_total = event_total
            largest_client = event["client"]
    return largest_client


def format_event_line(
    client: str, total: float, signoff: bool, second_chef: bool
) -> str:
    """Returns one line of the report."""
    signoff_str = "yes" if signoff else "no"
    chef_str = "yes" if second_chef else "no"
    return f"{client}: ${total:.2f} | sign-off: {signoff_str} | second chef: {chef_str}"
