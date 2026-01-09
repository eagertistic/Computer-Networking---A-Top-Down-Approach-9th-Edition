# 2.1 Principles of Network Applications

## key terms:

_Application Architectures_ : Designed by application developers

_Client-server Architecture_ : The server **services requests** from clients, while clients **do not communicate directly with each other**. Another characteristic of this architecture is that the server typically has a **fixed (well-known) IP address or domain name**. **Data centers** are designed to handle **large volumes of client requests** in this architecture.

\*P2P (Peer to Peer) Architecture : This architecture provides applications with **self-scalability**. By exploiting **direct connections between hosts**, it has **minimal or no reliance on dedicated servers**. Each peer can act as **both a client and a server**, sharing resources directly with other peers.

_API (Application Programming Interface)_ : An interface that allows the application layer to communicate with the transport layer within a host, enabling processes to exchange data with other end systems over the Internet. Application developers have limited control over the transport layer; they can only use the services provided by the chosen transport protocols (e.g., TCP) and configure a few transport-layer parameters, such as maximum buffer size and maximum segment size.

_IP and Port number_ : An IP address identifies the destination host on the network. Since a host may run multiple network applications simultaneously, a port number is used to identify the specific receiving process on that host.

_Services provided by transport-layer protocol_ and deciding which protocol to use:

- **Reliable data transfer** : ensure the data sent by one end of the application is delivered correctly and completely to the other end of the application.
- **Throughput** :For **bandwidth-sensitive applications**, the available throughput must be maintained at a required rate between the sending process and the receiving process during a session. However, **elastic applications** can make use of whatever throughput happens to be available.
- **Timing** : A constraint that the bits sent from the sending process to the receiving process’s socket must not be delayed beyond a given time limit.
- **Security** : A protocol that can encrypt and decrypt all data transmitted between the sending process and the receiving process is often favored. In addition to encryption, such a protocol can also provide data integrity and end-point authentication.

_TLC(Transport Layer Security)_ : A TCP enhancement implemented in the application layer of both client and server side.

_Application Layer Protocols_ :

- Define the type of messages exchanged
- Syntax of various message types
- Semantic of the fields (meaning of the information in the fields)
- Rules for determining when and how a process sends message and responds to messages.

**HTTP** is an important application layer protocol. It stands for **HyperText Transfer Protocol** and defines the format and sequence of messages exchanged between a web browser and a web server. In addition to HTTP, many applications use **proprietary protocols**, to restrict access and conceal internal communication details from the public domain.

**DASH (Dynamic Adaptive Streaming over HTTP)** is a video streaming protocol (Used by Netflix) that **splits media into small segments** and lets the client **dynamically switch quality levels over HTTP** based on current network conditions.

# 2.2 The Web and HTTP

## Key Terms:

