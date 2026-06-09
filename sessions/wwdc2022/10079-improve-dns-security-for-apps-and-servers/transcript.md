---
id: "wwdc2022-10079"
event: "wwdc2022"
title: "Improve DNS security for apps and servers"
url: "https://developer.apple.com/videos/play/wwdc2022/10079"
language: "eng"
words: 1745
---

# Improve DNS security for apps and servers — Transcript

[Session page](https://developer.apple.com/videos/play/wwdc2022/10079) · [Metadata](metadata.json) · [Structured JSON](transcript.json)

**[0:09]** Qiaoyu Deng: Hello. Welcome to “Improve DNS security for apps and servers.” My name is Qiaoyu Deng. In this video, we are going to talk about why DNS is often not secure and how to protect it using DNSSEC and encrypted DNS with DDR. First, let’s talk about why DNS is not secure. DNS is the phone book of the internet. It translates domain names, which are human readable and easy to remember,

**[0:57]** to IP addresses, which are made for machines. Other internet protocols, such as TCP, TLS, and QUIC, rely on having an IP address, so everything starts with DNS. Today, TLS is widely used to secure internet communication. That’s great, but DNS, the foundational layer, has some security issues. DNS is historically not secure. It was designed back in 1983 with few security considerations. In the years since, many DNS attacks have been created.

**[1:46]** One example is DNS cache poisoning, where the attacker exploits flaws of DNS resolvers and make them cache incorrect IP addresses, causing clients to connect to malicious hosts. This reveals one vulnerability of DNS: it is unauthenticated. Traditional DNS clients today have no way to validate answers, so they can easily be spoofed. Another common attack is DNS sniffing, where the attacker watches DNS traffic between a client and a DNS server,

**[2:32]** collecting the client's history. This is a serious problem for user privacy. The reason this attack is possible is that DNS traffic was originally unencrypted. In order to be a secure starting point for the protocols that build on top of it, DNS needs to be both authenticated and encrypted. When we use DNSSEC to sign DNS response, it provides authentication. When we use TLS and HTTPS to encrypt DNS resolution, it ensures privacy.

**[3:18]** Next, let’s talk about DNSSEC. DNSSEC is a suite of extension specifications created by IETF. Many DNS service providers already support it, but client support is still ramping up. iOS 16 and macOS Ventura now support client side DNSSEC validation. DNSSEC ensures the authentication of data by adding digital signatures. It protects data integrity. It authenticates denial of existence when answers do not exist.

**[4:04]** It also provides cryptographic authentication. DNSSEC protects data integrity by attaching signatures in responses. If a response is altered by an attacker, the signature of the altered data will not match the original one. In that case, the client can detect the altered response and discard it. DNSSEC also asserts the existence and nonexistence of records in a zone, by using special types of DNS records such as the NSEC record. The NSEC record tells you what the next record name is,

**[4:52]** securely, in alphabetical order. The names listed by it are the ones that exist, and any name not listed does not exist. For example, we have three NSEC records here. The record set reveals that zone org only has three record names, A.org, C.org, and E.org. Now, if there is an attacker that says A.org does not exist, the client can detect this attack. A.org does exist because it is listed in the first NSEC record.

**[5:39]** Likewise, if an attacker says that D.org exists, the client can also detect that, because according to the second NSEC record, D.org is in between C.org and E.org and no name should exist in between the two names. DNSSEC authenticates records by establishing a chain of trust. Here is an example. A device wants to resolve www.example.org with DNSSEC validation enabled. It sends queries asking for the IP addresses,

**[6:25]** signatures, and keys. With the responses, the trust relationship can be built from the IP addresses to key number 1. Then the client sends queries to the parent zone, org, asking for the records that can be used to authenticate key number 1, so it can build the trust relationship from key number 1 to key number 2. So the device repeats this process recursively, until it has reached the root. Now, if the root key, which is key number 3 in the diagram, can be trusted, the trust relationship from the IP addresses

**[7:12]** to key number 3 can be authenticated. The hash of the root key is always stored in the device securely. In DNSSEC, it is called the root trust anchor. If the hash of key number 3 matches the pre-installed anchor, a trust chain can be established securely. With the trust chain, the IP addresses of www.example.org are now authenticated. If you want to require DNSSEC validation in your apps, here are the things you need to do. Support IPv6 for your domains.

**[7:58]** In an IPv6-only environment, IPv4-only addresses are translated into synthetic IPv6 addresses. If domains are signed, synthesized addresses cannot pass DNSSEC validation; they are unreachable with DNSSEC enabled. So make sure that your domains support IPv6. Make sure your DNS service provider signs your domain with DNSSEC. If you enable DNSSEC in your app without signing your domain, you will get no benefit, but you will get additional DNS traffic and extended resolution time

**[8:46]** to attempt authentication for your unsigned domain. Once you have the corresponding infrastructure support, here is the code needed to adopt DNSSEC for your apps. If you are an NSURLSession client, you can require DNSSEC validation for your URL request. Here is an example. You will first create a default session configuration. Then you will require DNSSEC validation. Next, you will create the session with the modified configuration. It enables DNSSEC for all URL requests

**[9:33]** created from this session. If you do not want to enable DNSSEC for the entire session, you can also do this at the request level. First, create a session with the default configuration where DNSSEC validation is disabled. Then enable it in the request. Now, this session task will only be started when DNSSEC validation is completed. If you are a Network.framework client, you can also require DNSSEC validation for your connections. First, when you create a parameters object,

**[10:20]** require DNSSEC validation. Then create the NWConnection with the parameters object. Now, when you start your connection, it will only move into the ready state when the DNSSEC validation has completed and a connection to the validated IP address has been established. When DNSSEC is enabled, only the validated addresses will be used to establish a connection. In HTTPS, errors are reported through the APIs. In DNSSEC, no error is returned for the validation failure.

**[11:06]** Receiving a response that fails validation is equal to not receiving any response. If there is a DNS provider that tampers with the response, the addresses will not pass the authentication check, so they will be discarded directly. When the device joins a new network where the DNS provider is not tampering with responses, the validation will make progress again and the resolution will be back to normal automatically. Here are a few cases that can cause DNSSEC failure. When the original DNS response is altered,

**[11:51]** the mismatched signature will not pass the DNSSEC check, causing a validation failure. When the device is unable to reach any pre-installed trust anchor and unable to establish a trust chain from it. When the network does not support the necessary protocols required by DNSSEC, such as DNS over TCP and EDNS0 option, that carries the DNSSEC enablement bit. When the signed domain does not support IPv6, the synthesized IPv6 addresses

**[12:38]** provided by the internet service provider will fail the validation. So that’s how to authenticate DNS responses with DNSSEC, but if they are still unencrypted, anyone on the network can see them. Next, we will talk about how to enable DNS encryption automatically with DDR. In iOS 14 and macOS Big Sur, we introduced encrypted DNS to help preserve privacy. You can use NEDNSSettingsManager in an app

**[13:24]** or DNSSettings in a profile to manually configure encrypted DNS system-wide. You can also opt into encrypted DNS for your app using the PrivacyContext on NWParameters. For more information, please watch "Enable encrypted DNS." New in iOS 16 and macOS Ventura, encrypted DNS can be used automatically. If your network supports Discovery of Designated Resolvers, also called DDR, DNS queries will automatically use TLS or HTTPS.

**[14:10]** To use encrypted DNS, your device needs to know that a resolver supports TLS or HTTPS, and it may need to learn a port or URL path as well. Common mechanisms such as DHCP or Router Advertisements only provide a plain IP address. DDR is a new protocol developed in the IETF by Apple working with other industry partners. It provides a way for DNS clients to learn this necessary information

**[14:55]** by using a special DNS query. When your device joins a new network, it will issue a Service Binding query for “_dns.resolver.arpa”. If the DNS server supports DDR, it will reply with one or more configurations. Then, the device uses this information to set up an encrypted connection to the designated resolver. It verifies that the IP address of the unencrypted resolver is included in the TLS certificate of the designated resolver. This is done to ensure that the unencrypted resolver

**[15:43]** and the encrypted one belong to the same entity. If everything looks good, the device now uses encrypted DNS by default. DDR applies to a single network at a time. Your device will use encrypted DNS automatically only if the current network supports it. It's also important to note that DDR does not work if your DNS server's IP address is a private IP address. This is because such IP addresses are not allowed in TLS certificates, since their ownership cannot be verified.

**[16:32]** In iOS 16 and macOS Ventura, we also support the ability to specify client authentication when using encrypted DNS for a configuration setup, using NEDNSSettingsManager or the DNSSettings profile. Client authentication allows encrypted DNS servers to be used in enterprise environments where servers need to validate clients before allowing access. You can now configure a client certificate using the identityReference property of NEDNSSettings. This behaves just like client certificates for VPNs.

**[17:22]** These can apply to both DNS over TLS and DNS over HTTPS. This is the path to securing DNS. Sign your domain with DNSSEC and require DNSSEC validation in your apps to authenticate your IP addresses. Enable DDR on your network so that the clients can switch to encrypted DNS automatically for better user privacy. Adopt client authentication in enterprises where better access control is needed. I am looking forward to a more secure DNS foundation

**[18:10]** that you help to build in the future. Thanks for watching!
