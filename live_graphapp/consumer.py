from channels.generic.websocket import AsyncWebsocketConsumer
import json
from random import randint
from asyncio import sleep
class GraphConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Called on connection.
        # To accept the connection call:
        await self.accept()
        print('Channel connected')
        for i in range(1000):
            await self.send(json.dumps({"value":randint(-20,20)}))
            await sleep(1)
