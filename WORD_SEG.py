import dictionary
import surname
import math
#the function to adjust segmentation according to the rules           
#  
#  name: adjust
#  @param   result  type<class 'list'>  the list which is the result of the basic segmentation
#  @return  result  type<class 'list'>  the list which is the result after the adjustment
#  
#    this function first add three special signs '***' in the list in case of the IndexError.
#    then make a judgment for each word in the list, to find the word which is fit for one of the sepcial cases(bugs)
#    and deal with it relevantly.
#    after the handling of all the words, return the current list(result) which is more perfect.
#
def adjust(result):
        result = ['***'] + result
        result.append('***')
        result.append('***')
        i = 1
        while result[i] != '***':
                #in following cases, two words should be segmented as one word
                #'花儿'form
                if result[i+1] == '儿':
                        result[i] += result[i+1]
                        del result[i+1]

                #'物理学家'form, noun + '家手性员子化头者'  
                if dictionary.A.get(result[i],(1,'0'))[1] == 'n' and result[i+1] in '家手性员子化头者':
                        result[i] += result[i+1]
                        del result[i+1]
                #'非党员'form, '非' + noun    
                if result[i] == '非' and dictionary.A.get(result[i+1],(1,'0'))[1] == 'n':
                        result[i+1] = result[i] + result[i+1]
                        del result[i]
                #'陈总'form, surname + respectful rank    
                if dictionary.A.get(result[i],(1,'0'))[1] == 'nr' and result[i+1] in '老总董':
                        result[i] += result[i+1]
                        del result[i+1]

                #'容不容易'form, for a verb of a adjective with two words in 'A不AB' form    
                if result[i] == result[i+2][0] and result[i+1] == '不'\
                         and len(result[i+2]) == 2 and dictionary.A.get(result[i+2],(1,'0'))[1] in 'av':
                        result[i] = result[i] + result[i+1] + result[i+2]
                        del result[i+1]
                        del result[i+1]

                #in following cases, the word has a special segmentation
                #'听说读写' should be segmented as '听|说|读|写'
                if result[i] == '听说' and result[i+1] == '读写':
                        result = result[:i]+[result[i][0],result[i][1],result[i+1][0],result[i+1][1]]+result[i+2:]

                #'四分之一'form, '分之'should be segmented as one word
                if result[i][-1] == '分' and result[i+1][0] == '之' and is_num(result[i][:-1]):
                        if is_num(result[i+1][1:]):
                                result = result[:i]+[result[i][:-1],'分之',result[i+1][1:]]+result[i+2:]
                        elif result[i+1] == '之' and is_num(result[i+2]):
                                result = result[:i]+[result[i][:-1],'分之']+result[i+2:]

                #in following cases, one word should be segmented as several words
                if len(result[i]) == 3:
                        #'想一想','看没看'form, verb A in 'A一A','A了A','A没A' should be segmented as three single words 
                        if result[i][1] in '一了没' and result[i][0] == result[i][2] and 'v' in dictionary.A.get(result[i][0],(1,'0'))[1]:
                                result = split(result,i,3)
                        #'打得倒','提不高'form, verb A and complement B in 'A得B','A不B' should be segmented as three single words
                        if result[i][1] in '得不' and 'v' in dictionary.A.get(result[i][0],(1,'0'))[1]:
                                result = split(result,i,3)

                #'未完成'form, verb with a negtive adverb in front of it, the adverb and verb should be segmented, sepcial case '未来','不停','没有'     
                if result[i][0] in '不没未' and 'v' in dictionary.A.get(result[i][1:],(1,'0'))[1] and result[i] not in ['未来','不断','不停','不禁','没有']:
                        result = split(result,i,2)

                #'***的'form, '的' should be segmented, sepcial case '有的','目的'
                if len(result[i]) > 1 and result[i][-1] == '的' and result[i] not in ['好的','有的','别的','目的']:
                        result = split(result,i,-2)
                        
                #'不好'form, adjective with a negtive adverb '不' in front of it, '不' should be segmented
                if result[i][0] == '不' and dictionary.A.get(result[i][1:],(1,'0'))[1] == 'a':
                        result = split(result,i,2)
                        
                #'那人'form, '这' or '那' in front of a noun of a measure word, '这' or '那' should be segmented   
                if result[i][0] in '这那哪' and dictionary.A.get(result[i][1:],(1,'0'))[1] in 'nm':
                        result = split(result,i,2)

                #'本校'form, the following pronoun in front of a noun of a measure word should be segmented, sepcial case '全部'    
                if result[i][0] in '各每某本该此全':
                        if dictionary.A.get(result[i][1:],(1,'0'))[1] in 'nm' and result[i][1:] not in ['部','力']:
                                result = split(result,i,2)
                        for j in range(len(result[i+1])-1):
                                if dictionary.A.get(result[i+1][:j+1],(1,'0'))[1] == 'm' and dictionary.A.get(result[i+1][j+1:],(1,'0'))[1] == 'n':
                                        result = result[:i+1] + [result[i+1][:j+1],result[i+1][j+1:]] + result[i+2:]
                                        break

                #'越走越远','又高又大'form  
                if len(result[i]) == 4 and result[i][0] == result[i][2] and result[i][0] in '越又':
                        #'越来越' should be segmented as one word
                        if result[i][:3] in ['越来越','越來越']:
                                result = split(result,i,-2)
                        #in other '越A越B','又A又B' forms, is should be segmented as four single words
                        else:
                                result = split(result,i,4)

                #'看着'form, the tense auxiliary word '着' should be segmented, sepcial case '沉着','执着'
                if len(result[i]) > 1 and result[i][-1] in '着' and 'v' in dictionary.A.get(result[i][:-1],(1,'0'))[1] and result[i] not in ['沉着','执着','点着','睡着']:
                        result = split(result,i,-2)
                        
                
                #'所想'form, '所' in front of a verb should be segmented, sepcial case '所有','所谓'   
                if result[i][0] == '所' and 'v' in dictionary.A.get(result[i][1:],(1,'0'))[1] and result[i] not in ['所有','所谓']:
                        result = split(result,i,2)

                #'生于','驶向'form, these prepositions after a verb should be segmented, sepcial case '关于','敢于'  
                if result[i][-1] in '于向自' and 'v' in dictionary.A.get(result[i][:-1],(1,'0'))[1] and result[i] not in ['关于','属于','敢于','善于','出于']:
                        result = split(result,i,-2)

                #'十个'form, in measure words, the number should be segmented, '千克','千米' are measure words.    
                if result[i] not in ['千克','千米','一些'] and dictionary.A.get(result[i][1:],(1,'0'))[1] in 'mq' and not is_num(result[i][1:]) and is_num(result[i][0]):
                        result = split(result,i,2)
                        
                if result[i][0] in '第数约近幾數上同':
                        #'第一','上百'form, the number should be segmented
                        if len(result[i]) == 2 and is_num(result[i][1]):
                                result = split(result,i,2)
                        #'近千人','数百家'form， the number should be segmented('两','人' can be a measure unit)
                        elif len(result[i]) > 2 and is_num(result[i][1]) and (dictionary.A.get(result[i][2:],(1,'0'))[1] in 'mq' or result[i][2] in ['兩','两','只','块','项','人']):
                                result = split(result,i,3)

                #'多人','来个', the words which show the probability in front of the measure unit should be segmented            
                if is_num(result[i-1]) and result[i][0] in '多来几余' and (dictionary.A.get(result[i][1:],(1,'0'))[1] in 'mq' or result[i][1:] in ['兩','两','只','块','项','人']):
                        result = split(result,i,2)

                #'成功之路'form, structure auxiliary word '之' should be segmented
                if len(result[i]) > 2 and result[i][-2] == '之' and dictionary.A.get(result[i][-1],(1,'0'))[1] == 'n':
                        result = split(result,i,-3)

                #for the chinese name
                if surname.is_surname(result[i]):
                        if len(result[i+1]) == 1 and len(result[i+2]) == 1 and dictionary.A.get(result[i+1],(0,'0'))[0] + dictionary.A.get(result[i+2],(0,'0'))[0] < 8000:
                                result[i] = result[i] + result[i+1] + result[i+2]
                                del result[i+1]
                                del result[i+1]
                        elif len(result[i+1]) == 1 and dictionary.A.get(result[i+1],(0,'0'))[0] < 4000:
                                result[i] += result[i+1]
                                del result[i+1]
                        
                i += 1
        del result[0]
        del result[-2:]
        return result


