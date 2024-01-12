import logging
import argparse
from pyftg import Gateway
from KickAI import KickAI
from Randman_p1 import Randman_p1
from Randman_p2 import Randman_p2
from DisplayInfo import DisplayInfo

def start_game(port: int):
    gateway = Gateway(port=port)
    character = 'ZEN'
    game_num = 1
    agent1 = Randman_p1()
    agent2 = Randman_p2()
    #agent2 = KickAI()
    gateway.register_ai("Randman_p1", agent1)
    gateway.register_ai("Randman_p2", agent2)
    gateway.run_game([character, character], ["Randman_p1", "Randman_p2"], game_num)
    gateway.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', default='INFO', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])
    parser.add_argument('--port', default=50051, type=int, help='Port used by DareFightingICE')
    args = parser.parse_args()
    logging.basicConfig(level=args.log)
    start_game(args.port)
