import psutil

def terminate_processes_by_names(process_names):
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] in process_names:
            print(f"Terminating process {process.info['name']} (PID: {process.info['pid']})")
            try:
                psutil.Process(process.info['pid']).terminate()
            except psutil.NoSuchProcess:
                print(f"Process {process.info['name']} (PID: {process.info['pid']}) not found.")
            except psutil.AccessDenied:
                print(f"Access denied to terminate process {process.info['name']} (PID: {process.info['pid']}).")

if __name__ == "__main__":
    target_process_names = ["Adobe Desktop Service.exe", "AdobeIPCBroker.exe", "CCLibrary.exe", "CCXProcess.exe", "AdobeUpdateService.exe", "Adobe Crash Processor.exe", "AdobeNotificationClient.exe", "Creative Cloud Helper.exe", "CoreSync.exe"]
    terminate_processes_by_names(target_process_names)
