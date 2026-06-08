#!/usr/bin/python
# Filename: Sample.py
# Description: Implementation of the Sample class

from cos.data.score.Score import Score

class OneShotSample(Score):
    def __init__(self):
        Score.__init__(None)
        return

    def add(self, v:float):
        if not(self.counter):
            self.counter   = v

    def reset(self):
        Score.reset(None)
        return 

    def mean(self):
        if not self.counter:
            return 0.0
        return self.counter

    def min(self):
        return self.mean()

    def max(self):
        return self.mean()


class MaxSample(OneShotSample):
    def __init__(self):
        OneShotSample.__init__(self)
        return

    def add(self, v:float):
        if not(self.counter):
            self.counter   = v
            return
        
        if self.counter < v:
            return
        
        self.counter    = v
        return

    def evaluate( self ):
        return self.counter

class Sample(Score):
    def __init__(self):
        Score.__init__([])
        return

    def update( self, counter, duration ):
        self.counter.append(counter)
        self.duration	= duration
        return

    def evaluate( self ):
        return self.mean()

    def add(self, t, v:float):
        self.counter.add( v )
        return

    def reset(self):
        samples, self.counter = self.counter, []
        return samples

    def mean(self):
        if not self.counter:
            return 0.0
        return sum(self.counter) / len(self.counter)

    def average(self):
        return self.mean()

    def min(self):
        return min(self.counter) if self.counter else 0.0

    def max(self):
        return max(self.counter) if self.counter else 0.0


class TimedSample(Score):
    def __init__(self):
        Score.__init__([])
        return

    def update( self, counter, duration ):
        self.counter.append( (duration,counter) )
        self.duration	= duration
        return

    def reset(self):
        samples, self.counter = self.counter, []
        return samples

    def mean(self):
        if not self.counter:
            return 0.0

        return sum(v for _, v in self.counter) / len(self.counter)

    def average(self):
        if not self.counter:
            return 0.0

        tmin = min(t for t, _ in self.counter) if self.counter else 0.0
        tmax = max(t for t, _ in self.counter) if self.counter else 0.0

        return sum(v for _, v in self.counter) / (tmax-tmin)

    def min(self):
        return min(v for _, v in self.counter) if self.counter else 0.0

    def max(self):
        return max(v for _, v in self.counter) if self.counter else 0.0


