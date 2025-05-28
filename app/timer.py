from PyQt6.QtCore import QTimer, pyqtSignal, QObject


class Timer(QObject):
    """Timer class for managing work and break intervals."""

    time_updated = pyqtSignal(int)

    def __init__(self, overlay, work_duration, break_duration):
        super().__init__()
        self.overlay = overlay
        self.work_duration = work_duration * 60
        self.break_duration = break_duration * 60
        self.is_work_time = True
        self.remaining = self.work_duration

        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.switch_state)

        self.tick_timer = QTimer()
        self.tick_timer.timeout.connect(self.tick)
        self.tick_timer.start(1000)

    def start(self):
        """Start the timer with initial work duration."""
        self.remaining = self.work_duration
        self.time_updated.emit(self.remaining // 60)
        self.timer.start(self.remaining * 1000)

    def switch_state(self):
        """Switch between work and break states."""
        self.is_work_time = not self.is_work_time
        if self.is_work_time:
            self.remaining = self.work_duration
            self.overlay.color = "green"
        else:
            self.remaining = self.break_duration
            self.overlay.color = "red"
        self.time_updated.emit(self.remaining // 60)
        self.timer.start(self.remaining * 1000)
        self.overlay.update()

    def tick(self):
        """Update timer every second."""
        if self.remaining > 0:
            self.remaining -= 1
            self.time_updated.emit(self.remaining // 60)
