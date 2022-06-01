'''
LINUX w pigułce
przypomnienie najwazniejszych info i skrótów z podstaw Linuxa

ls - lista plików i folderów
-la list all
-s size
-S sort by size
-h human
-F zaznacz foldery

cat file.txt  - wyświetla zawartość pliku

echo "tektowo" >> plik.txt

cd -  powrót do ostatniego

rm -r folder and file recursively
-f force
-d empty dir
-v verbose


ctrl +][ >> przesunięcie kodu o tab (vsc)

(terminal:)
ctrl + a >> początek lini
ctrl + e >> koniec linii
ctrl + u >> usuwa lewo
ctrl + k >> usuwa prawo
ctrl + w >> po słowie usuwa

'''
'''
systemctl daemon-reload
systemctl restart nginx
systemctl restart.service
'''


'''
deluser uzytkownik
rm -r /home/uzytkownik
delgroup uzytkownik

NEW_USER = uzykownik_nazwa
adduser $NEW_USER
adduser $NEW_USER www-data (przypisanie do gr )
adduser $NEW_USER sudo
groups $NEW_USER  (w jakiej grupie)

sudo apt update
sudo apt upgrade


chmod 700 /home/user/.ssh
cd /home/user/.ssh

klucz = nazwa
ssh-keygen -f /home/user/.ssh/$klucz -C user -N ''
cat /home/user/.ssh/$klucz.pub > authorized_keys
chmod 600 authorized_keys

scp root@IP:sciezka nazwa_klucza
ssh -i nazwa_klucza użykownik@IP

skopiować do .ssh
w Config :
Host nazwa
HostName IP
User użytkownik
IdentityFile pełna ściezka

Host my_server
  HostName 46.41.140.160
  User puunina
  IdentityFile C:\Users\Ja\.ssh\xd_puunina

'''




'''
ps aux | grep program.py

kill -9 PID

man -k kill
'''


'''
crontab -e
'''


'''

sudo systemctl status flaga
'''

'''
nano ~./bash_aliases

'''
