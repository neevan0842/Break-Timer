# cli.py
import click
import subprocess
from app.config import load_config, save_config


@click.group()
def cli():
    pass


@cli.command()
def start():
    subprocess.Popen(["python", "main.py"])


@cli.command()
def stop():
    # Implement logic to stop the application
    pass


@cli.command()
@click.argument("minutes", type=int)
def set_work(minutes):
    config = load_config()
    config["work_duration"] = minutes
    save_config(config)
    click.echo(f"Work duration set to {minutes} minutes.")


@cli.command()
@click.argument("minutes", type=int)
def set_break(minutes):
    config = load_config()
    config["break_duration"] = minutes
    save_config(config)
    click.echo(f"Break duration set to {minutes} minutes.")


if __name__ == "__main__":
    cli()
