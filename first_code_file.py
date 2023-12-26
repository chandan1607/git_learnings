import subprocess
from scripts.Microbots.Log_bot import log_and_print
from scripts.Microbots.Email_Log import log_email
from datetime import datetime
today_date = datetime.now().strftime("%d-%m-%Y")


def Post_Health(Name):
    try:
        # Commands to retrieve CPU usage, memory usage, and uptime
        running_services = f"sudo ssh {Name}  systemctl --type=service --state=running"
        CPU = f"sudo ssh {Name} top -b -n 1 | grep 'Cpu(s)' | awk '{{print $2 + $4}}'"
        Memory = f"sudo ssh {Name} free | awk 'FNR == 2 {{print $3*100/$2}}'"
        Uptime = f"sudo ssh {Name} uptime|awk '{{print $3}}'"

        # Execute the commands using subprocess
        CPU_Usage = subprocess.check_output(CPU, shell=True).decode('utf-8').strip()
        Memory_Usage = subprocess.check_output(Memory, shell=True).decode('utf-8').strip()
        Uptime_Value = subprocess.check_output(Uptime, shell=True).decode('utf-8').strip()
        Running_services = subprocess.check_output(running_services, shell=True).decode('utf-8').strip()

        log_and_print(f"Current server is {Name}",f"{today_date}_logs.txt")
        log_and_print("------POST HEALTH CHECK------", f"{today_date}_logs.txt")

        # Log the pre-health check results
        log_and_print(f"CPU Usage: {CPU_Usage}% \nMemory Usage: {Memory_Usage}% \nUptime: {Uptime_Value}Days",f"{today_date}_logs.txt")
        log_email("------POST HEALTH CHECK ------\n")
        log_email(f"CPU Usage: {CPU_Usage}% \nMemory Usage: {Memory_Usage}% \nUptime: {Uptime_Value}Days\n")

        log_and_print(Running_services, f"{today_date}_logs.txt")
        log_email(f"------RUNNING SERVICES------\n{Running_services}\n")

        return True

    except Exception as e:
        # Handle any exceptions that may occur and log an error message
        log_and_print(f"Error: {e}", f"{today_date}_logs.txt")
        return False
