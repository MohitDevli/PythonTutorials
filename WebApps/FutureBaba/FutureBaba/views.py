from django.http import HttpResponse
from django.shortcuts import render, redirect

html="""
<!DOCTYPE html><head><title>Your Future.</title><style>

.split {
  height: 100%;
  width: 50%;
  position: fixed;
  z-index: 1;
  top: 0;
  overflow-x: hidden;
  padding-top: 20px;
}

/* Control the left side */
.left {
  left: 50;

}


.bg{
  background-color: #111;
}


/* Control the right side */
.right {
  right: 0;
  
}

/* If you want the content centered horizontally and vertically */
.centered {
  position: absolute;
  text-align: center;
}


</style></head>

<body bgcolor="#166bb5">

<center>
	<textarea rows="20px" cols="100px" readonly="true">""" 


fhtml="""
<!DOCTYPE html><head><title>Your Future.</title><style>

.split {
  height: 100%;
  width: 50%;
  position: fixed;
  z-index: 1;
  top: 0;
  overflow-x: hidden;
  padding-top: 20px;
}

/* Control the left side */
.left {
  left: 50;

}


.bg{
  background-color: #111;
}


/* Control the right side */
.right {
  right: 0;
  
}

/* If you want the content centered horizontally and vertically */
.centered {
  position: absolute;
  text-align: center;
}


</style></head>

<body bgcolor="#166bb5">

<center>
	<textarea rows="40px" cols="100px" readonly="true">""" 



def index(request):
	return render(request, 'index.html')


def Start(request):
	return render(request, 'start.html')


def BodyType(request):
	return render(request, 'bodyType.html')

def FemaleBody(request):
	return render(request, 'femaleBody.html')

def MaleBody(request):	
	return render(request, 'maleBody.html')

def Terms(request):
	return render(request, 'terms.html')
	


end="""</textarea>
</center>
</body>
</html>
"""

#HeadSize
BigheadSize="Inteliigent Person. "
SmallHeadSize='You have less money. '

####
LargeAndWideHeadSize='You have more money. You are also Culturer. '
WideAndRoundedHeadSize='You have more money. You are also Culturer. '

#EyeBrows
#

#Eyes
redEyeCorner="You are Favorable of Girls. "
redEyes="You have more attractiveness toward womens. "
deepEyes='You are a most clever person and sometime become Trustless, in eye of others. '
roundedEyes='You are powerful and having muscular strength or you are a Robber. '
bigAndRaisedEyes='You have a good manners and in terms of giving or accepting love, you are so trustful. '


#Noes
SimpleNoes='You are a Intelligent Person and also do lot of HardWork. '
HighNoes="You are trustable Person. "
FattyNose='Sometime you be so Selfish. '									
compresedAtMidddleNose='You have so cleverness, and also has attention towards Sexual thinking. '


#Ears
SmallEars='You are a type of fullish person. '
BigEars='You are so Intelligent. '
ThinEars='You are a type of leader or a King with so intteligence. '
FattyEars='You are a type of person which has less or no manners also you are not a trustable Person in eye of others. '

#Face
RoundedFace='You are a person, which will be happy most of time. Also you are so frank and social. '
HighFace='You are a Intelligent person and have good manners. '
BigFace='You have not so much good luck also, There is chances that you will be poor in future if you not do much Hardwork for make your future bright. '
SmallFace='You are Intelligent,but you are not so Peaceful Person. '
SmallAndBlack='You are Intelligent,but you are not so Peaceful Person. You may have habit of fighting with everyone. '
SmallAndRed='You are Intelligent,but you are not so Peaceful Person. You area type of selfish Person. '




def Future(request):
	future=''
	if request.method == "POST": 
		try:
			try:
				headSize=request.POST['headSize']
			except:
				headSize=''
			
			
			#Eyes
			redeyecorner=request.POST.get('RedCorners', "off")
			redeye=request.POST.get('RedEyes', "off")
			deepeye=request.POST.get('deepEyes', "off")
			roundedeyes=request.POST.get('roundedEyes', "off")
			bigAndraisedeyes=request.POST.get('bigAndRaisedEyes', "off")
			
			try:
				#Noes
				noseType=request.POST['noseType']
			except:
				noseType=''
				
			compressednoes=request.POST.get('compresedAtMidddle', "off")
			
			try:
				#Ears
				Ears=request.POST['Ears']
			except:
				Ears=''
			
			try:
				#Face
				Face=request.POST['Face']
			except:
				Face='' 
				
			MuscularFace=request.POST.get('muscularFace', 'off')
			
			#Head
			if headSize=='Big':
				future=future+BigheadSize
			
			elif headSize=='Small':
				future = future + SmallHeadSize
				
			elif headSize=='LargeAndWide':
				future = future +LargeAndWideHeadSize
				
			elif headSize=='WideAndRounded':
				future = future +WideAndRoundedHeadSize			
			
			#Eyes
			if redeyecorner=='on':
				future=future+redEyeCorner
			
			if redeye == 'on':
				future=future+redEyes
				
			if deepeye == 'on':
				future=future+deepEyes
			
			if roundedeyes == 'on':
				future=future+roundedEyes
			
			if bigAndraisedeyes == 'on':
				future=future+bigAndRaisedEyes
				
			
			#Noes
			if noseType=='simple':
				future=future+SimpleNoes
			
			elif noseType=='high':
				future=future+HighNoes
			
			elif noseType=='fatty':
				future=future+FattyNose
			
			if  compressednoes=='on':
				future=future+compresedAtMidddleNose
			
			
			
			#Ears
			if Ears=='smallEars':
				future=future+SmallEars			
			elif Ears=='bigEars':
				future=future+BigEars
			elif Ears=='thinEars':
				future=future+ThinEars
			elif Ears=='fattyEars':
				future=future+FattyEars
			
			
			#Face
			if Face=="roundedFace":
				future=future+RoundedFace
			elif  Face=="highFace":
				future=future+HighFace
			elif  Face=="bigFace":
				future=future+BigFace		
			elif  Face=="smallFace":
				future=future+SmallFace
			elif  Face=="smallAndBlack":
				future=future+SmallAndBlack			
			elif  Face=="smallAndRed":
				future=future+SmallAndRed		
			if MuscularFace=='on':
				future=future+muscularFace
			
		except Exception as e:
			pass
			
	result=html+future+end			
	return HttpResponse(result)


