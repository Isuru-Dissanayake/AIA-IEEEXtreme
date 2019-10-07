def find_anc(k):
    anc = []
    t = k
    anc.append(t)
    while t>1:
        t = int(t/2)
        anc.append(t)
    return (anc)
t = int(input())
for cases in range(t):
    n,m = list(map(int,input().split()))
    if n == m:
        print (0)
    else:
        n_anc = find_anc(n)
        m_anc = find_anc(m)
        n_len = len(n_anc)
        m_len = len(m_anc)
        if n_len < m_len:
            n_new_anc = n_anc
            m_new_anc = m_anc[-n_len:]
        else:
            m_new_anc = m_anc
            n_new_anc = n_anc[-m_len:]
        indx = len(n_new_anc)
        for i in range(len(n_new_anc)):
            if n_new_anc[i] == m_new_anc[i]:
                indx = i
                break
        dist = n_len + m_len - 2*(len(n_new_anc) - indx)
        print (dist)
        '''
        indx = len(n_anc)
        for i in range(len(n_anc)):
            if n_anc[i] in m_anc:
                indx = i
                break
        dist = len(n_anc) + len(m_anc) - 2*(len(n_anc) - indx)
        print (dist)
        '''