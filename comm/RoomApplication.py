
import logging
import json
import asyncio

from autobahn import wamp
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.exception import ApplicationError

logger = logging.getLogger(__name__)

class RoomApplication(ApplicationSession):
    def __init__(self, config = None):
        ApplicationSession.__init__(self, config)
        self.room_counter=0
        self.rooms=[]
    
    @wamp.register('rooms.get_new_room')
    def get_new_room(self, name):
        roomId = self.room_counter
        self.room_counter += 1
        room = {
            'id': roomId,
            'name': name,
            'num_users': 1,
        }
        self.rooms.append(room)
        logger.debug("new room created: %s", roomId)
        return json.dumps(room)

    @wamp.register('rooms.get_all_rooms')
    def get_all_rooms(self):
        return json.dumps(self.rooms)

    @asyncio.coroutine
    def onJoin(self, details):
        results = yield from self.register(self)
        for res in results:
            if isinstance(res, wamp.protocol.Registration):
                logger.debug('Registered procedure with ID %s'.res.id)
            else:
                logger.debug('Failed to register procedure %s',res)

    def onDisconnect(self):
        print('onDisconnect was called')
        asyncio.get_event_loop().stop()


def register_modules():
    logger.debug("starting RoomApplication")
    runner = ApplicationRunner(
                "ws://localhost:8080/ws",
                 u"realm1",
                 debug_wamp=False,  # optional; log many WAMP details
                 debug=False,  # optional; log even more details
             )
    runner.run(RoomApplication)
