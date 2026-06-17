# 🖥️ vFCL Device Management Dashboard

### Centralized Monitoring and Device Provisioning Platform for the Virtual Fault Current Limiting (vFCL) System

The vFCL Device Management Dashboard is a desktop-based monitoring and device provisioning application developed to manage, authenticate, configure, and monitor IoT devices deployed within the Virtual Fault Current Limiting (vFCL) ecosystem.

The platform provides a secure interface for device onboarding, user authentication, device verification, encrypted data exchange, and real-time monitoring of electrical fault events received through MQTT communication channels.

The dashboard acts as the operational control center of the vFCL platform, enabling engineers and operators to monitor device health, fault conditions, telemetry data, and waveform information from a centralized interface.

---

# 🚀 Key Features

* 🔐 User Authentication & Access Control
* 🏷️ Device Registration & Verification
* 🔑 API Key-Based Device Authorization
* 📡 MQTT-Based Real-Time Communication
* 📊 Live Fault Status Monitoring
* 📈 Waveform Visualization Dashboard
* 🔒 AES-256 Device File Encryption Integration
* ☁️ Device-to-Platform Secure Communication
* 🖥️ Real-Time Device Health Monitoring
* 📅 Session Management & Device Tracking

---

# 🏗️ System Architecture

```text
Electrical System
        │
        ▼
┌───────────────────────┐
│ ESP32 Fault Detector  │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Raspberry Pi Device   │
│ Signal Sender Module  │
└───────────┬───────────┘
            │ MQTT
            ▼
┌───────────────────────┐
│ MQTT Communication    │
│ Publish / Subscribe   │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ vFCL Dashboard        │
│ Management Platform   │
└───────────┬───────────┘
            │
            ├── User Login
            ├── Device Verification
            ├── Device Health
            ├── Fault Monitoring
            ├── Waveform Display
            └── Security Controls
```

---

# 🔐 Authentication Workflow

The dashboard implements a multi-stage authentication and verification process.

### Step 1 – User Login

Users authenticate using platform credentials.

```text
Username + Password
        │
        ▼
Authentication Server
        │
        ▼
Access Token Generated
```

### Step 2 – Device Verification

Each device must be verified before it can participate in the vFCL network.

Verification is performed using:

* Device MAC Address
* Device API Key
* User Access Token

```text
MAC Address
      +
API Key
      +
User Token
      │
      ▼
Verification Service
      │
      ▼
Approved Device
```

---

# 📡 MQTT Communication Layer

The dashboard subscribes to MQTT topics and receives:

* Fault Events
* Device Status Updates
* Health Metrics
* Waveform Data
* Telemetry Information

Real-time updates are displayed immediately on the monitoring interface.

---

# 📊 Dashboard Features

### Device Monitoring

* Device Status
* Connection State
* Last Synchronization Time
* Device Identification

### Fault Monitoring

* Fault Status (ON/OFF)
* Health Status
* Fault Occurrence Tracking
* Event History

### Waveform Visualization

* Electrical Signal Visualization
* Real-Time Graph Updates
* Fault Pattern Observation

### Device Health

* Operational Status
* Connectivity State
* Telemetry Availability

---

# 🔒 Security Integration

The dashboard integrates with the vFCL Security Module.

Supported security features include:

* AES-256 Encrypted File Transfers
* Device Authentication
* API Key Validation
* Session Management
* Secure MQTT Communication
* Access Token Validation

Only authorized devices can transmit data to the platform.

---

# 📂 Project Structure

| Component      | Description                               |
| -------------- | ----------------------------------------- |
| `app.py`       | Application entry point                   |
| `controllers/` | Navigation and application control logic  |
| `views/`       | User interface screens                    |
| `models/`      | API communication and device models       |
| `mqtt/`        | MQTT communication and encryption modules |
| `common/`      | Shared utilities and constants            |
| `session.json` | Session persistence                       |
| `data.json`    | Device and telemetry data                 |

---

# 🖥️ User Interface Modules

### 🔑 Login Screen

Allows operators to authenticate with platform credentials.

### 📱 Device Verification Screen

Used to:

* View Device MAC Address
* Enter API Keys
* Register Devices
* Verify Device Authorization

### 📊 Device Dashboard

Provides:

* Live Device Status
* Fault Monitoring
* Telemetry Information
* Waveform Visualization
* Device Health Tracking

---

# 🛠️ Technology Stack

### Frontend

* Python Tkinter
* Matplotlib
* JSON

### Backend Integration

* REST APIs
* Authentication Services
* Device Verification Services

### Communication

* MQTT
* Publish / Subscribe Architecture

### Security

* AES-256 Encryption
* API Key Authentication
* Session Management

### Hardware Integration

* Raspberry Pi
* ESP32 Microcontroller
* vFCL Monitoring Devices

---

# 🎯 Role Within the vFCL Ecosystem

The vFCL Device Management Dashboard serves as the operational interface between field devices and platform administrators.

It provides centralized control over:

* Device onboarding
* Device verification
* Security enforcement
* Fault monitoring
* Telemetry visualization
* System health management

This dashboard acts as the command center for the entire Virtual Fault Current Limiting (vFCL) infrastructure.

---

# 📖 Project Summary

Designed and developed a desktop-based Industrial IoT management platform for the Virtual Fault Current Limiting (vFCL) System. Implemented secure user authentication, device verification, MQTT-based real-time monitoring, telemetry visualization, and AES-256 security integration to provide centralized management and monitoring of distributed electrical fault detection devices.


By AkshayKumar Nayee - Graduate Research Assistant | Gannon University &  Dr.Fong Mak (Professor)
