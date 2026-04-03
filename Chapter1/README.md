
![[4e1fc950d27ec1b498b1e46b98dfc96a.avif]]

[^1]: Pieces of the internet



# Chapter 1.1 What is the Internet ? 

## Key Terms

*Internet* : The internet consists of multiple types of network systems, and they are interconnected with each other. 

*Host/End system*: An edge device that sends and receives data over the Internet, such as a **client** or a **server**. 

*packet*s : Packages of Information that are send through network to destination end system.  

*Packet Switches* : An important component that forwards data packets between end systems(hosts), such as **routers** and **linker-layer switches**.

*Communication Links* : **Physical media** (e.g., coaxial cable, copper wire, optical fiber) and **wireless channels** (radio spectrum) used to carry/transfer information between devices.

*Path/Route* : The **sequence of links** and **routers** that a packet travels from the sending end system to the receiving end system. 

*Internet Service Providers (ISPs)* : They provide internet access to end systems, such as BT. 

*Protocols* : A set of rules that define how end systems communicate with each other efficiently and reliably.

*Modem*: A device that demodulates signals(turns digital data into signals) and connects home network to ISP. 


# Chapter 1.2 The network edge 

## Key Terms

*Access Networks* : It connects end system to the first router on the path to other systems. 

*Digital subscriber line (DSL)* : Uses existing copper telephone lines to carry **voice and Internet data simultaneously** by separating them into different **frequency bands** (frequency-division multiplexing), typically **three channels**: **one for voice**, **one for downstream data**, and **one for upstream data**.

*FTTH (Fiber to the Home)* : It provides a direct optical fiber path from the central office to homes, enabling gigabit-per-second Internet speeds. 

Fixed wireless Internet (FWI)* : It delivers high-speed access wirelessly from a provider’s base station to a home modem.

*LEO satellites* : It can provide broadband Internet in remote areas via satellites, with **lower latency (signal delay)** than **geostationary (GEO) satellites**. 

*Ethernet* : It uses twisted-pair copper wire to connect end systems to Ethernet switches, which then connect to the Internet.

Wireless LANs (Wi-Fi)* : It allow users to connect to the network within a limited range from an access point.

# Chapter 1.3 The Network Core

## Key Terms

*Store-and-Forward Transmission/delays* :  A packet switch must receive the entire packet's bits before forwarding it to the next node/system.


![[Pasted image 20251213001303.png]]

[^2]: delay formula for P packets sent over a series of N links 

Assume the source end system or a packet switch is sending a packet of **L** bits over a link with **transmission** rate **R**. (L/R)

*output buffer/queue delays* : Arriving packets may need to wait in a switch’s output buffer when the outgoing link is busy transmitting another packet. If the output buffer becomes full, either the arriving packet or one of the already-queued packets will be dropped(**packet loss**).

A router uses portion of destination address to index a forwarding table (which is set up by a number of special routing protocols) and determine the appropriate outbound link. 

*Circuit switching* : Unlike packet switching, the resources along the communication path between two end systems are **reserved** for the duration of the **dedicated end-to-end connection**. Switches on the path between the sender and receiver maintain connection state for the connection (**Circuit**), and the transmission rate is guaranteed to remain constant. 

*Frequency-division multiplexing (FDM)* : the link’s available **frequency range** is split into **multiple frequency bands**, and each connection (or channel/user) gets **one band** to send data.

*Time-division multiplexing(TDM)* : Each connection gets **one time slot per frame**.




# Chapter 1.4 Delay, Loss, and Throughput in Packet-switched Networks

## Key Terms

*Throughput* : The amount of data per second that can be transferred 

*Processing delay* : Time required to examine a packet's header, check for errors that occurred during the transmission, and directs the packet to the queue. 

*Queuing delay* : The time a packet waits in the queue before being transmitted onto the link, while other packets ahead of it finish transmission.

