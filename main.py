import time
import argparse

from data.acc.info import GameInfo as ACCGameInfo
from connection.websockets import WebSocketsClient


if __name__ == "__main__":
    gameInfo = ACCGameInfo()

    server = WebSocketsClient("wss://accs.sekhmet.pl", gameInfo)
    server.run()
