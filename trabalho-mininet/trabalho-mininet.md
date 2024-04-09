---
lang: pt-BR
---

# Trabalho mininet aprendizado

Considere uma topologia tree com profundidade (depth=3) e ramificação (fanout=3).

Com uso de linha de comando padrão do Mininet, crie a topologia considerando o
endereço MAC padronizado, larguras de banda bw de 35Mbps e controlador do
Mininet (não precisa especificar);

```bash
$ sudo -E mn --topo=tree,depth=3,fanout=3 --mac --link tc,bw=35
mininet>
```

Inspecione informações das interfaces, endereços MAC, IP e portas através de
linhas de comando;

```bash
$ pingall
*** Ping: testing ping reachability
h1 -> h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h2 -> h1 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h3 -> h1 h2 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h4 -> h1 h2 h3 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h5 -> h1 h2 h3 h4 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h6 -> h1 h2 h3 h4 h5 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h7 -> h1 h2 h3 h4 h5 h6 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h8 -> h1 h2 h3 h4 h5 h6 h7 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h9 -> h1 h2 h3 h4 h5 h6 h7 h8 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h10 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h11 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h12 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h13 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h14 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h15 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h16 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h17 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27
h18 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h19 h20 h21 h22 h23 h24 h25 h26 h27
h19 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h20 h21 h22 h23 h24 h25 h26 h27
h20 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h21 h22 h23 h24 h25 h26 h27
h21 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h22 h23 h24 h25 h26 h27
h22 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h23 h24 h25 h26 h27
h23 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h24 h25 h26 h27
h24 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h25 h26 h27
h25 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h26 h27
h26 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h27
h27 -> h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26
*** Results: 0% dropped (702/702 received)
$ h1 ifconfig
h1-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.1  netmask 255.0.0.0  broadcast 10.255.255.255
        ether 00:00:00:00:00:01  txqueuelen 1000  (Ethernet)
        RX packets 11856  bytes 123985632 (123.9 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 11367  bytes 750702 (750.7 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
$ h2 ifconfig
h2-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.2  netmask 255.0.0.0  broadcast 10.255.255.255
        ether 00:00:00:00:00:02  txqueuelen 1000  (Ethernet)
        RX packets 11692  bytes 764352 (764.3 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 11519  bytes 123971190 (123.9 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
$ nodes
c0 h1 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h2 h20 h21 h22 h23 h24 h25 h26 h27 h3 h4 h5 h6 h7 h8 h9 s1 s10 s11 s12 s13 s2 s3 s4 s5 s6 s7 s8 s9
```

Execute testes de ping entre os diferentes nós.

```bash
$ h2 ping 10.0.0.10 -c 5
PING 10.0.0.10 (10.0.0.10) 56(84) bytes of data.
64 bytes from 10.0.0.10: icmp_seq=1 ttl=64 time=0.795 ms
64 bytes from 10.0.0.10: icmp_seq=2 ttl=64 time=0.074 ms
64 bytes from 10.0.0.10: icmp_seq=3 ttl=64 time=0.074 ms
64 bytes from 10.0.0.10: icmp_seq=4 ttl=64 time=0.075 ms
64 bytes from 10.0.0.10: icmp_seq=5 ttl=64 time=0.079 ms

--- 10.0.0.10 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4086ms
rtt min/avg/max/mdev = 0.074/0.219/0.795/0.287 ms
$ h10 ping 10.0.0.2 -c 5
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=1.42 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.376 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.139 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.053 ms
64 bytes from 10.0.0.2: icmp_seq=5 ttl=64 time=0.051 ms

--- 10.0.0.2 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4075ms
rtt min/avg/max/mdev = 0.051/0.407/1.418/0.519 ms
```

Especifique que o host 1 na porta 5555 vai ser um servidor TCP e o host 2 um
cliente e execute testes de iperf, considere um relatório por segundo com teste
de 20 segundos. Faça os testes para larguras de banda bw de 15 Mbps.

```bash
# h1
$ iperf -s -p 5555 -i 1
------------------------------------------------------------
Server listening on TCP port 5555
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  4] local 10.0.0.1 port 5555 connected with 10.0.0.2 port 58730
[ ID] Interval       Transfer     Bandwidth
[  4]  0.0- 1.0 sec  1.88 MBytes  15.8 Mbits/sec
[  4]  1.0- 2.0 sec  1.88 MBytes  15.7 Mbits/sec
[  4]  2.0- 3.0 sec  1.88 MBytes  15.8 Mbits/sec
[  4]  3.0- 4.0 sec  1.87 MBytes  15.7 Mbits/sec
[  4]  4.0- 5.0 sec  1.88 MBytes  15.8 Mbits/sec
[  4]  5.0- 6.0 sec  1.87 MBytes  15.7 Mbits/sec
[  4]  6.0- 7.0 sec  1.88 MBytes  15.8 Mbits/sec
[  4]  7.0- 8.0 sec  1.87 MBytes  15.7 Mbits/sec
[  4]  8.0- 9.0 sec  1.90 MBytes  15.9 Mbits/sec
[  4]  9.0-10.0 sec  1.86 MBytes  15.6 Mbits/sec
[  4] 10.0-11.0 sec  1.86 MBytes  15.6 Mbits/sec
[  4] 11.0-12.0 sec  1.89 MBytes  15.9 Mbits/sec
[  4] 12.0-13.0 sec  1.88 MBytes  15.8 Mbits/sec
[  4] 13.0-14.0 sec  1.86 MBytes  15.6 Mbits/sec
[  4] 14.0-15.0 sec  1.87 MBytes  15.7 Mbits/sec
[  4] 15.0-16.0 sec  1.87 MBytes  15.7 Mbits/sec
[  4] 16.0-17.0 sec  1.89 MBytes  15.9 Mbits/sec
[  4] 17.0-18.0 sec  1.86 MBytes  15.6 Mbits/sec
[  4] 18.0-19.0 sec  1.88 MBytes  15.7 Mbits/sec
[  4] 19.0-20.0 sec  1.86 MBytes  15.6 Mbits/sec
[  4]  0.0-20.0 sec  37.5 MBytes  15.7 Mbits/sec

# h2
$ iperf -c 10.0.0.1 -p 5555 -i 1 -t 20 -b 15M
------------------------------------------------------------
Client connecting to 10.0.0.1, TCP port 5555
TCP window size:  136 KByte (default)
------------------------------------------------------------
[  3] local 10.0.0.2 port 58732 connected with 10.0.0.1 port 5555
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0- 1.0 sec  2.00 MBytes  16.8 Mbits/sec
[  3]  1.0- 2.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3]  2.0- 3.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3]  3.0- 4.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3]  4.0- 5.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3]  5.0- 6.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3]  6.0- 7.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3]  7.0- 8.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3]  8.0- 9.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3]  9.0-10.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3] 10.0-11.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3] 11.0-12.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3] 12.0-13.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3] 13.0-14.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3] 14.0-15.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3] 15.0-16.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3] 16.0-17.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3] 17.0-18.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3] 18.0-19.0 sec  1.88 MBytes  15.7 Mbits/sec
[  3]  0.0-20.0 sec  37.5 MBytes  15.7 Mbits/sec
```
