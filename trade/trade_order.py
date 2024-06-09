from trade.constants import DIVINE_RATIO
class TradeOrder():
    def __init__(self, buyer, item_name, item_type, sell_amount, sell_currency, tab, pos_left, pos_top):
        self.buyer = buyer
        self.item_name = item_name
        self.item_type = item_type
        self.sell_amount = sell_amount
        self.sell_currency = sell_currency
        self.tab = tab
        self.pos_left = pos_left
        self.pos_top = pos_top
        
        if sell_currency == "divine":
            self.total_in_d = sell_amount
        else:
            self.total_in_d = sell_currency / DIVINE_RATIO

    def update_buy_amount(self, amount):
        self.buy_amount = amount

    def __str__(self):
        return (f"Trade Order:\n"
                f"  Buyer: {self.buyer}\n"
                f"  Item Name: {self.item_name}\n"
                f"  Item Type: {self.item_type}\n"
                f"  Sell Amount: {self.sell_amount}\n"
                f"  Sell Currency: {self.sell_currency}\n"
                f"  Tab: {self.tab}\n"
                f"  Position Left: {self.pos_left}\n"
                f"  Position Top: {self.pos_top}")