# 파일의 역할
# 컴퓨터에 의해 처리될 또는 처된 데이터와 정보가 임시적으로 저장된 상태
# 일련의 연속된 바이트
# 프로그램(파이썬 소스코드)에 읽혀 가공 처리

# 저장방식에 따라 분류
# 텍스트파일
# 바이너리 파일

# 파일 객체 생성
# 물리적인 파일과 연결된 파일 객체를 생성하고 참조변수에 할당
# 모드 r : 읽기용도, w : 새로운 파일을 쓰기 용도, a : 파일의 끝에 데이터를 덧붙이기 용도
# 파일객체_참조변수 = open(파일이름, 모드)

# 파일 읽기 모드

# 파일 읽기
# 특정 범위의 데이터를 파일에서 읽고 문자열로 반환
# 파일 포인터의 이동을 동반
# open("파일명", "r")

# 파일 쓰기
# 문자열을 파일 포인터가 위치한 지점에 기록
# w 모드로 존재하는 파일 오픈 시 데이터 삭제
# open("파일명", "w")
# .write("파일에 내용 작성")

# 데이터 추가
# 파일의 끝에 데이터를 덧붙이는 작업
# 파일 오픈 후 파일 포인터를 EoF로 이동
# 존재하지 않는 파일은 write와 동일
# open("파일명", "a")
# .write("파일에 내용 작성")

# 반드시 close()를 해야함

# open("khan.txt", "w")
khan_fp = open("khan.txt", "r")
# print(khan_fp.read(10))
# print(khan_fp.readline())
# .strip() : 불필요한 스페이스, 개행문자 등을 지워줌
for motto in khan_fp.readlines():
    print(motto.strip())

khan_fp.close()

khan_fp = open("khan.txt", "a")

khan_fp.write("\n")
khan_fp.write(format("-칭기스 칸-", ">50s"))
khan_fp.close()