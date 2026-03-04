import streamlit as st
import os
import json

ACCOUNTS_DIR = "outputs/accounts"
if not os.path.exists(ACCOUNTS_DIR):
    st.error("No accounts generated yet. Run the pipeline first.")
    st.stop()

st.title("Clara Agent Automation Dashboard")

accounts = os.listdir(ACCOUNTS_DIR)

account = st.selectbox("Select Account", accounts)

account_path = os.path.join(ACCOUNTS_DIR, account)

v1_path = os.path.join(account_path,"v1","memo.json")
v2_path = os.path.join(account_path,"v2","memo.json")

st.header("Account Memo")

col1, col2 = st.columns(2)

with col1:
    st.subheader("v1 Memo")
    if os.path.exists(v1_path):
        with open(v1_path) as f:
            st.json(json.load(f))

with col2:
    st.subheader("v2 Memo")
    if os.path.exists(v2_path):
        with open(v2_path) as f:
            st.json(json.load(f))

def show_diff(v1, v2):

    st.subheader("Changes")

    for key in v2:

        if key not in v1:
            st.write(f"Added: {key}")

        elif v1[key] != v2[key]:
            st.write(f"Updated: {key}")
            st.write("Old:", v1[key])
            st.write("New:", v2[key])

if os.path.exists(v1_path) and os.path.exists(v2_path):

    with open(v1_path) as f:
        v1 = json.load(f)

    with open(v2_path) as f:
        v2 = json.load(f)

    show_diff(v1,v2)

st.header("Pipeline Metrics")

total_accounts = len(accounts)

v2_count = 0

for acc in accounts:
    if os.path.exists(f"outputs/accounts/{acc}/v2/memo.json"):
        v2_count += 1

st.metric("Total Accounts", total_accounts)
st.metric("Accounts Processed (v2)", v2_count)

st.header("Pipeline Metrics")

total_accounts = len(accounts)

v2_count = 0

for acc in accounts:
    if os.path.exists(f"outputs/accounts/{acc}/v2/memo.json"):
        v2_count += 1

st.metric("Total Accounts", total_accounts)
st.metric("Accounts Updated to v2", v2_count)