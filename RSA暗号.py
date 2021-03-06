from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes


# 鍵の生成

# private_key = rsa.generate_private_key(
    # public_exponent=65537,
    # key_size=2048
    # )
    
# # 公開鍰の取変

# public_key = private_key.public_key()

# # 公開鍰の係数の取変

# exponent = public_key.public_numbers().e

# # 公開鍰の指数の取変

# modulus = public_key.public_numbers().n

# # 公開鍰の係数の表示

# print(exponent)

# # 公開鍰の指数の表示

# print(modulus)

# # 公開鍰の係数の表示

# print(exponent)

# # 公開鍰の指数の表示

# print(modulus)

# # メッセレタの生�

# message = b"abcpython"

# # メッセレタの暗号化

# ciphertext = public_key.encrypt(
    # message,
    # padding.OAEP(
        # mgf=padding.MGF1(algorithm=hashes.SHA256()),

            # algorithm=hashes.SHA256(),
            # label=None
            # )
            


# 鍵の生成
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# 公開鍵の取得
# public_key = private_key.public_key()

# 公開鍵の取得
public_key = private_key.public_key()

# メッセージの暗号化
message = b"abcpython"
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

print(f'original msg:{message}')
print(f'Decrypted Msg:{decrypted_message.decode("utf-8")}')

