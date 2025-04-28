# 카드 생성
shape_card = ["S", "D", "H", "C"]
num_card = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# print(*shape_card)
# print(*num_card)

import random
card_list = []


for sh in shape_card :
    for nu in num_card :
        #card_list.append([sh + "_" + nu])
        card_list.append("{}_{}".format(sh, nu))

# 플레이어 생성
print("플레이어 수를 선택")
players = int(input())
if players > 4 :
    print("인원수 초과")
playcardlist = []

# 플레이어 수에 따라 분배 방법 바꾸기
for rnu in range(1) :
    playcardlist.append(random.sample(card_list, players*2 + 2))


dealer = []
player1 = []
player2 = []
player3 = []
player4 = []

if players == 1 :
    dealer.append(playcardlist[0], playcardlist[1])
    player1.append(playcardlist[2], playcardlist[3])
elif players == 2 :
    dealer.append(playcardlist[0], playcardlist[1])
    player1.append(playcardlist[2], playcardlist[3])

    


# dealer.append(playcardlist[0], playcardlist[1])
# player.append(random.sample(card_list, 1))

# print(dealer[0], dealer[1])
# print(player[0], player[1])


# print(str(player[0]).split)
# 플레이어 히트/스탠드/스플릿/더블다운 선택
#if(player[])


# 딜러 카드 오픈 후 히트/스탠드 선택(17부터 히트 불가능)

# 결과 확인
