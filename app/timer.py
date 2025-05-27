from PyQt6.QtCore import QTimer, pyqtSignal, QObject


class Timer(QObject):  # Inherit QObject for signals
    time_updated = pyqtSignal(int)  # Emit remaining minutes as int

    def __init__(self, overlay, work_duration, break_duration):
        super().__init__()
        self.overlay = overlay
        self.work_duration = work_duration * 60  # minutes → seconds
        self.break_duration = break_duration * 60
        self.is_work_time = True
        self.remaining = self.work_duration

        # Main timer (single shot for full duration)
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.switch_state)

        # Add a ticking timer (every second)
        self.tick_timer = QTimer()
        self.tick_timer.timeout.connect(self.tick)
        self.tick_timer.start(1000)  # 1 second intervals

    def start(self):
        self.remaining = self.work_duration
        self.time_updated.emit(self.remaining // 60)  # Emit initial minutes
        self.timer.start(self.remaining * 1000)

    def switch_state(self):
        self.is_work_time = not self.is_work_time
        if self.is_work_time:
            self.remaining = self.work_duration
            self.overlay.color = "green"
        else:
            self.remaining = self.break_duration
            self.overlay.color = "red"
        self.time_updated.emit(self.remaining // 60)  # Emit updated minutes
        self.timer.start(self.remaining * 1000)
        self.overlay.update()

    def tick(self):
        if self.remaining > 0:
            self.remaining -= 1
            self.time_updated.emit(self.remaining // 60)  # Emit minutes countdown
