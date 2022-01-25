from amocrm.v2 import tokens
import requests
import json


tokens.default_token_manager(
    client_id="bfe9fcdb-88c5-4d99-95a5-9aa88529202f",
    client_secret="m1y2R6ftY7Bo9CLgWtnuJ4i58WtDt99oSprTMRdSK26ddlheTMK6kOD4ThTDBMTO",
    subdomain="aleeexgerttt",
    redirect_url="https://example.com",
    storage=tokens.FileTokensStorage(),
)
tokens.default_token_manager.init(code="def5020037c7374fad51dda7d6edac48c2b2b5e00855b0a90a9df20e2dec9151cfefb3ef2692100ba8a207e93d4e44762ec3537dd790b33f756f06d8d7d0ec2f9fec87a7939053c79c221a231e7878bf1c72d2238d42bc3157726f7ddd1288b7ed7e98d80c52d238d0bfcf55e2477c74574b7dd5f513ede1cf30c2a60f5b89c787020d9015fb67c2a8b8ef7cfb6e4aaf67054b3c1c1bfb6b338ca807781a3344d8a106c2a851b246efe9646e0faa5ecd9fee2bb67da07b42abc2e934947414d7617bb506174a5ee35810a425b4fe370ddaf4e3d9d25206b4f2a74e6446bbc560e21eec8472755937fcaf536e7da0230863a532eab776b2a5d1242e029eaa2d6bf42346b66dbd2f447b52e826aa8276123a4eb3982bc5638181d3a7f3a95487d89d67da559c5b84fa19da2327d4a0dc881d4cfe4e3c0074646403c9097a6c98f11f26ddf7717c629e66ffe48dc321f50a2108c06c5c08c22855f299d135a6db3e31965c4dcdf5291048846d4844f87d4f51ab6b482d5fff3795041bafb1034aa2512f20d0e3f818263a5d6184d793016f643e68a274b50a3e947952f9218062b8b605d6f2d044bf89e8c061b3a9b82dd2e73ef6808cd7d0992609438495",  skip_error=True)

token = tokens.default_token_manager.get_access_token()
link = 'https://aleeexgerttt.amocrm.ru'

headers = {
    'Authorization': 'Bearer ' + token
}

r = requests.get(link + "/api/v2/account", headers=headers)
print(json.loads(r.content.decode('utf-8')))
