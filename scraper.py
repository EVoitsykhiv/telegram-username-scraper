import os
from telethon.sync import TelegramClient
import csv

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
group = os.getenv("GROUP")

if not api_id or not api_hash or not group:
    raise ValueError("Missing API_ID, API_HASH or GROUP environment variables")

client = TelegramClient("session", api_id, api_hash)

client.start()

users = []

for user in client.iter_participants(group):
    if user.username:
        users.append([user.username, user.id])

with open("users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["username", "id"])
    writer.writerows(users)

print("Saved users to users.csv")

client.disconnect()
