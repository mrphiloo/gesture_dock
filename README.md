# Gesture Dock: Workload Management of Docker Containers through Hand Gesture Recognition

## Description
Gesture Dock is an innovative project that enables the management of Docker containers using hand gestures. By leveraging AWS services, OpenCV, and the cvzone hand tracking module, users can launch and manage Docker containers on an EC2 instance through intuitive hand gestures. This system aims to simplify container orchestration, enhance user interaction, and provide a hands-free management solution for Docker containers.

## Use Cases
1. **Hands-Free DevOps Management:**
	DevOps engineers can manage Docker containers without needing to manually type commands, improving efficiency and reducing the risk of errors.

2. **Educational Demonstrations:**
	Educators can use this project to demonstrate the capabilities of machine learning and cloud computing in a visually engaging and interactive way.

3. **Accessibility Solutions:**
	Users with limited mobility can manage Docker containers using hand gestures, providing a more accessible solution for container orchestration.

## Prerequisites
- AWS account with necessary permissions
- Python 3.x installed
- OpenCV and cvzone libraries installed
- AWS CLI configured with necessary IAM roles

## Steps to Set Up the Project

### 1. Create an EC2 Instance
- Install Docker:
  ```bash
  sudo yum update -y
  sudo yum install docker -y
  sudo service docker start
  sudo systemctl enable docker

- Add an IAM role with `AmazonSSMFullAccess` policy to the EC2 instance

## 2. Create a Lambda Function
- Create a Lambda Function with Python
- Use the following code in `lambda_code.py`
- Assign an IAM role with `AmazonSSMFullAccess` policy to the Lambda function. 

## 3. Create an API Gateway
- Create a REST API.
- Add a GET Method with the endpoint `/docker`

## 4. Automate with Python Code
- Use the following code in `main.py` to automate the process
NOTE: Run this code on your local Machine

## How to Use
1. Follow the setup instructions to configure your AWS environment and EC2 instance.
2. Deploy the Lambda function with the provided code.
3. Create the API Gateway with the specified endpoint.
3. Run the main.py script to start the hand gesture recognition and launch Docker containers based on recognized gestures.


## Contact
If anything is not working or needs changes, connect with me on [LinkedIn](https://www.linkedin.com/in/mrphiloo/).

