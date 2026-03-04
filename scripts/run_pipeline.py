import os
import copy

from extract_demo import process_demo_transcript, save_output
from generate_agent import create_agent_spec, save_agent
from update_onboarding import (
    load_v1_memo,
    load_onboarding,
    extract_updates,
    apply_updates,
    generate_changelog,
    save_v2,
    save_changelog
)


def process_demo_calls():

    demo_folder = "data/demo_calls"

    files = os.listdir(demo_folder)

    for i, file in enumerate(files):

        path = os.path.join(demo_folder, file)

        account_id = f"account_{i+1:03}"

        print("Processing demo:", file)

        memo = process_demo_transcript(path, account_id)

        save_output(memo)

        agent = create_agent_spec(account_id, "v1")

        save_agent(agent, account_id, "v1")


def process_onboarding_calls():

    onboarding_folder = "data/onboarding_calls"

    files = os.listdir(onboarding_folder)

    for i, file in enumerate(files):

        path = os.path.join(onboarding_folder, file)

        account_id = f"account_{i+1:03}"

        print("Processing onboarding:", file)

        v1 = load_v1_memo(account_id)

        text = load_onboarding(path)

        updates = extract_updates(text)

        v2 = apply_updates(copy.deepcopy(v1), updates)

        changelog = generate_changelog(v1, v2)

        save_v2(account_id, v2)

        agent_v2 = create_agent_spec(account_id, "v2")

        save_agent(agent_v2, account_id, "v2")

        save_changelog(account_id, changelog)


if __name__ == "__main__":

    print("Starting Clara Automation Pipeline")

    process_demo_calls()

    process_onboarding_calls()

    print("Pipeline completed successfully")