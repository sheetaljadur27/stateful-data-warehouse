# Data Flow

1. Legacy data extracted as CSV
2. Translator reads each row
3. Fields mapped to FHIR elements
4. Magic strings normalized
5. Resources grouped into transaction bundles
6. Bundle submitted to FHIR server
7. Server validates and stores data
