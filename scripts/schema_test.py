from schema import AccountMemo

memo = AccountMemo(
    account_id="acc_001",
    company_name="ABC Fire Protection"
)

print(memo.model_dump_json(indent=2))