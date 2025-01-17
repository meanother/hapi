import pathlib
from loguru import logger

log_dir = pathlib.Path.home().joinpath("logs")
log_dir.mkdir(parents=True, exist_ok=True)

logger.add(
    log_dir.joinpath("fake-api.log"),
    format="{time} [{level}] {module} {name} {function} - {message}",
    level="DEBUG",
    compression="zip",
    rotation="30 MB",
)