import os
import re
import json
from schema import AccountMemo 

def load_transcript(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().lower() 
    
def extract_company_name(text):

    patterns = [
        r"we are ([a-zA-Z\s]+)",
        r"company name is ([a-zA-Z\s]+)",
        r"this is ([a-zA-Z\s]+)"
    ]

    for p in patterns:
        match = re.search(p, text)
        if match:
            return match.group(1).strip()

    return None

def extract_services(text):

    services = []

    keywords = [
        "sprinkler",
        "fire alarm",
        "extinguisher",
        "inspection",
        "maintenance"
    ]

    for k in keywords:
        if k in text:
            services.append(k)

    return services if services else None

def extract_business_hours(text):

    if "monday" in text or "weekdays" in text:

        hours_match = re.search(r"(\d+)\s*(am|pm)\s*to\s*(\d+)\s*(am|pm)", text)

        if hours_match:
            start = hours_match.group(1) + hours_match.group(2)
            end = hours_match.group(3) + hours_match.group(4)

            return {
                "days": ["mon","tue","wed","thu","fri"],
                "start": start,
                "end": end
            }

    return None

def extract_emergency_definition(text):

    emergencies = []

    if "sprinkler leak" in text:
        emergencies.append("sprinkler leak")

    if "fire alarm" in text:
        emergencies.append("fire alarm triggered")

    return emergencies if emergencies else None

def extract_routing(text):

    if "dispatch" in text:
        return {
            "transfer_to": "dispatch",
            "timeout": None,
            "fallback_action": None
        }

    return None

def process_demo_transcript(file_path, account_id):

    text = load_transcript(file_path)

    memo = AccountMemo(
        account_id=account_id,
        company_name=extract_company_name(text),
        services_supported=extract_services(text),
        emergency_definition=extract_emergency_definition(text),
        emergency_routing_rules=extract_routing(text)
    )

    return memo

def save_output(memo):

    output_dir = f"outputs/accounts/{memo.account_id}/v1"
    os.makedirs(output_dir, exist_ok=True)

    file_path = f"{output_dir}/memo.json"

    with open(file_path, "w") as f:
        f.write(memo.model_dump_json(indent=2))

    print("Saved:", file_path)

if __name__ == "__main__":

    transcript = "data/demo_calls/demo_001.txt"

    memo = process_demo_transcript(transcript, "account_001")

    save_output(memo)

