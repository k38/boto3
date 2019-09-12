import session

def main():
    client = session.client()
    res = client.create_ledger(
        Name="test-ledger",
        Tags={
            "key": "value",
        },
        PermissionsMode="ALLOW_ALL",
        DeletionProtection=True
    )
    print(res)

main()
