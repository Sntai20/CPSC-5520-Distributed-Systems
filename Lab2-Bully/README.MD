# Bully Algorithm


## Specification

The goal is to implement the Bully election algorithm for distributed algorithms.

### Local

The complete list of flags is:

```bash
# Run the following in Lab2-Bully/
pip install -r requirements.txt
```

```bash
python3 run.py -h
```

### Local Testing Expected output

Start of gcd2

python3 Lab2-Bully/tests/gcd2.py 23633
Wait 0.25 seconds for the server to start listening

End of gcd2

Start of Members

python3 Lab2-Bully/tests/member1.py localhost 23633 2022-11-01 1234561
This is the message we are sending ('JOIN', ((20, 1234561), ('127.0.0.1', 55661)))
This is the message we are receiving {(20, 1234561): ('127.0.0.1', 55661), (50, 1234568): ('127.0.0.1', 55644), (20, 1234567): ('127.0.0.1', 55645), (24, 1234566): ('127.0.0.1', 52917)}

python3 Lab2-Bully/tests/member2.py localhost 23633 2022-12-01 1234568
This is the message we are sending ('JOIN', ((50, 1234568), ('127.0.0.1', 55663)))
This is the message we are receiving {(20, 1234561): ('127.0.0.1', 55661), (50, 1234568): ('127.0.0.1', 55663), (20, 1234567): ('127.0.0.1', 55645), (24, 1234566): ('127.0.0.1', 52917)}


End of Members

Start of lab2

python3 Lab2-Bully/lab2.py localhost 23633 2022-11-01 1234567
This is the message we are sending ('JOIN', ((20, 1234567), ('127.0.0.1', 55664)))
in start_election
(20, 1234561)
(50, 1234568)
(20, 1234567)
(24, 1234566)
Member's Process ID (50, 1234568) is higher than mine (20, 1234567). Send them a message.

End of lab2

Shutting down the gcd2 server.
