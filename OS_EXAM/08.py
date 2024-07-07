#내 파이썬 프로그램의 이름을 알아보자.
#psutil로 프로세스 조회후 0.8py와 id가 같은 것을 찾아서 출력
import psutil
import os

if __name__ == '__main__':
    # 현재 프로세스의 PID
    current_pid = os.getpid()
    print('08.py 프로세스 아이디 :', current_pid)
    
    # 모든 프로세스를 순회하면서 현재 프로세스를 찾기
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.pid == current_pid:
            print(f"PID: {proc.pid}, Name: {proc.info['name']}")