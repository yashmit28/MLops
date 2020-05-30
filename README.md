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

# Job :2
## Check the code for being a Deep learning code and then Launch the Docker image

![Screenshot (28)](https://user-images.githubusercontent.com/60083481/83325284-cb670600-a288-11ea-8678-5d0af72bb69b.png)
![Screenshot (29)](https://user-images.githubusercontent.com/60083481/83325286-ce61f680-a288-11ea-93f4-fcefb5628359.png)