*Transmission delay* : It's the time required for a host to push the entire packet onto the link before propagation begins. If the packet length is **L** bits and the transmission rate of the link is **R** bits per second, then the transmission delay is **L / R** seconds.

*Propagation delay* : The time required to propagate from the beginning of the link to the next router is the propagation delay. If the propagation speed is **s** meters per second and the distance between two hosts is **m** meters, then the propagation delay is **m / s** seconds.

*Traffic intensity* : Let a be the average packet arrival rate (packets/s), R the link transmission rate (bits/s), and assume each packet has length L bits. The average bit arrival rate is La bits/s. The traffic intensity is ρ=La/R​. If ρ>1, packets arrive faster than they can be transmitted, so the queue becomes unstable and the average queueing delay is unbounded. If ρ<1, the queuing delay depends on the traffic pattern (periodic vs. packets arriving in bursts).


![[Pasted image 20251219154936.png]]
[^3]:Dependence of average queuing delay on traffic intensity

As the traffic intensity approaches 1, the average queuing delay increases rapidly. A small percentage increase in the intensity will result in a much larger percentage-wise increase in delay. 



*instantaneous throughput* : the **rate (bits/s)** at a particular instant that the receiver (end host) is **actually receiving data**. 

*Bottleneck link* : The end-to-end throughput of a path is limited by the link with the **minimum transmission rate** (the bottleneck) and by **intervening traffic** when multiple clients share a common link (e.g., in the Internet core).


# Chapter 1.5 Protocol Layers and Their Service Models 

## Key Terms 


*Application layer* : The place where network application and their application-layer protocols reside. 

*HTTP* : A protocol which provides for Web document request and transfer 

*SMTP* : A protocol which provides for the transfer of e-mail. 

*DNS* : A protocol that translate human-friendly domain names into IP addresses. 

*Transport layer* : The layer where application-layer message are exchanged between application endpoints. There are two transport protocols: TCP and UDP. 

*TCP* : Provides a **connection-oriented** (sets up a connection before sending data) transport service. It offers **reliable, in-order delivery** of data between applications, plus **flow control** (matches sender rate to receiver capacity) and **congestion control** (adjusts sending rate based on network congestion).

*UDP* : Provides a connectionless and no-frills service to its applications. 

*Application Layer Responsibilities* : It provides network application and application protocols. Such as message formatting. 

*Protocol stack* : A set of protocol layers used to transmit data over a network. Data starts at the **application layer** as an application-layer message. This message is encapsulated by the **transport layer**, which adds a transport-layer header, forming a **transport-layer segment**. The segment is then encapsulated by the **network layer**, which adds a network-layer header containing the source and destination IP addresses, creating a **network-layer datagram**. Finally, the datagram is encapsulated by the **link layer**, which adds a link-layer header to form a **frame** for transmission over the physical medium. At each layer, the packet consists of two main parts: a **header** and a **payload**, where the payload is typically the packet received from the layer above.



# Chapter 1.6 Networks under Attack 

## Key terms 

*DoS* : denial-of-service attacks which renders a network, host, or other piece of infrastructure unusable by legitimate users. Dos is mainly fall into three categories: 

* *Vulnerability Attack* : An attack in which an adversary sends **well-crafted (malicious) messages** to an application or operating system on a target host in order to **exploit a software vulnerability** and cause unintended behavior. 
* *Bandwidth Flooding* : An attack in which an attacker sends a **deluge of packets** to a target host so that the **access link becomes congested**, preventing **legitimate packets from reaching the server**.
* *Connection Flooding* : An attack in which an attacker establishes a large number of half-open or fully open TCP connections at the target host. The host can become so bogged down with these bogus connections that it stops accepting legitimate connections. 

*Passive Sniffier* : A malicious device **placed within range of a wireless transmitter** that **silently listens to the channel** and obtains a copy of every packet transmitted, without altering or injecting any traffic.

*IP Spoofing* : An intent to **fake the source IP address** in packets so the traffic _looks like it’s coming from someone else_.


