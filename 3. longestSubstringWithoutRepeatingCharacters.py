def lengthOfLongestSubstring(s):
    n = len(s)
    unique_list = []
    res = 0
    for i in range(n):
        for j in range(i, n):
            if (s[j] in unique_list):
                unique_list.clear()
                break
            else:
                unique_list.append(s[j])
                # Jika tidak ada line di bawah ini res terakhir yang akan didefinisikan bukan res yang benar
                # Pengkondisian untuk menemukan nilai res maksimum
                if (res < j - i + 1):
                    res = j - i + 1

    return res
