def grade_mcq(sol,ans):
    if(len(sol)!=len(ans)):
        return -1
    count =0
    for i in range(len(sol)):
        if sol[i]==ans[i]:
            count +=1

    return count








exec(input())