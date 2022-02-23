import streamlit as st
import math
import pandas as pd

   
df = pd.read_csv('slider.csv')

def value(cpu,mem,sto):
   mem = f'{mem}GB'
   sto = f'{sto}GB'

   k=list(df["CPUs"])
   l=list(df["Memory"])
   m=list(df["Storage"])
   arr=[]
   for i in range(len(k)):
      if k[i] == cpu:
         arr.append(i)
   
   li = []
   for j in arr:
      if l[j] == mem:
         li.append(j)
         
   ll = []
   for x in li:
      if m[x] == sto:
         ll.append(x)
         
   res = []
   ll2 = []
   if not len(ll) == 0:
      for i in ll:
         res = []
         temp=pd.DataFrame(df.iloc[[i]]).iloc[:,3:8]
         a= list(temp['AWS'])
         b=list(temp['GCP '])
         c=list(temp['Azure'])
         d=list(temp['DigitalOcean'])
         e=list(temp['PaperSpace'])

         if not len(a) == 0 and not len(b) == 0 and not len(c) == 0 and not len(d) == 0 and not len(e) == 0:
            res = a + b + c + d + e
            ll2.append(res)
      
   if len(ll2) == 0:
      return None
   else:
      return ll2

def callValue():
   k = value(cpu_count, Memory, Storage)
   if not k:
      st.warning("This combination does'nt exists!")
   else:
      st.info(f"AWS - {k[0][0]}")
      st.info(f"GCP - {k[0][1]}")
      st.info(f"Azure - {k[0][2]}")
      st.info(f"DigitalOcean - {k[0][3]}")
      st.info(f"PaperSpace - {k[0][4]}")

def callValue1():
   k = value1(cpu_count1, Memory1)
   if not k:
      st.warning("This combination does'nt exists!")
   else:
      st.info(f"AWS - {k[0][0]}")
      st.info(f"GCP - {k[0][1]}")
      st.info(f"Azure - {k[0][2]}")
      st.info(f"PaperSpace - {k[0][3]}")

def value1(cpu, mem):
   mem = f'{mem} GB'
   
   k=list(df["CPU"])
   l=list(df["GPU Memory"])
   
   arr=[]
   for i in range(len(k)):
      if k[i] == cpu:
         arr.append(i)
   
   li = []
   for j in arr:
      if l[j] == mem:
         li.append(j)
         
   res = []
   ll2 = []
   if not len(li) == 0:
      for i in li:
         res = []
         temp=pd.DataFrame(df.iloc[[i]]).iloc[:,10:15]
         a=list(temp['AWS1'])
         b=list(temp['GCP1'])
         c=list(temp['Azure1'])
         e=list(temp['PaperSpace1'])

         if not len(a) == 0 and not len(b) == 0 and not len(c) == 0 and not len(e) == 0:
            res = a + b + c + e
            ll2.append(res)
      
   if len(ll2) == 0:
      return None
   else:
      return ll2

cpu_count = st.select_slider("Choose CPU count", options=[1, 2, 4, 6, 8, 12, 16, 32])
Memory = st.select_slider("Choose Memory in GB", options=[1, 2, 4, 8, 12, 16, 32, 48, 64, 128])
Storage = st.select_slider("Choose Storage in GB", options=[25, 50, 80, 100, 160, 200, 320, 400, 640, 960])
GPU = st.radio("Do you need GPU?", options=['yes', 'no'])

callValue()

if GPU =='yes':
   cpu_count1 = st.select_slider("Choose CPU count for GPU", options=[4, 6, 8, 12, 16, 32, 48, 64])
   Memory1 = st.select_slider("Choose GPU Memory in GB", options=[12, 16, 24, 32, 48, 64, 92, 122, 128, 192, 256])
   callValue1()
   



