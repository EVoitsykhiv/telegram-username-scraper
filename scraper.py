from telethon.sync import TelegramClient
import csv

api_id = 123456
api_hash = "your_api_hash"

group = "group_username"

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
