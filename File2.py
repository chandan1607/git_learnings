import paramiko
def reboot_remote_server(hostname, username, key_filename):
    try:
        # Establish an SSH connection using the provided key file
        key = paramiko.RSAKey.from_private_key_file(key_filename)
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, pkey=key)
 
        # Execute the reboot command
        stdin, stdout, stderr = client.exec_command('sudo reboot')
        stdout.channel.recv_exit_status()
 
        # Close the SSH connection
        client.close()
        print(f"Reboot command sent to {hostname}")
 
    except Exception as e:
        print(f"Error: {str(e)}")
    if __name__ == "__main__":
    # Replace these values with your server details
    host = 'ec2-35-153-105-220.compute-1.amazonaws.com'
    ssh_username = 'ubuntu'
    key_file = 'C:\\Users\\CHANDAJ\\Downloads\\ubuntu.pem'
    reboot_remote_server(host, ssh_username, key_file)
 

