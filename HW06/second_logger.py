import logging

logging.basicConfig(
  format="%(asctime)s (%(name)s, %(levelname)s): %(message)s",
  datefmt="%d.%m.%Y, %H:%M",
  filename="second_alternative.log", filemode="a", level=logging.INFO
)

logger = logging.getLogger(name = "Second")
another_logger = logging.getLogger(name = "Second")


"""
5. What happens when two loggers log to the same file with mode 'a'
-> Both logs get appended.
"""

logger.warning("Logger {}".format("Nachricht"))
another_logger.warning("Logger 2 {}".format("Nachricht"))

