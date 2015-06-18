
import logging

import asyncio

from autobahn import wamp
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner
from autobahn.wamp.exception import ApplicationError

logger = logging.getLogger(__name__)

class Out(ApplicationSession):
    @wamp.register('de.meet_here.hello')
    def hello(self, name):
        logger.debug('hello was called')
        return ('Hello {}'.format(name))

    @asyncio.coroutine
    def onJoin(self, details):
        logger.debug('onJoin was called')
        results = yield from self.register(self)
        for res in results:
            if isinstance(res, wamp.protocol.Registration):
                logger.debug('Registered procedure with ID {}'.format(res.id))
            else:
                logger.debug('Failed to register procedure {}'.format(res))

    def onDisconnect(self):
        logger.debug('onDisconnect was called')
        asyncio.get_event_loop().stop()

class In(ApplicationSession):
    @asyncio.coroutine
    def onJoin(self, details):
        logger.debug('onJoin was called')

        setName(u'George')

        logger.debug('Closing session')
        self.leave()

    def setName(name):
        logger.debug('setName was called')
        yield from self.call('de.meet_here.set_name', name=name)

    def onDisconnect(self):
        logger.debug('onDisconnect was called')
        asyncio.get_event_loop().stop()

def register_modules():
    runner = ApplicationRunner(
                "ws://localhost:8080/ws",
                 u"realm1",
                 debug_wamp=False,  # optional; log many WAMP details
                 debug=False,  # optional; log even more details
             )
    runner.run(Out)
    runner.run(In)
