from LoggerInterface import LoggerInterface;

class Logger(LoggerInterface):
    pass

logger = Logger()
print(logger)

print(isinstance(logger, LoggerInterface))