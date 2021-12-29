import dns.resolver
import time
import sys
import os.path
import os

dirName = 'filtered-domains'
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
rackspace = ('mx1.emailsrvr.com.', 'mx2.emailsrvr.com.')
icloud = ('mx01.mail.icloud.com.', 'mx02.mail.icloud.com.')
msn = ('	msn-com.olc.protection.outlook.com.')
centurylink = ('mx.centurylink.net.')
web = ('web-com.mail.eo.outlook.com.')
wanadoo = ('	blackhole.wanadoo.com.')
gmx = ('mx00.gmx.net.', 'mx01.gmx.net.')
live = ('live-com.olc.protection.outlook.com.')
rogers = ('	mx-rogers.mail.am0.yahoodns.net.')
juno = ('mx.vgs.untd.com', 'mx.dca.untd.com.')
sympatico = ('mxmta.owm.bell.net.')
earthlink = ('mx01.oxsus-vadesecure.net.', 'mx02.oxsus-vadesecure.net.',
             'mx03.oxsus-vadesecure.net.', 'mx04.oxsus-vadesecure.net.')
bellsouth = ('al-ip4-mx-vip1.prodigy.net.', '	ff-ip4-mx-vip2.prodigy.net.',
             'ff-ip4-mx-vip1.prodigy.net.', 'al-ip4-mx-vip2.prodigy.net.')  # check this
att = ('al-ip4-mx-vip2.prodigy.net.', 'al-ip4-mx-vip1.prodigy.net.',
       'ff-ip4-mx-vip2.prodigy.net.', 'ff-ip4-mx-vip1.prodigy.net.')  # check this
verizon = ('mx-aol.mail.gm0.yahoodns.net.')
netzero = ('mx.dca.untd.com.', 'mx.vgs.untd.com.')
ntt = ('mxa-004dc302.gslb.pphosted.com.', 'mxb-004dc302.gslb.pphosted.com.')
tiscali = ('etb-3.mail.tiscali.it.', 'etb-4.mail.tiscali.it.',
           'imp-5.mail.tiscali.it.', 'etb-1.mail.tiscali.it.', 'etb-2.mail.tiscali.it.')
yandex = ('mx.yandex.ru.')
zynga = ('mxa-00296702.gslb.pphosted.com.', 'mxb-00296702.gslb.pphosted.com.')
optonline = ('mx.mx-altice.prod.cloud.synchronoss.net.')
frontier = ('mx.dlls.pa.frontiernet.net.', 'mx.frontiernet.net.')
windstream = ('mx01.windstream.net.')
spectrum = ('mx0.charter.net.')
suddenlink = ('mx.suddenlink.net.')
tds = ('mx.tds.net.')
godaddy = ('smtp.secureserver.net.','mailstore1.secureserver.net')
rediff = ('	mx.rediffmail.rediff.akadns.net.')
#######################-------------------japan-------------------#######################
yahoo_jp = ('mx5.mail.yahoo.co.jp.', 'mx3.mail.yahoo.co.jp.',
            'mx2.mail.yahoo.co.jp.', 'mx1.mail.yahoo.co.jp.')
a24h_co_jp = ('mx01.lolipop.jp.')
excite_co_jp = ('mx.mose-mail.jp.')
goo_jp = ('mta000.goo.ne.jp.')


########################################################################################################################
usa_directory = './usa/'
canada_directory = './canada/'
france_directory = './france/'
australia_directory = './australia/'
japan_directory = './japan/'

########################################################################################################################
try:
        # Create target Directory
    os.mkdir(dirName)
    print("Directory ", dirName,  " Created ")
