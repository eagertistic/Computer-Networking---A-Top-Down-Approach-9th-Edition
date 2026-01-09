![img1](assets/images/img1.avif)

[^1]: Pieces of the internet

# Chapter 1.1 What is the Internet ?

## Key Terms

_Internet_ : The internet consists of multiple types of network systems, and they are interconnected with each other.

_Host/End system_: An edge device that sends and receives data over the Internet, such as a **client** or a **server**.

*packet*s : Packages of Information that are send through network to destination end system.

_Packet Switches_ : An important component that forwards data packets between end systems(hosts), such as **routers** and **linker-layer switches**.

_Communication Links_ : **Physical media** (e.g., coaxial cable, copper wire, optical fiber) and **wireless channels** (radio spectrum) used to carry/transfer information between devices.

_Path/Route_ : The **sequence of links** and **routers** that a packet travels from the sending end system to the receiving end system.

_Internet Service Providers (ISPs)_ : They provide internet access to end systems, such as BT.

_Protocols_ : A set of rules that define how end systems communicate with each other efficiently and reliably.

_Modem_: A device that demodulates signals(turns digital data into signals) and connects home network to ISP.

# Chapter 1.2 The network edge

## Key Terms

_Access Networks_ : It connects end system to the first router on the path to other systems.

_Digital subscriber line (DSL)_ : Uses existing copper telephone lines to carry **voice and Internet data simultaneously** by separating them into different **frequency bands** (frequency-division multiplexing), typically **three channels**: **one for voice**, **one for downstream data**, and **one for upstream data**.

_FTTH (Fiber to the Home)_ : It provides a direct optical fiber path from the central office to homes, enabling gigabit-per-second Internet speeds.

Fixed wireless Internet (FWI)\* : It delivers high-speed access wirelessly from a provider’s base station to a home modem.

_LEO satellites_ : It can provide broadband Internet in remote areas via satellites, with **lower latency (signal delay)** than **geostationary (GEO) satellites**.

_Ethernet_ : It uses twisted-pair copper wire to connect end systems to Ethernet switches, which then connect to the Internet.

Wireless LANs (Wi-Fi)\* : It allow users to connect to the network within a limited range from an access point.

# Chapter 1.3 The Network Core

## Key Terms

_Store-and-Forward Transmission/delays_ : A packet switch must receive the entire packet's bits before forwarding it to the next node/system.

![img2](assets/images/img2.png)

[^2]: delay formula for P packets sent over a series of N links

Assume the source end system or a packet switch is sending a packet of **L** bits over a link with **transmission** rate **R**. (L/R)

_output buffer/queue delays_ : Arriving packets may need to wait in a switch’s output buffer when the outgoing link is busy transmitting another packet. If the output buffer becomes full, either the arriving packet or one of the already-queued packets will be dropped(**packet loss**).

A router uses portion of destination address to index a forwarding table (which is set up by a number of special routing protocols) and determine the appropriate outbound link.

_Circuit switching_ : Unlike packet switching, the resources along the communication path between two end systems are **reserved** for the duration of the **dedicated end-to-end connection**. Switches on the path between the sender and receiver maintain connection state for the connection (**Circuit**), and the transmission rate is guaranteed to remain constant.

_Frequency-division multiplexing (FDM)_ : the link’s available **frequency range** is split into **multiple frequency bands**, and each connection (or channel/user) gets **one band** to send data.

_Time-division multiplexing(TDM)_ : Each connection gets **one time slot per frame**.

# Chapter 1.4 Delay, Loss, and Throughput in Packet-switched Networks

## Key Terms

_Throughput_ : The amount of data per second that can be transferred

_Processing delay_ : Time required to examine a packet's header, check for errors that occurred during the transmission, and directs the packet to the queue.

_Queuing delay_ : The time a packet waits in the queue before being transmitted onto the link, while other packets ahead of it finish transmission.

