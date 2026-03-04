from pydantic import BaseModel
from typing import List, Optional


class BusinessHours(BaseModel):
    days: Optional[List[str]] = None
    start: Optional[str] = None
    end: Optional[str] = None
    timezone: Optional[str] = None


class EmergencyRouting(BaseModel):
    transfer_to: Optional[str] = None
    timeout: Optional[int] = None
    fallback_action: Optional[str] = None


class NonEmergencyRouting(BaseModel):
    collect_details: Optional[bool] = None
    schedule_during_hours: Optional[bool] = None


class AccountMemo(BaseModel):
    account_id: str
    company_name: Optional[str] = None

    business_hours: Optional[BusinessHours] = None

    office_address: Optional[str] = None

    services_supported: Optional[List[str]] = None

    emergency_definition: Optional[List[str]] = None

    emergency_routing_rules: Optional[EmergencyRouting] = None

    non_emergency_routing_rules: Optional[NonEmergencyRouting] = None

    call_transfer_rules: Optional[str] = None

    integration_constraints: Optional[List[str]] = None

    after_hours_flow_summary: Optional[str] = None

    office_hours_flow_summary: Optional[str] = None

    questions_or_unknowns: Optional[List[str]] = None

    notes: Optional[str] = None


class AgentVariables(BaseModel):
    timezone: Optional[str] = None
    business_hours: Optional[str] = None
    office_address: Optional[str] = None
    emergency_rules: Optional[str] = None


class RetellAgentSpec(BaseModel):
    agent_name: str
    voice_style: str
    system_prompt: str
    variables: AgentVariables
    version: str


class VersionChange(BaseModel):
    field_changed: str
    old_value: Optional[str] = None
    new_value: Optional[str] = None
    reason: Optional[str] = None