import psutil

def check_system_health():
    cpu_threshold = int(input("Enter the CPU Threshold:"))
    disk_threshold = int(input("Enter the Disk Threshold:"))
    memory_threshold = int(input("Enter the Memory Threshold:"))

    current_cpu = psutil.cpu_percent(interval=1)
    disk_usage = psutil.disk_usage('/').percent
    memory = psutil.virtual_memory().percent

    print("==== System Health Report ====")

    if cpu_threshold > current_cpu:
        print(f"CPU Usage is {current_cpu}%")
    else:
        print("CPU usage is not normal")
    
    if disk_threshold > disk_usage:
        print(f"Disk Usage is {disk_usage}%")
    else:
        print("Disk usage is not normal")

    if memory_threshold > memory:
        print(f"Memory Usage: {memory}%")
    else:
        print("Memory usage is not normal")
check_system_health()