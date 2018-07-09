from dataclasses import dataclass


@dataclass
class TrustedSource:
    name: str
    url: str


tencent = TrustedSource('Tencent',
                        'https://mirrors.cloud.tencent.com/pypi/simple')

douban = TrustedSource('Douban', 'http://pypi.doubanio.com/simple')

pypi = TrustedSource('Pypi', ' https://pypi.org/simple')

aliyun = TrustedSource('Aliyun', ' https://mirrors.aliyun.com/pypi/simple/')

sources = []

sources.append(tencent)
sources.append(douban)
sources.append(pypi)
sources.append(aliyun)


def __dir__():
    return ['sources']