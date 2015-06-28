import time

import comm.RoomApplication as RoomApplication

def main():
    RoomApplication.register_modules()

    while True:
        time.sleep(10)

if __name__ == '__main__':
    import logging
    import logging.config
    logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
    main()
