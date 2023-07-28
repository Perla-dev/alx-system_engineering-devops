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
