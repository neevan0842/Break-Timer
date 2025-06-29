import sys
import click
import subprocess
from app.logger import logger
from PyQt6.QtWidgets import QApplication
from app.overlay import Overlay
from app.timer import Timer
from app.utils import (
    load_config,
    save_config,
    set_pid,
    is_process_running,
    delete_process,
)


class BreakTimerApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.config = load_config()
        self.overlay = Overlay("green")
        self.timer = Timer(
            self.overlay, self.config["work_duration"], self.config["break_duration"]
        )
        self.timer.time_updated.connect(
            lambda minutes: self._update_overlay_time(minutes)
        )

    def run(self):
        """Run the application event loop."""
        self.timer.start()
        self.app.exec()

    def quit(self):
        """Stop the timers and close the overlay."""
        if self.timer:
            self.timer.timer.stop()
            self.timer.tick_timer.stop()
        if self.overlay:
            self.overlay.close()
        self.app.quit()

    def _update_overlay_time(self, minutes):
        self.overlay.remaining_minutes = minutes
        self.overlay.update()


# Create the BreakTimerApp instance
app = BreakTimerApp()


@click.group()
def cli():
    """Break Timer CLI commands."""
    pass


@cli.command()
def start():
    """Start the Break Timer application."""
    try:
        process = subprocess.Popen([sys.executable, __file__, "run"])
        set_pid(process.pid)
        logger.info("Break Timer started successfully.")
    except Exception as e:
        logger.error(f"Error starting the application: {e}")


@cli.command()
def stop():
    """Stop the Break Timer application."""
    try:
        delete_process()
        logger.info("Application stopped successfully.")
    except Exception as e:
        logger.error(f"Error: {e}")


@cli.command()
def status():
    """Check the status of the Break Timer application."""
    pid = is_process_running()
    if pid is None:
        logger.info("Application is not running.")
    else:
        logger.info(
            f"PID: {pid}, Work: {app.config['work_duration']}, Break: {app.config['break_duration']}"
        )


@cli.command()
def restart():
    """Restart the Break Timer application."""
    try:
        delete_process()
        process = subprocess.Popen([sys.executable, __file__, "run"])
        set_pid(process.pid)
        logger.info("Application restarted successfully.")
    except Exception as e:
        logger.error(f"Error: {e}")


@cli.command()
@click.argument("minutes", type=int)
def set_work(minutes):
    """Set the work duration in minutes."""
    try:
        app.config["work_duration"] = minutes
        save_config(app.config)
        delete_process()
        process = subprocess.Popen([sys.executable, __file__, "run"])
        set_pid(process.pid)
        logger.info(f"Work duration set to {minutes} minutes.")
    except Exception as e:
        logger.error(f"Error setting work duration: {e}")


@cli.command()
@click.argument("minutes", type=int)
def set_break(minutes):
    """Set the break duration in minutes."""
    try:
        app.config["break_duration"] = minutes
        save_config(app.config)
        delete_process()
        process = subprocess.Popen([sys.executable, __file__, "run"])
        set_pid(process.pid)
        logger.info(f"Break duration set to {minutes} minutes.")
    except Exception as e:
        logger.error(f"Error setting break duration: {e}")


@cli.command()
def run():
    app.run()


if __name__ == "__main__":
    cli()
