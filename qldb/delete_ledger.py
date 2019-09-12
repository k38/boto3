import session

def main():
    client = session.client()
    res = client.delete_ledger(
        Name="test-ledger"
    )
    print(res)

main()
