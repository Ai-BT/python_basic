# %%
# 문제 7567
# 그릇을 바닥에 놓았을 때 그 높이는 10cm 이다. 그런데 두 개의 그릇을 같은 방향으로 포개면 그 높이는 5cm만 증가된다.
# 만일 그릇이 서로 반대방향으로 쌓이면 높이는 그릇만큼, 즉 10cm 늘어난다. 그릇을 괄호 기호로 나타내어 설명해보자.
# 편의상 그릇이 쌓여지는 방향은 왼쪽에서 오른쪽이라고 가정한다. 그림에서 ‘(’은 그릇이 바닥에 바로 놓인 상태를 나타내며, ‘)’은 그릇이 거꾸로 놓인 상태를 나타낸다.

# 만일 그릇이 포개진 모양이 ((((와 같다면 전체의 높이는 25cm가 된다.
# 왜냐하면 처음 바닥에 있는 그릇의 높이가 10cm이고 이후 같은 방향으로 3개의 그릇이 포개져 있으므로 늘어난 높이는 5+5+5=15 이기 때문이다.
# ()()와 같은 경우라면 그 높이는 10*4=40cm가 된다.

# 여러분은 입력에 주어진 모양대로 그릇을 쌓을 때 최종의 전체 그릇 높이를 계산해서 출력해야 한다. 즉 처음 입력으로 주어진 각 그릇의 방향은 바꿀 수 없다.

# 입력
# 첫 줄에는 괄호문자로만 이루어진 문자열이 주어진다. 입력 문자열에서 열린 괄호
# ‘(’은 바로 놓인 그릇, 닫힌 괄호 ‘)’은 거꾸로 놓인 그릇을 나타난다. 문자열의 길이는 3이상 50 이하이다.

# 출력
# 여러분은 그릇 방향이 괄호 문자로 표시된 문자열을 읽어서 그 최종의 높이를 정수로 출력해야 한다.

# 예제 입력 1
# ((((
# 예제 출력 1
# 25
# 예제 입력 2
# ()()()))(
# 예제 출력 2
# 80

plates = input()
ans = 10  # 처음 그릇을 바닥에 놓았을 때 높이 10cm

for i in range(1, len(plates)):
    # 두 번째 그릇부터 이전 그릇과 비교 시작
    if plates[i] == plates[i - 1]:
        ans += 5  # 같은 방향이면 5cm 추가
    else:
        ans += 10  # 다른 방향이면 10cm 추가

print(ans)


# %%
# 5063
# 문제
# 상근이는 TGN사의 사장이다. TGN은 Teenager Game Network의 약자 같지만, 사실 Temporary Group Name의 약자이다.
# 이 회사는 청소년을 위한 앱을 만드는 회사이다. 일년에 걸친 개발기간 끝에 드디어 앱을 완성했고, 이제 팔기만 하면 된다.
# 상근이는 데이트를 인간의 두뇌로 이해할 수 없을 정도로 많이 한다. 따라서 엄청난 데이트 비용이 필요하다. 상근이는 광고를 적절히 해서 수익을 최대한 올리려고 한다.
# 어느 날 하늘을 바라보던 상근이는 시리우스의 기운을 받게 되었고, 광고 효과를 예측하는 능력을 갖게 되었다.
# 광고 효과가 주어졌을 때, 광고를 해야할지 말아야할지 결정하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 N이 주어진다. 다음 N개의 줄에는 3개의 정수 r, e, c가 주어진다.
# r은 광고를 하지 않았을 때 수익, e는 광고를 했을 때의 수익, c는 광고 비용이다. (-106 ≤ r,e ≤ 106, 0 ≤ c ≤ 106)

# 출력
# 각 테스트 케이스에 대해서, 광고를 해야 하면 "advertise", 하지 않아야 하면 "do not advertise", 광고를 해도 수익이 차이가 없다면 "does not matter"를 출력한다.

# 예제 입력 1
# 3
# 0 100 70
# 100 130 30
# -100 -70 40
# 예제 출력 1
# advertise
# does not matter
# do not advertise

case = int(input())

for _ in range(case):
    r, e, c = map(int, input().split())
    if r > e - c:
        print("do not advertise")
    elif r == e - c:
        print("does not matter")
    else:
        print("advertise")

# %%

# 문제 10102
# A와 B가 한 오디션 프로의 결승전에 진출했다. 결승전의 승자는 심사위원의 투표로 결정된다.
# 심사위원의 투표 결과가 주어졌을 때, 어떤 사람이 우승하는지 구하는 프로그램을 작성하시오.

# 입력
# 입력은 총 두 줄로 이루어져 있다. 첫째 줄에는 심사위원의 수 V (1 ≤  V ≤  15)가 주어지고,
# 둘째 줄에는 각 심사위원이 누구에게 투표했는지가 주어진다. A와 B는 각각 그 참가자를 나타낸다.

# 출력
# A가 받은 표가 B보다 많은 경우에는 A
# B가 받은 표가 A보다 많은 경우에는 B
# 같은 경우에는 Tie
# 를 출력한다.

# 예제 입력 1
# 6
# ABBABB
# 예제 출력 1
# B

V = int(input())
vote = list(str(input()))

A = B = 0
for v in vote:
    if v == "A":
        A += 1
    else:
        B += 1

if A > B:
    print("A")
elif A == B:
    print("Tie")
else:
    print("B")
