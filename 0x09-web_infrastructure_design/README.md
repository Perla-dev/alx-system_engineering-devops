# Web Infrastructure Design Project

## Task 0: Simple web stack
1. `What is a server?`: A server is a computer or system that manages access to centralized resources or services in a network.
2. `What is the role of the domain name?` A domain name is a human-friendly address that points to a server's IP address. Here, 'foobar.com' points to the server's IP address (8.8.8.8).
3. `What type of DNS record 'www' is in 'www.foobar.com'?` 'www' is a subdomain and typically it's an A or CNAME record in DNS.
What is the role of the web server (Nginx)? Nginx accepts the HTTP request from the client and forwards it to the appropriate application server.
4. `What is the role of the application server?` The application server runs the web application code (your code base), which might interact with the database.
5. `What is the role of the database (MySQL)?` The MySQL database stores and retrieves data as requested by the application server.
6. `What is the server using to communicate with the user's computer?` The server is using the HTTP/HTTPS protocol to communicate with the user's computer.

### Issues:

* `SPOF (Single Point of Failure):` If the single server fails, the whole website will be inaccessible.
* `Downtime when maintenance needed:` If you need to update the website code, you might need to restart the server, causing downtime.
* `Cannot scale if too much incoming traffic:` If the website receives too much traffic, the single server might not be able to handle all the requests, leading to slow response times or even crashes.



## Task 1: Distributed web infrastructure

1- `Why additional elements?` We add a load balancer and an additional application server to handle increased traffic and provide redundancy. If one server fails, the other can continue to provide service, reducing downtime and improving reliability.

2- `Load balancer distribution algorithm:` The load balancer could use several algorithms, such as Round Robin, Least Connections, or IP Hash. Round Robin, for example, distributes client requests evenly across all servers, while Least Connections assigns more requests to servers with fewer active connections.

3- `Active-Active vs Active-Passive setup:` In an Active-Active setup, traffic is distributed across all servers, while in an Active-Passive setup, the passive server only comes into play if the active server fails. Our setup is Active-Active, allowing us to utilize the resources of both servers and providing redundancy.

4- `Primary-Replica (Master-Slave) database cluster:` This involves one Primary (Master) database that receives all write operations and one or more Replica (Slave) databases that replicate the Primary's data and handle read operations. This can improve performance and provide data redundancy.

5- `Primary vs Replica node:` The Primary node (master) is responsible for handling write operations, while the Replica node (slave) synchronizes with the master and can handle read operations. In case the Primary node fails, the Replica can step in to avoid downtime.

### issues

* `SPOF (Single Point of Failure):` While we have mitigated some points of failure by adding a load balancer and an extra server, the database and load balancer themselves are single points of failure. If either goes down, it could cause significant problems.

* `Security Issues:` Without a firewall, our servers are vulnerable to unauthorized access. Additionally, if we don't use HTTPS, the data exchanged between the user and our servers is not encrypted and could be intercepted.

* `No Monitoring:` Without a system to monitor the performance and health of our servers, we might not become aware of issues until they have caused significant problems.

## Task 2: Secured and monitored web infrastructure

2- `Firewalls:` Firewalls are crucial for our infrastructure security. They provide a barrier against unauthorized access, monitor, and control network traffic based on predefined security rules.
3- `SSL Certificate:` Serving traffic over HTTPS is essential to ensure all data exchanged between users and our servers is encrypted and secure. It prevents data breaches and enhances user trust in our website.
4- `Monitoring Clients:` These are used for monitoring server performance and identifying potential issues in real-time. This can aid in proactive problem resolution, capacity planning, and maintaining an optimum user experience.
The monitoring tool collects data through the installed clients on the servers. They gather metrics like CPU usage, memory consumption, network statistics, and log files, then send them to a centralized monitoring service for analysis.

* To monitor your web server QPS (Queries Per Second), you should configure your monitoring client to collect this specific metric from your web server. This data can help you understand your web server's load and performance.

### issues:

* `SSL Termination at Load Balancer:` If the traffic between the load balancer and the application servers isn't encrypted, it's vulnerable to attacks within the internal network.

* `Single MySQL Write Server:` If this server fails, no application can make data changes until the server is restored, causing potential service disruption.

* `Identical Server Components:` Servers with identical roles (database, web server, application server) can lead to inefficient resource use. Dedicating specific servers to specific tasks can help in optimizing resource use and performance.

## Task 3: Scale up

1- `Additional Server:` With only one server, the system would have a single point of failure. By adding an additional server, we are adding redundancy, thereby improving the system's reliability. It also improves performance as now the load can be distributed between servers.

2- `Load Balancer (HAproxy) Cluster:` The clustering of HAproxy is to ensure high availability and reliability. If one load balancer goes down, the other can take its place, keeping the system up and running. It also helps in distributing the load among multiple servers, improving performance.

3- `Split Components:` Splitting components into their own servers makes it easier to manage and scale the system. If there's a high load on the application, you can simply scale up the application server without having to touch the database or web server, and vice versa. It also improves security, as an issue in one server won't directly affect the other servers.
