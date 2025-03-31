# 🔐 Secure Socket Communication with DH Key Exchange & AES Encryption

<br>
이 프로젝트는 Python 소켓 프로그래밍을 기반으로 Diffie-Hellman 키 교환(DH) 및 AES 암호화를 통해 안전한 통신을 구현한 실습용 예제입니다.

- **키 교환**: Diffie-Hellman(DH)을 통해 안전하게 공유 키 생성  
- **암호화**: 공유 키를 기반으로 AES-256 암호화를 적용  
- **통신 구조**: 클라이언트-서버 구조 기반의 소켓 통신  

---
<br>

## 📁 파일 구성

| 파일명        | 설명 |
|---------------|------|
| `server.py`   | 서버 측 프로그램. 클라이언트와 연결 후 DH 키 교환 수행 및 AES 복호화 |
| `client.py`   | 클라이언트 측 프로그램. 서버와 연결 후 키 교환 및 AES 암호화 메시지 전송 |
| `DH.py`       | Diffie-Hellman 관련 함수 정의 |
| `internet.py` | 네트워크 설정 및 경로 변수 관리 |
| `AES.py`      | AES 암호화/복호화 함수 정의 |

---

<br>

## 🔄 동작 방식 요약
### 1. 키 교환
1. 서버가 클라이언트에게 DH 키 교환을 요청
2. 클라이언트가 수락 시, DH 키 교환 수행:
   - `prime`, `generator` 공유
   - 서로의 DH 계산 값 교환
   - `Shared Key` 계산 후, SHA-256으로 압축하여 AES 키 생성
### 2. 암호화 및 전송
- 클라이언트가 사용자 입력을 AES-256으로 암호화하여 전송
- 서버가 수신된 암호문을 복호화하여 출력

---

