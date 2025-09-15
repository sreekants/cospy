# COS (Co-Simulation Operating System) - Core packages

[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](https://opensource.org/license/apache-2-0) 
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


- **Github repository**: <https://github.com/sreekants/cospy>

## Introduction

The Co-Simulation Operating System (COS) is a "testable metaverse" designed for digital twinning of autonomous vessels, thus allowing large-scale simulations with augmented fidelity for testing. It introduces the concept of a ’simulules’ - containerized simulation capsules running on a high-performance computing (HPC) cluster. Each simulule is an isolated instance that tests one permutation of a scenario, within which the evaluated autonomous software is introduced as a digital twin. The results are stored in a database, then analyzed and visualized through a performance dashboard. COS is built as an embedded operating system for large-scale distributed simulations. It supports 100,000 to 10 million scenarios in parallel, is domain-agnostic (for maritime, road, rail, or aerial simulations), and allows limitless expansion through plug-in features called "faculties." COS is based on a microkernel design, making it flexible to run on both desktop and HPC clusters, while also emulating realworld systems (propulsiion  systems, telecommunication, sonar and visual detectors etc.) for enhanced simulation fidelity.

The platform draws extensively from the [Inferno Operating System](https://en.wikipedia.org/wiki/Inferno_(operating_system)) and ROS - the [Robotic Operating System](https://en.wikipedia.org/wiki/Robot_Operating_System#Services). All resources are exposed as sockets (not files). Resources appear in a hierarchical namespace that may represent physically separated (inprocess or remote) resources. All capabilities of the system are plugin software modules exposed as nodes advertising [services](https://en.wikipedia.org/wiki/Robot_Operating_System#Services) (often extended as faculties), with an inter-process messaging system based advertised as [topics](https://en.wikipedia.org/wiki/Robot_Operating_System#Topics) serving the backbone for a standard communication protocol.

The following research publications provide more information about the background work behind the project.
* [Safety Assurances of Autonomous Vessels](https://www.researchgate.net/publication/385274872_Safety_Assurances_in_Autonomous_Vessels)
* [Legata - a domain language for regulatory compliance](https://www.researchgate.net/publication/386174675_Legata_-A_domain_language_for_regulatory_compliance)

![Concept Diagram](docs/images/Datapipeline.png)
## Quick Links
  * [Getting Started Guide](docs/GettingStarted.md)

<sub>Copyright 2023, Norwegian University of Science and Technology.</sub>
