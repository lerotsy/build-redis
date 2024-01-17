[![progress-banner](https://backend.codecrafters.io/progress/redis/a2e232f6-41c5-45fc-b3e9-36d8857e45cc)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)
# Python Redis Server

A lightweight Redis-like server implementation in Python with limited functionality.

## Introduction

This project is a simple Redis-like server written in Python. It is not intended to be a full-fledged production-ready Redis server, but rather a minimalistic version that implements some of the core functionalities of Redis for educational purposes or for simple use-cases.

## Features

The server supports the following commands:

- `PING`: Checks the connection to the server. The server replies with `PONG`.
- `ECHO`: Returns the given string back to the client.
- `SET`: Sets a string value in the server's data store under the specified key.
- `GET`: Retrieves the string value of a key from the server's data store. If the key does not exist, `(nil)` is returned.
- `EXPIRE`: Sets a key's time to live in seconds. After the timeout has expired, the key will automatically be deleted.
- `TTL`: Queries the time to live of a key.

## Future Improvements

Potential future improvements could include more Redis functionalities, such as:

- Additional data types (lists, sets, sorted sets, hashes)
- Persistence to disk
- Transactions
- Pub/Sub capabilities
- More complex commands like `INCR`, `DECR`, `MSET`, etc.

## Usage

To start the server, run the `app.py` file. By default, the server listens on `127.0.0.1:6379`.

```bash
python app.py
