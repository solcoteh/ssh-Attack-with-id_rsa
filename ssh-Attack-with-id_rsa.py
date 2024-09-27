import paramiko
import getpass
import os

def get_ip_address():
    return input("Please enter your IP address: ")

def read_file_and_convert_to_lowercase(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        return [line.strip().lower() for line in lines]
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return []

def get_id_rsa_path():
    return input("Please enter the path to your id_rsa file: ")

def get_passphrase():
    return getpass.getpass("Enter passphrase (if any, leave blank if none): ")

def try_ssh_connection(ip, id_rsa_path, passphrase, user):
    ssh_client = paramiko.SSHClient()
    
    # Automatically accept unknown host keys
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh_key = paramiko.RSAKey.from_private_key_file(id_rsa_path, password=passphrase)
        
        # Connect to the remote server
        ssh_client.connect(ip, username=user, pkey=ssh_key)
        print(f"Successful SSH connection as user: {user}")
        return True
    
    except paramiko.AuthenticationException:
        print(f"Authentication failed for user: {user}")
    except paramiko.SSHException as e:
        print(f"SSH connection failed for user: {user} with error: {e}")
    except Exception as e:
        print(f"Unexpected error for user: {user} with error: {e}")
    
    finally:
        ssh_client.close()
    
    return False

def main():
    ip = get_ip_address()
    file_path = input("Please enter the path to your file with usernames: ")
    
    users = read_file_and_convert_to_lowercase(file_path)
    if not users:
        return

    id_rsa_path = get_id_rsa_path()
    passphrase = get_passphrase()
    
    for user in users:
        if try_ssh_connection(ip, id_rsa_path, passphrase, user):
            break  # Stop after the first successful connection

if __name__ == "__main__":
    main()
