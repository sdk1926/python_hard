# 파이썬 심화
# Asyncio
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return(yield) 사용
# 즉, 실행 Stop -> 다른 작업으로 위임 -> Stop 지점 부터 재실행 원리
# non-blocking 비동기 처리에 적합

# BlockIO -> 스레드 사용 
# 쓰레드 개수 및 GIL 문제 염두, 공유 메모리 문제 해결 
# 순차 실행

import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

urls =['https://daum.net', 'https://google.com', 'https://apple.com', 'https://tistory.com', 'https://github.com/', 'https://gmarket.co.kr/']
start = timeit.default_timer()

def fetch(url):
    print('Thread Name : ', threading.current_thread().getName(), 'start', url)
    urlopen(url)
    print('Tread Name : ', threading.current_thread().getName(), 'Done', url)

if __name__ == '__main__':
    # 함수 실행 
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in urls:
            executor.submit(fetch, url)


    # 완료시간 - 시작시간
    duration = timeit.default_timer() - start

    # 총 실행 시간
    print('Total Time : ', duration)