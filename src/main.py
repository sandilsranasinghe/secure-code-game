from collections import namedtuple

Order = namedtuple("Order", "id, items")
Item = namedtuple("Item", "type, description, amount, quantity")


def validorder(order: Order):
    net = 0

    print("Test PR")

    for item in order.items:
        if item.type == "payment":
            net += item.amount
        elif item.type == "product":
            net -= item.amount * item.quantity
        elif item.type == "shipping":
            net -= item.amount
        else:
            return "Invalid item type: %s" % item.type

    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)
    else:
        return "Order ID: %s - Full payment received!" % order.id
