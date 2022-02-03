#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#code snippet 1
def fun(flavours,s):
    #snippet to split using ;

    for i in range(len(flavours)):
        if type(flavours[i])==float:
            flavours[i]="NA"
        elif type(flavours[i])==str:
            flavours[i]=flavours[i].split(";")

    flavours_new=[]
    for i in flavours:
        for j in i:
            flavours_new.append(j)
    flavours_new=np.unique(flavours_new)

    #snippet to split using ||
    new_flavours=[]
    for i in range(len(flavours_new)):
            new_flavours.append(flavours_new[i].split("||"))

    flavours_new2=[]
    for i in new_flavours:
        for j in i:
            if(len(j)>2):
                flavours_new2.append(j)
    flavours_new2=np.unique(flavours_new2)

    for i in range(len(flavours_new2)):
        flavours_new2[i]=flavours_new2[i].upper()
        flavours_new2[i]=flavours_new2[i].strip()
    flavours_new2=np.unique(flavours_new2)

    for i in range(len(flavours_new2)):
        flavours_new2[i]=flavours_new2[i].replace("NOT SPECIFIED","")

    for i in range(len(flavours_new2)):
        flavours_new2[i]=flavours_new2[i].strip()

    unique_flavours=pd.DataFrame(data=flavours_new2,columns=["flavours"])
    unique_flavours.to_excel(s+".xlsx",sheet_name=s,index=False)
    
product=pd.read_excel("Products.xlsx",sheetname="sheet1")
category=product["market_subcategory"].values  
un_cat=np.unique(category)   
for i in un_cat:
    fun(product[product["market_subcategory"]==i]["flavor"].values,i)
    
    
# code snippet 2

def fun(flavours,s,df):
    #snippet to split using ;

    for i in range(len(flavours)):
        if type(flavours[i])==float:
            flavours[i]="NA"
        elif type(flavours[i])==str:
            flavours[i]=flavours[i].split(";")

    flavours_new=[]
    for i in flavours:
        for j in i:
            flavours_new.append(j)
    flavours_new=np.unique(flavours_new)

    #snippet to split using ||
    new_flavours=[]
    for i in range(len(flavours_new)):
            new_flavours.append(flavours_new[i].split("||"))

    flavours_new2=[]
    for i in new_flavours:
        for j in i:
            if(len(j)>2):
                flavours_new2.append(j)
    flavours_new2=np.unique(flavours_new2)

    for i in range(len(flavours_new2)):
        flavours_new2[i]=flavours_new2[i].upper()
        flavours_new2[i]=flavours_new2[i].strip()
    flavours_new2=np.unique(flavours_new2)

    for i in range(len(flavours_new2)):
        flavours_new2[i]=flavours_new2[i].replace("NOT SPECIFIED","")

    for i in range(len(flavours_new2)):
        flavours_new2[i]=flavours_new2[i].strip()

    unique_flavours=pd.Series(flavours_new2)
    df[s]=unique_flavours
    return df
df=pd.DataFrame()    
product=pd.read_excel("Products.xlsx",sheetname="sheet1")
category=product["market_subcategory"].values  
un_cat=np.unique(category)   
for i in un_cat:
    df=fun(product[product["market_subcategory"]==i]["flavor"].values,i,df)

