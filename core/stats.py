from time import time


class Stats:

    def __init__(self):

        self.started_at = time()

        self.success = 0
        self.failed = 0
        self.deleted = 0
        self.floods = 0

        self.current_chat = "..."

    @property
    def uptime(self):

        return int(
            time() - self.started_at
        )

    @property
    def speed(self):

        if self.uptime <= 0:
            return 0

        return round(
            self.success / (self.uptime / 60),
            2
        )

    def render(self):

        return (
            "📡 Рассылка активна\n\n"

            f"✅ Успешно: {self.success}\n"
            f"❌ Ошибок: {self.failed}\n"
            f"🗑 Удалено: {self.deleted}\n"
            f"⏳ FloodWait: {self.floods}\n\n"

            f"🚀 Скорость: {self.speed}/мин\n"
            f"⏱ Аптайм: {self.uptime} сек\n\n"

            f"📍 Текущий чат:\n"
            f"{self.current_chat}"
        )