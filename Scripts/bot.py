from Trading212 import Invest

stockName = "BMW AG"

try:
    trading = Invest("trading14102@trash-mail.com", "trading14102")
    print("Connection established!")

    try:
        trading.buy_stock(stockName, 2)
        print("Buyed " + stockName)
    except Exception:
        print("[Error] by buying stock")
except Exception:
    print("[Error] by establishing connection")
