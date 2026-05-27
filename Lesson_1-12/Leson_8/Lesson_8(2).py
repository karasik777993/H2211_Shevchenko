import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="Lesson_8(2).log",
                    filemode="w",
                    format="We have next logging message: %(asctime)s:%(levelname)s -%(message)s")

try:
    print(0/10)
except Exception:
    logging.exception("Exception")