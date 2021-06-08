### README 0x0C Web Server 

### Web Server

Web Servers use HTTP *((Hypertext Transer Protocol)* and other protocols to respond to client requests. 
Web servers support **HTTP**, **SMTP**, and **FTP**.  Web servers uses include email, downloading requests for FTP and building and and serving webpages.  

### 5 BASIC STEPS of a Server Query

1.) client sends a request to server
2.) server looks for file requested
3.) server must at least provide an error message
4.) if file is found, server returns file to client
5.) if file is not found, server returns error message to client

### DNS
## A records
**'A' records** maps a domain name to an IP address.  An 'A' record uses a domain name to find the IP address of a computer connected to the internet. The 'A' in 'A record' stands for **address**.

you can use **dig** A api. and the web address to provide information about the address.

```$ dig A api.dnsimple.com

; <<>> DiG 9.8.3-P1 <<>> A api.dnsimple.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 5792
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;api.dnsimple.com.		IN	A

;; ANSWER SECTION:
api.dnsimple.com.	59	IN	A	208.93.64.253

;; Query time: 80 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Sun Jul 31 22:21:31 2016
;; MSG SIZE  rcvd: 50
```
## CNAME record
Canonical Name Record is a resource record in the domain Name System that maps one domaine name to another.  CNAME records must always point to another domain= name, never to an IP address. 
*example: toys.com, puzzles.com, and games.com can all be aliases of the CNAME toysRus.com*

## TXT record
TXT record is a resource record in the DNSA which provides the ability to associate arbitrarty text to a DNS.  Such as a human readable text about a server, network, data center etc. 
*example: example.com IN TXT "This domain is reserved for documentation"*

 
