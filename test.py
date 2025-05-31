import requests
import subprocess
import datetime
import time

# 저장할 위치
save_path = r'C:\Users\yeomo\Desktop\SASA allskycam\SASA-allSkyCam-and-AWS\image.jpg'

# Git 레포 폴더 경로
git_folder = r'C:\Users\yeomo\Desktop\SASA allskycam\SASA-allSkyCam-and-AWS'

# 이미지 URL
url = "http://nysc.dothome.co.kr/im.jpg"

# Git 명령어 실행 함수
def run_git_command(cmd):
    result = subprocess.run(cmd, cwd=git_folder, shell=True, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr)

# 무한 반복
while True:
    try:
        # 1️⃣ 이미지 다운로드
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"[{datetime.datetime.now()}] 이미지 저장 완료!")

            # 2️⃣ Git add → commit → push
            run_git_command('git add image.jpg')

            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            run_git_command(f'git commit -m "Auto-upload {timestamp}"')

            run_git_command('git push origin main')

        else:
            print(f"[{datetime.datetime.now()}] 이미지 다운로드 실패: {response.status_code}")

    except Exception as e:
        print(f"[{datetime.datetime.now()}] 에러 발생: {e}")

    # 3️⃣ 반복 주기 (예: 3분 = 180초)
    time.sleep(180)