#the function to split one word into several words
#  
#  name: split
#  @param   result  type<class 'list'>  the list which is the result of the segmentation
#  @param   i           type<class 'int'>   the index of the word which should be splited
#  @param   n           type<class 'int'>   the number which means how many parts the word should be split
#  @return  result  type<class 'list'>  the list of the result which the word has already been split
#  
#    this function splits a word in a list character by character into several parts and add into the list 
#    without changing the order.
#    if n>0, it will split from the start of the word.('abcd' into 'a','b','cd')
#    if n<0, it will split from the end of the word.('abcd' into 'ab','c','d')
#
def split(result,i,n):
        midresult = []
        if n > 0:
                for j in range(n-1):
                        midresult.append(result[i][j])
                midresult.append(result[i][n-1:])
                return result[:i]+midresult+result[i+1:]
        elif n < 0:
                midresult.append(result[i][:n+1])
                for j in range(n+1,0,1):
                        midresult.append(result[i][j])
                return result[:i]+midresult+result[i+1:]
        else:
                return result


#  
#  name: wordfreq
#  @param   word        type<class 'str'>       the string(word), of which the frequence is needed
#  @return  n           type<class 'float'>     the new frequence of the word
#  
#    this function find the initial frequence of the word in the dictionary, and make a transformation(which also 
#    depends on the length of the word) such that the frequence could be more rational during the segmentation.
#
def wordfreq(word):
        l = len(word)
        n = math.log2(dictionary.A.get(word,(1,'0'))[0])**0.4*l**1.5
        if l == 1:
                return n ** 0.3
        else:
                return n

