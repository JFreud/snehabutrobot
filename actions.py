import discord

async def status_task():
    while True:
        await test_bot.change_presence(...)
        await asyncio.sleep(10)
        await test_bot.change_presence(...)
        await asyncio.sleep(10)