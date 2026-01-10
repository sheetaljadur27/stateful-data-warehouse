# Stateful Data Warehouse Project
## Project Overview

This project demonstrates the design of a stateful data warehouse using a 
layered repository structure. The objective is to show how data moves from 
raw ingestion to processed, analytics-ready formats while maintaining clarity, 
traceability, and scalability.

The repository is structured to reflect real-world data warehousing practices 
rather than a simple collection of scripts or files.


## Repository Structure
This repository is designed following a stateful data warehouse architecture. 
Instead of being a simple code dump, it organizes data across multiple layers to 
represent different stages of data processing and transformation.
stateful-data-warehouse/
├── raw-data/
│   └── Contains source data ingested from upstream systems
│
├── staging/
│   └── Holds cleaned and standardized intermediate datasets
│
├── processed/
│   └── Stores transformed, analytics-ready datasets
│
├── models/
│   └── Includes business logic, mappings, and transformation rules
│
├── docs/
│   └── Project documentation and architectural explanations
│
└── README.md
    └── Overview of the project and usage instructionsThis layered structure ensures:
- Clear separation of concerns
- Stateful data flow across layers
- Scalability and maintainability of the warehouse design
## Infrastructure: Containerized FHIR Warehouse

The FHIR warehouse is implemented using the HAPI FHIR JPA server, deployed in a Docker container 
to ensure a consistent and reproducible runtime environment.

**Docker Advantages:**
- Eliminates dependency issues with Java, database versions, and operating systems.
- Ensures the FHIR server behaves identically on different machines.
- Provides a self-contained, isolated environment for the server.

**Port Mapping:**
- The container’s internal port `8080` is mapped to the host machine.
- This allows the FHIR server to be accessed via a browser or client scripts at:
  `http://localhost:8080/fhir`.

**Statefulness and Reliability:**
- The containerized server stores persistent data, ensuring that resources remain 
  available throughout the migration process.
- Using Docker allows for easy recreation of the environment without breaking dependencies.

**Evidence:**
- Docker container running successfully.
- HAPI FHIR server accessible at the mapped host URL.


