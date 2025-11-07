import sys
import os
import time
from datetime import datetime


class ConsoleLogger:
    """
    Captures console output (stdout) and writes it to both console and a file.
    Also tracks total program runtime.
    """

    def __init__(self, log_file_path):
        self.log_file_path = log_file_path
        self.terminal = sys.stdout
        self.log_file = None
        self.start_time = None
        self.end_time = None

    def start(self):
        """Start capturing console output and begin timing."""
        self.start_time = time.time()
        # ===== FIX: Ensure the directory exists before opening the file =====
        log_dir = os.path.dirname(self.log_file_path)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        self.log_file = open(self.log_file_path, 'w', encoding='utf-8')
        sys.stdout = self

        # Write header with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"Console Output Log - Started at {timestamp}\n{'=' * 60}\n\n"
        self.log_file.write(header)
        print(header.strip())  # Also print to console

    def write(self, message):
        """Write message to both console and file."""
        self.terminal.write(message)
        if self.log_file:
            self.log_file.write(message)

    def flush(self):
        """Flush both outputs."""
        self.terminal.flush()
        if self.log_file:
            self.log_file.flush()

    def stop(self):
        """Stop capturing, calculate runtime, and close the log file."""
        self.end_time = time.time()
        runtime_seconds = self.end_time - self.start_time

        # Format runtime
        if runtime_seconds < 60:
            runtime_str = f"{runtime_seconds:.2f} seconds"
        else:
            minutes = int(runtime_seconds // 60)
            seconds = runtime_seconds % 60
            runtime_str = f"{minutes} min {seconds:.2f} sec"

        if self.log_file:
            # Write footer with runtime
            end_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            footer = (
                f"\n{'=' * 60}\n"
                f"Log completed at {end_timestamp}\n"
                f"Total runtime: {runtime_str}\n"
                f"{'=' * 60}\n"
            )
            self.log_file.write(footer)
            self.log_file.close()
            self.log_file = None

        # Restore original stdout
        sys.stdout = self.terminal

        # Return runtime for further use if needed
        return runtime_seconds


def enable_console_logging(output_dir):
    """
    Enable console output logging to a text file with runtime tracking.

    Args:
        output_dir (str): Directory where console_output.txt will be saved.

    Returns:
        ConsoleLogger: Logger instance (call .stop() when done).
    """
    import os
    log_file_path = os.path.join(output_dir, "console_output.txt")
    logger = ConsoleLogger(log_file_path)
    logger.start()
    return logger
