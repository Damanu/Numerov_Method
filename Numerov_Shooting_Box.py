#/usr/bin/python!

import numpy as np
import os
import argparse
from argparse import ArgumentParser
import datetime

path="./Measurements"

#---------------Functions-----------------
def pot_box(x) #potential energy
	if x>=-L and x<=L
		return 0
	else
		return float("inf")



psi0=0
psi1=1
h=1
h12=h**2/12

p1=psi1
f1=2*(pot(-xmax)-ee)
q0=psi0*(1-h12*f1)
f1=2*(pot(-xmax+h)-ee)
q1=psi1*(1-h12*f1)
	


#Start Main Program
if __name__=="__main__":
	main(sys.argv) 

