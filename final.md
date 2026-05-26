# DoY5BlockTeamF  
## Distributed Flood Response System for a North Sea Island

Distributed Systems Practical Course  
Hochschule Darmstadt — Sommersemester 2026

---

# Overview

This repository contains the implementation of a distributed disaster-response system developed for the Distributed Systems practical course at Hochschule Darmstadt.

The project simulates emergency coordination on a fictional North Sea island after a severe storm flood. Multiple distributed components communicate over different protocols to monitor the environment, report incidents, coordinate autonomous vehicles, and visualize the current system state through a browser-based dashboard.

The system is intentionally implemented using low-level communication primitives such as raw TCP sockets and manually parsed HTTP requests in order to better understand the internal mechanics of distributed communication systems.

---

# Project Goals

The project focuses on:

- distributed system architecture
- inter-process communication
- custom HTTP communication
- REST-based service interaction
- RPC communication
- event-driven incident management
- infrastructure monitoring
- containerized deployment
- automated testing
- reproducibility and observability

The system is developed incrementally throughout the semester and continuously extended with new distributed communication mechanisms.

---

# Scenario

After a storm flood, the island infrastructure becomes partially damaged and inaccessible.

A central control center coordinates:

- autonomous vehicles
- environmental sensors
- emergency incidents
- infrastructure monitoring
- island visualization

Sensors continuously monitor the island and generate alerts when dangerous situations occur. Vehicles are intended to react to incidents and operate across different terrain types.

The entire system is deployed as distributed services running in separate containers.

---

# Implemented Milestone

## Aufgabe 1 — Leitstelle und Registrierung via Sockets, HTTP und REST

The current implementation includes:

- custom TCP-based HTTP server
- manual HTTP parsing
- REST API implementation without frameworks
- registration of vehicles and sensors
- incident creation and management
- dashboard visualization
- island map representation
- browser-rendered monitoring interface
- automated functional tests
- automated non-functional tests
- latency and concurrency measurements
- Docker-based deployment

The repository already contains the foundations for future milestones including RPC communication using Protocol Buffers.

---

# System Architecture

```text
                                    +----------------------+
                                    |      Dashboard       |
                                    |  Browser Interface   |
                                    +----------+-----------+
                                               |
                                               | HTTP GET
                                               |
+------------------+          +----------------v----------------+
|      Sensors     |--------->|         Control Center          |
|------------------|          |--------------------------------|
| Camera Sensors   |          | Custom TCP HTTP Server         |
| Water Sensors    |          | HTTP Parsing & Routing         |
| Vibration Sensor |          | REST API                       |
+------------------+          | Incident Management            |
                              | Vehicle Registration           |
                              | Status Aggregation             |
                              | Map Management                 |
                              +----------------+---------------+
                                               |
                                               |
                                               v
                                   +----------------------+
                                   |      RPC Layer       |
                                   | Protocol Buffers     |
                                   +----------------------+

                    +----------------+----------------+
                    |                |                |
                    v                v                v

             +-------------+  +-------------+  +-------------+
             |    Drone    |  |    Rover    |  |     Boat    |
             +-------------+  +-------------+  +-------------+
```

---

# Core Components

## Control Center

The control center is the central component of the system and acts as the main coordination and communication service.

Responsibilities include:

- accepting TCP connections
- parsing HTTP requests
- request routing
- REST endpoint handling
- registration of vehicles and sensors
- incident management
- dashboard rendering
- island map management
- system status aggregation

The HTTP server is implemented manually without using Flask, FastAPI, Django, or other HTTP frameworks.

### Important Modules

| Module | Purpose |
|---|---|
| `tcpserversocket.py` | Low-level TCP socket server |
| `parsing.py` | Manual HTTP request parsing |
| `routes.py` | Route management |
| `handlers.py` | Endpoint request handling |
| `state.py` | Shared system state |
| `status.py` | Global status generation |

---

## Dashboard

The dashboard provides a browser-accessible visualization of the current system state.

### Endpoint

```text
GET /dashboard
```

The dashboard is generated dynamically by the custom HTTP server and rendered directly inside a web browser.

### Dashboard Features

The dashboard visualizes:

- registered vehicles
- active sensors
- incidents
- map overview
- infrastructure elements
- system statistics
- unit positions
- incident details
- overall control center state

The dashboard demonstrates browser-compatible HTTP rendering without external web frameworks.

---

## Vehicles

The system currently supports three autonomous vehicle types.

| Vehicle | Description |
|---|---|
| Drone | Fast aerial unit |
| Rover | Ground-based exploration unit |
| Boat | Water-based transport unit |

Vehicles register themselves through the REST API and are managed by the control center.

The repository already contains the foundations for future RPC-based vehicle coordination.

---

## Sensors

Different sensor types monitor the environment and automatically generate incidents when thresholds are exceeded.

### Implemented Sensor Types

| Sensor | Purpose |
|---|---|
| Camera Sensor | Person detection |
| Water Sensor | Water level monitoring |
| Vibration Sensor | Structural vibration monitoring |

Sensors simulate environmental measurements and continuously interact with the control center.

---

# Incident Management

The system supports centralized incident processing and monitoring.

## Supported Incident Types