fend="""</textarea>
</center>
</body>
</html>
"""

#Head
WideHead='You may have not so good Luck. '
HighHead='You are lucky, and also you are a sign of Luckyness and Richness for your family. '
halfMoon='You are similar to Goddes Laxmi, you brought Money and Peacefulness in your family, after you taking Birth. '
smallHead='You may be not so rich in your Future. '

#Eyes
BlackAndRoundedEyes='You are so preety and beutiful in your self, and may be you have more attractiveness toward mens. '
RedEyes='You want to be more attractive towards mens, also you may be trustless.'
BigHighBlackAndRedLinesEyes='You are famous or will be famous. '
BlueEyes='You may be trustless and you have more attractiveness toward males. '

#Noes
ParrotNoes='You are famous by your self, also you are so clever, and you are a girl who get the Goodwishes of everyone. '
SimpleNoes='You are beautiful, Inteliigent and a girl who do lot of HardWork. '
FattyNoes='You may be lazy, selfish, and a person who want to live a Happy Life. '
SmallNoes='You are clever person and may be hot have good manners. '

#Ears
HighSimpleEars='You are blessed with Luckyness and you will have a Happy Life. '
IrregularEars='You may have not so good Luck. '

#Face
RoundedFace='You are so lucky, mannerful, have a abiltity to become a good leader, and full of self confidenc. '
HighFace='You are so frank, and have a nature of person which establish his/her Rights everywhere. '
ParentsFace='As your face matches to your parents which is a sign of Luckyness. '



def FFuture(request):
	ffuture=''
	
	if request.method == "POST": 
		try:
			
			try:
				
				#Head
				headSize=request.POST['headSize']
				
			except:
				headSize=''
				
				
			try:	
				
				#Eyes
				Eyes=request.POST['Eyes']
				
			except:
				Eyes=''
				
			
			try:	
				
				#Noes
				Noes=request.POST['Noes']
				
			except:
				Noes=''
			
			try:
				
				#Ears
				Ears=request.POST['Ears']
				
			except:
				Ears=''
				
			try:	
				
				#Face
				Face=request.POST['Face']
				
			except:
				Face=''
				

			#Head
			if headSize=='WideHead':
				ffuture=ffuture+WideHead	
			elif headSize=='HighHead':
				ffuture=ffuture+HighHead
			elif headSize=='halfMoon':
				ffuture=ffuture+halfMoon
			elif headSize=='smallHead':
				ffuture=ffuture+smallHead				
			
			#Eyes
			if Eyes=='BlackAndRoundedEyes':
				ffuture=ffuture+BlackAndRoundedEyes	
			elif Eyes=='RedEyes':
				ffuture=ffuture+RedEyes
			elif Eyes=='BigHighBlackAndRedLinesEyes':
				ffuture=ffuture+BigHighBlackAndRedLinesEyes
			elif Eyes=='BlueEyes':
				ffuture=ffuture+BlueEyes			
			
			
			#Noes
			if Noes=='ParrotNoes':
				ffuture=ffuture+ParrotNoes				
			elif Noes=='SimpleNoes':
				ffuture=ffuture+SimpleNoes	
			elif Noes=='FattyNoes':
				ffuture=ffuture+FattyNoes
			elif Noes=='SmallNoes':
				ffuture=ffuture+SmallNoes
			
			#Ears
			if Ears=='HighSimpleEars':
				ffuture=ffuture+HighSimpleEars	
			elif Ears=='IrregularEars':
				ffuture=ffuture+IrregularEars	
			
			
			#Face
			if Face=='RoundedFace':
				ffuture=ffuture+RoundedFace	
			elif  Face=='HighFace':
				ffuture=ffuture+HighFace	
			elif  Face=='ParentsFace':
				ffuture=ffuture+ParentsFace			
			
			
			
		
		except Exception as e:
			print('-------------\n\n',e,'\n\n----------')
	
	fresult=fhtml+ffuture+fend			
	return HttpResponse(fresult)	


