# Break Timer 🕒

A lightweight, command-line application to help you maintain a healthy work-break balance using the Pomodoro technique. Perfect for developers, students, and anyone who wants to stay productive while avoiding burnout.

## Installation 🛠️

1. **Install uv** (if not already installed):

   ```bash
   pip install uv
   ```

2. **Clone the repository**:

   ```bash
   git clone https://github.com/neevan0842/Break-Timer.git
   cd Break-Timer
   ```

3. **Set up the virtual environment and install dependencies**:
   ```bash
   uv sync
   ```

## Quick Setup for Windows PowerShell 🪟

Add this function to your PowerShell profile (`$PROFILE`) for easy access:

```powershell
function bt {
    & "D:\Projects\Break-Timer\.venv\Scripts\python.exe" D:\Projects\Break-Timer\main.py $args
}
```

To edit your PowerShell profile, run:

```powershell
notepad $PROFILE
```

## Usage 📝

### Basic Commands

| Command  | Description                | Example     |
| -------- | -------------------------- | ----------- |
| `start`  | Start the timer            | `bt start`  |
| `stop`   | Stop the timer             | `bt stop`   |
| `status` | Check current timer status | `bt status` |

### Configuration

| Command               | Description                | Example          |
| --------------------- | -------------------------- | ---------------- |
| `set-work <minutes>`  | Set work session duration  | `bt set-work 25` |
| `set-break <minutes>` | Set break session duration | `bt set-break 5` |

### Examples

```bash
# Start a work session
bt start

# Set work duration to 25 minutes
bt set-work 25

# Set break duration to 5 minutes
bt set-break 5

# Check current status
bt status

# Stop the timer
bt stop
```

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Made with ❤️ by [neevan0842](https://github.com/neevan0842)
