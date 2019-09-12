import boto3

def client():
    session = boto3.session.Session(
        region_name="",
        aws_access_key_id="",
        aws_secret_access_key="",
    )
    return session.client("qldb")
