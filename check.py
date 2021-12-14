import dns.resolver
import time
import sys
import os.path


dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

yahoo = ('mta7.am0.yahoodns.net.',
         'mta6.am0.yahoodns.net.', 'mta5.am0.yahoodns.net.')
gmail = ('alt3.gmail-smtp-in.l.google.com.', 'alt4.gmail-smtp-in.l.google.com.',
         'alt1.gmail-smtp-in.l.google.com.', 'alt2.gmail-smtp-in.l.google.com.', 'gmail-smtp-in.l.google.com.')
hotmail = ('hotmail-com.olc.protection.outlook.com.')
outlook = ('outlook-com.olc.protection.outlook.com.')
cox = ('cxr.mx.a.cloudfilter.net.')
comcast = ('mx2h1.comcast.net.', 'mx1a1.comcast.net.', 'mx1c1.comcast.net.',
           'mx1h1.comcast.net.', 'mx2a1.comcast.net.', 'mx2c1.comcast.net.')
aol = ('mx-aol.mail.gm0.yahoodns.net.')
rackspace = ('mx1.emailsrvr.com.','mx2.emailsrvr.com.')
icloud = ('mx01.mail.icloud.com.','mx02.mail.icloud.com.')
msn =('	msn-com.olc.protection.outlook.com.')
centurylink = ('mx.centurylink.net.')
web = ('web-com.mail.eo.outlook.com.')
wanadoo =('	blackhole.wanadoo.com.')
gmx = ('mx00.gmx.net.','mx01.gmx.net.')
live = ('live-com.olc.protection.outlook.com.')
rogers = ('	mx-rogers.mail.am0.yahoodns.net.')
juno = ('mx.vgs.untd.com','mx.dca.untd.com.')
sympatico =('mxmta.owm.bell.net.')
earthlink = ('mx01.oxsus-vadesecure.net.', 'mx02.oxsus-vadesecure.net.', 'mx03.oxsus-vadesecure.net.', 'mx04.oxsus-vadesecure.net.')
bellsouth = ('al-ip4-mx-vip1.prodigy.net.','	ff-ip4-mx-vip2.prodigy.net.','ff-ip4-mx-vip1.prodigy.net.','al-ip4-mx-vip2.prodigy.net.')  #check this
att =       ('al-ip4-mx-vip2.prodigy.net.','al-ip4-mx-vip1.prodigy.net.','ff-ip4-mx-vip2.prodigy.net.','ff-ip4-mx-vip1.prodigy.net.')   #check this
verizon = ('mx-aol.mail.gm0.yahoodns.net.')
netzero = ('mx.dca.untd.com.','mx.vgs.untd.com.')
ntt = ('mxa-004dc302.gslb.pphosted.com.','mxb-004dc302.gslb.pphosted.com.')
tiscali = ('etb-3.mail.tiscali.it.','etb-4.mail.tiscali.it.','imp-5.mail.tiscali.it.','etb-1.mail.tiscali.it.','etb-2.mail.tiscali.it.')
yandex = ('mx.yandex.ru.')
zynga =('mxa-00296702.gslb.pphosted.com.','mxb-00296702.gslb.pphosted.com.')
optonline = ('mx.mx-altice.prod.cloud.synchronoss.net.')
frontier = ('mx.dlls.pa.frontiernet.net.','mx.frontiernet.net.')

########################################################################################################################
usa_directory = './usa/'
canada_directory = './canada/'
france_directory = './france/'
australia_directory = './australia/'
japan_directory = './japan/'

########################################################################################################################

filename = input("\033[94m[?]\033[97m drag the \033[91memail-list \033[97m:")
# loading the file. This is just a simple file with email addresses consecutive lines
try:
    print("Trying to open file ", filename)
    with open(filename) as f:
        domains = [line.rstrip() for line in f]
except:
    print("Error while loading", filename)
    sys.exit("IO error")
else:
    print(len(domains), "addresses loaded...starting mx lookup.\n\n")

time.sleep(1)

mxRecords = []
emailAddresses = []


