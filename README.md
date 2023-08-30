# Blog-Checker
 매일 블로그를 작성하는 스터디를 진행하면서 자정에 일일이 들어가 확인하는 것이 번거로웠다. 자동화할 필요성을 느꼈고 해당 코드를 통해 블로그 확인을 대신해주고 그 결과를 메일로 받아볼 수 있는 서비스를 만들었다.

## Usage
1. 먼저 Git Clone을 통해 코드를 받는다.
2. 다음 명령어를 통해 필요한 라이브러리를 받는다.
```shell
pip install -r requirements.txt
```
3. .env 파일을 생성하고 메일링 서비스를 위한 Google 앱 비밀번호를 설정한다

```env
GMAIL_PASSWORD=${GMAIL_PASSWORD}
GMAIL_ID=${GMAIL_ID}
```
4. 해당 코드는 GHA bot이 자동 커밋을 해주기 때문에 해당 권한 설정이 필요하다. 레포지토리 Setting-Actions-General에서 Workflow permissions 설정을 Read and Write permissions로 해주고 Save를 누른다.
<img width="577" alt="스크린샷 2023-08-30 오후 1 18 08" src="https://github.com/SmileJune/blog-checker/assets/91049936/7b3a97a1-1636-4c25-8d6a-8ff1facf7595">

5. main 브랜치에 푸시해서 정상적으로 작동하는지 확인한다.
