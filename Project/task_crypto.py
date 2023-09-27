from tradingview_ta import TA_Handler, Interval, Recommendation



response = TA_Handler(
    symbol='BTCUSDT',                 #торговая пара
    screener="crypto",
    exchange="BINANCE",
    interval=Interval.INTERVAL_5_MINUTES
)

print(response.get_analysis().summary)