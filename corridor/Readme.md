# Corridor thm
- IDOR based machined, nothing from nmap
- added to `sudo vi /etc/hosts`, go to the site and `view-source:http://{added site}`
- they are bunch of hashes, try to crack it nothing comes up, but hitting the hash as routes working
- try to look like userId 1,2,3,4,5.. replace with hash
- created a python program which convertes text to hash md5
- go with 12,13 you can see the hashes in the source code now try with 14,15 nope not works
- try with 0 works.. BOOM!