# -*- coding: utf-8 -*-
class string_list:
    def __init__(self,max_size):
        self.max_size=max_size
        self.str=""
        self.length=0
        
    def is_empty(self):
        if self.length==0:
            return True
        else:
            return False
        
    def size(self):
        return self.length
        
    def create(self):
        input_str=input()
        if len(input_str)>self.max_size:
            print("len str>max_size,unable to save excess parts")
            self.str=input_str[:self.max_size]
            self.length = self.max_size
        else:
            self.str=input_str
            self.length = len(input_str)
            
    def append_str(self,string):
        len_string = string.length
        string_ = string.str
        if len_string+self.length>=self.max_size:
            print("len str>max_size,unable to save excess parts")
            size = self.max_size-self.length
            self.str=self.str+string_[0:size]
            self.length = self.max_size
        else:
            self.str = self.str+string_
            self.length = self.length+len_string
            
    #get sub str from ipos and len(sub str) = length       
    def get_sub_string_ipos(self,ipos,length):
        if ipos>self.length-1 or ipos<0 or length<1 or (length+ipos)>self.length:
            print("unable to get sub string")
        else:
            substring=self.str[ipos:ipos+length]
            return substring
        
    def converse(self):
        self.str=self.str[::-1]
        print(self.str)
   
      
    def str_tok(self,char):
        return self.str.split(char)
    
    def upper_str(self):
        self.str=self.str.upper()
        print(self.str)
        
    def lower_str(self):
        self.str=self.str.lower()
        print(self.str)
        
    def show_only_CharNum(self):
        string = self.str
        srt_ = self.str.lower()
        fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
        for c in srt_:
            if not c in fomart:
                string=string.replace(c,' ')
        print(string)
        return string
                
    #find sub str       
    def find_sub_str(self,string):
        return self.str.find(string.str)

    #bf       
    def find_sub_str_bf(self,string):
        tmp_len = string.length
        str_tmp = string.str
        str_src = self.str
        if string.length> self.length:
            print("unable to match")
            return
        else:
            i=0
            while(i<=self.length-tmp_len):
                it=i
                j=0
                tag=False
                while j<tmp_len:
                    if str_src[i]==str_tmp[j]:
                        i=i+1
                        j=j+1
                    else:
                        break
                if j == tmp_len:
                    print("match success:",it)
                    tag=True
                    break
                else:
                    i=it+1
            if tag== False:
                print("match failed")

    #kmp
    def find_sub_str_kmp(self,string):
        str_tmp = string.str
        str_src = self.str
        
        #next array
        next_array = [None for x in range(0,len(str_tmp))]
        next_array[0]=-1
        k_=-1
        j_=0
        while j_<len(str_src):
            if k_==-1 or str_src[j_]==str_src[k_]:
                k_=k_+1
                j_=j_+1
                next_array[j_]=k_
            else:
                k_=next_array[k_]
                
        #kmp
        i=0
        j=0
        length = len(str_tmp)
        while i<len(str_src) and j<length:
            if j==-1 or str_src[i]==str_tmp[j]:
                i=i+1
                j=j+1
            else:
                j=next_array[j]
        if j==length:
            print("match success:",i-length)
        else:
            print("match failed")
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        