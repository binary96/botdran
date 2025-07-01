from pyrogram import Client, filters

api_id = 25033102
api_hash = "ae4e5a5400179a141beeaaedb01955a7"
bot_token = "7915517571:AAHGr7D8t3dhH6y5tE5QD6AL_L8Rp55LTsc"

app = Client("dex_trade_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("👋 Welcome to the Dex Trade Bot!\nUse /menu to begin.")

app.run()