except FileExistsError:
    print("Directory " , dirName ,  " already exists") 



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
            answers = dns.resolver.resolve(domain.split("@", 1)[1], 'MX')
        except Exception as e:
            print("some error")
            mxRecord = "some error"
        else:

            mxRecord = answers[0].exchange.to_text()
            if mxRecord in yahoo:
                print("\033[91m[!]\033[97m", domain, "is  yahoo")
                file = open("filtered-domains/yahoo.txt", "a")
                file.write(domain + "\n")
                file.close()  # lol
            elif mxRecord in gmail:
                print("\033[91m[!]\033[97m", domain, "is  gmail")
                file = open("filtered-domains/gmail.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in hotmail:
                print("\033[91m[!]\033[97m", domain, "is  hotmail")
                file = open("filtered-domains/hotmail.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in outlook:
                print("\033[91m[!]\033[97m", domain, "is  outlook")
                file = open("filtered-domains/outlook.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in cox:
                print("\033[91m[!]\033[97m", domain, "is  cox")
                file = open("filtered-domains/cox.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in comcast:
                print("\033[91m[!]\033[97m", domain, "is  comcast")
                file = open("filtered-domains/comcast.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in aol:
                print("\033[91m[!]\033[97m", domain, "is  aol")
                file = open("filtered-domains/aol.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in rackspace:
                print("\033[91m[!]\033[97m", domain, "is  rackspace")
                file = open("filtered-domains/rackspace.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in icloud:
                print("\033[91m[!]\033[97m", domain, "is  icloud")
                file = open("filtered-domains/icloud.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in msn:
                print("\033[91m[!]\033[97m", domain, "is  msn")
                file = open("filtered-domains/msn.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in centurylink:
                print("\033[91m[!]\033[97m", domain, "is  centurylink")
                file = open("filtered-domains/centurylink.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in web:
                print("\033[91m[!]\033[97m", domain, "is  web")
                file = open("filtered-domains/web.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in wanadoo:
                print("\033[91m[!]\033[97m", domain, "is  wanadoo")
                file = open("filtered-domains/wanadoo.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in gmx:
                print("\033[91m[!]\033[97m", domain, "is  gmx")
                file = open("filtered-domains/gmx.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in live:
                print("\033[91m[!]\033[97m", domain, "is  live")
                file = open("filtered-domains/live.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in verizon:
                print("\033[91m[!]\033[97m", domain, "is  verizon")
                file = open("filtered-domains/verizon.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in bellsouth:
                print("\033[91m[!]\033[97m", domain, "is  bellsouth")
                file = open("filtered-domains/bellsouth.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in att:
                print("\033[91m[!]\033[97m", domain, "is  att")
                file = open("filtered-domains/att.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in comcast:
                print("\033[91m[!]\033[97m", domain, "is  comcast")
                file = open("filtered-domains/comcast.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in netzero:
                print("\033[91m[!]\033[97m", domain, "is  netzero")
                file = open("filtered-domains/netzero.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in ntt:
                print("\033[91m[!]\033[97m", domain, "is  ntt")
                file = open("filtered-domains/ntt.txt", "a")
                file.write(domain + "\n")
                file.close()
            # elif mxRecord in qwest:
            #     print("\033[91m[!]\033[97m", domain, "is  qwest")
            #     file = open("qwest.txt", "a")
            #     file.write(domain + "\n")
            #     file.close()
            # elif mxRecord in sbcglobal:
            #     print("\033[91m[!]\033[97m", domain, "is  sbcglobal")
            #     file = open("sbcglobal.txt", "a")
            #     file.write(domain + "\n")
            #     file.close()
            elif mxRecord in tiscali:
                print("\033[91m[!]\033[97m", domain, "is  tiscali")
                file = open("filtered-domains/tiscali.txt", "a")
                file.write(domain + "\n")
                file.close()
            # elif mxRecord in vodafone:
            #     print("\033[91m[!]\033[97m", domain, "is  vodafone")
            #     file = open("vodafone.txt", "a")
            #     file.write(domain + "\n")
            #     file.close()
            # elif mxRecord in yandex:
            #     print("\033[91m[!]\033[97m", domain, "is  yandex")
            #     file = open("filtered-domains/yandex.txt", "a")
            #     file.write(domain + "\n")
            #     file.close()
            # elif mxRecord in zoho:
            #     print("\033[91m[!]\033[97m", domain, "is  zoho")
            #     file = open("zoho.txt", "a")
            #     file.write(domain + "\n")
            #     file.close()
            elif mxRecord in zynga:
                print("\033[91m[!]\033[97m", domain, "is  zynga")
                file = open("filtered-domains/zynga.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in yandex:
                print("\033[91m[!]\033[97m", domain, "is  yandex")
                file = open("filtered-domains/yandex.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in optonline:
                print("\033[91m[!]\033[97m", domain, "is  optonline")
                file = open("filtered-domains/optonline.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in frontier:
                print("\033[91m[!]\033[97m", domain, "is  frontier")
                file = open("filtered-domains/frontier.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in windstream:
                print("\033[91m[!]\033[97m", domain, "is  windstream")
                file = open("filtered-domains/windstream.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in spectrum:
                print("\033[91m[!]\033[97m", domain, "is  spectrum")
                file = open("filtered-domains/spectrum.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in suddenlink:
                print("\033[91m[!]\033[97m", domain, "is  suddenlink")
                file = open("filtered-domains/suddenlink.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in tds:
                print("\033[91m[!]\033[97m", domain, "is  tds")
                file = open("filtered-domains/tds.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in godaddy:
                print("\033[91m[!]\033[97m", domain, "is  godaddy")
                file = open("filtered-domains/godaddy.txt", "a")
                file.write(domain + "\n")
                file.close()
            elif mxRecord in rediff:
                print("\033[91m[!]\033[97m", domain, "is  rediff")
                file = open("filtered-domains/rediff.txt", "a")
                file.write(domain + "\n")
                file.close()
            else :
                print("\033[91m[!]\033[97m", domain, "is  unknown")
                file = open("filtered-domains/unknown.txt", "a")
                file.write(domain + "\n")
                file.close()
            
        finally:
            mxRecords.append(mxRecord)
            emailAddresses.append(domain)
            # print(domain, ":", mxRecord + "\n")
            time.sleep(.200)
    return mxRecord




if __name__ == "__main__":
    start_time = time.time()
    lookup()
    print("\n\033[91m[!]\033[97m", len(emailAddresses), "emails sorted")
    time_took = time.strftime( " Time: %H:%M:%S ", time.gmtime(time.time() - start_time))
    print("\n\033[91m[!]\033[97m", time_took)







