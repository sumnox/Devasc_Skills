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
The first and last task were easy enough with the documentation, I got completely stuck on the second task because I was under the impression I had to line it up with the first "name". After I sorted that issue,, I googled how to print the output, this was also easy enough.
# Task troubleshooting
This took much longer than it should have, I was completely stuck on the second task, when someone pointed out the indentation error... 
# Task verification
![ansible-proof-1](/assets/task_2/ansible-proof-1.png)
![ansible-proof-2](/assets/task_2/ansible-proof-2.png)
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
This task was relatively easy, I feel confident in Python. I performed all the curl requests to make sure I could get the correct output, after that I started building a generic function to perform a request. Seeing that most of the requests shared a lot of information I created a menu to interact and perform different requests with the supplied information. This code is easily expanded on, taking more user input for different payloads, credentials, urls etc.

# Task troubleshooting
Only ran into some slight issues in formatting the JSON data, this took some time but was easily solved.

# Task verification
![task-5-proof-1](/assets/task_5/task-5-proof-1.png)
![task-5-proof-1](/assets/task_5/task-5-proof-2.png)
![task-5-proof-1](/assets/task_5/task-5-proof-3.png)

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
Getting the JSON to parse correctly was a huge challenge and took me several hours to troubleshoot, see troubleshooting for further information. After finally getting the code to work, I sought out how to output the response code and the output of the GET request in different variables. After getting the right output I added the flow control to check that the statuscode is between 200 and 300.
# Task troubleshooting
To verify the requests I used Postman and copied the script. For some reason I kept running into issues in my bash script, mainly due to variable unpacking. copying the Postman script verbatim seemed to work, but when introducing variables I kept running into issues with obscure error references. Finally I made it work by changing one variable at a time and each time running it.
# Task verification
![restconf-bash-proof](/assets/task_7/restconf-bash-proof.png)

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
