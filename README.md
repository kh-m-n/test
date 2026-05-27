# Test_Termin3 Report — DoY5BlockTeamF

## Project Overview

The purpose of these tests is to verify:

- Dashboard availability and frontend delivery
- Mission dispatch and vehicle selection logic
- RPC mission execution lifecycle
- Vehicle assignment compatibility and state transitions
- System status visibility
- Latency and stress performance

---

# Test Execution

## Deploy all Containers

```bash
docker compose up
```

## Run Selected Tests

```bash
pytest -v
```

---

# Test Summary

| Test Category | Test Count | Passed | Failed |
|---|---:|---:|---:|
| Dashboard API Tests | 4 | 4 | 0 |
| Dispatcher Tests | 6 | 6 | 0 |
| RPC Mission Tests | 2 | 2 | 0 |
| RPC Vehicle Tests | 3 | 3 | 0 |
| RPC Performance Tests | 2 | 2 | 0 |
| Status API Tests | 4 | 4 | 0 |
| TOTAL | 21 | 21 | 0 |

---

# 1. Dashboard API Tests

File:

```text
tests/test_dashboard_api.py
```

## Objective

Validate dashboard UI delivery and live map integration.

### Verified

- Dashboard HTML shell loads
- Static JS/CSS assets are reachable
- Structured map JSON is returned
- Legacy map page remains functional

## Tested Endpoints

| Endpoint | Method |
|---|---|
| /dashboard | GET |
| /dashboard.css | GET |
| /dashboard.js | GET |
| /map-data | GET |
| /map | GET |

## Test Cases

- test_dashboard_serves_static_application_shell  
- test_dashboard_assets_are_available  
- test_map_data_returns_structured_map_for_live_dashboard  
- test_legacy_map_page_remains_available  

---

# 2. Dispatcher Tests

File:

```text
tests/test_dispatcher.py
```

## Objective

Verify automatic mission dispatch and recovery behavior.

### Verified

- Correct vehicle type selection by incident and terrain
- Mission requeue after vehicle failure
- Mission completion updates incident state
- Vehicles become reusable after returning idle

### Vehicle Routing Matrix

| Incident | Area | Vehicle |
|---|---|---|
| person_detected | LAND | rover |
| person_detected | WATER | boat |
| vibration_alert | LAND | rover |
| water_level_alert | WATER | drone |

### Test Cases

- test_required_vehicle_type[person_detected-LAND-rover]  
- test_required_vehicle_type[person_detected-WATER-boat]  
- test_required_vehicle_type[vibration_alert-LAND-rover]  
- test_required_vehicle_type[water_level_alert-WATER-drone]  
- test_error_requeues_mission_until_vehicle_reports_idle  
- test_completed_mission_resolves_incident_and_releases_vehicle_on_idle  

---

# 3. RPC Mission Tests

File:

```text
tests/test_rpc_mission.py
```

## Objective

Validate mission assignment lifecycle.

### Verified

- Vehicle receives mission assignment
- Mission stores assigned vehicle
- Vehicle returns to idle after recovery

### Test Cases

- test_assign_mission_updates_vehicle_and_mission  
- test_vehicle_becomes_idle_again  

---

# 4. RPC Vehicle Tests

File:

```text
tests/test_rpc_vehicle.py
```

## Objective

Validate vehicle-side RPC acceptance rules.

### Verified

- Idle vehicles accept missions
- Busy vehicles reject new missions
- Incompatible missions are denied

### Test Cases

- test_vehicle_accepts_mission_when_idle  
- test_vehicle_rejects_second_mission_when_busy  
- test_vehicle_rejects_incompatible_mission  

---

# 5. RPC Performance Tests

Files:

```text
tests/test_rpc_latency.py
tests/test_rpc_stress.py
```

## Objective

Measure responsiveness and concurrent mission execution.

### Latency Validation

- End-to-end mission execution completes successfully

### Stress Validation

- Concurrent mission execution remains stable
- No mission loss during load
- System stays responsive under stress

### Test Cases

- test_end_to_end_mission_flow_latency  
- test_rpc_mission_flow_stress  

---

# 6. Status API Tests

File:

```text
tests/test_status_api.py
```

## Objective

Validate monitoring and service status endpoints.

### Verified JSON Response

- System returns HTTP 200
- JSON payload structure is valid
- Status endpoint is accessible

### Test Cases

- test_get_status_returns_200_and_json  

---

# Final Result

All selected Test Termin 3 scenarios completed successfully.

Result:

```text
PASSED: 21
FAILED: 0
SUCCESS RATE: 100%
```