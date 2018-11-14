import hashlib
def md5(password):
    hl = hashlib.md5()
    hl.update(password.encode(encoding='utf-8'))
    print('MD5加密前为 ：' + password)
    print('MD5加密后为 ：' + hl.hexdigest())
    return hl.hexdigest()
if __name__ == "__main__":
    password = "a123456"
    md5(password)
