from trade.constants import LOG_FILE, LOG_REGEX, INCOMING_PLAYER_WHISPER_REGEX, AFK_REGEX, BEST_OFFER_TRADE, LEAGUE, PLAYER_JOINED_AREA_REGEX
from trade.trade_order import TradeOrder
import pyautogui
import re
import queue
from trade.stash import go_to_item
from trade.trade_actions import verify_whisper, invite_user, execute_trade
import time
# import misc_utils.windowFocus as windowFocus
# from util import invite

class TradeListener():
    def __init__(self):
        self.log_file = open(LOG_FILE, 'r', encoding='utf8')
        self.log_file_player = open(LOG_FILE, 'r', encoding='utf8')
        # readlines() moves the file cursor to the end so we only see newly added chat messages
        self.log_file.readlines()
        self.log_file_player.readlines()
        self.trade_queue = queue.Queue()
    
    def listen(self):
        while True:
            pyautogui.sleep(1)
            line = self.log_file.readline()
            # print(line)
            if line:
                try:
                    log = re.match(LOG_REGEX, line).group(2)

                    if re.match(AFK_REGEX, log):
                        print('Waking the bot up from being afk')
                        # afk_off()
                    elif re.match(INCOMING_PLAYER_WHISPER_REGEX, log):
                        print(f'Incoming offer: {log}')
                        trade_whisper = re.match(BEST_OFFER_TRADE, log)
                        if trade_whisper.group(7) != LEAGUE:
                            print('invalid league')
                            continue
                        current_trade = TradeOrder(buyer=trade_whisper.group(2),
                                                item_name=trade_whisper.group(3),
                                                item_type=trade_whisper.group(4),
                                                sell_amount=int(trade_whisper.group(5)),
                                                sell_currency=trade_whisper.group(6),
                                                tab=trade_whisper.group(8),
                                                pos_left=int(trade_whisper.group(9)),
                                                pos_top=int(trade_whisper.group(10))
                                                    )
                        print(current_trade)
                        time.sleep(5)
                        if verify_whisper(current_trade):
                            invite_user(current_trade.buyer)
                            print(f"trade verified, inviting user: {current_trade.buyer}")
                            time.sleep(1)
                            self.wait_for_buyer_to_join(current_trade.buyer)
                            execute_trade(current_trade)
                        else:
                            print("could not verify trade, waiting for another player message")
                            continue
                except Exception as e:
                        print(e)
                        pass
                
    # def execute_trade(trade_order):
    #     invite(buyer)


    def wait_for_buyer_to_join(self, buyer):
        while True:
                print("waiting for player to joing")
                pyautogui.sleep(1)
                line = self.log_file_player.readline()
                print(line)
                # print(line)
                if line:
                    try:
                        log = re.match(LOG_REGEX, line).group(2)

                        if re.match(PLAYER_JOINED_AREA_REGEX, log):
                            print("matched")
                            player_joined_name = re.match(PLAYER_JOINED_AREA_REGEX, log).group(1)
                            if player_joined_name == buyer:
                                    print(f'{buyer} has joined the area')
                                    return
                    except Exception as e:
                        print(e)
                        pass
 