#  
#  name: participle
#  @param   string  type<class 'str'>       the string(sentence) that is to be segmented
#  @return  result  type<class 'list'>      the list which is the result of the segmentation
#  
#    the function first create two list: freq and f. 
def dp(string):
        freq = [0] * (len(string) + 1)
        f = [-1] * (len(string) + 1)
        num = []
        k = 0
        for i in range(len(string)-1,-1,-1):
                freq[i] = freq[i+1] + wordfreq(string[i])
                f[i] = i+1
                if '龥' >= string[i] >= '一':
                        for j in range(1,17):
                                if i + j <= len(string) - 1:
                                        if freq[i+j+1]+wordfreq(string[i:i+j+1])> freq[i]:
                                                freq[i] = freq[i+j+1]+wordfreq(string[i:i+j+1])
                                                f[i] = i + j + 1
                                else:
                                        break
                        if k != 0:
                                f[i+1] = i + k + 1
                                k = 0
                else:
                        k += 1
        result = []
        i = 0
        while f[i] != -1:
                result.append(string[i:f[i]])
                i = f[i]    
        return result


#  
#  name: is_num
#  @param   s       type<class 'str'>           a string of characters
#  @return  True    type<class 'bool'>      the string of characters is a chinese number
#           False   type<class 'bool'>      the string of characters is not a chinese number
#  
def is_num(s):
    flag=1
    if s == '':
            return False
    for ch in s:
            if( not '0'<=ch<='9'):
                    flag=0
    if(flag==1):
            return True
    if s[-1] in '两' and len(s)!=1:
            return False
    if s[0] not in '一二三四五六七八九十零两':
                if s[0]not in '百千万亿零億兩两兆萬':
                     return False
                elif(len(s)!=1):
                     return False
                else :#special single-character numbers such as ‘百’ in ‘百分之一’
                     return True
    for ch in s:
            if ch not in '一二三四五六七八九十百千万亿零億兩两兆萬两':
                    return False
    if len(s) >= 2 and s[-2]==s[-1] and s[-1]!='亿':
            return False
    return True

#  
#  name: separate
#  @param   s           type<class 'str'>   the string(sentence) that is to be segmented
#  @return  ans_list    type<class 'list'>  the list that consists of all the words segmented
#  
#   This function first find cutting points and cut the sentences into smaller slices. Cutting points are numbers, symbols,etc,
#   and including chinese numbers which have more than one character.
#   Then it passes each part to 'dp' function to segment each slice, and finally connects all the slices.
#
def separate(s):
        i=0
        flag=0#mark the starting index of the current slice
        ans_list=[]
        rear=len(s)
        while(i<rear):
                if('\u4e00'<=s[i]<='\u9fa5'):
                        if not is_num(s[i]):
                                i+=1
                                continue
                        else:
                                j=1
                                while(i+j<=len(s) and is_num(s[i:i+j+1])):
                                        j+=1
                                if j==1:#numbers but only one character, give up cutting(because it may be other meanings)
                                        i+=1
                                        continue
                                else:#numbers more than one character
                                        ans_list.extend(dp(s[flag:i]))
                                        ans_list.extend([s[i:i+j]])
                                        flag=i+j
                                        i=i+j               
                else:
                        j=1
                        while(i+j<len(s) and not '\u4e00'<=s[i+j]<='\u9fa5'):#not chinese characters
                                j+=1
                        ans_list.extend(dp(s[flag:i]))
                        ans_list.extend([s[i:i+j]])
                        flag=i+j
                        i=i+j       
        ans_list.extend(dp(s[flag:rear]))#extend the last slice
        return ans_list

#  
#  name: word_seg
#  @param   s           type<class 'str'>   the string(sentence) that is to be segmented
#  @return  ans_string  type<class 'str'>   the string after segmentation, with partition symbol added
#
def word_seg(s):
        ans_string=s[:2]+'|'
        ans_list=separate(s[2:])
        #print(ans_list)
        ans_list=adjust(ans_list)#adjust the segmentation according to the rules
        for word in ans_list:
                if(word!=''):
                        ans_string+=word+'|'
        return ans_string


