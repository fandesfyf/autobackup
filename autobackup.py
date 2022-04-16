import os
import shutil
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
filenames = []


def logwrite(s: str, ln="./log.txt"):
    size = os.path.getsize(ln) if os.path.exists(ln) else 0
    with open(ln, mode='a' if size < 1024 * 1024 else 'w', encoding='utf-8') as log:
        log.write("{} ".format(time.strftime("%d/%m/%Y %H:%M:%S")) + s + "\n")
        print(s)


class WatchdogHandler(FileSystemEventHandler):
    def __init__(self):
        super(WatchdogHandler, self).__init__()
        self.backuptime = time.time()

    def on_modified(self, event):
        try:
            __filename = os.path.split(event.src_path)[1]
            if __filename in filenames:
                print("修改了 %s" % event.src_path)
                self.backupfile(__filename)
        except:
            logwrite(str(sys.exc_info()[1]))

    def backupfile(self, filename):
        if not os.path.exists("backups"):
            os.mkdir("backups")
        if time.time() - self.backuptime > 10:
            logwrite("复制文件 {}".format(filename))
            self.backuptime = time.time()
            shutil.copy(filename,
                        "backups/{}{}{}".format(os.path.splitext(filename)[0], time.strftime('%Y_%m_%d %H.%M.%S'),
                                                os.path.splitext(filename)[1]))


if __name__ == '__main__':
    print(sys.argv)
    observer = Observer()
    if len(sys.argv) == 2:
        filenames = []
        abspath = os.path.abspath(sys.argv[1])
        path, filename = os.path.split(abspath)
        filenames.append(filename)
        observer.schedule(WatchdogHandler(), path, recursive=True)
        print("开始备份", abspath)
    else:
        filenames.extend(["毕业论文.docx", "毕业论文.doc"])
        observer.schedule(WatchdogHandler(), ".", recursive=True)
        print("开始备份")
    observer.start()
    observer.join()
