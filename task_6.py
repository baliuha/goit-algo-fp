from typing import Dict, List, Tuple


ITEMS = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items: Dict[str, Dict[str, int]], budget: int) -> Tuple[int, int, List[str]]:
    """
    Selects items to maximize the calorie-to-cost ratio within the budget (greedy approach)
    Args:
        items: Dictionary of items
        budget: Maximum cost allowed
    Returns:
        Tuple: (Total Calories, Remaining Budget, List of Chosen items)
    """
    # the ratio (calories / cost) for each item
    item_list = []
    for name, details in items.items():
        ratio = details['calories'] / details['cost']
        item_list.append({
            "name": name,
            "cost": details['cost'],
            "calories": details['calories'],
            "ratio": ratio
        })

    # sort items by ratio in descending order (highest value first)
    sorted_items = sorted(item_list, key=lambda x: x['ratio'], reverse=True)

    total_calories = 0
    remaining_budget = budget
    chosen_items = []
    for item in sorted_items:
        if item['cost'] <= remaining_budget:
            chosen_items.append(item['name'])
            total_calories += item['calories']
            remaining_budget -= item['cost']

    return total_calories, budget - remaining_budget, chosen_items


def dynamic_programming(items: Dict[str, Dict[str, int]], budget: int) -> Tuple[int, int, List[str]]:
    """
    Finds the optimal set of items to maximize total calories within the budget
    using Dynamic programming aproach
    Args:
        items: Dictionary of items
        budget: Maximum cost allowed
    Returns:
        Tuple: (Total Calories, Remaining Budget, List of Chosen items)
    """
    # convert for easier indexing
    item_names = list(items.keys())
    costs = [items[name]['cost'] for name in item_names]
    calories = [items[name]['calories'] for name in item_names]
    items_num = len(items)

    # create DP table with size
    # dp_table[i][j] stores the max calories using first i items with budget j
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(items_num + 1)]
    for i in range(1, items_num + 1):
        for j in range(1, budget + 1):
            item_cost = costs[i - 1]
            item_calorie = calories[i - 1]

            if item_cost <= j:
                # either include the item or exclude it
                dp_table[i][j] = max(
                    dp_table[i - 1][j],  # exclude
                    item_calorie + dp_table[i - 1][j - item_cost]  # include
                )
            else:
                # item is too expensive
                dp_table[i][j] = dp_table[i - 1][j]

    # backtracking to find chosen items
    chosen_items = []
    j = budget
    total_calories = dp_table[items_num][budget]
    # going backwards from the bottom right corner of the table
    for i in range(items_num, 0, -1):
        # if the value came from the row above, the item was NOT included
        if dp_table[i][j] != dp_table[i - 1][j]:
            item_name = item_names[i - 1]
            chosen_items.append(item_name)
            # current budget minus item's cost to navigate back
            j -= costs[i - 1]

    spent_budget = budget - j

    return total_calories, spent_budget, chosen_items


if __name__ == '__main__':
    my_budget = 100
    print(f"---------- Budget: {my_budget} ----------")
    for k, v in ITEMS.items():
        print(f"{k}: Cost={v['cost']}, Cal={v['calories']}")

    greedy_cal, greedy_spent, greedy_items = greedy_algorithm(ITEMS, my_budget)
    print("---------- Greedy Algorithm ----------")
    print(f"Chosen items: {greedy_items}")
    print(f"Total Calories: {greedy_cal}")
    print(f"Total Cost: {greedy_spent}")

    dp_cal, dp_spent, dp_items = dynamic_programming(ITEMS, my_budget)
    print("---------- Dynamic Programming ----------")
    print(f"Chosen items: {dp_items}")
    print(f"Total Calories: {dp_cal}")
    print(f"Total Cost: {dp_spent}")
