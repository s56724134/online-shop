# 🛒 Barney

Barney is an online store project based on **Flask**, managed through **Docker** containerization, and using **MySQL** as the backend database. **The project is currently in development**, and below are the progress and future plans."

## 🏗️ Development Progress 
The following features have been implemented in the project so far：
### Homepage:
- Currently, the basic design of the homepage has been completed, including the display of different sections as shown below.

![homepage1](https://github.com/user-attachments/assets/b499d93a-1db3-4e6a-a994-98d0239820b4)
![homepage2](https://github.com/user-attachments/assets/29ada74e-f730-41f9-8e30-c27ac600c127)
![homepage3](https://github.com/user-attachments/assets/ef8fa7b2-f25d-45a5-930a-467507ba2b66)

### Login page:
- Currently, the design of the login page has been completed, and the basic layout is set up, though no functional features have been implemented yet.

![Login](https://github.com/user-attachments/assets/28e4f222-544d-4137-8c59-5d57282c6532)

   
Features under development: 
- Registration
- Login
- Permission management

## 🚧 Pending Features
- 🛍️ Product Browsing and Search
- 🛒 Shopping Cart Functionality
- 💳 Payment Integration (Third-Party Payment Integration)
- 👤 User Registration / Login / Access Control
- 📦 Order Management System
- 🤖  Smart Customer Service Feature

## 🖥️ Technical Architecture
- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MySQL
- **Container Management**: Docker, Docker Compose
- **Version Control**: Git / GitHub

## ⚙️ Installation & Setup

### **Prerequisites**
Ensure that Docker and Docker Compose are installed on your system:
- **Windows & macOS**  
    - Install [Docker Desktop](https://www.docker.com/)  
    - Docker Compose is included in Docker Desktop, no additional installation is needed.

- **Linux**  
    - Install [Docker](https://docs.docker.com/engine/install/)  
    - If Docker Compose is not included, install it manually:  

      ```sh
      sudo apt-get install docker-compose -y  # Ubuntu/Debian
      ```
### **1️⃣ Clone the repository**
```sh
git clone https://github.com/s56724134/online-shop.git
cd online-shop
```

### **2️⃣ Build and start the project**
```sh
docker-compose up --build -d
```

### **3️⃣ Verify that the services are running**
Check the running containers:
```sh
docker ps
```
If everything is working properly, you should see output similar to this:
```sh
CONTAINER ID   IMAGE           STATUS         PORTS                   NAMES
123456789abc   barney_flask    Up 10 minutes  0.0.0.0:5000->5000/tcp  flask-app
987654321xyz   mysql:latest    Up 10 minutes  3306/tcp                mysql
```

### **4️⃣ Access the application**
Once you have the flask container ID, use the following command to enter the container:
```sh
# Please replace <flask-container-id> with the actual Flask container ID. You can find the ID by running `docker ps`.
docker exec -it <flask-container-id> bash
```
Once inside the container, you should see a prompt like:
```sh
root@221e419488c9:/app# 
```
Now, you can run the application by executing:
```sh
python main.py
```

### **5️⃣ Stop the application**
To stop all running containers:
```sh
docker-compose down
```


               




