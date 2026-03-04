Agent Automation Pipeline

This project implements an automation pipeline that converts customer call transcripts into structured AI agent configurations.
It simulates how Clara could automatically generate and update voice agent behavior from demo and onboarding calls.

The system processes transcripts in two stages:

Demo Call Processing – extracts business information and creates the initial configuration.

Onboarding Call Processing – updates the configuration based on onboarding discussions and produces version differences.

The pipeline is designed to be automated, versioned, and observable through a dashboard.

Architecture Overview

The system is composed of four major components:

1. Python Processing Pipeline

Handles all data extraction, transformation, and versioning.

Responsible for:

Parsing transcripts

Generating structured account memos

Generating AI agent specifications

Applying onboarding updates

Detecting configuration changes

Main scripts:

scripts/
extract_demo.py
generate_agent.py
update_onboarding.py
run_pipeline.py
2. n8n Workflow Automation

n8n is used to simulate workflow orchestration similar to what Clara might use internally.

The n8n workflow:

Trigger → HTTP Request → Python Pipeline

Purpose of using n8n:

Automates pipeline execution

Simulates event-driven processing

Allows integration with APIs, CRMs, or scheduling systems

Makes the pipeline extensible without changing core code

Example future triggers:

new transcript uploaded

CRM event

webhook from call system

3. Docker Containerization

Docker is used to run n8n as an isolated service.

Benefits:

consistent environment

easy setup

avoids dependency conflicts

portable deployment

Docker configuration:

docker-compose.yml

Service started:

n8nio/n8n

Port mapping:

5678 → n8n dashboard

Docker environment variables allow the n8n code node to execute external commands.

4. Streamlit Dashboard

Streamlit provides a lightweight UI for:

viewing generated memos

comparing configuration versions

viewing detected changes

monitoring pipeline processing

Dashboard file:

dashboard/app.py
Project Workflow

The system processes transcripts in two sequential stages.

Stage 1 – Demo Call Processing

Purpose:
Extract business information from the demo call.

Steps:

Read transcript from

data/demo_calls/

Extract structured data using rule-based parsing.

Information extracted includes:

company name

supported services

emergency definition

business hours

integration references

Generate account memo.

Output stored as:

outputs/accounts/<account_id>/v1/memo.json

Generate AI agent specification.

Output stored as:

outputs/accounts/<account_id>/v1/agent.json
Stage 2 – Onboarding Call Processing

Purpose:
Update the configuration using onboarding discussions.

Steps:

Read transcript from

data/onboarding_calls/

Detect updates such as:

routing rules

timeout values

timezone configuration

integration restrictions

Apply updates to the previous memo.

Creates version:

v2/memo.json

Regenerate agent configuration.

Creates:

v2/agent.json

Detect differences between versions using DeepDiff.

Creates:

changes.json
Versioning Strategy

The system maintains configuration history.

outputs/accounts/account_xxx/

v1/
memo.json
agent.json

v2/
memo.json
agent.json

changes.json

Benefits:

auditability

safe configuration updates

easy rollback

clear change visibility

Technologies Used
Python

Core processing pipeline.

Used for:

transcript parsing

memo generation

agent spec generation

version comparison

Regex-based NLP

Lightweight text extraction method.

Chosen because:

fast

deterministic

no external dependencies

predictable behavior

DeepDiff

Used to detect structural differences between JSON objects.

Benefits:

precise change tracking

structured output

supports nested JSON

n8n

Used as a workflow orchestrator.

Advantages:

visual workflow automation

supports triggers, APIs, and integrations

enables scalable event-driven architecture

Docker

Used to run n8n as a container.

Benefits:

environment isolation

easy deployment

reproducible setup

Streamlit

Used for the project dashboard.

Advantages:

minimal code

instant UI

ideal for data inspection tools

Why This Architecture Is Effective
Modular Design

Each component has a clear responsibility:

Python → processing
n8n → orchestration
Docker → infrastructure
Streamlit → visualization
Scalable

The system can easily scale to process many accounts.

Possible extensions:

automatic transcript ingestion

CRM integration

webhook triggers

scheduled processing

Version Safe

Configuration updates do not overwrite previous data.

This ensures:

traceability

debugging capability

safe experimentation

Automation Ready

The pipeline can run:

manually

via n8n trigger

via API endpoint

Installation

Clone repository.

git clone <repo_url>
cd clara-agent-automation
Create Virtual Environment
python -m venv venv

Activate environment.

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
Install Dependencies
pip install deepdiff streamlit pandas
Run Docker (n8n)

Start n8n container.

docker-compose up -d

Open n8n dashboard:

http://localhost:5678
Run Processing Pipeline

Execute the automation pipeline.

python scripts/run_pipeline.py

The pipeline will:

process demo transcripts

generate initial memo

process onboarding transcripts

update configuration

produce change logs

Launch Dashboard

Run Streamlit interface.
streamlit run dashboard/app.py

Open:

http://localhost:8501
