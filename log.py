# тут функционал работы с журналом

import time
import settings

def add2log(text,direction = '> '):
    with open(settings.my_log, 'a', encoding='UTF-8') as f:
        f.write(f'{time.strftime("%Y.%m.%d %H:%M:%S",time.gmtime(time.time()))}:{direction} {text}\n')
    return
