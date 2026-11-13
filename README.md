# Research Portfolio

The hub of the **Structure Recognition Research Program** by Jonghun Choi (최종훈), an independent researcher and 2nd-year student at Inha Technical College.

> How do humans come to see something new?

**Read it here: <https://inha20.github.io/Research-Portfolio/>**

The page shows the two current papers (7 and 8), how all eight papers fit together, the archived early notes (papers 1–6), the order in which the ideas arrived, and the working documents behind them. Every paper lives in its own repository with its own page. This repository only holds the hub that connects them.

Contact: cjh3cjh@naver.com · GitHub profile: [inha20](https://github.com/inha20)

For AI collaborators, the single entry point is [`SESSION_START.md`](https://github.com/inha20/inha20/blob/main/SESSION_START.md) in the `inha20` repository.

---

## 관리 메모 (maintainer notes)

이 저장소는 허브 페이지 하나를 만듭니다. 내용은 전부 `program.toml`에 있고, `build.py`가 그 파일에서 `index.html`과 `404.html`을 생성합니다. 손으로 `index.html`을 고치지 마세요. 다음 빌드에서 덮어써집니다.

### 내용을 바꾸는 순서

1. `program.toml`을 고칩니다. 논문 상태·제목·요약, 지도의 층, 개념 계보, 문서 카드, 소개 문구가 모두 이 파일에 있습니다.
2. `python build.py`를 실행합니다. Python 3.11 이상이 필요하고 표준 라이브러리만 씁니다.
3. `program.toml`, `index.html`, `404.html`을 함께 커밋합니다. `python build.py --check`는 생성 파일이 최신인지 확인하며, 오래됐으면 종료 코드 1을 돌려줍니다.

화면을 로컬에서 보려면 이 폴더에서 `python -m http.server`를 실행하고 `http://localhost:8000/`을 엽니다. `index.html`을 `file://`로 직접 열면 Chrome이 글꼴 파일을 막아서 글꼴이 달라 보입니다.

### 자주 하는 변경

- **논문을 숨기기:** 해당 `[[papers]]` 항목에 `show = false`. 숨긴 논문까지 넣어 미리 보려면 `python build.py --include-hidden --out 임시폴더`(`assets/`가 그 폴더 옆에 있어야 합니다).
- **논문 카드에 링크 더하기:** 해당 `[[papers]]` 항목에 `extra_links = [{ label = "표시 문구", path = "lecture/" }]`. `path`는 그 논문의 Pages 주소 뒤에 붙습니다(예: 7번 논문의 강의 사이트).
- **새 논문 추가:** `[[papers]]`에 항목을 추가하고, 지도에 넣을 층의 `papers` 목록에 번호를 더합니다. 빌드가 빠진 필드와 잘못된 참조를 알려줍니다.
- **링크 미리보기 이미지(`assets/og.png`) 바꾸기:** `python tools/make_og.py`(Playwright와 Chrome 필요). 문구나 디자인을 바꿀 때만 다시 만듭니다.
- **스타일이나 레이아웃을 바꾼 뒤:** `python tools/check_layout.py`(Playwright와 Chrome 필요)가 320~1600px 모든 폭에서 가로 넘침이 없는지 검사합니다. 메뉴가 접히는 폭처럼 두 레이아웃 사이 구간의 문제를 잡기 위한 것입니다.

### 파일

| 경로 | 역할 |
|---|---|
| `program.toml` | 허브의 모든 내용 (유일한 편집 대상) |
| `build.py` | `program.toml`에서 `index.html`·`404.html` 생성, 검증 |
| `src/site.css`, `src/site.js` | 스타일과 동작. 빌드할 때 `index.html` 안에 포함됩니다 |
| `assets/` | 글꼴(OFL, 라이선스는 `assets/fonts/LICENSES.txt`), `favicon.svg`, `og.png` |
| `tools/make_og.py` | `og.png` 생성기 |
| `tools/check_layout.py` | 모든 폭에서 가로 넘침 검사 |
| `docs/` | 2026-10-08 검토 기록 (인계용 내부 문서, 허브에는 연결하지 않음) |

### 바꾸지 않는 것

- 허브 주소 `https://inha20.github.io/Research-Portfolio/`와 이 저장소 이름. 다른 저장소와 프로필 링크가 이 주소를 가리킵니다.
- 각 논문 저장소의 이름과 Pages 주소. 허브는 주소만 가리키고, 논문 쪽 구조는 건드리지 않습니다.
