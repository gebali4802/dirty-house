# 2023 전국 청소년 GAME 코딩대회
## 더러운 우리집
이 게임은 2023 전국 청소년 GAME 코딩대회 출품작입니다. 이 게임은 파이썬으로 작성되었으며, 세이브 파일 저장을 위해 SQLite3모듈을 사용하였습니다. 그 외에는 기본 내장 라이브러리와 직접 만든 내부 라이브러리를 사용하였으며, 윈도우 환경에서 원활하게 돌아갑니다. 타 환경에서는 작동은 합니다만, 사실상 윈도우 전용입니다. 이 게임을 만들때 아이디어는 4년전 망상으로만 구상했던 게임의 아이디어를 실제로 만든 것이라 더 애착이 갑니다. 게임은 게임이라고 할것도 없이 보잘것 없을정도로 심심하나 열심히 만들었습니다.

## 시스템
### 수치
이 게임의 수치은 총 5개로 이루어져 있다.
|수치|기본|최대|
|---|---|---|
|돈|100만원|없음|
|스트레스|10|100|
|더러움|10|100|
|인기도|10|100|
|아르바이트|0개|2개|

* 주인공의 돈 : `기본 100만원`, `최대 없음`
* 스트레스 수치 : `기본 10`, `최대 100`
* 집 더러움 정도 : `기본 10`, `최대 100`
* 인기도와 인지도 : `기본 10`, `최대 100`
* 아르바이트 정보 : `기본 0개`, `최대 2개`

### 아르바이트
아르바이트는 총 3개를 할 수 있다. 이 게임의 유일한 수익 창출 수단이며 세금은 복잡하니 계산하지 않는다.
* 1. 편의점 알바
    - 편의점 알바는 월급 150만원이며 시간당 최저시급(9,620)원을 기준으로 할 때 한달간 156시간을 일하며, 일주일동안 5일을 일한다.(주말은 제외한다.)
    - 가끔식 폐기를 가져갈 수 있는데, 이때 스트레스 수치는 5낮아진다.(가끔의 기준은 일주일에 1번 50%의 확률이다.)
    - 그리고 또 가끔식 진상 손님이 올 수 있는데 이 때 스트레스 수치는 3올라간다.(가끔의 기준은 위와 같다.)
    - 매 월 1일에 월급이 들어온다. 앞서 말했듯 세금은 게임 내에서도 계산하지 않는다.
* 2. 카페 알바
    - 카페 알바는 월급 180만원이며 시간당 최저시급(9,620)원을 기준으로 할 때 위 편의점 알바와 같이 한달간 156시간을 일하며, 일주일동안 5일을 일한다.(주말은 제외한다.)
    - 가끔식 진상 손님도 오는데, 이 때 스트레스 수치는 5씩 올라간다.(가끔의 기준은 일주일에 2번 100%의 확률이다.)
    - 편의점 알바와 같이 매 월 1일에 월급이 들어온다.(위에서 말했듯이 세금은 계산하지 않는다.)
* 3. 상하차 알바
    - 상하차 알바는 위와는 다르게 일당으로 계산하며 일당 15만원이다. 하루종일 일하며, 주말에만 할 수 있다.
    - 그리고 상하차 알바는 1달에 2번만 가능하며, 한번 할 때 스트레스 수치가 15높아진다.

## 스토리
### 1년차 - 새로운 시작과 친구들의 모임
주인공은 대학에 진학하면서 대학 근처에서 월세집을 구한다. 월세는 30만원이다. 작은 원룸이지만 주변이 편리하고 대학 생활에 적합한 장소였다. 주인공은 새로운 도전에 두려움을 느끼지만, 동기들과 함께 대학 생활을 시작한다. 이때 최현수라는 친구를 만난다. 첫 학기에는 친구들과 자주 만나고, 다양한 동아리에 가입하며 더 재밌고 새로운 친구들을 만난다. 이제 시작부터 활력 넘치는 대학 생활이 시작된다.

### 2년차 - 과제와 시험의 압박
대학 생활이 익숙해지면서 주인공은 본격적인 과제와 시험에 직면한다. 알바를 하면서 돈을 벌어 월세를 감당하는 동안, 주인공은 강의 내용에 집중하고 과제에 노력한다. 그러나 시간이 부족해지면서 스트레스가 쌓이고, 때로는 좌절과 힘들어함을 느끼게 된다. 주인공은 고민을 털어놓을 친구들을 찾아가고, 도서관이나 공원에서 새로운 공부 방법을 찾아본다. 어려움을 극복하기 위해 노력하는 주인공은 결국 어려운 시험들을 헤쳐나가며 자신감을 회복한다.

### 3년차 - 친구들과의 갈등과 성장
대학 생활의 중간에 주인공은 친구들과의 갈등을 경험한다. 서로 다른 목표와 가치관으로 인해 대립하며 소중한 인연들을 잃을 위기에 처한다. 주인공은 이런 갈등을 해결하기 위해 대화와 이해를 시도한다. 종종 심리적인 도움을 주는 상담사에게 조언을 구하며 자신과 타인을 이해하는 방법을 배워간다. 이 과정에서 주인공은 성장하고 변화하며, 진정한 친구들과의 연결을 강화한다.

### 4년차 - 대학 졸업과 새로운 도전
마지막 학년에 접어들면서 주인공은 대학 생활의 마지막을 선물처럼 여기며 소중한 추억을 만들기 위해 노력한다. 졸업 프로젝트와 취업 준비로 바쁜 일상이 주어지지만, 주인공은 여전히 친구들과 함께 시간을 보내고, 동아리 활동을 즐긴다. 이제는 대학에서의 모든 경험과 지식을 살려 새로운 도전을 위해 대학을 떠나야 한다는 사실에 서운함을 느끼지만, 미래에 대한 희망과 설렘이 주인공을 움직인다.

### 최종 - 새로운 시작, 한 장의 엔딩과 새로운 세계
대학 졸업 후, 주인공은 다른 도시로 이사하며 새로운 삶을 시작한다. 주인공은 대학에서의 경험을 통해 성장하고 변화한 모습으로 다가오는 도전에 맞서야 한다. 게임은 주인공이 이전에 만났던 사람들과 새로운 사람들과의 관계, 업적 및 선택에 따라 다양한 엔딩을 제공한다. 주인공은 새로운 세계에서 자신의 길을 찾고, 행복과 성공을 추구하기 위해 노력한다.