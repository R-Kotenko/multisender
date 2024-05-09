import tqdm
from loguru import logger as log
import time


log.add("logger.log", format="{time:YYYY-MM-DD | HH:mm:ss.SSS} | {level} \t| {line}:{function} | {message}")


def generate_timestamp():
    timestamp = int(time.time() * 1000)
    return timestamp


def sleeping(x):
    print()
    for _ in tqdm.tqdm(range(x), desc='Sleeping', bar_format='{l_bar}%s{bar}%s{r_bar}' % ('\033[20m', '\033[10m')):
        time.sleep(1)
    print()