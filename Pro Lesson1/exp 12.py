import  logging
from stat import filemode

logging.basicConfig(format="Время ошибки: %(asctime)s (.)(.) "
                           "Уровень ошибки: %(levelname)s "
                           "|| id ошибки %(process)d",
                    filename="test.log", encoding="UTF-8",
                    filemode="w")
logging.critical("error critical")
