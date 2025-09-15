from apscheduler import Scheduler


class HozonWatcher:
    def __init__(self):
        self.scheduler = Scheduler()

    def run(self):
        with self.scheduler as scheduler:
            try:
                print(" [*] Watcher started. To exit press CTRL+C")
                scheduler.run_until_stopped()
            except KeyboardInterrupt:
                print(" [x] Watcher stopped")
