import asyncio
import json
import websockets

REFRESH_RATE = 1 / 2


class WebSocketsClient:
    def __init__(self, uri, gameInfo):
        self.uri = uri
        self.gameInfo = gameInfo

    async def handler(self):
        async with websockets.connect(self.uri) as websocket:
            await self.authenticate(websocket, 'SyntaxError')

            while True:
                await self.update(websocket, self.gameInfo.read())

                greeting = await websocket.recv()
                print(f"< {greeting}")

                await asyncio.sleep(REFRESH_RATE)

    async def authenticate(self, websocket, identifier):
        await self.send(websocket, 'INIT', identifier)

    async def update(self, websocket, data):
        await self.send(websocket, 'UPDATE', data)

    async def send(self, websocket, packet_type, payload):
        packet = {
            'type': packet_type,
            'payload': payload,
        }

        await websocket.send(json.dumps(packet))



    def run(self):
        asyncio.get_event_loop().run_until_complete(self.handler())
