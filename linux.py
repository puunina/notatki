'''
LINUX w pigułce
przypomnienie najwazniejszych info i skrótów z podstaw Linuxa

ls - lista plików i folderów
-la list all
-s size
-S sort by size
-h human
-F zaznacz foldery
ls d* > listuje wszystko zaczynające się od "d"
  *.txt
  ??.txt >> określona długość
  [] >>> do wyboru
  file[1-9].txt

touch {jan,feb,mar}_{2010,2011,2012,2013}/{1..200} >> kolejne foldery w każdym 200 plików
mkdir {jan,feb,mar}_{2010,2011,2012,2013} >> same foldery

cp file.txt file2.txt .   >>> kopia do aktulnego folderu(lub dowolna ściezka)
cp -r kopia z zawartością

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
nano ~/.bash_aliases

'''
'''
!! ostatnie polecenie
!10 polecenie nr
which eho > gdzie polecenie
man -k szukanafraza
man section(1-8) nameofpage
help command > zamiast man

rev letters backwards
tac lines backwards


chmod +x filename >> zmina uprawnień

bash plik.sh > wywołuje

apt-cache search program
apt-co show name_of_package

removing package:
sudo apt-get purge name_of_package
sudo apt-get autoremove >> will remove any dependencies that are no longer used
sudo apt-get clean >> ges rid of archive files in /var/cacheapt/archivers
sudo apt-get autoclean >> gets rid of files that are no longer available

cal
cal 2017 > kalendarz
date
date -u date universal time



cat 2>> error.txt
cat >>file.txt

cat < text.txt >> reads file

piping:
date | cut --delimeter "" --fileds 1

tee >>> data in to 2 directions (pipe and file)
date | tee file.txt | cut --delimeter " " --field=1 >> date.txt
(powyższa linia zapisuje 2 pliki)

xargs - for piping which does not accept standar input e.g:
date | xargs echo

'''