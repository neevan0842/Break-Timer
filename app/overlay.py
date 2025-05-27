# app/overlay.py
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QColor


class Overlay(QWidget):
    def __init__(self, color):
        super().__init__()
        self.color = color
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
        painter.setBrush(QColor(self.color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(0, 0, self.width(), self.height())

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = (
                event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            )

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
