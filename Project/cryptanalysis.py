# https://www.tradingview.com/symbols/BTSUSDT/
# https://python-tradingview-ta.readthedocs.io/en/latest/overview.html
# https://tvdb.brianthe.dev/  TradingView List
# https://mastergroosha.github.io/aiogram-3-guide/quickstart/#hello-world


import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from tradingview_ta import TA_Handler, Interval, Recommendation, Exchange



RECOMMENDATIONS = {
    Recommendation.buy: 'Покупай',
    Recommendation.strong_buy: 'Срочно_покупай',
    Recommendation.sell: 'Продавай',
    Recommendation.strong_sell: 'Срочно_продавай',
    Recommendation.neutral: 'Непонятная ситуация',
    Recommendation.error: 'Ошибка',
}




# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("/start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


    

@dp.message()
async def currency(message: types.Message):
    try:
        response = TA_Handler(
            symbol=message.text,                 #торговая пара
            # symbol='BTCUSDT',
            screener="crypto",
            exchange="BINANCE",
            interval=Interval.INTERVAL_5_MINUTES
        )

        result = response.get_analysis().summary
        await message.answer(result)

        analysis = result.get('RECOMMENDATION', Recommendation.error)
        await message.answer(RECOMMENDATIONS.get(analysis))

    except:
        await message.answer('Некорректный ввод')





# # Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

