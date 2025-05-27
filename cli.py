# cli.py
import os
import click
import subprocess
import psutil
from app.utils import load_config, save_config

# Constants
APP_DIR = os.path.dirname(os.path.abspath(__file__))
PID_FILE = os.path.join(APP_DIR, "app.pid")
BREAKTIMER_EXE = os.path.join(APP_DIR, "dist", "breaktimer.exe")


@click.group()
def cli():
    pass


@cli.command()
def start():
    try:
        if not os.path.isfile(BREAKTIMER_EXE):
            click.echo(f"Error: {BREAKTIMER_EXE} not found.")
            return

        process = subprocess.Popen([BREAKTIMER_EXE], shell=False)
        with open(PID_FILE, "w") as f:
            f.write(str(process.pid))
        click.echo(f"Application started with PID {process.pid}")
    except Exception as e:
        click.echo(f"Failed to start application: {e}")


@cli.command()
def stop():
    try:
        if not os.path.isfile(PID_FILE):
            click.echo("PID file not found. Application may not be running.")
            return

        with open(PID_FILE, "r") as f:
            pid = int(f.read())

        parent = psutil.Process(pid)
        children = parent.children(recursive=True)
        # Terminate child processes
        for child in children:
            child.terminate()
        gone, alive = psutil.wait_procs(children, timeout=3)
        # Terminate parent
        parent.terminate()
        parent.wait(timeout=3)

        os.remove(PID_FILE)
        click.echo("Application stopped successfully.")
    except subprocess.CalledProcessError:
        click.echo("Failed to stop the application. It may not be running.")
    except Exception as e:
        click.echo(f"Error stopping application: {e}")


@cli.command()
def status():
    try:
        if not os.path.isfile(PID_FILE):
            click.echo("Application is not running.")
            return

        with open(PID_FILE, "r") as f:
            pid = int(f.read())

        if psutil.pid_exists(pid):
            config = load_config()
            click.echo(
                f"PID-{pid}, Work: {config['work_duration']}, Break: {config['break_duration']}"
            )
        else:
            click.echo("Application is not running.")
    except Exception as e:
        click.echo(f"Error checking application status: {e}")


@cli.command()
@click.argument("minutes", type=int)
def set_work(minutes):
    try:
        config = load_config()
        config["work_duration"] = minutes
        save_config(config)
        click.echo(f"Work duration set to {minutes} minutes.")
    except Exception as e:
        click.echo(f"Failed to set work duration: {e}")


@cli.command()
@click.argument("minutes", type=int)
def set_break(minutes):
    try:
        config = load_config()
        config["break_duration"] = minutes
        save_config(config)
        click.echo(f"Break duration set to {minutes} minutes.")
    except Exception as e:
        click.echo(f"Failed to set break duration: {e}")


if __name__ == "__main__":
    cli()
