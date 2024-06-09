
from trade.constants import READY, MESSAGE_RECEIVED, WAITING_FOR_PLAYER, PLAYER_DID_NOT_JOIN, PLAYER_DID_NOT_JOIN_RETRY, PLAYER_JOINED_AREA, IN_TRADE, TRADE_ACCEPTED, TRADE_CANCELLED, CLEANUP, CURSOR_CLEAN, CURSOR_CURRENCY
from trade.trade_actions import invite_user, leave_party, ignore_player, take_item, execute_trade
from trade.trade_order import TradeOrder


class LogStateMachine:
    def __init__(self):
        self.state = READY

    def on_event(self, action, payload: TradeOrder):
        if self.state == READY:
            if action == MESSAGE_RECEIVED:
                self.trade_order = payload
                invite_user(self.trade_order.buyer)
                self.state = WAITING_FOR_PLAYER
        elif self.state == WAITING_FOR_PLAYER:
            if action == PLAYER_DID_NOT_JOIN:
                leave_party()
            if action == PLAYER_DID_NOT_JOIN_RETRY:
                ignore_player(self.trade_order.buyer)
                self.state = READY
            elif action == PLAYER_JOINED_AREA:
                take_item(self.trade_order)
                trade_currency_for_currency(self.trade_order)
                self.state = IN_TRADE
        elif self.state == IN_TRADE:
            if action == TRADE_ACCEPTED:
                trade_accepted(self.trade_order)
                self.state = READY
            elif action == TRADE_CANCELLED:
                leave_party()
                move_to_stash(self.trade_order.sell_currency, self.trade_order.sell_amount)
                ignore_player(self.trade_order.buyer)
                self.state = READY
        elif self.state == CLEANUP:
            if action == CURSOR_CLEAN:
                self.state = READY
            if action == CURSOR_CURRENCY:
                self.state = READY
