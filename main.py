import aiohttp, asyncio

class Massban:

    def __init__(self):
      self.token = input("Token -> ")
      self.guild = input("Guild -> ")
      self.headers = {"Authorization" : f"Bot {self.token}"}
      self.users = open("users.txt").read().splitlines()

    def request_sender(self):
      tasks = []
      for user in self.users:
        tasks.append(asyncio.create_task(aiohttp.ClientSession(headers = self.headers).put(f"https://discord.com/api/v9/guilds/{self.guild}/bans/{user}")))
      return tasks

    async def gather_tasks(self):
      tasks = self.request_sender()
      await asyncio.gather(*tasks)

if __name__ == "__main__":
  massban = Massban()
  asyncio.run(massban.gather_tasks())
