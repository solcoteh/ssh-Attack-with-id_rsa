# ssh Attack with id_rsa

Brute force attack with id_rsa key

### Example: Using the SSH Connection Script

#### 1. **Install Python and Dependencies**

Make sure you have Python 3 installed on your machine. Then, install the `paramiko` library:

```bash
pip install paramiko
```

#### 2. **Create a Usernames File**

Create a text file named `usernames.txt` with the following content (one username per line):

```
admin
user1
guest
developer
```

#### 3. **Run the Script**

Save the SSH connection script in a file named `ssh-Attack-with-id.py`. Open your terminal (or command prompt) and navigate to the directory where the script and the `usernames.txt` file are located.

Run the script using:

```bash
python ssh-Attack-with-id.py
```

#### 4. **Follow the Prompts**

You will see prompts in the terminal. For example:

```
Please enter your IP address: 192.168.1.10
Please enter the path to your file with usernames: usernames.txt
Please enter the path to your id_rsa file: id_rsa
Enter passphrase (if any, leave blank if none): 
```

- **IP Address**: Enter the IP address of the remote server you want to connect to (e.g., `192.168.1.10`).
- **Usernames File Path**: Enter the path to your `usernames.txt` file (e.g., `usernames.txt` if it's in the same directory).
- **RSA Key Path**: Enter the path to your RSA private key file (e.g., `id_rsa`).
- **Passphrase**: If your RSA key is not passphrase-protected, just press Enter.

#### 5. **View Results**

The script will try to connect using each username from the `usernames.txt` file. You will see output like this:

```
Successful SSH connection as user: admin
```

If the script successfully connects, it will stop trying further usernames. If authentication fails for all usernames, the script will notify you accordingly.
