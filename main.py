import aiohttp, asyncio

class Massban:

    def __init__(self):
      self.token = input("Token -> ")
      self.guild = input("Guild -> ")
      self.headers = {"Authorization" : f"Bot {self.token}"}
      self.users = open("users.txt").read().splitlines()

    def request_sender(self, session):
      tasks = []
      for user in self.users:
        tasks.append(asyncio.create_task(session.put(f"https://discord.com/api/v9/guilds/{self.guild}/bans/{user}")))
      return tasks

    async def gather_tasks(self):
      async with aiohttp.ClientSession(headers = self.headers) as session:
        tasks = self.request_sender(session)
        await asyncio.gather(*tasks)

if __name__ == "__main__":
  massban = Massban()
  asyncio.run(massban.gather_tasks())
