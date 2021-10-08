#!/usr/bin/env python
# coding: utf-8

# In[12]:


# URI 1715

n, m = map(int, input().split())
val = [all(map(int, input().split())) for _ in range(n)]

print(sum(val))


# In[19]:


# URI 1940

jog, rod = map(int, input().split())

pontos = list(map(int, input().split()))
soma_pontos = [sum([pontos[j] for j in range(i, jog*rod, jog)]) for i in range(jog)]
soma_pontos = soma_pontos[::-1]
print(len(soma_pontos)-soma_pontos.index(max(soma_pontos)))


# In[ ]:




