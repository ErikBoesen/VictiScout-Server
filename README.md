# VictiScout-Server

Server for [VictiScout](https://github.com/frc1418/VictiScout).

## How this server works
Instead of using a complicated framework like MongoDB, this server is a simple in/out system. Data is recieved from `POST` requests to the address `[Host computer's IP]:8080/api/data`. Data is then stored in the file `data.json`. When a `GET` request is submitted to that same address, the contents of `data.json` are sent in response. This whole process is handled by the [VictiScout application](https://github.com/frc1418/VictiScout).

## Dependencies
* Python 3
* Assorted python dependencies. To install:

        pip install -r requirements.txt

    Append `--user` to that command if you don't have administrator privileges.

## Using
Run the server by typing:

        python server.py

## Credits
* [Erik Boesen](https://github.com/ErikBoesen) - Main developer
* [Tom Orth](https://github.com/atf1999) - Original server framework