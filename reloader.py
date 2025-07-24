import os
import sys
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class BotRestartHandler(FileSystemEventHandler):
    def __init__(self, script, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.script = script
        self.process = None
        self.start_bot()

    def start_bot(self):
        if self.process:
            self.process.kill()
        self.process = subprocess.Popen([sys.executable, '-m', self.script], 
                                        env=os.environ.copy())

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f'Change detected in {event.src_path}. Reloading bot...')
            self.start_bot()

if __name__ == "__main__":
    path = 'Bot'
    print(f'Watching for changes in: {path}')
    event_handler = BotRestartHandler('Bot')
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()