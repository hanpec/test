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
<<<<<<< HEAD
<<<<<<< HEAD
message = b"abc"
=======
message = b"This is a pan,pbn,pcn,pdn,pen!"
>>>>>>> 2cc911b (branch わけた)
=======
message = b"abc"
>>>>>>> 65a087a (abc)
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

print("original msg:", message)
print("Decrypted Msg:", decrypted_message.decode('utf-8'))
