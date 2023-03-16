import platform
import psutil


class SettingsPC:

    def __init__(self):
      self.settings = self.get_os_info()

    def get_os_info(self):
        self.settings = {
            "os": platform.system(),
            "os_version": platform.version(),
            "os_architecture": platform.architecture(),
            # "ram": round(psutil.virtual_memory().total / (1024.0 **3)),
        }
        return self.settings