_Web Page_ : a document consists of objects(a file that's addressable by an URL like a HTML file). Each URL has two components: a hostname of the server that houses the object and the object's path name. For example, http://www.someSchool.edu/someDepartment/picture.gif, www.someSchool.edu is the hostname and /someDepartment/picture.gif is the path name.

_Stateless Protocol_ : Because an HTTP server does not store any information about the state of its clients between requests, **HTTP is considered a stateless protocol**. For example, if a client requests the same object twice in a short period of time, the server processes each request independently, as if the previous request never occurred.

_Persistent Connections vs Non-Persistent Connections_ : A **persistent connection** uses the **same TCP connection** to send **multiple** client–server request/response pairs. In contrast, a **non-persistent connection** uses a **separate TCP connection for each request/response pair**.

_Round-Trip Time (RTT)_ : The time it takes for a packet to travel from client to server and back to the client.

_HTTP Request Message_ : An HTTP request message starts with a **request line** (e.g., `GET /index.html HTTP/1.1`). This is followed by **header lines**. The **request line** has three fields: the **method**, the **request target** (often a URL path), and the **HTTP version**.

_HTTP Response Message_ : An HTTP response message consists of an initial **status line**, followed by **header lines**, and an optional **entity body** that contains the **requested object** (e.g., an HTML page, image, JSON data). The **status line** has three fields: the **protocol version**, a **status code**, and a **reason phrase/status message** (e.g., `HTTP/1.1 200 OK`).

Common status codes and their associated phrases:

- `200 OK`: Request succeeded and the information is returned in the response.
- `301 Moved Permanently`: Requested object has been permanently moved; the new URL is specified in `Location`: header of the response message. The client software will automatically retrieve the new URL.
- `400 Bad Request`: This is a generic error code indicating that the request could not be understood by the server.
- `404 Not Found`: The requested document does not exist on this server.
- `505 HTTP Version Not Supported`: The requested HTTP protocol version is not supported by the server.
- `304 Not Modified`: It tells the browser that the copy of the object in the browser’s cache is current, and therefore there is no need to send the requested object.

In order to make sure that a cached object is up to date, both the HTTP GET request and the HTTP response messages use fields to help the server and the browser manage caching:
The cache-control field let the server specify how the content in the HTTP reply message should be cached. `Cache Control:no-store` directive instructs the browser to not cache/store the content locally Additionally, a server can explicitly instruct the browser about the amount of time that an object can remain in the cache. `Cache-Control: max-age=3600` tells the browser the content can be cached for 3600 seconds. `If-Modified-Since` is used to facilitate caching through a mechanism known as a **conditional GET** request. It lets the server know that the requested object is already stored in the browser cache and indicates the time when that object was last cached (or last modified).

_Quick UDP Internet Connections (QUIC) transport protocol_ :

![img1](assets/images/img1.png)
Developers can create a QUIC socket to establish connections. QUIC reduces the latency caused by the traditional double round-trip time (RTT) by integrating the TLS handshake directly into the initial connection setup. Additionally, when reconnecting, QUIC can reuse previously stored session and encryption parameters, allowing it to resume connections with lower latency without requiring a full handshake.

Additional benefits provided by QUIC:

- **Built-in Encryption:** QUIC integrates TLS directly into its protocol, providing encrypted communication by default.
- **Independent Data Stream** : Unlike TCP-based HTTP/2, where multiple streams can be blocked by packet loss due to _head-of-line blocking_ at the transport layer, QUIC manages streams independently. This means loss in one stream doesn’t necessarily delay others, and streams can be scheduled and **prioritized** based on application needs.
- **0-RTT handshake** : Data can be sent immediately for returning clients
- **Connection migration** : QUIC can keep a connection active even if the client’s IP address changes, because it identifies the connection using **Connection IDs (CIDs)** rather than relying on the IP/port pair.

_Network Cache Server_ : Also known as Proxy Servers

# 2.3 Electronic Mail in the Internet

## Key terms:

_Three major components of an Internet mail system_ :

- User Agent : Microsoft Outlook, Web-based Gmail (HTTP-based)
- Mail Servers: Mail servers store outgoing messages in an outgoing queue, and they store received messages in users’ mailboxes. The outgoing queue temporarily holds messages waiting to be delivered, while the mailbox maintains messages that have been delivered to the user.
- Simple Mail Transfer Protocol (SMTP) : A principle application-layer protocol which uses persistent TCP to transfer emails. There's no intermediate mail server in between.

_Internet Mail Access Protocol (IMAP)_ : is used to pull/retrieve emails from a mail server.

# 2.4 DNS-The Internet's Directory Service

## Key terms:

An IPv4 address is **32 bits (4 bytes)** long. It’s written in **dotted-decimal notation** as **four numbers separated by periods**, where each number represents **1 byte (8 bits)** and ranges from **0 to 255**. `121.7.106.83`

To reconcile the fact that people prefer using **hostnames** (like `example.com`) while routers forward traffic using **IP addresses**, the **Domain Name System (DNS)** is used to translate hostnames into IP addresses. The DNS is a distributed database in a hierarchy of DNS servers, and an application-layer protocol that allows hosts to query the distributed database.

In addition to hostname translation, DNS also provides following services:

- **Host aliasing**: DNS allows multiple alias hostnames to map to a single canonical hostname using **CNAME**. The canonical hostname is then resolved to an IP address using **A/AAAA** records.
- **Mail server aliasing** : DNS can map a domain name to its mail server(s) using **MX (Mail Exchange) records**, which specify which hostnames handle email for that domain (often with priorities). Those mail server hostnames then resolve to IP addresses via **A/AAAA** records.
- **Load distribution** : For a busy website, a single hostname can map to **multiple IP addresses**, each belonging to a replicated server (or load balancer). When clients query DNS, the DNS server may **rotate the order** of these IP addresses in its replies, so different clients tend to connect to different servers, helping distribute traffic.

_Resource Records(RRs)_ : A resource record is a four-tuple that contains the following fields:
`(Name, Value, Type, TTL)` where TTL refers to when a resource should be removed from a cache. The meaning of name and value depends on the type.

_Registrar_ : A commercial entity that sells and manages domain names(GoDaddy, Namecheap)

# 2.5 Video Streaming and Content Distribution Networks

## Key terms:

Video is formatted as a sequence of uncompressed, digitally encoded images, each consisting of an array of pixels. Each pixel is encoded using a number of bits to represent luminance and color. In order to have continuous playout, the network must provide an average end-to-end throughput that is at least as large as the bit rate of the compressed video.

_Content Distribution Networks (CDNs)_ : CDNs are B2B services that store and deliver content on behalf of companies so end users can access data from a geographically closer location. CDNs typically use a **pull strategy**: when a user requests an object that is not stored in the nearest CDN cluster, the cluster retrieves it from another cluster or the origin server and caches it. Over time, only frequently requested content is kept in the CDN caches.

_CDN Cluster Strategy_ : This mechanism dynamically directs clients to an appropriate server cluster or data center within a CDN. The **geographically closest strategy** uses geo-location databases to map the client’s LDNS (Local DNS) to the nearest cluster. However, the nearest cluster in terms of geography may still result in a network path with more hops. CDNs can carry out **real-time measurements** to assess current network traffic conditions by sending probes, such as ping messages, to the LDNS. However, this approach depends on the LDNS being able to respond to these probes.

# 2.6 Socket Programming: Creating Network Applications

## Key terms:

_Open_ : In computer networking, an open network application refers to a program whose operation is specified in a public protocol standard, allowing independently developed client-side and server-side programs to interoperate.

_Proprietary_ : The client and server programs employ a protocol that is not openly published as a standard. The developer has complete control over the protocol specification and its implementation.

_Port number_ : A port number identifies a specific application or service on a device. A network socket uses a port number so the operating system knows which application should send or receive the data.

_Welcoming socket and Connection socket_ : A **welcoming socket** listens for incoming client connection requests. After TCP completes the three-way handshake, the server accepts the connection and creates a dedicated connection socket for that client. This **connection socket** is then used to exchange bytes in both directions between the client and server.
