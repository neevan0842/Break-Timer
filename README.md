# Break Timer

A simple CLI application to manage work and break sessions.

## Setup

1. Install uv if you haven't already:

```bash
pip install uv
```

2. Clone this repository:

```bash
git clone https://github.com/neevan0842/Break-Timer.git
cd Break-Timer
```

3. Install dependencies using uv:

```bash
uv sync
```

## Usage

```bash
# Start the timer
uv run main.py start

# Set work duration (in minutes)
uv run main.py set-work <minutes>

# Set break duration (in minutes)
uv run main.py set-break <minutes>

# Check timer status
uv run main.py status

# Stop the timer
uv run main.py stop
```

## Requirements

- Python 3.x
- uv (Python package manager)
