import json
import os

from schema import RetellAgentSpec, AgentVariables 

def load_memo(account_id):

    path = f"outputs/accounts/{account_id}/v1/memo.json"

    with open(path, "r") as f:
        return json.load(f)
    
def load_template():

    with open("templates/agent_prompt_template.txt") as f:
        return f.read()
    
def generate_prompt(memo):

    template = load_template()

    services = ", ".join(memo.get("services_supported", [])) if memo.get("services_supported") else "Unknown"

    emergency_rules = ", ".join(memo.get("emergency_definition", [])) if memo.get("emergency_definition") else "Unknown"

    business_hours = memo.get("business_hours")

    if business_hours:
        hours = f"{business_hours.get('start')} - {business_hours.get('end')}"
    else:
        hours = "Not specified"

    prompt = template.format(
        company_name=memo.get("company_name","Unknown Company"),
        business_hours=hours,
        office_address=memo.get("office_address","Not specified"),
        services=services,
        emergency_rules=emergency_rules
    )

    return prompt

def create_agent_spec(account_id, version="v1"):

    path = f"outputs/accounts/{account_id}/{version}/memo.json"

    with open(path,"r") as f:
        memo = json.load(f)

    prompt = generate_prompt(memo)

    variables = AgentVariables(
        timezone=None,
        business_hours=str(memo.get("business_hours")),
        office_address=memo.get("office_address"),
        emergency_rules=str(memo.get("emergency_definition"))
    )

    agent = RetellAgentSpec(
        agent_name=f"{memo.get('company_name','Company')} Agent",
        voice_style="professional",
        system_prompt=prompt,
        variables=variables,
        version="v1"
    )

    return agent

def save_agent(agent, account_id, version):

    output_dir = f"outputs/accounts/{account_id}/{version}"
    os.makedirs(output_dir, exist_ok=True)

    path = f"{output_dir}/agent.json"

    with open(path, "w") as f:
        f.write(agent.model_dump_json(indent=2))

    print(f"Agent saved: {path}")

if __name__ == "__main__":

    account_id = "account_001"

    agent = create_agent_spec(account_id,"v1")

    save_agent(agent, account_id)

