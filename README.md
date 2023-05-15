# GateOpener
# short instruction

apt-get install lighttpd

lighty-enable-mod cgi

service lighttpd force-reload


git clone https://github.com/LakYtron/GateOpener.git


apt-get install python3-rpi.gpio


V kofiguraci lighttpd CGI  - zakomentovat
    $HTTP["url"] =~ "^/cgi-bin" {
        cgi.assign = ( "" => "" )
    }
    
    
Pridat uzivatele www-data do skupiny gpio
/etc/group



Neni potreba

#git clone https://github.com/Leapo/Rock64-R64.GPIO.git
#cp -r R64/ /usr/local/lib/python3.6/dist-packages/
#chmod +x *.py 
#ln -s /usr/local/lib/python3.6/dist-packages/R64 /usr/local/lib/python3.6/dist-packages/RPi
