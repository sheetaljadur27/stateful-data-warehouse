# System Architecture

The system follows a warehouse-based architecture:

- Dockerized HAPI FHIR server
- FHIR Shorthand profiles for validation
- Python-based translator for data migration
- Transaction-based ingestion for atomicity
