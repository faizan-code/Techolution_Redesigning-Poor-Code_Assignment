import datetime


class Logger:
    def __init__(self, file_name="app.log"):
        """
        Initializes a new Logger instance.
        :param file_name: Name of the file where logs will be written.
        """
        self.file_name = file_name

    def log(self, message, level="INFO"):
        """
        Writes a log message to the console and a file with the specified log level.
        :param message: Log message to be written.
        :param level: Log level (e.g., INFO, ERROR).
        """
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp} - {level} - {message}\n"

        # Print to console
        print(log_message, end="")

        # Append to a log file
        with open(self.file_name, "a") as log_file:
            log_file.write(log_message)
