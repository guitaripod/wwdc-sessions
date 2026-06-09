---
id: "wwdc2022-10109"
event: "wwdc2022"
year: 2022
title: "What’s new in notarization for Mac apps"
type: "Video"
url: "https://developer.apple.com/videos/play/wwdc2022/10109"
topics: ["Privacy & Security"]
platforms: ["macOS"]
hasTranscript: true
---

# What’s new in notarization for Mac apps

**Event:** WWDC22 · **Topic:** Privacy & Security · **Platforms:** macOS · **Published:** 2022-06-07 · **Session:** [wwdc2022-10109](https://developer.apple.com/videos/play/wwdc2022/10109)

Notarization works in tandem with macOS to help people safely download software for their Mac outside of the App Store. Learn about the required transition from altool to notarytool and how the Xcode GUI can help you achieve better overall performance when notarizing your app. We'll also share information about APIs for interacting with the Notary service from any internet-connected machine.

**Keywords:** `malware`, `notarizing`, `notary`, `webhook`

## Transcript

[Read the transcript](transcript.md) · [Structured JSON](transcript.json)
(1,259 words)

## Documentation & Resources

- [Notary API](https://developer.apple.com/documentation/NotaryAPI) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/NotaryAPI
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/NotaryAPI.json
- [Notarizing macOS software before distribution](https://developer.apple.com/documentation/Security/notarizing-macos-software-before-distribution) _documentation_
  - Markdown (sosumi.ai): https://sosumi.ai/documentation/Security/notarizing-macos-software-before-distribution
  - DocC JSON: https://developer.apple.com/tutorials/data/documentation/Security/notarizing-macos-software-before-distribution.json

## Code Snippets

### REST API: upload file for notarization — [4:53]

```python
# Upload file for notarization

def upload_file(token, filepath, sha256):
    data = { "sha256": sha256, "submissionName": os.path.basename(filepath) }
    resp = requests.post(
       "https://appstoreconnect.apple.com/notary/v2/submissions",
        json=data,
        headers={"Authorization": "Bearer " + token})

    output = resp.json()
    aws_info = output["data"]["attributes"]
    submission_id = output["data"]["id"] 

    client = boto3.client(
        "s3",  
        aws_access_key_id=aws_info["awsAccessKeyId"],
        aws_secret_access_key=aws_info["awsSecretAccessKey"],
        aws_session_token=aws_info["awsSessionToken"])
    client.upload_file(filepath, aws_info["bucket"], aws_info["object"])
```

### REST API: wait for completion — [6:12]

```python
# Wait for completion

def watch_upload(submission_id, token):
    while True:
        resp = requests.get(
            "https://appstoreconnect.apple.com/notary/v2/submissions/" + submission_id, 
            headers={"Authorization": "Bearer " + token})

        output = resp.json()
        current_status = output["data"]["attributes"]["status"]

        if current_status != "In Progress":
            return current_status # For example: Accepted or Invalid

        time.sleep(30) # Allow time for submission to progress
```

## Video

- HLS stream: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10109/3/AC093573-81B2-4A1E-BA66-50E413DF5660/cmaf.m3u8
- Download: https://devstreaming-cdn.apple.com/videos/wwdc/2022/10109/3/AC093573-81B2-4A1E-BA66-50E413DF5660/cmaf-download.m3u8

---

_Source: [Apple Inc.](https://developer.apple.com/videos/play/wwdc2022/10109) — developer.apple.com. Indexed for agent consumption._
