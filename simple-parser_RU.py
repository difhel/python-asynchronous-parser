'''
Простой асинхронный парсер на Python
Лицензия: MIT
Автор: Марк Фомин
Электронная почта: luring.uliksir@gmail.com
'''

#импортируем нужные модули
import aiohttp
import asyncio

#создаем основную функцию
async def main():
    #создаем асинхронную сессию соединения
    async with aiohttp.ClientSession() as session:
        #делаем GET-запрос с официальной страницы разработчика этого парсера ВКонтакте (вставьте свой url)
        async with session.get("https://vk.com/na_official") as response:
            #выводим код этого запроса
            print("Status:", response.status)
            #выводим content-type
            print("Content-type:", response.headers['content-type'])
            #создаем переменную с ответом сервера
            html = await response.text()
            #и выводим ее
            print("Body:", html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
