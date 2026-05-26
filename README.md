# DoY5BlockTeamF  
## Distributed Flood Response System — Sturmflut Nordsee

Distributed Systems Practical Course  
Hochschule Darmstadt — Sommersemester 2026

---

# Overview

This project implements a distributed disaster-response system for a fictional North Sea island after a severe storm flood.

The system simulates a central control center that coordinates:

- autonomous vehicles
- stationary sensors
- incident reporting
- infrastructure monitoring
- map visualization
- emergency management

The project is developed as part of the Distributed Systems practical course and is implemented incrementally across multiple milestones.

---

# Scenario

After a storm flood, the island infrastructure is partially damaged.

Different autonomous units operate across the island:

- drones
- rovers
- boats

Sensors and cameras continuously monitor the environment and report incidents such as:

- person detected
- high water level
- vibration alerts
- blocked routes

A central control center receives and manages all events and provides a live dashboard for monitoring the entire system.

---

# Current Milestone

## Aufgabe 1 — Control Center and REST Communication via TCP Sockets

Implemented features:

- Custom TCP-based HTTP server
- Manual HTTP request parsing
- REST API without external web frameworks
- Vehicle registration
- Sensor registration
- Incident management
- Dashboard and status visualization
- 20x20 island map
- Infrastructure representation
- Automated testing

---

# System Architecture

```text
                    +-------------------+
                    |     Dashboard     |
                    |  Browser Client   |
                    +---------+---------+
                              |
                              | HTTP GET
                              |
+-------------+     +---------v---------+      +-------------+
|   Sensors   |---->|   Control Center  |<-----|  Vehicles   |
| Cameras     |     |   TCP HTTP Server |      | Boat/Rover  |
| WaterSensor |     |                   |      | Drone       |
| Vibration   |     +-------------------+      +-------------+
+-------------+
```

---

# Components

## Control Center

Central management component of the system.

Responsibilities:

- HTTP request handling
- REST endpoint management
- unit registration
- incident management
- map management
- dashboard rendering
- system status aggregation

The HTTP server is implemented manually using TCP sockets.

No external web frameworks are used.

---

## Vehicles

The system currently supports three vehicle types:

| Vehicle | Description |
|---|---|
| Drone | Fast aerial vehicle |
| Rover | Ground-based exploration vehicle |
| Boat | Water-based transport vehicle |

Vehicles register themselves through the REST API.

---

## Sensors and Cameras

Different sensor types simulate environmental monitoring.

### Implemented Sensor Types

| Sensor | Purpose |
|---|---|
| Camera | Person detection |
| Water Sensor | Water level monitoring |
| Vibration Sensor | Structural vibration detection |

Sensors generate incidents based on threshold values or simulated measurements.

---

# Incident System

The control center processes incidents reported by sensors.

## Supported Incident Types

| Incident | Description |
|---|---|
| `person_detected` | Camera detects a person |
| `water_level_alert` | Water level exceeds threshold |
| `vibration_detected` | Dangerous vibration detected |

Incidents are stored and displayed in the dashboard and system status.

---

# REST API

The REST interface is implemented manually over raw TCP sockets.

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/unit` | Register vehicle or sensor |
| POST | `/incident` | Create incident |
| GET | `/status` | Get system status |
| GET | `/map` | Get island map |

---

# Example Requests

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
  }
}
```

---

# Island Map

The system contains a 20x20 grid-based island map.

Each field is either:

- land
- water

## Infrastructure

The map currently includes:

- 2 harbors
- 2 charging stations
- bridges
- roads and terrain zones

The map state is accessible through the dashboard and REST API.

---

# Dashboard

The dashboard provides a live overview of the system state.

## Displayed Information

- registered vehicles
- registered sensors
- active incidents
- infrastructure
- map overview
- unit positions
- incident details

The dashboard is served directly by the custom HTTP server and can be accessed from a browser.

---

# Technologies

| Technology | Usage |
|---|---|
| Python | Main implementation |
| TCP Sockets | HTTP communication |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| pytest | Automated testing |
| requests | API testing |
| threading | Concurrency testing |

---

# Project Structure

```text
.
├── control-center/
├── dashboard/
├── sensors/
├── vehicles/
├── tests/
├── reports/
├── docker-compose.yml
└── README.md
```

---

# Running the System

## Requirements

- Docker
- Docker Compose
- Python 3.14+

---

## Start Containers

```bash
docker compose up --build
```

---

## Access Dashboard

```text
http://127.0.0.1:8080
```

---

# Testing

Automated tests are implemented using `pytest`.

## Run Tests

```bash
pytest -v
```

---

## Generate HTML Test Report

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
- route validation

## Non-Functional Tests

- latency testing
- concurrent request testing
- burst load testing

---

# Example Test Result

```text
==============================
19 passed in 0.33s
==============================
```

---

# Design Decisions

## Manual HTTP Parsing

The project intentionally avoids external web frameworks to better understand:

- TCP communication
- HTTP protocol structure
- request parsing
- routing
- response generation

---

## Distributed Architecture

The system is designed as a distributed multi-component architecture where:

- sensors
- vehicles
- dashboard
- control center

can operate independently in separate containers.

---

# Future Milestones

Planned future extensions include:

- RPC-based vehicle dispatching
- MQTT event communication
- decentralized coordination algorithms
- battery and charging management
- autonomous routing
- distributed resource allocation
- fault tolerance mechanisms

---

# Authors

DoY5BlockTeamF  
Distributed Systems Practical Course  
Hochschule Darmstadt  
Sommersemester 2026
