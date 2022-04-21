import subprocess


def install(packages: list, channels: list):
    """Install a list of packages."""
    logs = subprocess.check_output(
        [
            "mamba", "install", "--yes", *packages,
            *[f"-c {channel}" for channel in channels]
        ]
    )

    print(logs.decode(encoding="utf-8"))

    return logs
