import logging
import logging.config
import os

import yaml


class Logger:
    fileLogger = logging.getLogger("fileLogger")

    def init_logger(self):
        conf_file = 'logging.yaml'
        if os.path.exists(conf_file):
            with open(conf_file, 'r') as f:
                config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)

    def debug_log(self, file_name, msg):
        if self.fileLogger.hasHandlers():
            if len(file_name.strip()) > 0:
                self.fileLogger.handlers[0].setFileName("debug_" + file_name)
            else:
                self.fileLogger.handlers[0].setFileName(self.fileLogger.handlers[0].defaultFileName)
            self.fileLogger.debug(msg)

    def error_log(self, file_name, msg):
        if self.fileLogger.hasHandlers():
            if len(file_name.strip()) > 0:
                self.fileLogger.handlers[0].setFileName("error_" + file_name)
            else:
                self.fileLogger.handlers[0].setFileName(self.fileLogger.handlers[0].defaultFileName)
            if isinstance(msg, Exception):
                try:
                    self.fileLogger.error(msg, exc_info=True)
                except Exception:
                    self.fileLogger.error(str(msg))
            else:
                self.fileLogger.error(str(msg))
