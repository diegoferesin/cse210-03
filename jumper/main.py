from socket import create_server
import game.manager as manager
'''Creates an instance of manager object to call the start_game method'''
manager = manager.Manager()
manager.start_game()