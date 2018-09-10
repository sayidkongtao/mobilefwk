import logging.handlers


class CustomLog:
    def __init__(self, log_name, backup_file_path, log_level=logging.INFO):
        self.logger = logging.getLogger(log_name)
        if len(self.logger.handlers) == 0:
            # create handler, to save the log to file "log.log"
            file_handler = logging.handlers.RotatingFileHandler(filename=backup_file_path, maxBytes=1024 * 1024 * 10,
                                                                backupCount=5, encoding="utf-8")
            # create handler, to print log to control Panel
            control_handler = logging.StreamHandler()
            # Set format for handler
            formatter = logging.Formatter("%(asctime)s-%(name)s-%(module)s-%(lineno)d -%(levelname)s-%(message)s ")
            file_handler.setFormatter(formatter)
            control_handler.setFormatter(formatter)
            # add handler to logger
            self.logger.addHandler(file_handler)
            self.logger.addHandler(control_handler)
        self.logger.setLevel(log_level)

    @property
    def get_log(self):
        return self.logger

    def set_log_level(self, level):
        self.logger.setLevel(level)
