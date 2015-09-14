#/usr/bin/python!
import sys
import numpy as np
import os
import argparse
from argparse import ArgumentParser
import datetime
import matplotlib.pyplot as plt
path="./Measurements"

#---------------Functions-----------------
def pot_box(x,L): #potential energy
	
	if x>=-L or x<=L:
		if x>=-L/8 and x<=L/8:
			return 0
		else:
			return 0
	else:
		return float("inf")
def Numerov_psi(ee,psi0,psi1,L,steps,m,hq):
	q=[]
	psi=[]
	h=L*2/steps
	h12=h**2/12.0
#	print("h12",h12)
	psi.append(psi0)
	psi.append(psi1)

#	print(pot_box(-L,2.0*L))
	f1=m/hq**2*2.0*(pot_box(-L,2.0*L)-ee)
	q.append(psi[0]*(1.0-h12*f1))
	f1=m/hq**2*2.0*(pot_box(-L+h,2*L)-ee)
	q.append(psi[1]*(1.0-h12*f1))
#	print(q[0])
#	print(q[1])	
	for ix in range(2,steps+1):
		x=-L+h*ix
		q.append(h**2*f1*psi[ix-1]+2.0*q[ix-1]-q[ix-2])
		f1=m/hq**2*2.0*(pot_box(x,2.0*L)-ee) 
		psi.append(q[ix]/(1.0-h12*f1))
#		print(-L+ix*h)
		#print("f1: ",f1)
#	print("psi: ",psi)
#	print("q",q)
#	steps=steps
#	x_axe= [x*2.0/steps for x in range(-steps/2,steps/2+1)]
#	print(x_axe)
#	plot=plt.plot(x_axe,psi)
#	plt.show()
	return psi

def main(argv): #Main Program
	ee=5
	psi0=0.0
	psi1=1.0
	L=1.0
	steps=1000
#	m=9.109
#	hq=6.62606957*10**-34
	m=1
	hq=1
	eps=0.001
	mark1=0
	mark2=0
	while True: #Shooting method, searching for two points one above 0 and one beneath
		psi=Numerov_psi(ee,psi0,psi1,L,steps,m,hq)
		if mark1==1 and mark2==1: break
		print(psi[steps])
		if psi[steps]>0:
			e0=ee
			ee+=0.01
			mark1=1
		else:
			e1=ee
			ee+=0.01
			mark2=1
			
		#if mark1==1 and mark2==1: break		
	while True: #search for a point where psi < eps --> eps 
		if abs(psi[steps])<eps: break
		ee=(e0+e1)/2
		psi=Numerov_psi(ee,psi0,psi1,L,steps,m,hq)
		if psi[steps]>0:
			e0=ee
		else:
			e1=ee
		ee=(e0+e1)/2
#		print(psi[steps])
#		print(eps)
		
	print(ee)

	#------------Normalize----------------
	h=L*2/steps
	psi2=[]
	T=0
	ii=0
	for i in psi:
		psi2.append(i**2)
	while True:
		if ii>=steps:break
		T+=h/2*(psi2[ii]+psi2[ii+1])
		ii+=1
	print(T)
	for i in range(0,steps+1): psi[i]=psi[i]/np.sqrt(T)	
	#-----------------------------------
	
	psi2=[]
	for i in psi:
		psi2.append(i**2)

	x_axe= [x*2.0/steps for x in range(-steps/2,steps/2+1)]
	pot_plot=[]
	for i in x_axe:
		pot_plot.append(pot_box(i,L))
	plot=plt.plot(x_axe,psi2)
#	plot_pot=plt.plot(x_axe,pot_plot)
	plt.show()
			
		
#Start Main Program
if __name__=="__main__":
	main(sys.argv) 

