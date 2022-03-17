# bot.py
import os
from leaderboard import weightClassMen, weightClassesWomen, ARRAY_LEN
from database.db import db

from leaderboard import bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

data = {"Test": ""}

for i in range(ARRAY_LEN):
    db.child("Men").child(str(weightClassMen[i])).set(data)
    db.child("Women").child(str(weightClassesWomen[i])).set(data)

bot.run(TOKEN)
