import os
import platform
import getpass

class SystemReport:
    def __init__(self):
        self.username = get_username()
        self.os_alias = get_os_alias()
        self.raw_os = get_raw_os()

def print_report(report):
    print(f"Operator: \"{report.username}\" ")
    print(f"OS Alias: {report.os_alias}")
    print(f"Raw OS: {report.raw_os}")

def get_username():
    return getpass.getuser()

def get_os_alias():
    os_alias = platform.system()
    os_map = {
    "Darwin": "macOS",
    "Windows": "Windows",
    "Linux": "Linux"
    }
    if os_alias in os_map:
        os_alias = os_map[os_alias]
    return(os_alias)

def get_raw_os():
    return(platform.system())

report=SystemReport()
print_report(report)