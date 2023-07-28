# Web Infrastructure Design Project

## Task 0:
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



