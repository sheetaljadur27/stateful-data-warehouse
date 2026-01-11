# Source to Target Mapping (STM)

This document defines how legacy CSV columns are mapped to FHIR resources
during migration.

| Legacy CSV Column | Description              | FHIR Resource | FHIR Element              |
|------------------|--------------------------|---------------|---------------------------|
| patient_id       | Legacy patient identifier| Patient       | Patient.id                |
| first_name       | Patient first name       | Patient       | Patient.name.given        |
| last_name        | Patient last name        | Patient       | Patient.name.family       |
| gender           | M/F values               | Patient       | Patient.gender            |
| dob              | Date of birth            | Patient       | Patient.birthDate         |
| obs_code         | Observation code         | Observation   | Observation.code.text     |
| obs_value        | Observation value        | Observation   | Observation.valueQuantity |
| obs_date         | Observation date         | Observation   | Observation.effectiveDateTime |

**Notes:**
- Magic strings such as M/F are translated to FHIR-compliant values.
- UUIDs are generated to link Patient and Observation resources.
