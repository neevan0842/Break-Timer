# app/overlay.py
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor, QFont


class Overlay(QWidget):
    def __init__(self, color):
        super().__init__()
        self.color = color
        self.remaining_minutes = 0
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(40, 40)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(self.color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(0, 0, self.width(), self.height())

        # Draw remaining minutes only (no seconds)
        painter.setPen(Qt.GlobalColor.white)
        font = QFont("Arial", 18, QFont.Weight.Bold)  # bigger font for minutes only
        painter.setFont(font)

        time_text = f"{self.remaining_minutes + 1}"

        rect = self.rect()
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, time_text)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = (
                event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            )

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