| Incident Type | Description |
|---|---|
| `person_detected` | Person detected by camera |
| `water_level_alert` | Water level exceeded threshold |
| `vibration_detected` | Dangerous structural vibration detected |

Each incident contains:

- unique incident ID
- source sensor ID
- message
- priority
- position
- incident type

Incidents are stored in the global system state and displayed in the dashboard.

---

# Island Map

The project contains a dynamically managed island map.

## Map Properties

| Property | Value |
|---|---|
| Grid Size | 20 × 20 |
| Terrain Types | Land / Water |

Each map cell represents either:

- land
- water

---

# Infrastructure

The map includes predefined infrastructure required for rescue and logistics operations.

## Implemented Infrastructure

| Infrastructure | Count |
|---|---|
| Harbors | 2 |
| Charging Stations | 2 |
| Bridges | Multiple |

Infrastructure information is integrated into the map and dashboard visualization.

---

# Communication Technologies

The project intentionally combines multiple communication technologies commonly used in distributed systems.

| Technology | Usage |
|---|---|
| TCP Sockets | Low-level HTTP communication |
| HTTP | Browser communication |
| REST API | Registration and incident handling |
| RPC | Vehicle coordination foundation |
| Docker Networking | Inter-container communication |
| Protocol Buffers | RPC interface definition |

---

# REST API

The REST interface is implemented manually using raw TCP sockets and custom request parsing.

## Supported Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/unit` | Register vehicle or sensor |
| POST | `/incident` | Create incident |
| GET | `/status` | Retrieve global system state |
| GET | `/map` | Retrieve island map |
| GET | `/dashboard` | Open monitoring dashboard |

---

# Example API Requests

## Register Vehicle

```http
POST /unit
Content-Type: application/json

{
  "id": "drone-1",
  "unit": "vehicle",
  "vehicle_type": "drone",
  "position": {
    "x": 2,
    "y": 3
  }
}
```

---

## Register Sensor

```http
POST /unit
Content-Type: application/json

{
  "id": "camera-1",
  "unit": "sensor",
  "sensor_type": "camera",
  "position": {
    "x": 10,
    "y": 12
  }
}
```

---

## Create Incident

```http
POST /incident
Content-Type: application/json

{
  "id": "incident-1",
  "incident_type": "person_detected",
  "source_id": "camera-1",
  "message": "Person near bridge",
  "position": {
    "x": 10,
    "y": 12
  },
  "priority": 2
}
```

---

# RPC Layer

The repository already contains the RPC foundation for future milestones.

## RPC Components

| File | Purpose |
|---|---|
| `rpc_server.py` | RPC server implementation |
| `mission.proto` | Protocol Buffers definition |

The RPC layer is intended for:

- mission assignment
- distributed coordination
- vehicle communication
- remote procedure execution

---

# Project Structure

```text
DoY5BlockTeamF/
│
├── app/
│   ├── control_center/
│   ├── dashboard/
│   ├── sensors/
│   ├── vehicles/
│   ├── common/
│   └── rpc/
│
├── tests/
├── docs/
├── proto/
├── assets/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Technologies

| Technology | Purpose |
|---|---|
| Python | Main implementation |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| TCP Sockets | Low-level networking |
| pytest | Automated testing |
| requests | REST API testing |
| threading | Concurrency testing |
| Protocol Buffers | RPC interface definitions |

---

# Running the System

## Requirements

- Docker
- Docker Compose
- Python 3.14+

---

# Start the System

```bash
docker compose up --build
```

---

# Access the Dashboard

Open in browser:

```text
http://127.0.0.1:8080/dashboard
```

---

# Testing

The repository contains automated functional and non-functional tests.

---

# Run All Tests

```bash
pytest -v
```

---

# Generate HTML Test Report

```bash
pytest --html=reports/latest_report.html --self-contained-html
```

---

# Implemented Tests

## Functional Tests

- vehicle registration
- sensor registration
- incident creation
- duplicate prevention
- invalid request handling
- unsupported method handling
- unknown route validation
- dashboard endpoint validation

---

## Non-Functional Tests

- latency measurement
- average response-time testing
- concurrent request handling
- burst request testing
- stability measurements

---

# Example Test Result

```text
==============================
19 passed in 0.33s
==============================
```

---

# Design Decisions

## Manual HTTP Implementation

The project intentionally avoids external web frameworks in order to better understand:

- TCP communication
- HTTP protocol structure
- socket handling
- request parsing
- routing
- response generation
- low-level distributed communication

---

## Distributed Architecture

The system is designed as a distributed multi-component architecture where:

- sensors
- vehicles
- dashboard
- RPC services
- control center

operate as independent logical components.

---

## Containerization

The project uses Docker and Docker Compose to ensure:

- reproducible deployments
- isolated execution environments
- simplified distributed setup
- consistent testing environments

---

# Future Milestones

Planned future extensions include:

- RPC-based mission assignment
- MQTT-based event communication
- decentralized coordination algorithms
- battery and charging management
- autonomous routing
- distributed synchronization
- fault tolerance mechanisms
- distributed locking algorithms
- load balancing strategies

---

# Testing Documentation

Detailed testing documentation and reports are available in:

```text
tests/
docs/
reports/
```

---

# Authors

DoY5BlockTeamF  
Distributed Systems Practical Course  
Hochschule Darmstadt  
Sommersemester 2026