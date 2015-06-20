import time

import comm.highway as highway

def main():
    highway.register_modules()

    while True:
        time.sleep(10)

if __name__ == '__main__':
    import logging
    import logging.config
    logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
    main()
