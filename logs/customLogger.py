import logging
import datetime

class CustomLogger:
    now = datetime.datetime.now()
    current_date = now.strftime("%Y_%m_%d_T%H:%M:%S")
    log_file = f"./logs/automation_{current_date}.log"

    def get_logger(self, logger_name: str, log_level=logging.DEBUG):
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        # Create console/file handler and set the log level
        file_handler = logging.FileHandler(filename=self.log_file, mode="a")
        # Create formatter - how you want your logs to be formatted
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s : %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
        # Add formatter to console of file handler
        file_handler.setFormatter(formatter)
        # Add console handler to logger
        logger.addHandler(file_handler)

        return logger