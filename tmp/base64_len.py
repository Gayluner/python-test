
import base64
from learn import date_type


#Base64编码会把3字节的二进制数据编码为4字节的文本数据
testbase64=b'1'
date_type(testbase64)

s=base64.b64encode(testbase64)
date_type(s)

# 将文本自己数据转化为二进制字节数据
des=base64.b64decode(s)
date_type(des)

#不足三个字节的将字节转换为4个字节
testbase64=b'a'
s=base64.b64encode(testbase64)
date_type(s)

des=base64.b64decode(s)
date_type(des)


testbase64=b'ab'
s=base64.b64encode(testbase64)
date_type(s)

des=base64.b64decode(s)
date_type(des)

testbase64=b'abc'
s=base64.b64encode(testbase64)
date_type(s)

des=base64.b64decode(s)
date_type(des)

