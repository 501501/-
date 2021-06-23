def solution(s):
    answer = 0
    count = 1

    s_result = ""
    result_array = []

    for j in range(1, len(s)):
        result = []
        for i in range(0, len(s), j):
            result.append(s[i:i + j])
        #print(result)

        for x in range(len(result)):
            if x < len(result) - 1:
                if result[x] == result[x+1]:
                    count += 1
                    continue

                if result[x] != result[x+1]:
                    if count != 1:
                        s_result += (str(count))
                    s_result += (result[x])
                    count = 1

                elif result[x-1] == result[x]:
                    continue

                else:
                    s_result += result[x]

            else:
                if count != 1:
                    s_result += (str(count))
                s_result += (result[x])
                count = 1

        #print(s_result)
        result_array.append(len(s_result))
        s_result = ""

    if not result_array:
        answer = 1
    else:
        answer = min(result_array)

    #print(answer)
    return answer

#s = input()
#solution(s)
