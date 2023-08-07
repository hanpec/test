from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# 鍵の生成
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# 公開鍵の取得
public_key = private_key.public_key()

# メッセージの暗号化
message = b"This is a pan,pbn,pcn,pdn,pen!"
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 復号化
decrypted_message = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("おりじなる めっせーじ：", message)
print("復号化されたメッセージ：", decrypted_message.decode('utf-8'))
