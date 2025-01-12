import api.fetch as api
import math

config = api.get_settings()

"""
Format your strategies responses as a dict with the values you need.

Example:

response = {
    "buy": True,
    "price": current_candle["open"],
    "amount": config["account"]["baseOrderValue"],
}
"""
def your_strategy(candle):
    if candle["rsi"]<30:
        response={
            "buy": True,
            "amount":config["baseOrderValue"],
            "price":candle["close"],
        }
    else:
        response= {
            "buy":False
        }
    return response
