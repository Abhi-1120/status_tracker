# Status Tracker

This project is a messaging system that tracks and processes status updates using RabbitMQ for communication, MongoDB for storage, and Python 3.12 for implementation. It includes components for producing messages, consuming messages, and querying stored data via an API.

## Features

* **Message Producer:** Generates and publishes random status updates to RabbitMQ.
* **Message Consumer:** Listens to RabbitMQ messages, processes them, and stores the data in MongoDB.
* **API Endpoint:** Provides an HTTP-based interface to fetch status counts for a specific time range.

## Prerequisites

Ensure the following are installed and properly configured:

* **Python 3.12**
* **RabbitMQ:** A running RabbitMQ server instance.
* **MongoDB:** A running MongoDB server instance.


## Installation

1. **Clone the Repository**

```bash
git clone git@github.com:Abhi-1120/status_tracker.git
cd status_tracker
```

2. **Install Dependencies Install the required Python packages using pip:**

```bash
pip install -r requirements.txt
```

3. **Start RabbitMQ and MongoDB**

* Make sure RabbitMQ is running on localhost at port 15672.
* Start MongoDB on localhost at port 27017.


## Project Structure

* **producer.py:** Publishes random status messages to RabbitMQ.
* **consumer.py:** Listens to RabbitMQ and stores messages in MongoDB.
* **get_status.py:** Exposes an API endpoint to query status counts.
* **requirements.txt:** Lists all the Python dependencies.


## Usage

1. **Start the Producer**

Run the producer.py script to send messages to RabbitMQ:

```bash
python producer.py
```

2. **Start the Consumer**

Run the consumer.py script to send messages to RabbitMQ:

```bash
python consumer.py
```

3. **Run the API Server**

Start the API server from get_status.py to query the stored data:

```bash
python get_status.py
```
The API server will be available at http://localhost:5555.

