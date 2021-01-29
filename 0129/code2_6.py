scores=[88,90,95]
scores.append(34)
scores.append(72)
scores.remove(72)
scores[0]=82
total=sum(scores)
avg=total/len(scores)
print(f'合計{total}点、平均{avg:.1f}点')
