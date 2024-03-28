import random
import string


# 生成指定长度的随机字符串
def generate_random_string(length):
    letters = string.ascii_letters + string.digits  # 包含字母和数字
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

