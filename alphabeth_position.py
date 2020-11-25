def alphabeth_position(text):
    charlist =[]
    numlist=[]
    x=a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z

    for i in text :
        _type= type(i) in str
        if _type==True:
            charlist.append(i)
        else:
            numlist.append(i)

    
