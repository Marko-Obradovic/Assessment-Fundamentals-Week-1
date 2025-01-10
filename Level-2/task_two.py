"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []


def add_to_basket(item: dict) -> list:
    item["price"] = round(item["price"], 2)
    basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    if not basket:
        return "Basket is empty"

    costs = [price["price"] for price in basket]
    total = round(sum(costs), 2)
    format_total = f"Total: £{total:.2f}"

    print(basket)

    receipt = []
    item_appearance_count = {}
    item_appearance_tracking = {}
    for item in basket:
        if item['price'] != "Free":
            if item['name'] not in item_appearance_count:
                item_appearance_count[item["name"]] = 1
            else:
                item_appearance_count[item["name"]] += 1

            formatted_item = ''.join(str(f"{item['name']} x {item_appearance_count[item["name"]]} - £{item["price"]:.2f}"))

            if item['name'] in item_appearance_tracking:
                receipt.remove(item_appearance_tracking[item["name"]])

            receipt.append(formatted_item)

            item_appearance_tracking[item["name"]] = formatted_item
        else:
            receipt.append(''.join(str(f"{item['name']} - Free")))

    receipt.append(format_total)
    format_receipt = '\n'.join(receipt)
    return format_receipt


if __name__ == "__main__":
    item1 = {'name': 'Apple', 'price': 0.5}
    item2 = {'name': 'Toffee', 'price': 0.3}
    add_to_basket(item1)
    add_to_basket(item1)
    add_to_basket(item1)
    add_to_basket(item2)
    add_to_basket(item2)
    print(generate_receipt(basket))
