
		
stop_punc='。，?？！、；;]】!！？…'

#add the sentence into the list
def add_sentence(ans_list,sent):
	ans_list.append(str(len(ans_list)+1)+'.'+sent)
	return ans_list

#  
#  name: sentence_segment
#  @param	s	type<class 'str'>	the paragraph to be segmented
#  @return	ans type<class 'list'>	the list containing all sentences
#


def sentence_segment(s):
	import re
	ans=[]
	tmp=''
	i=0
	while(i<len(s)):
		if s[i] in stop_punc:
			tmp+=s[i]
			if(i<len(s)-1 and s[i+1] in '”’》'+stop_punc):
				i+=1
				tmp+=s[i]			
			ans=add_sentence(ans,tmp)
			tmp=''
		elif s[i] =='\n':
			if(tmp!=''):
				ans=add_sentence(ans,tmp)
				tmp=''
		elif s[i] in '"”' or s[i] in "'’":
			tmp+=s[i]			
			if(i>0 and s[i-1] in stop_punc):				
				ans=add_sentence(ans,tmp)
				tmp=''
		elif s[i] in ':：':
			if(i>0 and re.findall(r'[0-9a-zA-Z]',s[i-1])!=[]):
				tmp+=s[i]
			else:
				tmp+=s[i]
				ans=add_sentence(ans,tmp)
				tmp=''
		elif s[i] =='《':
			tmp+=s[i]
			i+=1
			while(s[i]!='》'):
				tmp+=s[i]
				i+=1
			tmp+=s[i]			
		elif re.match(r'\s',s[i]):
			if(len(tmp)==0):
				pass
			elif(i>0 and i<len(s)-1 and re.findall(r'[0-9a-zA-Z]',s[i-1])!=[] and re.findall(r'[0-9a-zA-Z]',s[i+1])!=[]):
				tmp+=s[i]
			else:
				ans=add_sentence(ans,tmp)
				tmp=''
		else:
						tmp+=s[i]
		i+=1
	if(tmp!=''):
				ans=add_sentence(ans,tmp)
	return ans
	

	
	
