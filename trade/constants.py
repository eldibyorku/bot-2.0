# import re
# import time
# # from trade_order import TradeOrder
LEAGUE = "Standard"
LOG_FILE = "/Users/ahmedel-dib/Library/Caches/com.GGG.PathOfExile/Logs/Client.txt"

line = """2024/04/12 12:41:05 3543082026 d06169ea [INFO Client 74272] @From <asf> AsdaBloodMine: Hi, I would like to buy your Foe Cut, Viridian Jewel listed for 1 divine in Standard (stash tab "~b/o 1 divine"; position: left 11, top 15)"""

LOG_REGEX = r'.+\[INFO Client \d+\] (: )?(.+)'
INCOMING_PLAYER_WHISPER_REGEX = r'@From .+'
AFK_REGEX = r'AFK mode is now ON\. Autoreply "This player is AFK\."'
BEST_OFFER_TRADE = r"@From (<.+> )?(.+): Hi, I would like to buy your (.*?)+,? (.*?) listed for (\d+) (.*?) in (.*?) \(stash tab \"(.*?)\"; position: left (\d+), top (\d+)\)"
PLAYER_JOINED_AREA_REGEX = '(.+) has joined the area\.'


READY = 'READY'
WAITING_FOR_PLAYER = 'WAITING_FOR_PLAYER'
IN_TRADE = 'IN_TRADE'
CLEANUP = 'CLEANUP'

PLAYER_DID_NOT_JOIN = 'PLAYER_DID_NOT_JOIN'
PLAYER_DID_NOT_JOIN_RETRY = 'PLAYER_DID_NOT_JOIN_RETRY'
CURRENCY_FOR_CURRENCY = 'CURRENCY_FOR_CURRENCY'
MESSAGE_RECEIVED = 'MESSAGE_RECEIVED'
PLAYER_JOINED_AREA = 'PLAYER_JOINED_AREA'
TRADE_ACCEPTED = 'TRADE_ACCEPTED'
TRADE_CANCELLED = 'TRADE_CANCELLED'
CURSOR_CLEAN = 'CURSOR_CLEAN'
CURSOR_CURRENCY = 'CURSOR_CURRENCY'

DIVINE_RATIO = 300



# log = re.match(LOG_REGEX, line).group(2)
# # print(match1)
# match2 = re.match(INCOMING_PLAYER_WHISPER_REGEX, log)
# # print(match2)
# trade_whisper = re.match(BEST_OFFER_TRADE, log)

# current_trade = TradeOrder(buyer=trade_whisper.group(2),
#                                             item_name=trade_whisper.group(3),
#                                             item_type=trade_whisper.group(4),
#                                             sell_amount=trade_whisper.group(5),
#                                             sell_currency=trade_whisper.group(6),
#                                             tab=trade_whisper.group(8),
#                                             pos_left=trade_whisper.group(9),
#                                             pos_top=trade_whisper.group(10)
#                                                 )
# print(current_trade)
