#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import time

from subprocess import Popen

devnull = open(os.devnull, 'wb')


ip_araligi_deger = raw_input("IP Araligini giriniz ( example: 192.168.0 ) ---> ")


print 'Taranan ip araligi',ip_araligi_deger


if ip_araligi_deger == "":
 print 'Gecerli bir ip araligi deneyiniz...'

p = []
aktif = 0
yanit_yok = 0
pasif = 0

for aralik in range(0,255):
    ip = ip_araligi_deger + ".%d" % aralik
    p.append((ip, Popen(['ping', '-c', '3', ip], stdout=devnull)))
while p:
    for i, (ip, proc) in enumerate(p[:]):
        if proc.poll() is not None:
            p.remove((ip, proc))
            if proc.returncode == 0:
                print('%s Aktif' % ip)
                aktif = aktif + 1
            elif proc.returncode == 2:
                print('%s Yanit yok' % ip)
                aktif = yanit_yok + 1
            else:
                print('%s Pasif' % ip)
                pasif = pasif + 1
    time.sleep(.04)
devnull.close()


print "Gecerli isletim sistemi",os.name
print "Ag Durumu"
print "Aktif Ipler  [ ",aktif," ]"
print "Pasif IPler [ ",pasif," ]"
print "Yanit Yok  [ ",yanit_yok," ]"


bitis_mesaj = "Tarama tamamlandi.."

print bitis_mesaj
