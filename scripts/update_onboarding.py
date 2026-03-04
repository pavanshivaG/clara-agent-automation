import os
import json
import re
import copy

from generate_agent import create_agent_spec, save_agent
from deepdiff import DeepDiff


def load_v1_memo(account_id):

    path = f"outputs/accounts/{account_id}/v1/memo.json"

    with open(path, "r") as f:
        return json.load(f)


def load_onboarding(file_path):

    with open(file_path, "r") as f:
        return f.read().lower()


def extract_updates(text):

    updates = {}

    if "timezone" in text:
        tz_match = re.search(r"timezone\s*(is)?\s*([a-z]+)", text)
        if tz_match:
            updates["timezone"] = tz_match.group(2)

    if "servicetrade" in text:
        updates["integration_constraints"] = [
            "never create sprinkler jobs in servicetrade"
        ]

    timeout_match = re.search(r"(\d+)\s*seconds", text)
    if timeout_match:
        updates["transfer_timeout"] = int(timeout_match.group(1))

    return updates


def apply_updates(memo, updates):

    if "timezone" in updates:

        if memo.get("business_hours") is None:
            memo["business_hours"] = {}

        memo["business_hours"]["timezone"] = updates["timezone"]

    if "integration_constraints" in updates:
        memo["integration_constraints"] = updates["integration_constraints"]

    if "transfer_timeout" in updates:

        if memo.get("emergency_routing_rules") is None:
            memo["emergency_routing_rules"] = {}

        memo["emergency_routing_rules"]["timeout"] = updates["transfer_timeout"]

    return memo


def generate_changelog(v1, v2):

    diff = DeepDiff(v1, v2, ignore_order=True)
    return diff


def save_v2(account_id, memo_v2):

    output_dir = f"outputs/accounts/{account_id}/v2"
    os.makedirs(output_dir, exist_ok=True)

    memo_path = f"{output_dir}/memo.json"

    with open(memo_path, "w") as f:
        json.dump(memo_v2, f, indent=2)

    print(f"Saved: {memo_path}")
    return memo_path


def save_changelog(account_id, changelog):

    path = f"outputs/accounts/{account_id}/changes.json"

    with open(path, "w") as f:
        f.write(changelog.to_json(indent=2))


if __name__ == "__main__":

    account_id = "account_001"

    onboarding_file = "data/onboarding_calls/onboard_001.txt"

    v1 = load_v1_memo(account_id)

    text = load_onboarding(onboarding_file)

    updates = extract_updates(text)

    v2 = apply_updates(copy.deepcopy(v1), updates)

    changelog = generate_changelog(v1, v2)

    save_v2(account_id, v2)

    agent_v2 = create_agent_spec(account_id, "v2")
    save_agent(agent_v2, account_id, "v2")

    save_changelog(account_id, changelog)

    print("Onboarding update completed")