Profile: SimplePatientProfile
Parent: Patient
Description: "A simple patient profile requiring name and birth date"

* name 1..* MS
* name.family 1..1
* name.given 1..*
* birthDate 1..1 MS
* gender 0..1
