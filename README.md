# 🖥️ vFCL Monitoring GUI

### Raspberry Pi-Based Monitoring and Fault Visualization Platform for the Virtual Fault Current Limiting (vFCL) System

The vFCL Monitoring GUI is a Raspberry Pi-based application designed to provide real-time monitoring, visualization, and management of electrical fault events within the Virtual Fault Current Limiting (vFCL) ecosystem.

The application acts as a local monitoring station that receives telemetry and fault information through MQTT communication channels and displays device health, fault conditions, waveform data, and operational status through an intuitive graphical interface.

The platform is designed to work with a wide range of electrical systems and can be integrated with industrial inverters, power monitoring equipment, and fault detection devices.

---

# ⚡ Key Features

* 🖥️ Raspberry Pi-based GUI application
* 📡 Real-time MQTT communication
* ⚡ Electrical fault monitoring
* 📊 Waveform visualization
* 🔐 Device authentication and verification
* 📈 Device health monitoring
* 🔔 Real-time fault alerts
* 🔌 Inverter integration support
* ☁️ Secure communication with vFCL infrastructure
* 🏭 Industrial monitoring capabilities

---

# 🏗️ System Architecture

```text
Electrical System / Inverter
            │
            ▼
┌─────────────────────┐
│ ESP32 Fault Sensor  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Signal Sender       │
│ Raspberry Pi Edge   │
└──────────┬──────────┘
           │ MQTT
           ▼
┌─────────────────────┐
│ MQTT Broker         │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ vFCL Monitoring GUI │
│ Raspberry Pi        │
└─────────────────────┘
```

---

# 🔌 Inverter Integration

One of the primary objectives of the vFCL Monitoring GUI is to provide a universal monitoring platform that can be connected to different inverter systems and electrical installations.

The platform can:

* Monitor inverter fault conditions
* Display operational status
* Receive electrical fault notifications
* Visualize waveform data
* Track device health metrics
* Provide real-time alerts to operators

This flexibility allows the system to be deployed across multiple industrial and power distribution environments.

---

# 📊 Real-Time Monitoring

The GUI provides:

### Fault Monitoring

* Fault ON/OFF Status
* Fault Event Tracking
* Device Health Status

### Waveform Monitoring

* Signal Visualization
* Waveform Analysis
* Event Correlation

### Device Monitoring

* Connection Status
* Device Identification
* Telemetry Information

---

# 🔒 Security Features

* AES-256 encrypted communication support
* Device authentication
* API-key verification
* Secure MQTT integration
* Session management

Only authorized devices can communicate with the vFCL ecosystem.

---

# 🛠️ Technology Stack

### Software

* Python
* Tkinter
* MQTT
* JSON
* Matplotlib

### Hardware

* Raspberry Pi
* ESP32
* Industrial Inverters
* Electrical Fault Detection Devices

### Architecture

* Industrial IoT
* Edge Computing
* Real-Time Monitoring
* MQTT Publish/Subscribe

---

# 🎯 Applications

* Virtual Fault Current Limiting (vFCL) Systems
* Industrial Inverter Monitoring
* Electrical Fault Detection
* Smart Grid Monitoring
* Power Distribution Systems
* Industrial Automation
* Remote Equipment Monitoring

---

# 📖 Project Summary

Developed a Raspberry Pi-based Industrial IoT monitoring platform for the Virtual Fault Current Limiting (vFCL) System. Implemented MQTT-based real-time fault monitoring, inverter integration, waveform visualization, device authentication, and secure communication capabilities to provide operators with centralized visibility into electrical system health and fault conditions.


By AkshayKumar Nayee - Graduate Research Assistant & Dr.Fong Mak - Professor | Gannon University
