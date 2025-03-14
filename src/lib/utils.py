from google.cloud import storage

bucket_name = "planetapi"

storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)
bucket.cors = [
    {
        "origin": ["*"],
        "responseHeader": [
            "Content-Type",
            "x-goog-resumable"],
        "method": ['GET'],
        "maxAgeSeconds": 3600
    }
]
bucket.patch()

print(f"ID: {bucket.id}")
print(f"Name: {bucket.name}")
print(f"Storage Class: {bucket.storage_class}")
print(f"Location: {bucket.location}")
print(f"Location Type: {bucket.location_type}")
print(f"Cors: {bucket.cors}")
print(f"Default Event Based Hold: {bucket.default_event_based_hold}")
print(f"Default KMS Key Name: {bucket.default_kms_key_name}")
print(f"Metageneration: {bucket.metageneration}")
print(
    f"Public Access Prevention: {bucket.iam_configuration.public_access_prevention}"
)
print(f"Retention Effective Time: {bucket.retention_policy_effective_time}")
print(f"Retention Period: {bucket.retention_period}")
print(f"Retention Policy Locked: {bucket.retention_policy_locked}")
print(f"Requester Pays: {bucket.requester_pays}")
print(f"Self Link: {bucket.self_link}")
print(f"Time Created: {bucket.time_created}")
print(f"Versioning Enabled: {bucket.versioning_enabled}")
print(f"Labels: {bucket.labels}")