"""
Logging is a way of inspecting program state.
It is helpful while debugging software both during development and productive use.
Without logging, it would not be possible to quickly check results.
We would have to rely on other techniques like unit tests entirely, which do not necessarily tackle the problem as well.
"""

import logging

logging.basicConfig(
  format="%(asctime)s :: %(name)s ::%(levelname)s :: %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S",
  filename="jan.log", filemode="a", level=logging.INFO
)
logger = logging.getLogger(name = "Jan")

def log_my_name() -> None:
  logger.warning("Logger {}".format(logger.name))

def make_int(val: str) -> int:
  try:
    return int(val)
  except ValueError:
    logger.error("{} is not an int".format(val))
    return 0
make_int("notanint")
make_int(10)
