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
- ## Evidence

### Docker & FHIR Server Running
![Docker and FHIR Evidence]([screenshots/docker_fhir_running.png](https://github.com/sheetaljadur27/stateful-data-warehouse/tree/main/Screenshots))
## Rulebook: FHIR Shorthand (FSH) Profiles

The Rulebook defines validation rules for our FHIR resources using **FHIR Shorthand (FSH)**. 
We created profiles for both **Patient** and **Observation** resources.

**Profiles Created:**
- `PatientProfile.fsh` → Defines required fields like name, birthDate, and gender.
- `ObservationProfile.fsh` → Defines clinical observations such as vital signs and lab results.

**FSH Tool Compilation:**
- The FSH files were compiled using the class FSH tool.
- Compilation generates JSON StructureDefinitions, which are used by the HAPI FHIR server to validate incoming resources.
- Generated JSON files are stored in `/Rulebook/generated/`.

**Evidence:**
![FSH Compilation Success - Patient](Screenshots/patient_fsh.png)
![FSH Compilation Success - Observation](Screenshots/observation_fsh.png)
https://github.com/sheetaljadur27/stateful-data-warehouse/blob/main/Screenshot%202026-01-10%20143705.png
https://github.com/sheetaljadur27/stateful-data-warehouse/blob/main/Screenshot%202026-01-10%20143801.png
https://github.com/sheetaljadur27/stateful-data-warehouse/blob/main/Screenshot%202026-01-10%20143921.png
## Translator: Legacy Data Migration Layer

The Translator layer converts flat, legacy CSV data into FHIR-compliant
resources for ingestion into the warehouse.

**Responsibilities:**
- Map legacy columns to FHIR elements
- Handle magic strings (M/F → male/female)
- Generate UUIDs for resource linkage
- Create Transaction Bundles to ensure atomic ingestion

**Transactional Atomicity:**
Patient and Observation resources are submitted together in a single
transaction bundle, preventing orphaned clinical data.

**Evidence:**
![Sample CSV](Screenshots/sample_csv.png)
![Translator Script](Screenshots/translator_code.png)
![Transaction Bundle](Screenshots/transaction_bundle.png)
https://github.com/sheetaljadur27/stateful-data-warehouse/blob/main/Screenshots/translator%20-%20ss%201.png
https://github.com/sheetaljadur27/stateful-data-warehouse/blob/main/Translator/sample_data.csv
https://github.com/sheetaljadur27/stateful-data-warehouse/blob/main/Screenshots/T%20SS%202.png



