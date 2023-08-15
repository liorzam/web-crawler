import logging
import os
import time


def setup_logger(logger_name="crawler"):
    logger = logging.getLogger(logger_name)

    # Read log level from environment variable, default to INFO if not set
    log_level = os.environ.get("LOG_LEVEL", "INFO").upper()
    logger.setLevel(log_level)

    # Create console handler and set level to log_level
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(ch)
    return logger


def measure_time(logger):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            logger.debug(f"{func.__name__} took {elapsed_time:.4f} seconds to execute")
            return result
        return wrapper
    return decorator
