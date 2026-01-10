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


