import streamlit as st
import math
import pandas as pd

df = pd.read_csv('cost.csv')
df1 = pd.read_csv('cost1.csv')
df2 = pd.read_csv('slider.csv')

st.header("FinAILab's Jupyterhub Price Calculator")

def tabs(default_tabs = [], default_active_tab=0):
        if not default_tabs:
            return None
        active_tab = st.radio("", default_tabs, index=default_active_tab)
        child = default_tabs.index(active_tab)+1
        # st.markdown("""  
        #     <style type="text/css">
        #     div[role=radiogroup] > label > div:first-of-type {
        #        display: none
        #     }
        #     div[role=radiogroup] {
        #         flex-direction: unset
        #     }
        #     div[role=radiogroup] label {             
        #         border: 1px solid #999;
        #         background: #EEE;
        #         padding: 4px 12px;
        #         border-radius: 4px 4px 0 0;
        #         position: relative;
        #         top: 1px;
        #         }
        #     div[role=radiogroup] label:nth-child(""" + str(child) + """) {    
        #         background: #FFF !important;
        #         border-bottom: 1px solid transparent;
        #     }            
        #     </style>
        # """,unsafe_allow_html=True)        
        return active_tab

page = tabs(["By Resources", "By number of users"])

if page == "By Resources":

    def value(cpu,mem,sto):
        mem = f'{mem}GB'
        sto = f'{sto}GB'

        k=list(df2["CPUs"])
        l=list(df2["Memory"])
        m=list(df2["Storage"])
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
                temp=pd.DataFrame(df2.iloc[[i]]).iloc[:,3:8]
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
        
        k=list(df2["CPU"])
        l=list(df2["GPU Memory"])
        
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
                temp=pd.DataFrame(df2.iloc[[i]]).iloc[:,10:15]
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

        
elif page == "By number of users":
        basic = df1.iloc[0: 16, :9]

        AWS = df.iloc[35: 43, :6]
        PaperSpace = df.iloc[47: 54, :6]
        GCP = df.iloc[58: 62, :7]
        Azure = df.iloc[66: 72, :7]

        Condition = st.radio("You want to see recommendations for?", options=['Without GPU', 'With GPU'])
        if Condition == 'Without GPU':
            user = st.select_slider("Choose the number of users", options=[1, 2, 4, 5, 10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 85, 100])
            if user == 1:
                st.info(f"CPU : {list(basic.iloc[0])[1]}")
                st.info(f"Memory : {list(basic.iloc[0])[2]}")
                st.info(f"Storage : {list(basic.iloc[0])[3]}")
                st.info(f"AWS : {list(basic.iloc[0])[4]}")
                st.info(f"GCP : {list(basic.iloc[0])[5]}")
                st.info(f"Azure : {list(basic.iloc[0])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[0])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[0])[8]}")
            elif user == 2:
                st.info(f"CPU : {list(basic.iloc[1])[1]}")
                st.info(f"Memory : {list(basic.iloc[1])[2]}")
                st.info(f"Storage : {list(basic.iloc[1])[3]}")
                st.info(f"AWS : {list(basic.iloc[1])[4]}")
                st.info(f"GCP : {list(basic.iloc[1])[5]}")
                st.info(f"Azure : {list(basic.iloc[1])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[1])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[1])[8]}")
            elif user == 4:
                st.info(f"CPU : {list(basic.iloc[2])[1]}")
                st.info(f"Memory : {list(basic.iloc[2])[2]}")
                st.info(f"Storage : {list(basic.iloc[2])[3]}")
                st.info(f"AWS : {list(basic.iloc[2])[4]}")
                st.info(f"GCP : {list(basic.iloc[2])[5]}")
                st.info(f"Azure : {list(basic.iloc[2])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[2])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[2])[8]}")
            elif user == 5:
                st.info(f"CPU : {list(basic.iloc[3])[1]}")
                st.info(f"Memory : {list(basic.iloc[3])[2]}")
                st.info(f"Storage : {list(basic.iloc[3])[3]}")
                st.info(f"AWS : {list(basic.iloc[3])[4]}")
                st.info(f"GCP : {list(basic.iloc[3])[5]}")
                st.info(f"Azure : {list(basic.iloc[3])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[3])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[3])[8]}")
            elif user == 10:
                st.info(f"CPU : {list(basic.iloc[4])[1]}")
                st.info(f"Memory : {list(basic.iloc[4])[2]}")
                st.info(f"Storage : {list(basic.iloc[4])[3]}")
                st.info(f"AWS : {list(basic.iloc[4])[4]}")
                st.info(f"GCP : {list(basic.iloc[4])[5]}")
                st.info(f"Azure : {list(basic.iloc[4])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[4])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[4])[8]}")
            elif user == 12:
                st.info(f"CPU : {list(basic.iloc[5])[1]}")
                st.info(f"Memory : {list(basic.iloc[5])[2]}")
                st.info(f"Storage : {list(basic.iloc[5])[3]}")
                st.info(f"AWS : {list(basic.iloc[5])[4]}")
                st.info(f"GCP : {list(basic.iloc[5])[5]}")
                st.info(f"Azure : {list(basic.iloc[5])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[5])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[5])[8]}")
            elif user == 15:
                st.info(f"CPU : {list(basic.iloc[6])[1]}")
                st.info(f"Memory : {list(basic.iloc[6])[2]}")
                st.info(f"Storage : {list(basic.iloc[6])[3]}")
                st.info(f"AWS : {list(basic.iloc[6])[4]}")
                st.info(f"GCP : {list(basic.iloc[6])[5]}")
                st.info(f"Azure : {list(basic.iloc[6])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[6])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[6])[8]}")
            elif user == 20:
                st.info(f"CPU : {list(basic.iloc[7])[1]}")
                st.info(f"Memory : {list(basic.iloc[7])[2]}")
                st.info(f"Storage : {list(basic.iloc[7])[3]}")
                st.info(f"AWS : {list(basic.iloc[7])[4]}")
                st.info(f"GCP : {list(basic.iloc[7])[5]}")
                st.info(f"Azure : {list(basic.iloc[7])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[7])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[7])[8]}")
            elif user == 25:
                st.info(f"CPU : {list(basic.iloc[8])[1]}")
                st.info(f"Memory : {list(basic.iloc[8])[2]}")
                st.info(f"Storage : {list(basic.iloc[8])[3]}")
                st.info(f"AWS : {list(basic.iloc[8])[4]}")
                st.info(f"GCP : {list(basic.iloc[8])[5]}")
                st.info(f"Azure : {list(basic.iloc[8])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[8])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[8])[8]}")
            elif user == 30:
                st.info(f"CPU : {list(basic.iloc[9])[1]}")
                st.info(f"Memory : {list(basic.iloc[9])[2]}")
                st.info(f"Storage : {list(basic.iloc[9])[3]}")
                st.info(f"AWS : {list(basic.iloc[9])[4]}")
                st.info(f"GCP : {list(basic.iloc[9])[5]}")
                st.info(f"Azure : {list(basic.iloc[9])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[9])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[9])[8]}")
            elif user == 40:
                st.info(f"CPU : {list(basic.iloc[10])[1]}")
                st.info(f"Memory : {list(basic.iloc[10])[2]}")
                st.info(f"Storage : {list(basic.iloc[10])[3]}")
                st.info(f"AWS : {list(basic.iloc[10])[4]}")
                st.info(f"GCP : {list(basic.iloc[10])[5]}")
                st.info(f"Azure : {list(basic.iloc[10])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[10])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[10])[8]}")
            elif user == 50:
                st.info(f"CPU : {list(basic.iloc[11])[1]}")
                st.info(f"Memory : {list(basic.iloc[11])[2]}")
                st.info(f"Storage : {list(basic.iloc[11])[3]}")
                st.info(f"AWS : {list(basic.iloc[11])[4]}")
                st.info(f"GCP : {list(basic.iloc[11])[5]}")
                st.info(f"Azure : {list(basic.iloc[11])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[11])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[11])[8]}")
            elif user == 60:
                st.info(f"CPU : {list(basic.iloc[12])[1]}")
                st.info(f"Memory : {list(basic.iloc[12])[2]}")
                st.info(f"Storage : {list(basic.iloc[12])[3]}")
                st.info(f"AWS : {list(basic.iloc[12])[4]}")
                st.info(f"GCP : {list(basic.iloc[12])[5]}")
                st.info(f"Azure : {list(basic.iloc[12])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[12])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[12])[8]}")
            elif user == 75:
                st.info(f"CPU : {list(basic.iloc[13])[1]}")
                st.info(f"Memory : {list(basic.iloc[13])[2]}")
                st.info(f"Storage : {list(basic.iloc[13])[3]}")
                st.info(f"AWS : {list(basic.iloc[13])[4]}")
                st.info(f"GCP : {list(basic.iloc[13])[5]}")
                st.info(f"Azure : {list(basic.iloc[13])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[13])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[13])[8]}")
            elif user == 85:
                st.info(f"CPU : {list(basic.iloc[14])[1]}")
                st.info(f"Memory : {list(basic.iloc[14])[2]}")
                st.info(f"Storage : {list(basic.iloc[14])[3]}")
                st.info(f"AWS : {list(basic.iloc[14])[4]}")
                st.info(f"GCP : {list(basic.iloc[14])[5]}")
                st.info(f"Azure : {list(basic.iloc[14])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[14])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[14])[8]}")
            elif user == 100:
                st.info(f"CPU : {list(basic.iloc[15])[1]}")
                st.info(f"Memory : {list(basic.iloc[15])[2]}")
                st.info(f"Storage : {list(basic.iloc[15])[3]}")
                st.info(f"AWS : {list(basic.iloc[15])[4]}")
                st.info(f"GCP : {list(basic.iloc[15])[5]}")
                st.info(f"Azure : {list(basic.iloc[15])[6]}")
                st.info(f"DigitalOcean : {list(basic.iloc[15])[7]}")
                st.info(f"PaperSpace : {list(basic.iloc[15])[8]}")
            
        elif Condition == 'With GPU':
            
            usercp = st.radio("Select Cloud Provider", options=['AWS', 'GCP', 'Azure', 'PaperSpace'])
            if usercp =='AWS':
                nou = st.select_slider("Choose the number of users", options=[5, 10, 20, 25, 50, 100, 150, 200])
                if nou == 5:
                    st.info(f"CPU : {list(AWS.iloc[0])[1]}")
                    st.info(f"GPU Memory : {list(AWS.iloc[0])[2]}")
                    st.info(f"Storage : {list(AWS.iloc[0])[3]}")
                    st.info(f"Instance Type : {list(AWS.iloc[0])[4]}")
                    st.info(f"Pricing : {list(AWS.iloc[0])[5]}")
                elif nou == 10:
                    st.info(f"CPU : {list(AWS.iloc[1])[1]}")
                    st.info(f"GPU Memory : {list(AWS.iloc[1])[2]}")
                    st.info(f"Storage : {list(AWS.iloc[1])[3]}")
                    st.info(f"Instance Type : {list(AWS.iloc[1])[4]}")
                    st.info(f"Pricing : {list(AWS.iloc[1])[5]}")
                elif nou == 20:
                    st.info(f"CPU : {list(AWS.iloc[2])[1]}")
                    st.info(f"GPU Memory : {list(AWS.iloc[2])[2]}")
                    st.info(f"Storage : {list(AWS.iloc[2])[3]}")
                    st.info(f"Instance Type : {list(AWS.iloc[2])[4]}")
                    st.info(f"Pricing : {list(AWS.iloc[2])[5]}")
                elif nou == 25:
                    st.info(f"CPU : {list(AWS.iloc[3])[1]}")
                    st.info(f"GPU Memory : {list(AWS.iloc[3])[2]}")
                    st.info(f"Storage : {list(AWS.iloc[3])[3]}")
                    st.info(f"Instance Type : {list(AWS.iloc[3])[4]}")
                    st.info(f"Pricing : {list(AWS.iloc[3])[5]}")
                elif nou == 50:
                    st.info(f"CPU : {list(AWS.iloc[4])[1]}")
                    st.info(f"GPU Memory : {list(AWS.iloc[4])[2]}")
                    st.info(f"Storage : {list(AWS.iloc[4])[3]}")
                    st.info(f"Instance Type : {list(AWS.iloc[4])[4]}")
                    st.info(f"Pricing : {list(AWS.iloc[4])[5]}")
                elif nou == 100:
                    st.info(f"CPU : {list(AWS.iloc[5])[1]}")
                    st.info(f"GPU Memory : {list(AWS.iloc[5])[2]}")
                    st.info(f"Storage : {list(AWS.iloc[5])[3]}")
                    st.info(f"Instance Type : {list(AWS.iloc[5])[4]}")
                    st.info(f"Pricing : {list(AWS.iloc[5])[5]}")
                elif nou == 150:
                    st.info(f"CPU : {list(AWS.iloc[6])[1]}")
                    st.info(f"GPU Memory : {list(AWS.iloc[6])[2]}")
                    st.info(f"Storage : {list(AWS.iloc[6])[3]}")
                    st.info(f"Instance Type : {list(AWS.iloc[6])[4]}")
                    st.info(f"Pricing : {list(AWS.iloc[6])[5]}")
                elif nou == 200:
                    st.info(f"CPU : {list(AWS.iloc[7])[1]}")
                    st.info(f"GPU Memory : {list(AWS.iloc[7])[2]}")
                    st.info(f"Storage : {list(AWS.iloc[7])[3]}")
                    st.info(f"Instance Type : {list(AWS.iloc[7])[4]}")
                    st.info(f"Pricing : {list(AWS.iloc[7])[5]}")
                
            elif usercp =='PaperSpace':
                nou = st.select_slider("Choose the number of users", options=[15, 20, 25, 40, 50, 55, 100])
                if nou == 15:
                    st.info(f"CPU : {list(PaperSpace.iloc[0])[1]}")
                    st.info(f"GPU Memory : {list(PaperSpace.iloc[0])[2]}")
                    st.info(f"CPU Memory : {list(PaperSpace.iloc[0])[3]}")
                    st.info(f"Instance Type : {list(PaperSpace.iloc[0])[4]}")
                    st.info(f"Pricing : {list(PaperSpace.iloc[0])[5]}")
                elif nou == 20:
                    st.info(f"CPU : {list(PaperSpace.iloc[1])[1]}")
                    st.info(f"GPU Memory : {list(PaperSpace.iloc[1])[2]}")
                    st.info(f"CPU Memory : {list(PaperSpace.iloc[1])[3]}")
                    st.info(f"Instance Type : {list(PaperSpace.iloc[1])[4]}")
                    st.info(f"Pricing : {list(PaperSpace.iloc[1])[5]}") 
                elif nou == 25:
                    st.info(f"CPU : {list(PaperSpace.iloc[2])[1]}")
                    st.info(f"GPU Memory : {list(PaperSpace.iloc[2])[2]}")
                    st.info(f"CPU Memory : {list(PaperSpace.iloc[2])[3]}")
                    st.info(f"Instance Type : {list(PaperSpace.iloc[2])[4]}")
                    st.info(f"Pricing : {list(PaperSpace.iloc[2])[5]}") 
                elif nou == 40:
                    st.info(f"CPU : {list(PaperSpace.iloc[3])[1]}")
                    st.info(f"GPU Memory : {list(PaperSpace.iloc[3])[2]}")
                    st.info(f"CPU Memory : {list(PaperSpace.iloc[3])[3]}")
                    st.info(f"Instance Type : {list(PaperSpace.iloc[3])[4]}")
                    st.info(f"Pricing : {list(PaperSpace.iloc[3])[5]}") 
                elif nou == 50:
                    st.info(f"CPU : {list(PaperSpace.iloc[4])[1]}")
                    st.info(f"GPU Memory : {list(PaperSpace.iloc[4])[2]}")
                    st.info(f"CPU Memory : {list(PaperSpace.iloc[4])[3]}")
                    st.info(f"Instance Type : {list(PaperSpace.iloc[4])[4]}")
                    st.info(f"Pricing : {list(PaperSpace.iloc[4])[5]}") 
                elif nou == 55:
                    st.info(f"CPU : {list(PaperSpace.iloc[5])[1]}")
                    st.info(f"GPU Memory : {list(PaperSpace.iloc[5])[2]}")
                    st.info(f"CPU Memory : {list(PaperSpace.iloc[5])[3]}")
                    st.info(f"Instance Type : {list(PaperSpace.iloc[5])[4]}")
                    st.info(f"Pricing : {list(PaperSpace.iloc[5])[5]}") 
                elif nou == 100:
                    st.info(f"CPU : {list(PaperSpace.iloc[6])[1]}")
                    st.info(f"GPU Memory : {list(PaperSpace.iloc[6])[2]}")
                    st.info(f"CPU Memory : {list(PaperSpace.iloc[6])[3]}")
                    st.info(f"Instance Type : {list(PaperSpace.iloc[6])[4]}")
                    st.info(f"Pricing : {list(PaperSpace.iloc[6])[5]}")

            elif usercp =='GCP':
                nou = st.select_slider("Choose the number of users", options=[3, 6, 10, 25])
                if nou == 3:
                    st.info(f"CPU : {list(GCP.iloc[0])[1]}")
                    st.info(f"GPU Type : {list(GCP.iloc[0])[2]}")
                    st.info(f"RAM : {list(GCP.iloc[0])[3]}")
                    st.info(f"Instance Type : {list(GCP.iloc[0])[4]}")
                    st.info(f"Type : {list(GCP.iloc[0])[5]}")
                    st.info(f"Pricing : {list(GCP.iloc[0])[6]}")
                elif nou == 6:
                    st.info(f"CPU : {list(GCP.iloc[1])[1]}")
                    st.info(f"GPU Type : {list(GCP.iloc[1])[2]}")
                    st.info(f"RAM : {list(GCP.iloc[1])[3]}")
                    st.info(f"Instance Type : {list(GCP.iloc[1])[4]}")
                    st.info(f"Type : {list(GCP.iloc[1])[5]}")
                    st.info(f"Pricing : {list(GCP.iloc[1])[6]}")
                elif nou == 10:
                    st.info(f"CPU : {list(GCP.iloc[2])[1]}")
                    st.info(f"GPU Type : {list(GCP.iloc[2])[2]}")
                    st.info(f"RAM : {list(GCP.iloc[2])[3]}")
                    st.info(f"Instance Type : {list(GCP.iloc[2])[4]}")
                    st.info(f"Type : {list(GCP.iloc[2])[5]}")
                    st.info(f"Pricing : {list(GCP.iloc[2])[6]}")
                elif nou == 25:
                    st.info(f"CPU : {list(GCP.iloc[3])[1]}")
                    st.info(f"GPU Type : {list(GCP.iloc[3])[2]}")
                    st.info(f"RAM : {list(GCP.iloc[3])[3]}")
                    st.info(f"Instance Type : {list(GCP.iloc[3])[4]}")
                    st.info(f"Type : {list(GCP.iloc[3])[5]}")
                    st.info(f"Pricing : {list(GCP.iloc[3])[6]}")
            elif usercp =='Azure':
                nou = st.select_slider("Choose the number of users", options=[8, 12, 15, 25, 35, 75])
                if nou == 8:
                    st.info(f"CPU : {list(Azure.iloc[0])[1]}")
                    st.info(f"GPU Memory : {list(Azure.iloc[0])[2]}")
                    st.info(f"RAM : {list(Azure.iloc[0])[3]}")
                    st.info(f"Instance Type : {list(Azure.iloc[0])[4]}")
                    st.info(f"Series : {list(Azure.iloc[0])[5]}")
                    st.info(f"Pricing : {list(Azure.iloc[0])[6]}")
                elif nou == 12:
                    st.info(f"CPU : {list(Azure.iloc[1])[1]}")
                    st.info(f"GPU Memory : {list(Azure.iloc[1])[2]}")
                    st.info(f"RAM : {list(Azure.iloc[1])[3]}")
                    st.info(f"Instance Type : {list(Azure.iloc[1])[4]}")
                    st.info(f"Series : {list(Azure.iloc[1])[5]}")
                    st.info(f"Pricing : {list(Azure.iloc[1])[6]}")
                elif nou == 15:
                    st.info(f"CPU : {list(Azure.iloc[2])[1]}")
                    st.info(f"GPU Memory : {list(Azure.iloc[2])[2]}")
                    st.info(f"RAM : {list(Azure.iloc[2])[3]}")
                    st.info(f"Instance Type : {list(Azure.iloc[2])[4]}")
                    st.info(f"Series : {list(Azure.iloc[2])[5]}")
                    st.info(f"Pricing : {list(Azure.iloc[2])[6]}")
                elif nou == 25:
                    st.info(f"CPU : {list(Azure.iloc[3])[1]}")
                    st.info(f"GPU Memory : {list(Azure.iloc[3])[2]}")
                    st.info(f"RAM : {list(Azure.iloc[3])[3]}")
                    st.info(f"Instance Type : {list(Azure.iloc[3])[4]}")
                    st.info(f"Series : {list(Azure.iloc[3])[5]}")
                    st.info(f"Pricing : {list(Azure.iloc[3])[6]}")
                elif nou == 35:
                    st.info(f"CPU : {list(Azure.iloc[4])[1]}")
                    st.info(f"GPU Memory : {list(Azure.iloc[4])[2]}")
                    st.info(f"RAM : {list(Azure.iloc[4])[3]}")
                    st.info(f"Instance Type : {list(Azure.iloc[4])[4]}")
                    st.info(f"Series : {list(Azure.iloc[4])[5]}")
                    st.info(f"Pricing : {list(Azure.iloc[4])[6]}")
                elif nou == 75:
                    st.info(f"CPU : {list(Azure.iloc[5])[1]}")
                    st.info(f"GPU Memory : {list(Azure.iloc[5])[2]}")
                    st.info(f"RAM : {list(Azure.iloc[5])[3]}")
                    st.info(f"Instance Type : {list(Azure.iloc[5])[4]}")
                    st.info(f"Series : {list(Azure.iloc[5])[5]}")
                    st.info(f"Pricing : {list(Azure.iloc[5])[6]}")
                
