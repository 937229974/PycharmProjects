import qrcode

qr = qrcode.QRCode(
    version=None,  # version:值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 控制二维码的错误纠正功能。可取值下列4个常量。
    box_size=10,  # 控制二维码中每个小格子包含的像素数。
    border=2,  # 控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）
)
url = 'helllp'
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image()
img.save('123.png')
