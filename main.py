import aiohttp, asyncio, random

class Massban:

    def __init__(self):
      self.token = input("Token -> ")
      self.guild = input("Guild -> ")
      self.headers = {"Authorization" : f"Bot {self.token}"}
      self.members = open("members.txt").read().splitlines()
      self.status_codes = [200, 201, 204]

    async def request_sender(self, session, member):
      async with session.put(f"https://discord.com/api/v{random.randint(8, 9)}/guilds/{self.guild}/bans/{member}", headers = self.headers) as r:
        if r.status in self.status_codes:
          print(f"[{r.status}] -> Banned Member {member}")
        else:
          print(f"[{r.status}] -> Error Banning Member {member}")
        return await r.text()
    
    
    async def fetch_all(self, session):
        tasks = []
        for member in self.members:
            task = asyncio.create_task(self.request_sender(session, member))
            tasks.append(task)
        res = await asyncio.gather(*tasks)
        return res

    async def gather_tasks(self): 
      async with aiohttp.ClientSession(headers = self.headers) as session:
            await self.fetch_all(session)

if __name__ == "__main__":
  massban = Massban()
  asyncio.run(massban.gather_tasks())
