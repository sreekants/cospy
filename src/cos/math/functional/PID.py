#!/usr/bin/python
# Filename: PID.py
# Description: Proportional–integral–derivative (PID) functor

class PID:
    def __init__(self, Fplant, Kp,  Ki, Kd, Fp, Fi=None, Fd=None,):
          self.Fplant    = Fplant
          self.Kp   = Kp
          self.Fp   = Fp
          self.Ki   = Ki
          self.Fi   = Fi
          self.Kd   = Kd
          self.Fd   = Fd

          if self.Fi is None:
                self.Fi = self.Fi.integral()

          if self.Fd is None:
                self.Fd = self.Fd.differential()
          return

    def __call__(self, x):
        result  = self.Kp*self.Fp(x) 

        if self.Ki is not None:
            result  = result + self.Ki*self.Fi(x)

        if self.Kd is not None:
            result  = result + self.Kd*self.Fd(x)

        return result

if __name__ == "__main__":
	test = PID(start,stop,terms,N)
