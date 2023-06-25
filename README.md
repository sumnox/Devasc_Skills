# Task name
GitHub

# Task preparation
Manage GitHub scripts and documents

# Task implementation
- created a remote repository
- created a local repository with `git init`
- added a README.md
- Staged and committed the repository
	`git add .`
	`git commit -m initial commit`
- connected to remote repository
	`git remote add origin <url>`
	`git push -u origin master`

# Task troubleshooting
Initially I had some trouble in setting up the correct repository. I made some mistakes. 
After learning what I did wrong, I deleted the repository and started over.

# Task verification
![git-proof](/assets/task_1/git-proof.png)

---
# Task name
Ansible

# Task preparation
Manage Ansible scripts

# Task implementation

# Task troubleshooting

# Task verification

---
# Task name
Docker

# Task preparation
Create a Docker microservice 

# Task implementation

# Task troubleshooting

# Task verification

---
# Task name
Jenkins

# Task preparation
Create a CI/CD pipeline 

# Task implementation

# Task troubleshooting

# Task verification

---
# Task name
Rest API & RESTCONF

# Task preparation
Create a Python script based on curl command examples

# Task implementation

# Task troubleshooting

# Task verification

---
# Task name
Webex Teams API

# Task preparation
Execute Webex Teams API calls using a Python script

# Task implementation
I took the existing scripts and modified them to hide the token. I also hid this from the commits through gitignore.
For the future I would expand the script to take user input and automatically list out the roomIDs. 
Due to the requirement to send screenshots, I created a new script to send screenshots to webex.

# Task troubleshooting
Initially I had trouble getting the roomId, after deleting and readding the room I copied the value. This would be something to further automate using the API docs as guidance.

# Task verification
![create-membership-proof](/assets/task_6/create-membership-proof.png)
![create-room-proof](/assets/task_6/create-room-proof.png)
![send-message-proof](/assets/task_6/send-message-proof.png)
![send-file-proof](/assets/task_6/send-file-proof.png)

---
# Task name
Bash

# Task preparation
Translate the given Python script into an equivalent bash script. 

# Task implementation
The first thing I did was translate all the text to bash and change the syntax around. I got pretty far using curl for the GET request.
Getting the JSON to parse correctly was a huge challenge and took me several hours to troubleshoot.
# Task troubleshooting
To verify the requests I used Postman and copied the script. For some reason I kept running into issues in my bash script, mainly due to variable unpacking.  
# Task verification

---
# Task name
Filtering DNAC Response Data

# Task preparation
Adapt the Python code in the script on the next page in order to obtain a working application that is able to provide the output shown in the output example OUTPUT TASK 10

# Task implementation
First I filled in the blanks I could gather from the code, the ones that I couldn't figure out from memory I looked up in Google. After filling out most of the code I ran it to try and figure out the final part. For the final part I printed out the keys of the dictionary in the list, from this it was easy enough to figure out what belonged where.

# Task troubleshooting
At first I got a large error about JSON parsing, I quickly discovered I was nog getting any output on my token request. The next thing I ran into, was that I got a 404 on the token request. Reading the docs I saw that I had to perform a POST request.

# Task verification
![dnac-proof](/assets/task_10/dnac-proof.png)
