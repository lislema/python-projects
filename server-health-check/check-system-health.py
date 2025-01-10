import psutil


def check_system_health():
    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    # Memory usage
    memory_info = psutil.virtual_memory()
    print(f"Memory Usage: {memory_info.percent}%")

    # Disk usage
    disk_usage = psutil.disk_usage('/')
    print(f"Disk Usage: {disk_usage.percent}%")

    # Network stats
    net_io = psutil.net_io_counters()
    print(f"Bytes Sent: {net_io.bytes_sent}, Bytes Received: {net_io.bytes_recv}")


if __name__ == "__main__":
    check_system_health()