# we use domain.split("@",1)[1] to seperate the domain from the email addresses
# the try-catch is necessary to avoid stopping th execution when a lookup fails.
def lookup():
    print("\n\033[92m[+]\033[97m Starting...")
    print("\033[92m[+]\033[97m Scanning...")
    for domain in domains:
        try:
            answers = dns.resolver.query(domain.split("@", 1)[1], 'MX')
        except Exception as e:
            print("some error")
            mxRecord = "some error"
        else:

            mxRecord = answers[0].exchange.to_text()
            if mxRecord in yahoo:
                print("\033[91m[!]\033[97m", domain, "is using yahoo")
                file = open("yahoo.txt", "a")
                file.write(domain + "\n")
                file.close()  # lol
            elif mxRecord in gmail:
                print("\033[91m[!]\033[97m", domain, "is using gmail")
                file = open("gmail.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in hotmail:
                print("\033[91m[!]\033[97m", domain, "is using hotmail")
                file = open("hotmail.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in outlook:
                print("\033[91m[!]\033[97m", domain, "is using outlook")
                file = open("outlook.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in cox:
                print("\033[91m[!]\033[97m", domain, "is using cox")
                file = open("cox.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in comcast:
                print("\033[91m[!]\033[97m", domain, "is using comcast")
                file = open("comcast.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in aol:
                print("\033[91m[!]\033[97m", domain, "is using aol")
                file = open("aol.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in rackspace:
                print("\033[91m[!]\033[97m", domain, "is using rackspace")
                file = open("rackspace.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in icloud:
                print("\033[91m[!]\033[97m", domain, "is using icloud")
                file = open("icloud.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in msn:
                print("\033[91m[!]\033[97m", domain, "is using msn")
                file = open("msn.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in centurylink:
                print("\033[91m[!]\033[97m", domain, "is using centurylink")
                file = open("centurylink.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in web:
                print("\033[91m[!]\033[97m", domain, "is using web")
                file = open("web.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in wanadoo:
                print("\033[91m[!]\033[97m", domain, "is using wanadoo")
                file = open("wanadoo.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in gmx:
                print("\033[91m[!]\033[97m", domain, "is using gmx")
                file = open("gmx.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in live:
                print("\033[91m[!]\033[97m", domain, "is using live")
                file = open("live.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in verizon:
                print("\033[91m[!]\033[97m", domain, "is using verizon")
                file = open("verizon.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in bellsouth:
                print("\033[91m[!]\033[97m", domain, "is using bellsouth")
                file = open("bellsouth.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in att:
                print("\033[91m[!]\033[97m", domain, "is using att")
                file = open("att.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in comcast:
                print("\033[91m[!]\033[97m", domain, "is using comcast")
                file = open("comcast.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in netzero:
                print("\033[91m[!]\033[97m", domain, "is using netzero")
                file = open("netzero.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in ntt:
                print("\033[91m[!]\033[97m", domain, "is using ntt")
                file = open("ntt.txt", "a")
                file.write(domain + "\n")
                file.close()
            # elif mxRecord in qwest:
            #     print("\033[91m[!]\033[97m", domain, "is using qwest")
            #     file = open("qwest.txt", "a")
            #     file.write(domain + "\n")
            #     file.close()
            # elif mxRecord in sbcglobal:
            #     print("\033[91m[!]\033[97m", domain, "is using sbcglobal")
            #     file = open("sbcglobal.txt", "a")
            #     file.write(domain + "\n")
            #     file.close()
            elif mxRecord in tiscali:
                print("\033[91m[!]\033[97m", domain, "is using tiscali")
                file = open("tiscali.txt", "a")
                file.write(domain + "\n")
                file.close()
            # elif mxRecord in vodafone:
            #     print("\033[91m[!]\033[97m", domain, "is using vodafone")
            #     file = open("vodafone.txt", "a")
            #     file.write(domain + "\n")
            #     file.close()
            # elif mxRecord in yandex:
                print("\033[91m[!]\033[97m", domain, "is using yandex")
                file = open("yandex.txt", "a")
                file.write(domain + "\n")
                file.close()
            # elif mxRecord in zoho:
            #     print("\033[91m[!]\033[97m", domain, "is using zoho")
            #     file = open("zoho.txt", "a")
            #     file.write(domain + "\n")
            #     file.close()
            elif mxRecord in zynga:
                print("\033[91m[!]\033[97m", domain, "is using zynga")
                file = open("zynga.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in yandex:
                print("\033[91m[!]\033[97m", domain, "is using yandex")
                file = open("yandex.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in optonline:
                print("\033[91m[!]\033[97m", domain, "is using optonline")
                file = open("optonline.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in frontier:
                print("\033[91m[!]\033[97m", domain, "is using frontier")
                file = open("frontier.txt", "a")
                file.write(domain + "\n")
                file.close()
            else :
                print("\033[91m[!]\033[97m", domain, "is using unknown")
                file = open("unknown.txt", "a")
                file.write(domain + "\n")
                file.close()
        finally:
            mxRecords.append(mxRecord)
            emailAddresses.append(domain)
            print(domain, ":", mxRecord + "\n")
            time.sleep(.200)
    return mxRecord

#print time taken by above function to run and return the time in seconds







if __name__ == "__main__":
    start_time = time.time()
    lookup()
    print("\n\033[91m[!]\033[97m", len(emailAddresses), "emails sorted")
    print("\n\033[91m[!]\033[97m", "--- %s seconds ---" % (time.time() - start_time))

