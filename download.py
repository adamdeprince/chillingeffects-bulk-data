#!/usr/bin/env python


import urllib2
import os.path

MILLION = 10**6
THOUSAND = 10**3


class DMCAStorage(object):
    @staticmethod
    def _build_path(i):
        millions = (i / MILLION) % 1000
        thousands = (i/ THOUSAND) % 1000
        directory = os.path.join('data', 'json', '%03d' % millions, '%03d' % thousands)
        full_path = os.path.join(directory, '%i.json' % (i,)) 
        return directory, full_path

    def __setitem__(self, k, v):
        k = int(k)
        directory, fullpath = self._build_path(k)
        if os.path.exists(fullpath):
            raise ValueError('Complaint #%d already exist; cannot override' % (k,))
        if not os.path.exists(directory):
            os.makedirs(directory)
        try:
            with open(fullpath, "w") as f:
                f.write(v)
        except KeyboardInterrupt:
            with open(fullpath, "w") as f:
                f.write(v)
            raise

    def __contains__(self, k):
        k = int(k)
        directory, fullpath = self._build_path(k)
        return os.path.exists(fullpath)


    def download(self):
        skips_left = 10
        x = 1
        while True:
            if x not in self:
                print "Requesting #", x
                try:
                    response = urllib2.urlopen('https://www.chillingeffects.org/notices/%d.json' % x).read()
                    skips_left = 10
                    self[x] = response
                        
                except urllib2.HTTPError:
                    print "Skipping ", x
                    skips_left -= 1
                    if not skips_left:
                        raise
            x += 1


DMCAStorage().download()
