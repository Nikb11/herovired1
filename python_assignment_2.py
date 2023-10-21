import psutil

threshold = 80

print("Monitoring CPU usage...")

try:
    while True:
        cpu_percent = psutil.cpu_percent()  
        if cpu_percent > threshold:
          print(f"Alert! CPU usage exceeds threshold: {cpu_percent}%")
except KeyboardInterrupt:
    print("CPU Monitoring stopped.")
except Exception as e:
    print(f"An error occurred: {str(e)}")