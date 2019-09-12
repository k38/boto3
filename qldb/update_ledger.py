import session

def main():
    client = session.client()
    res = client.update_ledger(
        Name="test-ledger",
        DeletionProtection=False
    )
    print(res)

main()
