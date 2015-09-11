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
		return 0
	else:
		return float("inf")

def main(argv): #Main Program
	ee=1.3
	q=[]
	psi=[]
	psi0=0.0
	psi1=1.0
	L=1.0
	steps=100
	h=L*2/steps
	h12=h**2/12.0
	print("h12",h12)
	psi.append(psi0)
	psi.append(psi1)

	print(pot_box(-L,2.0*L))
	f1=2.0*(pot_box(-L,2.0*L)-ee)
	q.append(psi[0]*(1.0-h12*f1))
	f1=2.0*(pot_box(-L+h,2*L)-ee)
	q.append(psi[1]*(1.0-h12*f1))
	print(q[0])
	print(q[1])	
	for ix in range(2,steps+1):
		x=-L+h*ix
		q.append(h**2*f1*psi[ix-1]+2.0*q[ix-1]-q[ix-2])
		f1=2.0*(pot_box(x,2.0*L)-ee) 
		psi.append(q[ix]/(1.0-h12*f1))
		print(-L+ix*h)
		#print("f1: ",f1)
	print("psi: ",psi)
#	print("q",q)
	steps=steps
	x_axe= [x*2.0/steps for x in range(-steps/2,steps/2+1)]
#	print(x_axe)
	plot=plt.plot(x_axe,psi)
	plt.show()

#Start Main Program
if __name__=="__main__":
	main(sys.argv) 

