# decrypt-oclean-traffic
Oclean Mobile Application decryptor

Oclean Mobile Application 2.1.2 communicates with an external website using HTTP so it is possible to eavesdrop the network traffic. The content of HTTP payload is encrypted using XOR with a hardcoded key, which allows for the possibility to decode the traffic.
