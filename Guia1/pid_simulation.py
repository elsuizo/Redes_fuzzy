#! /usr/bin/env python
# -*- coding -*-

class PID:
   """Clase PID"""

   def __init__(self, K_p, K_i, K_d):

       self.K_p = K_p
       self.K_i = K_i
       self.K_d = K_d
   def error(t, zeta, omega_n):