_Transmission delay_ : It's the time required for a host to push the entire packet onto the link before propagation begins. If the packet length is **L** bits and the transmission rate of the link is **R** bits per second, then the transmission delay is **L / R** seconds.

_Propagation delay_ : The time required to propagate from the beginning of the link to the next router is the propagation delay. If the propagation speed is **s** meters per second and the distance between two hosts is **m** meters, then the propagation delay is **m / s** seconds.

_Traffic intensity_ : Let a be the average packet arrival rate (packets/s), R the link transmission rate (bits/s), and assume each packet has length L bits. The average bit arrival rate is La bits/s. The traffic intensity is ρ=La/R​. If ρ>1, packets arrive faster than they can be transmitted, so the queue becomes unstable and the average queueing delay is unbounded. If ρ<1, the queuing delay depends on the traffic pattern (periodic vs. packets arriving in bursts).

![img3](assets/images/img3.png)
[^3]:Dependence of average queuing delay on traffic intensity

As the traffic intensity approaches 1, the average queuing delay increases rapidly. A small percentage increase in the intensity will result in a much larger percentage-wise increase in delay.

_instantaneous throughput_ : the **rate (bits/s)** at a particular instant that the receiver (end host) is **actually receiving data**.

_Bottleneck link_ : The end-to-end throughput of a path is limited by the link with the **minimum transmission rate** (the bottleneck) and by **intervening traffic** when multiple clients share a common link (e.g., in the Internet core).

# Chapter 1.5 Protocol Layers and Their Service Models

## Key Terms

_Application layer_ : The place where network application and their application-layer protocols reside.

_HTTP_ : A protocol which provides for Web document request and transfer

_SMTP_ : A protocol which provides for the transfer of e-mail.

_DNS_ : A protocol that translate human-friendly domain names into IP addresses.

_Transport layer_ : The layer where application-layer message are exchanged between application endpoints. There are two transport protocols: TCP and UDP.

_TCP_ : Provides a **connection-oriented** (sets up a connection before sending data) transport service. It offers **reliable, in-order delivery** of data between applications, plus **flow control** (matches sender rate to receiver capacity) and **congestion control** (adjusts sending rate based on network congestion).

_UDP_ : Provides a connectionless and no-frills service to its applications.

_Application Layer Responsibilities_ : It provides network application and application protocols. Such as message formatting.

_Protocol stack_ : A set of protocol layers used to transmit data over a network. Data starts at the **application layer** as an application-layer message. This message is encapsulated by the **transport layer**, which adds a transport-layer header, forming a **transport-layer segment**. The segment is then encapsulated by the **network layer**, which adds a network-layer header containing the source and destination IP addresses, creating a **network-layer datagram**. Finally, the datagram is encapsulated by the **link layer**, which adds a link-layer header to form a **frame** for transmission over the physical medium. At each layer, the packet consists of two main parts: a **header** and a **payload**, where the payload is typically the packet received from the layer above.

# Chapter 1.6 Networks under Attack

## Key terms

_DoS_ : denial-of-service attacks which renders a network, host, or other piece of infrastructure unusable by legitimate users. Dos is mainly fall into three categories:

- _Vulnerability Attack_ : An attack in which an adversary sends **well-crafted (malicious) messages** to an application or operating system on a target host in order to **exploit a software vulnerability** and cause unintended behavior.
- _Bandwidth Flooding_ : An attack in which an attacker sends a **deluge of packets** to a target host so that the **access link becomes congested**, preventing **legitimate packets from reaching the server**.
- _Connection Flooding_ : An attack in which an attacker establishes a large number of half-open or fully open TCP connections at the target host. The host can become so bogged down with these bogus connections that it stops accepting legitimate connections.

_Passive Sniffier_ : A malicious device **placed within range of a wireless transmitter** that **silently listens to the channel** and obtains a copy of every packet transmitted, without altering or injecting any traffic.

_IP Spoofing_ : An intent to **fake the source IP address** in packets so the traffic _looks like it’s coming from someone else_.
