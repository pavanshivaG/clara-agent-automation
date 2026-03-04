🤖 Agent Automation

📌 Overview

Clara Agent Automation is an AI-driven automation system designed to streamline communication workflows and automate operational tasks. The project integrates multiple technologies to build a scalable and efficient automation pipeline capable of handling structured workflows, task orchestration, and data processing.

The system leverages containerized infrastructure and workflow automation tools to ensure reliability, scalability, and ease of deployment.

---

VIDEO : [WORKFLOW AND DEMONSTRATION](https://drive.google.com/file/d/11XzVuHFhOHLBSWw3eEXqJk5oKRjXHlRz/view?usp=sharing)

---

🚀 Key Features

⚙️ Automated Workflows – Uses workflow automation to execute tasks without manual intervention.
🧠 AI-powered Processing – Integrates intelligent processing for automated decision making.
🔄 Task Orchestration – Handles multiple tasks and processes within a structured workflow pipeline.
🐳 Containerized Deployment – Runs within Docker containers for portability and consistent environments.
📊 Structured Logging – Maintains logs for monitoring and debugging system activities.
🔌 Modular Architecture – Allows easy extension of workflows and integrations.

---

🛠️ Tech Stack

Backend

-Python
-FastAPI

Automation & Workflow

-n8n – Used to create automation workflows and integrate services.

Infrastructure

-Docker – Containerized deployment for consistent runtime environments.

Additional Tools

-Virtual Environment (venv – Dependency isolation
-Git & GitHub – Version control and collaboration
-VS Code – Development environment

---

⚙️ System Architecture

The system is built around an automation pipeline that coordinates between backend services and workflow orchestration.

1. The backend service processes requests and handles business logic.
2. n8n orchestrates workflows and integrates external services or triggers.
3. Docker containers provide an isolated runtime environment.
4. Logs are generated to monitor workflow executions and backend operations.

This architecture ensures modularity, scalability, and easier debugging.

---

🔄 How the System Works

1️⃣ User Interaction
Users trigger automation processes through defined workflows or backend endpoints.

2️⃣ Workflow Trigger
n8n workflows listen for triggers such as API calls, events, or scheduled executions.

3️⃣ Processing Layer
The backend processes incoming data, performs logic execution, and communicates with workflows.

4️⃣ Automation Execution
Tasks such as communication, data handling, or integrations are automatically executed.

5️⃣ Logging & Monitoring
Execution logs are stored to track system activity and detect potential issues.

---

🐳 Running the Project

1️⃣ Navigate to Project Folder

Open terminal in the project directory.

cd clara-agent-automation

2️⃣ Create Virtual Environment

python -m venv venv

3️⃣ Activate Virtual Environment

Windows 
venv\Scripts\activate
Mac/Linux 
source venv/bin/activate

4️⃣ Install Dependencies

If you have a requirements.txt:

pip install -r requirements.txt

Or install manually:

pip install deepdiff streamlit pandas fastapi uvicorn

5️⃣ (Optional) Start n8n using Docker

Make sure Docker is installed.

Run:

docker-compose up -d

Open n8n:

http://localhost:5678

Import the workflow:

workflows/n8n_pipeline.json

6️⃣ Add Dataset Files

Place transcripts in:

data/demo_calls/
data/onboarding_calls/

Example:

data/demo_calls/demo_001.txt
data/onboarding_calls/onboard_001.txt

7️⃣ Run the Automation Pipeline

Run the full pipeline:

python scripts/run_pipeline.py

This will:

process demo transcript

generate memo v1

generate agent v1

process onboarding transcript

update memo v2

generate agent v2

create changelog

8️⃣ Check Generated Outputs

Open:

outputs/accounts/account_001/

You should see:

v1/memo.json
v1/agent.json
v2/memo.json
v2/agent.json
changes.json

9️⃣ Run the Dashboard

Start the Streamlit UI:

streamlit run dashboard/app.py

Open browser:

http://localhost:8501

The dashboard will show:

memo v1

memo v2

detected changes

pipeline metrics

🔟 (Optional) Run API Server

If using FastAPI endpoint:

uvicorn scripts.api_server:app --reload

Test pipeline trigger:

http://localhost:8000/run-pipeline

---

📂 Project Structure


clara-agent-automation
│
├── workflows/          # n8n workflow configurations
├── logs/               # Application logs
├── backend/            # Backend services
├── Dockerfile          # Docker container configuration
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation




📈 Why This Approach is Better

✔ Automation-first architecture reduces manual effort
✔ Containerized deployment ensures consistent environments
✔ Scalable workflow orchestration with n8n
✔ Modular design allows easy feature expansion
✔ Improved monitoring through structured logging

---

->Known Limitations
Rule-Based Extraction

The system uses regex-based extraction rather than machine learning or LLMs.
This makes extraction dependent on transcript phrasing.

Limited Semantic Understanding

Complex conversational nuances may not be captured accurately without more advanced NLP techniques.

Single Account Mapping

The current implementation assumes a simple one-to-one mapping between demo and onboarding transcripts.

No Real CRM Integration

CRM references (e.g., Jobber or ServiceTrade) are simulated rather than connected to live systems.

Transcript Format Sensitivity

Transcripts must contain recognizable phrases for extraction rules to work reliably.

---

->Improvements for Production

With production access, several improvements would significantly enhance the system.

LLM-Based Transcript Understanding

Using an LLM would allow:

better semantic extraction

handling varied conversation styles

capturing more nuanced business rules

Automated Speech-to-Text

Integrating a speech-to-text system would allow processing raw call recordings instead of requiring transcripts.

Direct CRM Integration

Connecting to systems like:

Jobber
ServiceTitan
Housecall Pro

would allow the pipeline to automatically update customer configuration.

Event-Driven Processing

Production systems would use event triggers such as:

webhook from call system

new recording upload

CRM account creation

to trigger pipeline execution automatically.

Scalable Processing

The system could be expanded to process large volumes of transcripts using:

queue-based workers

distributed processing

cloud storage pipelines

👨‍💻 Author

Pavan Shiva Golla
Final Year Computer Science Student – VIT Vellore

EXAMPLE OUTPUTS :

<img width="1309" height="884" alt="image" src="https://github.com/user-attachments/assets/022f0514-f616-4ec4-8903-b0ea840fde75" />

<img width="870" height="835" alt="image" src="https://github.com/user-attachments/assets/95552427-89f8-42b0-af73-7bb5830902b1" />

<img width="1026" height="794" alt="image" src="https://github.com/user-attachments/assets/c00670b1-7276-4749-a9bd-54bbd0e6def1" />



