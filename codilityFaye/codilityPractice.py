# def solution(S):
#     S = S.lower()
#     S = S.replace("minus", "-")
#     return(S.replace("plus", "+"))
#
# solution("PLUSPLUSMINUS")

# def solution(A):
#     ma = max(A)
#     mi= min(A)
#     return(ma-mi)
#
# def solution(A, B):
#     A.sort()
#     B.sort()
#     i = 0
#     for a in A:
#         if i < len(B) - 1 and B[i] < a:
#             i += 1
#         if a in B:
#             return a
#     return -1
#
# print(solution([1, 3, 2, 4], [4, 6, 9]))

# Q4
# this version only considers positive input
# def solution(N):
#     s=str(N)
#     c=0
#     for i in s[0:len(s)]:
#         if int(i)<5:
#             N=s[:c]+'5'+s[c:]
#             N=int(N)
#             return N
#         else:
#             c=c+1
# #
# print(solution(654))

def solution(N):
    s=str(N)
    if s[0]!='-':
        c=0
        while c<len(s):
            for i in s[0:len(s)]:
                if int(i)<5:
                    N=s[:c]+'5'+s[c:]
                    N=int(N)
                    return N
                else:
                    c=c+1
        if c == len(s):
            N = int(s + '5')
            return N
    else:
        if int(s[-1])<=5:
            N = s + '5'
            return N
        else:
            c = -1
            while c > -len(s)+1:
                for i in s[-len(s)+1:-1]:
                    if int(i)<=5:
                        N=s[:c]+'5'+s[c:]
                        N=int(N)
                        return N
                    else:
                        c=c-1
            if c==-len(s)+1:
                N = s[0]+'5'+s[1:]
                return N
# s ='-123'
# print(s[-1])
#
print(solution(88554))




#
# N=879
# s=str(N)
#
# c=0
# for i in s[0:len(s)]:
#         if int(i)<5:
#             N=s[:c]+'5'+s[c:]
#             N=int(N)
#         else:
#             c = c+1
#
# print(N)