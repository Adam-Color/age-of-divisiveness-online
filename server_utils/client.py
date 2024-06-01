import socket
import logging

logger = logging.getLogger(__name__)

FORMAT = 'utf-8'
HEADER = 200


class Client:
    """
    Client class for application.
    It handles connection to server, sending and getting messages.
    It sends requests as -> <REQUEST>:::.
    Which is afterwards smartly handled by server.
    """

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.available_civilizations = None
        self.current_players_on_server = None
        self.nick = None
        self.players = []
        self.started = False

    def rec_msg(self):
        """
        Listens for messages from server.
        """
        msg_len = self.sock.recv(HEADER).decode(FORMAT)
        if msg_len:
            incoming_msg = self.sock.recv(int(msg_len)).decode(FORMAT)
            logger.debug("rec_msg: %s", incoming_msg)
            return incoming_msg
        return ""

    def send_msg(self, msg):
        """
        Sends requests to server and expects a response.
        """
        self.only_send(msg)
        response = self.rec_msg()
        logger.debug("send_msg: %s", response)
        return response

    def only_send(self, msg):
        """
        Sends requests to the server without expecting a response.
        """
        message = msg.encode(FORMAT)
        message_length = len(message)
        send_length = str(message_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        self.sock.send(send_length)
        self.sock.send(message)
        logger.debug("send_msg_only: %s", message)

    def connect(self, ip, port):
        """
        Connects to the server.
        """
        try:
            self.sock.connect((ip, int(port)))
        except ConnectionRefusedError as e:
            logger.error("Game is not hosted yet. %s", e)
            return 'Game is not hosted yet.'

    def disconnect(self):
        """
        Disconnects from the server.
        """
        self.only_send(f"DISCONNECT:{self.nick}")
        self.sock.shutdown(socket.SHUT_RDWR)

    def die(self):
        """
        Notifies server of defeat.
        """
        msg = f"DEFEAT:{self.nick}"
        self.only_send(msg)
        return self.unexpected_messages(msg)

    def kill(self, player):
        """
        Notifies server of another player's defeat.
        """
        msg = f"DEFEAT:{player}"
        self.only_send(msg)
        return self.unexpected_messages(msg)

    def introduce_yourself(self, chosen_nick, chosen_civ):
        """
        Introduces the client to the server.
        """
        self.nick = chosen_nick
        self.send_msg(f"ADD_NEW_PLAYER:{chosen_nick}:::")
        self.send_msg(f"CHOOSE_CIVILISATION:{chosen_nick}:{chosen_civ}:::")
        self.rec_msg()

    def get_available_civilizations_from_server(self):
        """
        Requests available civilizations from the server.
        """
        self.available_civilizations = self.send_msg("LIST_CIVILIZATIONS:::")
        return self.available_civilizations

    def get_available_civilizations(self):
        """
        Gets available civilizations.
        """
        return self.get_available_civilizations_from_server()

    def get_current_players_from_server(self):
        """
        Requests current players from the server.
        """
        self.current_players_on_server = self.send_msg("LIST_PLAYERS:::")
        return self.current_players_on_server

    def get_current_players(self):
        """
        Gets current players.
        """
        return self.get_current_players_from_server()

    def set_nickname(self, nick):
        """
        Sets the client's nickname.
        """
        self.nick = nick

    def get_map_from_server(self):
        """
        Requests the map from the server.
        """
        map_from_server = self.send_msg("SHOW_MAP:::")
        logger.debug("map_from_server: %s", map_from_server)
        return map_from_server

    def exit_lobby(self):
        """
        Exits the lobby.
        """
        self.only_send("EXIT_LOBBY:::")

    def start_game(self):
        """
        Starts the game.
        """
        self.send_msg("START_GAME:::")

    def end_turn(self):
        """
        Ends the client's turn.
        """
        msg = f"END_TURN:{self.nick}:::"
        self.only_send(msg)
        return self.unexpected_messages(msg)

    def get_new_player(self):
        """
        Gets information about a new player.
        """
        new_player = self.rec_msg()
        return new_player.split(":")

    def get_opponents_move(self):
        """
        Waits for and returns the opponent's move.
        """
        try:
            mes = self.rec_msg()
            if not mes:
                return ["DISCONNECTED"]
            return mes.split(':')
        except OSError:
            return ["DISCONNECTED"]

    def end_game_by_host(self):
        """
        Ends the game by the host.
        """
        self.only_send("END_GAME")
        return self.unexpected_messages("END_GAME")

    def move_unit(self, x0, y0, x1, y1, cost):
        """
        Moves a unit from one tile to another.
        """
        msg = f"MOVE_UNIT:({x0},{y0}):({x1},{y1}):{cost}"
        self.only_send(msg)
        return self.unexpected_messages(msg)

    def add_unit(self, x, y, unit_type, count):
        """
        Adds a unit on a specified tile.
        """
        msg = f"ADD_UNIT:{self.nick}:({x},{y}):{unit_type}:{count}"
        self.only_send(msg)
        return self.unexpected_messages(msg)

    def update_health(self, x, y, new_health):
        """
        Updates the health of a unit on a specified tile.
        """
        msg = f"HEALTH:{(x, y)}:{new_health}"
        self.only_send(msg)
        return self.unexpected_messages(msg)

    def get_city(self, city):
        """
        Gets a city.
        """
        msg = f"GIVE_CITY:{city.tile.coords}:{self.nick}"
        self.only_send(msg)
        return self.unexpected_messages(msg)

    def add_city(self, x, y, city_name):
        """
        Adds a city on a specified tile.
        """
        msg = f"ADD_CITY:{self.nick}:({x},{y}):{city_name}"
        self.only_send(msg)
        return self.unexpected_messages(msg)

    def enhance_city_area(self, x, y):
        """
        Enhances the area of a city.
        """
        msg = f"MORE_AREA:({x},{y})"
        self.only_send(msg)
        return self.unexpected_messages(msg)

    def unexpected_messages(self, msg):
        """
        A generator of messages that were received between sending a request to the server and getting a confirmation.
        """
        new_msg = None
        while new_msg != msg:
            new_msg = self.rec_msg()
            yield new_msg.split(":")

    def send_alliance_request(self, receiver):
        """
        Sends an alliance request.
        """
        msg = f'DIPLOMACY:ALLIANCE:{self.nick}:{receiver}'
        self.only_send(msg)

    def end_alliance(self, receiver):
        """
        Ends an alliance.
        """
        msg = f'DIPLOMACY_ANSWER:END_ALLIANCE:{self.nick}:{receiver}'
        self.only_send(msg)

    def declare_war(self, receiver):
        """
        Declares war.
        """
        msg = f'DIPLOMACY_ANSWER:DECLARE_WAR:{self.nick}:{receiver}'
        self.only_send(msg)

    def send_truce_request(self, receiver):
        """
        Sends a truce request.
        """
        msg = f'DIPLOMACY:TRUCE:{self.nick}:{receiver}'
        self.only_send(msg)

    def buy_city(self, receiver, price, city_coords):
        """
        Buys a city.
        """
        msg = f'DIPLOMACY:BUY_CITY:{self.nick}:{receiver}:{city_coords}:{price}'
        self.only_send(msg)

    def buy_resource(self, receiver, price, resource, quantity):
        """
        Buys a resource.
        """
        msg = f'DIPLOMACY:BUY_RESOURCE:{self.nick}:{receiver}:{resource.lower()}:{price}:{quantity}'
        self.only_send(msg)
