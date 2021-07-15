import requests
import sys
import json
import socket
from datetime import datetime
import time
import shodan
from bs4 import BeautifulSoup
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
from pywhatcms import whatcms
from requests.exceptions import MissingSchema
from termcolor import colored, cprint


text = colored('''
 
                            ███████╗██████╗░███████╗░█████╗░██╗░░██╗
                            ██╔════╝██╔══██╗██╔════╝██╔══██╗██║░██╔╝
                            █████╗░░██████╔╝█████╗░░███████║█████═╝░    
                            ██╔══╝░░██╔══██╗██╔══╝░░██╔══██║██╔═██╗░
                            ██║░░░░░██║░░██║███████╗██║░░██║██║░╚██╗
                            ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝   
                                                                         
                                                            <3 coded by mohit_1337
                                                                                        ''', 'blue')


try:
        print(text)
        words = "shit", "fuck", "tit", "ass", "penis"
        dash = input("Enter Url: ")
except KeyboardInterrupt:
        err = colored('\n[-]Quiting', 'red')
        print(err)



def enter(dash,words):
                      try:
                            if dash in words:
                                    print("do you know what are you typing?")
                                    input("type again: ")
                            else:
                                    pass
                      except KeyboardInterrupt:
                            err = colored('\n[-]Quiting', 'red')
                            print(err)                          

def responsed(dash):
                        global user_agent
                        user_agent = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
                        }

                        try:
                                response = requests.get(dash)
                                if response.status_code == 200:
                                  ccx = colored(response.status_code, 'green')
                                  print('\nStatus_code: ', ccx)
                                elif response.status_code == 404:
                                    print("response code: ", {response.status_code})
                                    print("---------------------site doesn't exist check the spell--------------------\n")
                                    sys.exit()
                        except MissingSchema:
                                    url = colored("URL is in bad format", 'red')
                                    print(url)
                                    sys.exit()
                        except KeyboardInterrupt:
                                    err = colored('\n[-]Quiting', 'red')
                                    print(err)                        
                        except:
                                    ex = colored("[-]Connection refused by the server.....", 'red')
                                    print(ex)
                                    tex = colored('retrying......wait for few seconds.', 'yellow', attrs=['blink']) 
                                    print(tex)
                                    time.sleep(3)
                                    ext = colored("Can't connect to your application!...", 'red')
                                    print(ext)
                                    sys.exit()


def cms(dash): 
                    dash = dash.replace("https:\/\/", "")
                    key = "" #replace your key here
                    try:
                            cmd = requests.get("https://whatcms.org/APIEndpoint/Detect?key=" + key +"&url=" + dash)   
                            cc = colored("""\t\t\t\t\t\t-----------------------------------------------------------------------
                                                                             Detecting cms                   
                                            ----------------------------------------------------------------------------\n""", 'magenta')
                            time.sleep(3)
                            print(cc)
                            ccd = colored('[-]If whatcms key not configured the results will default to None\n\n', 'yellow')
                            print(ccd)
                            data = cmd.json()
                            whatcms.name = data['result']['name']
                            exc = colored(whatcms.name, 'green')
                            whatcms.code = data['result']['code']
                            exce = colored(whatcms.code, 'green')
                            whatcms.confidence = data['result']['confidence']
                            excel = colored(whatcms.confidence, 'green')
                            whatcms.cms_url = data['result']['cms_url']
                            ex = colored(whatcms.cms_url, 'green')
                            whatcms.version = data['result']['version']
                            e = colored(whatcms.version, 'green')
                            whatcms.msg = data['result']['msg']
                            ef = colored(whatcms.msg, 'green')
                            whatcms.id = data['result']['id']
                            efl = colored(whatcms.id, 'green')
                            whatcms.request = data['request']
                            whatcms.request_web = data['request_web']
                            print('[+] CMS: ' , exc)
                            print('[+] CMS Version: ' , whatcms.version)
                            print('[+] CMS Confidence: ' , excel)
                            print('[+] CMS URL: ' , ex)
                            print('[+] CMS ID: ' , efl)
                    except KeyboardInterrupt:
                               err = colored('[+] operation cancelled by user', 'red')
                               print(err)
             
        
def dir(dash):  
    try:
        cc = colored("""\t\t\t\t\t\t-----------------------------------------------------------------------
                                                            Finding robots File                   
                                    -----------------------------------------------------------------------\n""", 'magenta')
        print(cc)
        time.sleep(3)
        file = requests.get(dash + "/robots.txt")
        fal = file.text
        if "404" in file.text:
                     print("[+]no robots file detected")
        else:
                   cc = colored('[+]robots file is present', 'yellow')
                   print(cc)
    except KeyboardInterrupt:
       ccx = colored('[-]Operation cancelled by user', 'red')
       print(ccx)
       sys.exit()
    except:
       xxs = colored("[-]Connection refused by the server..", 'red')
       print(xxs)
       sys.exit()


