import socket
def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
def checkVulns(banner):
        if 'Something FTP' in banner:
                print('voi paska!')
        elif 'Something else FTP' in banner:
                print('ja lisää paskaa!')
        else:
                print('ei ole paskaa!')
        return
def main():
        ip1 = ''
        ip2 = ''
        port = 21
        banner1 = retBanner(ip1, port)
        if banner1:
                print('[+] ' + ip1 + ': ' + banner1)
                checkVulns(banner1)
        banner2 = retBanner(ip2, port)
        if banner2:
                print('[+] ' + ip2 + ': ' + banner2)
                checkVulns(banner2)
if __name__ == '__main__':
        main()