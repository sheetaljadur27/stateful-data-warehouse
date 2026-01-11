import csv
import uuid

def translate_gender(value):
    if value == "M":
        return "male"
    elif value == "F":
        return "female"
    else:
        return "unknown"

bundle = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": []
}

with open("sample_data.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        patient_uuid = str(uuid.uuid4())

        patient = {
            "resourceType": "Patient",
            "id": patient_uuid,
            "name": [{
                "family": row["last_name"],
                "given": [row["first_name"]]
            }],
            "gender": translate_gender(row["gender"]),
            "birthDate": row["dob"]
        }

        observation = {
            "resourceType": "Observation",
            "status": "final",
            "code": {
                "text": row["obs_code"]
            },
            "subject": {
                "reference": f"Patient/{patient_uuid}"
            },
            "effectiveDateTime": row["obs_date"],
            "valueQuantity": {
                "value": float(row["obs_value"])
            }
        }

        bundle["entry"].append({
            "request": {"method": "POST", "url": "Patient"},
            "resource": patient
        })

        bundle["entry"].append({
            "request": {"method": "POST", "url": "Observation"},
            "resource": observation
        })

print(bundle)