def pt():
    cc = colored("""\t\t\t\t\t\t-----------------------------------------------------------------------
                                                            Finding Potential Directories
                                    -----------------------------------------------------------------------\n""", 'magenta')
        
    print(cc)
    try:
        with open('dir.txt', 'r') as wordlist:
            for links in wordlist:
                links = dash + "/" + links
                r = requests.get(links)
                http = r.status_code
                if http == 200:
                    lik = links + colored("[-]Vulnerable", 'red')
                    print(lik)
                elif http == 404:
                   likes = links + colored("[+]Not Vulnerable]", 'green')
                   print(likes)
    except KeyboardInterrupt:
        col = colored('[+]Operation Cancelled by user', 'red')
        print(col)
    except:
        colg = colored("[-]Connection refused by the server..", 'red')
        sys.exit()

def header(dash):
    try:
         cc = colored("""\t\t\t\t\t\t-----------------------------------------------------------------------
                                                          Fetching URL via wayback 
                                    -----------------------------------------------------------------------\n""", 'magenta')
         print(cc)
         time.sleep(3)
         response = requests.get("https://web.archive.org/cdx/search?url="+ dash +"&matchType=prefix&collapse=urlkey&output=text&fl=original&\filter=&limit=10")
         resp = response.text
         print(resp)
    except KeyboardInterrupt:
        user = colored('[+]operation canccelled by the user', 'red')
        sys.exit()
    except:
        print("[-]Connection refused by the server..")
        sys.exit()

def whois(dash):
        cc = colored("""\t\t\t\t\t\t-----------------------------------------------------------------------
                                                            Finding Services Via Shodan
                                    -----------------------------------------------------------------------\n""", 'magenta')
        print(cc)
        lol = colored('[-]Tool will not work properly if you dont provide API keys', 'red')
        print(lol)
        time.sleep(3)
        dash = dash.replace("https://www.", "")
        dash = dash.replace("http://www.", "")
        dash = dash.replace('http://', "")
        dash = dash.replace('https://', "")
        dash = dash.replace('/', "")
        shodant = socket.gethostbyname(dash)
        api = shodan.Shodan('')    #replace you shodan key here
        host = api.host(shodant)
        try:
            print("""
                 IP: {}
                Organization: {}
                Operating System: {}
                ISP: {}
                Cloud Service Found: {}
                City: {}
                Country: {}
                Port: {}
                 """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'), host.get('isp'), host.get('hostnames'), host.get('city'), host.get('country'), host.get('port')))
                
       
        except KeyboardInterrupt:
                user = colred('[-]quitting', 'red')

        except Exception:
                pass


def js(dash):
    try:
        cc = colored("""\t\t\t\t\t\t-----------------------------------------------------------------------
                                                            Fetching js files
                                    -----------------------------------------------------------------------\n""", 'magenta')
        print(cc)
        time.sleep(3)
        html = requests.get(dash).content
        soup = BeautifulSoup(html, "html.parser")

        js_files = []
        url = []
        for script in soup.find_all("script"):
           if script.attrs.get("src"):
             url = script.attrs.get("src")
             print(dash+url)
    except KeyboardInterrupt:
        xd = colored('[+]operation Cancelled by user', 'red')
        print(xd)
    except:
        print("Connection refused by the server..")
        sys.exit()

def records(dash):
    try:
        dash = dash.replace("https://", "")
        dash = dash.replace("http://www.", "")
        dash = dash.replace('http://', "")
        dash = dash.replace('https://', "")
        dash = dash.replace("/", "")
        res = DNSDumpsterAPI(True).search(dash)

        dex = colored("\n\n\n\t\t\t\t\t\t----------------------DNS Servers -------------------------\n", 'magenta')
        time.sleep(3)
        print(dex)
        for entry in res['dns_records']['dns']:
            print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))

        jar = colored("\n\n\n\t\t\t\t\t\t-------------- MX Records ---------------------\n", 'magenta')
        print(jar)
        time.sleep(2)
        for entry in res['dns_records']['mx']:
            print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))

        print("\n\n\n\t\t\t\t\t----------------------- Host Records (A) ---------------------------\n")
        for entry in res['dns_records']['host']:
            if entry['reverse_dns']:
                print(("{domain} ({reverse_dns}) ({ip}) {as} {provider} {country}".format(**entry)))
            else:
                print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))

        jare = colored("\n\n\n\t\t\t\t\t-------------------------- TXT Records ------------------\n", 'magenta')
        for entry in res['dns_records']['txt']:
            print(entry)

    except KeyboardInterrupt:
        print('[+]operation Cancelled by user')

enter(dash,words)
responsed(dash)
cms(dash)
dir(dash)
pt()
header(dash)
whois(dash)
js(dash)
records(dash)
