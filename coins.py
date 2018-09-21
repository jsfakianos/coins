change_due = 31.23
available_denominations = [.01,.05,.10,.25,1.00,5.00,10.00,20.00,100.00]

def coins(change_due, i, memo):
    
    memo.append(available_denominations[i])
    s = round(sum(memo), 2)

    if s < change_due:
        return coins(change_due, i, memo)
    elif s > change_due:
        i-=1
        memo.pop()
        return coins(change_due, i, memo)

    return memo

print(coins(change_due=change_due, i=len(available_denominations)-1, memo=[]))
