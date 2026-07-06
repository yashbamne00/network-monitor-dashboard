\# Network Monitoring Dashboard



\## Overview



The \*\*Network Monitoring Dashboard\*\* is a Python-based system monitoring application that continuously collects information about a Linux machine and presents it through a simple web dashboard. The project combines system administration concepts with Python programming to provide real-time visibility into the health of a server.



The application monitors hardware usage, network connectivity, and Linux services while storing collected metrics in JSON format. A Flask web application reads this information and displays it in an interactive dashboard with charts and status indicators.



This project demonstrates how modern monitoring systems work by separating \*\*data collection\*\* from \*\*data visualization\*\*, making the design modular, scalable, and easy to maintain.



\---



\## Problem Statement



System administrators and DevOps engineers need to know whether a server is healthy, reachable, and running correctly. Instead of manually checking CPU usage, memory, disk space, network activity, or service status, a monitoring system automates these tasks and presents the information in one place.



This project provides a lightweight monitoring solution suitable for learning Linux administration, Python automation, and web development.



\---



\## Objectives



\* Monitor the overall health of a Linux system.

\* Collect hardware and network performance metrics.

\* Measure network latency to important hosts.

\* Check whether important services are running.

\* Store monitoring data in a structured format.

\* Display live information through a web dashboard.

\* Generate logs for troubleshooting.

\* Support automatic alerts when abnormal conditions occur.



\---



\## System Architecture



```

Linux Server

&#x20;     │

&#x20;     ▼

Python Monitoring Engine

&#x20;     │

&#x20;     ▼

Collect System Metrics

&#x20;     │

&#x20;     ▼

Store JSON Data

&#x20;     │

&#x20;     ▼

Flask Web Application

&#x20;     │

&#x20;     ▼

Interactive Dashboard

&#x20;     │

&#x20;     ▼

Web Browser

```



The monitoring script runs independently from the web application. This separation allows the dashboard to display information without directly accessing system resources every time a user opens the webpage.



\---



\## Key Features



\### System Monitoring



The application continuously monitors:



\* CPU Utilization

\* Memory Usage

\* Disk Usage

\* System Uptime

\* Network Statistics



These metrics provide a quick overview of the server's current health.



\---



\### Network Monitoring



The dashboard measures network latency by sending ICMP ping requests to commonly used servers such as:



\* Google DNS

\* Cloudflare DNS

\* GitHub

\* Local Router



If a host becomes unreachable, the dashboard immediately reflects the failure.



\---



\### Service Monitoring



Linux services can also be monitored.



Examples include:



\* Nginx

\* Apache

\* Docker

\* SSH

\* MySQL



The dashboard displays whether each service is currently running or has stopped unexpectedly.



\---



\### Dashboard



The Flask-based web interface provides a clean overview of all collected information.



The dashboard includes:



\* Current CPU usage

\* Memory usage

\* Disk utilization

\* Network traffic

\* Ping latency

\* System uptime

\* Service status

\* Live charts



The page automatically refreshes to display the latest monitoring data.



\---



\### Data Storage



All collected metrics are stored in JSON format.



Using JSON makes the project lightweight, portable, and easy to integrate with other applications or REST APIs in the future.



Example metrics include:



\* CPU percentage

\* Memory percentage

\* Disk percentage

\* Network traffic

\* Ping latency

\* Timestamp



\---



\### Logging



Every monitoring cycle is recorded in a log file.



The logs help with:



\* Performance analysis

\* Troubleshooting

\* Error tracking

\* Historical monitoring



\---



\### Alert System



The project supports automated alerts when predefined thresholds are exceeded.



Example conditions include:



\* High CPU usage

\* Low available memory

\* Disk almost full

\* Ping failures

\* Service failures



Alerts can be extended to email notifications or messaging platforms.



\---



\## Technologies Used



| Technology | Purpose                        |

| ---------- | ------------------------------ |

| Python     | Core application logic         |

| Flask      | Web dashboard                  |

| psutil     | System monitoring              |

| ping3      | Network latency testing        |

| JSON       | Data storage                   |

| Chart.js   | Interactive charts             |

| HTML       | Dashboard structure            |

| CSS        | User interface styling         |

| JavaScript | Dynamic updates                |

| Linux      | Operating system               |

| systemd    | Automatic background execution |



\---



\## Project Structure



```

network-monitor-dashboard/

│

├── app.py

├── monitor.py

├── requirements.txt

│

├── templates/

│   └── index.html

│

├── static/

│   ├── style.css

│   └── script.js

│

├── data/

│   └── metrics.json

│

├── logs/

│   └── monitor.log

│

├── charts/

│

└── README.md

```



\---



\## Skills Demonstrated



This project demonstrates practical experience with:



\* Python programming

\* Linux system administration

\* Process automation

\* System monitoring

\* Network monitoring

\* REST-style data handling

\* JSON processing

\* Web application development

\* Flask framework

\* Logging and debugging

\* Performance visualization

\* Service management using systemd



\---



\## Learning Outcomes



Through this project, I gained practical experience in designing a monitoring system that follows a modular architecture. I learned how to collect live system information, process it efficiently, store structured data, and present it through a responsive web interface.



The project also strengthened my understanding of Linux administration, process monitoring, network diagnostics, backend development, and real-time data visualization. It reflects the type of automation and monitoring tasks commonly found in DevOps, Cloud Engineering, and IT Infrastructure roles.



\---



\## Future Improvements



Potential enhancements include:



\* User authentication

\* Database integration

\* Historical performance reports

\* Docker deployment

\* REST API for external monitoring

\* Prometheus integration

\* Grafana dashboards

\* WebSocket-based live updates

\* Multi-server monitoring

\* Mobile-friendly responsive interface



\---



\## Conclusion



The \*\*Network Monitoring Dashboard\*\* is a practical project that demonstrates the integration of Python, Linux, and web technologies to solve a real-world infrastructure monitoring problem. It provides a strong foundation for understanding monitoring systems used in production environments and showcases skills relevant to Software Engineering, DevOps, Cloud Computing, and Linux Administration roles.



