# aksUnix
Unix Password cracker using dictionary attack

Files needed to run the program:
(1) Text file with encrypted password (encryptPass.txt)
(2) Text file with dictionary (dictionary.txt)

How it works:
The program cracks the encrypted unix password using dictionary attack.
From the encrypted password it takes the first 2 character which is a salt and use it to encrypt dictionary words and compare it with the original encrypted password.

How to run:
(1) Download the repository
(2) Give permission to aksUnix file -> chmod u+x aksUnix
(3) Run the file -> ./aksUnix

Important!
This program will not able to crack more secure hasing algorithms.


