# MLops Task - 3
# Automating Machine Learning with DevOps : ML + Jenkins + Docker + Github
With the help of the Git plugin Jenkins can easily pull source code from any Git repository that the Jenkins build node can access.

The GitHub plugin extends upon that integration further by providing improved bi-directional integration with GitHub. Allowing you to set up a Service Hook which will hit your Jenkins instance every time a change is pushed to GitHub.
Jenkins's job creation is an effortless process, In this article, we will learn how to create a job in Jenkins and configure project cloning from the Git.

## Creating Docker File

![Screenshot (20)](https://user-images.githubusercontent.com/60083481/83323590-85587500-a27d-11ea-86db-11caa3950abe.png)

### Creatimg Docker container
docker build -t cnn newcnn:v1 /ws/

## Creating the Github to push the ML program

![Screenshot (23)](https://user-images.githubusercontent.com/60083481/83323977-bb96f400-a27f-11ea-8258-1ae72d6504e9.png)

# JOB 1 :
## Pull the codes from the Github when the Developer pushes the code .

![Screenshot (24)](https://user-images.githubusercontent.com/60083481/83324313-0ca7e780-a282-11ea-8eb7-75722c7cab98.png)
![Screenshot (28)](https://user-images.githubusercontent.com/60083481/83324584-df5c3900-a283-11ea-9370-092388f01452.png)

### Creating enviroment
![Screenshot (27)](https://user-images.githubusercontent.com/60083481/83324613-0f0b4100-a284-11ea-9df9-4d7d80472909.png)

# Job 2:
## Check the code for being a Deep learning code and then Launch the Docker image

![Screenshot (28)](https://user-images.githubusercontent.com/60083481/83325284-cb670600-a288-11ea-8678-5d0af72bb69b.png)
![Screenshot (29)](https://user-images.githubusercontent.com/60083481/83325286-ce61f680-a288-11ea-93f4-fcefb5628359.png)

# Job 3:
## If the tweaking parameters are still left and accuracy hasn't been achieved then tweak and trigger job 2 . Otherwise , trigger Job 4 for merging the code to master branch of Github.

![Screenshot (32)](https://user-images.githubusercontent.com/60083481/83747354-1fedf500-a67e-11ea-8cbd-33e98b079e07.png)
![Screenshot (33)](https://user-images.githubusercontent.com/60083481/83747486-5297ed80-a67e-11ea-96ce-506d2f453007.png)

# Job 4:
## When the Job 3 triggers , then merge the code onto GitHub master branch .
![Screenshot (36)](https://user-images.githubusercontent.com/60083481/83747899-f71a2f80-a67e-11ea-86f0-51d03c3ffe9d.png)
![Screenshot (33)](https://user-images.githubusercontent.com/60083481/83748210-7576d180-a67f-11ea-926c-b6895f31b9ba.png)
![Screenshot (34)](https://user-images.githubusercontent.com/60083481/83748362-b5d64f80-a67f-11ea-957c-3ba609b18686.png)

# Job5
## Monitors the Docker . If the container stops suddenly due to some failure , then restart it.
![Screenshot (39)](https://user-images.githubusercontent.com/60083481/83749348-30539f00-a681-11ea-8093-afe3ca738081.png)
    
So , these are all the setting and management for creating the whole system.
These are following above mentioned steps I did to complete my MLops Task 3.  
Yashmit Sharma  
MLops Volunteer
