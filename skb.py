#!/usr/bin/env python3

# Importing Libraries
import subprocess
import os
import re

# Main Installation class
class Install:

    def __init__(self, cmd, arg1, arg2):
        self.cmd = cmd
        self.arg1 = arg1
        self.arg2 = arg2


class DebPkgPr(Install):

    #    def pkg_install(self, cmd, arg1):
    def __init__(self, cmd, arg1):
        super().__init__(cmd, arg1,
                         'apt-transport-https ca-certificates curl software-properties-common gpg-agent')

        print("[+] Installation of the prerequisite packages is starting:")

        for self.items in self.arg2.split():
            self.command = str(self.cmd) + '\n' + str(self.arg1) + '\n' + str(self.items)
            subprocess.run(self.command.split())
            print("\[+] Package {} Installed".format(str(self.items)))


class GPGpub(Install):
    def __init__(self, cmd, arg1, arg2, arg3, arg4, arg5):
        super().__init__(cmd, arg1, arg2)
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.arg5 = arg5
 #       subprocess.run([cmd, arg1, self.arg2, self.arg3, self.arg4, self.arg5, self.arg6], check=True)
        curld = subprocess.run([cmd, self.arg1, self.arg2], check=True, capture_output=True)
        #curld = subprocess.Popen([cmd, self.arg1, self.arg2], stdout=subprocess.PIPE)
        subprocess.run([self.arg3, self.arg4, self.arg5],input=curld.stdout, check=True)
        # print(gpgadd.stdout.decode('utf-8').strip())
        # gpgadd()[0]
        print("\[+] GPG pub key {} added")

 #   def pipe(self, cmd, arg1, arg2, arg3, arg4, arg5):

class GPGpub2(Install):
    def __init__(self, cmd, arg1, arg2, arg3):
        super().__init__(cmd, arg1, arg2)
        self.arg2 = arg2
        self.arg3 = arg3
        curld = subprocess.run([cmd, self.arg1], check=True, capture_output=True)
        subprocess.run([self.arg2, self.arg3],input=curld.stdout, check=True)
        print("\[+] GPG pub key", arg1, "added")

class GPGpub3(Install):
    def __init__(self, cmd, arg1, arg2, arg3, arg4, arg5):
        super().__init__(cmd, arg1, arg2)
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.arg5 = arg5
        curld = subprocess.run([cmd, self.arg1], check=True, capture_output=True)
        gpg = subprocess.run([self.arg2, self.arg3],input=curld.stdout, check=True, capture_output=True)
        subprocess.run([self.arg4, self.arg5],input=gpg.stdout, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print("\[+] GPG pub key", arg1, "added")


class AddRpstr(Install):
    def __init__(self, cmd):
        super().__init__(
            cmd, 'deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable', '')
        subprocess.run([self.cmd, self.arg1,], check=True)

class DebPkg(Install):

    #    def pkg_install(self, cmd, arg1):
    def __init__(self, cmd, arg1, arg2, arg3):
        print("[+] Installation of the package is starting:")
        subprocess.run([cmd, arg1, arg2, arg3], check=True)
        print("\[+] Package {} Installed".format(str(arg3)))

class Cmd2(Install):
    def __init__(self, cmd, arg1):
        print("[+] Run a command:", cmd, arg1)
        subprocess.run([cmd, arg1], check=True)

class Cmd2Shell(Install):
    def __init__(self, cmd, arg1):
        print("[+] Run a command:", cmd, arg1)
        subprocess.run([cmd, arg1], check=True, shell=True)

class Cmd3(Install):
    def __init__(self, cmd, arg1, arg2):
        print("[+] Run a command:", cmd, arg1, arg2)
        subprocess.run([cmd, arg1, arg2], check=True)

class Cmd3Shell(Install):
    def __init__(self, cmd, arg1, arg2):
        print("[+] Run a command:", cmd, arg1, arg2)
        subprocess.run([cmd, arg1, arg2], check=True, shell=True)

class Cmd4(Install):
    def __init__(self, cmd, arg1, arg2, arg3):
        print("[+] Run a command:", cmd, arg1, arg2, arg3)
        subprocess.run([cmd, arg1, arg2, arg3], check=True)
        #print("\[+] Package {} Installed".format(str(arg3)))

class Cmd5(Install):
    def __init__(self, cmd, arg1, arg2, arg3, arg4):
        print("[+] Run a command:", cmd, arg1, arg2, arg3, arg4)
        subprocess.run([cmd, arg1, arg2, arg3, arg4], check=True)


class Istio(Install):
    def __init__(self, cmd, arg1, arg2, arg3, arg4):
        print("[+] Run a command:", cmd, arg1, arg2, arg3, arg4)
        curld = subprocess.run([cmd, arg1, arg2], check=True, capture_output=True)
        subprocess.run([arg3, arg4],input=curld.stdout, check=True)
        print("\[+] Istio installed")

#        subprocess.run([cmd, arg1, arg2, arg3, arg4], check=True)

class SetEnv:
    def __init__(self):
        envbuff = os.environ.copy()
        envbuff["PATH"] = os.pathsep.join(["/usr/local/istio/bin/",envbuff["PATH"]])
        subprocess.run(["ls"],env=envbuff)
        print("\[+] PATH set")


class Scmd(Install): 
    def __init__(self, cmd):
        self.cmd = cmd
        super().__init__(self.cmd, '', '')
        splitcmd = subprocess.Popen(self.cmd.split(), stdout=subprocess.PIPE)
        #output, error = splitcmd.communicate()
        splitcmd.communicate()
        print("\[+] Helm setup")

class PortNumber:
  def input():
    while True:
      try:
        # Convert it into integer
        portn = int(input("Enter port number (between 26-65535) "))
        print("Port number = ", portn)
        try:
            pattern = re.compile("([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$")
        except ValueError:
            print("Entered number is not 16-bit, ranging from 0 to 65535")
            print("Try again.")
            continue
        else:
            break
      except ValueError:
            print("Input is not a number.", portn)
            print("Try again.")
            continue
      else:
            break

class PortForward(Install):
    def __init__(self, portn):
        self.arg2 = '-n'
        self.arg3 = 'istio-system'
        self.arg4 = 'svc/istio-ingressgateway'
        self.arg5 = '&'
        super().__init__('kubectl', 'port-forward', self.arg2)
        self.portnf = str(portn) + ":80"
        print("[+] Run a command:", self.cmd, self.arg1, self.arg2, self.arg3, self.arg4, self.portnf, self.arg5)
        subprocess.run([self.cmd, self.arg1, self.arg2, self.arg3, self.arg4, self.portnf, self.arg5 ], check=True, shell=True)   
        print('\n',"!!!kubectl port-forward is now running in background on port", self.portn,"!!!")
#kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80
#
# class Helm:
#     def __init__(self):
#         self.cmd = "helm"
#         self.arg1 = "install"
#         self.arg2 = "seldon-core"
#         self.arg3 = "seldon-core-operator"
#         self.arg4 = "--repo"
#         self.arg5 = "https://storage.googleapis.com/seldon-charts"
#         self.arg6 = "--set"
#         self.arg7 = "usageMetrics.enabled=true"
#         self.arg6 = "istio.enabled=true"
#         self.arg7 = 

#         super().__init__(
#             cmd, 'deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable', '')
#         subprocess.run([self.cmd, self.arg1,], check=True)




#DebPkgPr('apt-get','install -yq --no-install-recommends')


## Docker-ce 
#GPGpub('curl', '-vfsSL', 'https://download.docker.com/linux/ubuntu/gpg','apt-key', 'add', '-')
#AddRpstr('add-apt-repository')
#DebPkg('apt', 'install', '-y', 'docker-ce')

## Kind
if os.path.isfile('/usr/local/bin/kind') == False:
   Cmd4('curl', '-Lo', '/tmp/kind', 'https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64')
if os.path.isfile('/tmp/kind'):
   Cmd3('chmod', '+x', '/tmp/kind')
   Cmd3('mv', '/tmp/kind', '/usr/local/bin/kind')
##Cmd3('kind', '--version', '')

## Kubectl
if os.path.isdir('/etc/apt/keyrings') == False:
   Cmd3('mkdir', '-p', '/etc/apt/keyrings')
#Cmd4('curl', '-fsSLo', '/etc/apt/keyrings/kubernetes-archive-keyring.gpg', 'https://packages.cloud.google.com/apt/doc/apt-key.gpg')
#GPGpub2('echo', 'deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main', 'tee', '/etc/apt/sources.list.d/kubernetes.list')
#Cmd3('apt-get', '-q', 'update')
#DebPkg('apt', 'install', '-y', 'kubectl')

## Helm
#GPGpub3('curl', 'https://baltocdn.com/helm/signing.asc', 'gpg', '--dearmor', 'tee', '/usr/share/keyrings/helm.gpg')
#GPGpub2('echo', 'deb [arch=amd64 signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main', 'tee', '/etc/apt/sources.list.d/helm-stable-debian.list')
#Cmd3('apt-get', '-q', 'update')
#DebPkg('apt', 'install', '-y', 'helm')



## Istio

cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))
print("os.getcwd() returns an object of type: {0}".format(type(cwd)))
os.chdir('/tmp')
##Cmd3Shell('ls', '-lha', '/tmp/istio*')
##print(list(filter(os.path.isdir, os.listdir('/tmp'))))
##if os.path.isdir(istiofd[0]):
##    print ('hi')
if os.path.isdir('/usr/local/istio') == False:
   Istio('curl', '-L', 'https://istio.io/downloadIstio', 'sh', '-')
##if os.path.isdir(istiod):
   cwd2 = os.getcwd()
   print("Current working directory: {0}".format(cwd2))
   print("os.getcwd() returns an object of type: {0}".format(type(cwd)))
   ##Cmd2('ls', '-lha')
   istiofd=[istiofd for istiofd in os.listdir('/tmp') if re.match(r"^istio*", istiofd)]
   if istiofd:
     print(istiofd[0])
     Cmd3('mv', istiofd[0], '/usr/local/istio')
Cmd3('ls', '-lha', '/usr/local/istio')
Cmd2('touch', '/etc/profile.d/02-istio.sh')
##Cmd4('echo', '"export PATH=/usr/local/istio/bin:$PATH"', '>', '/etc/profile.d/02-istio.sh')
##Scmd('echo "export PATH=/usr/local/istio/bin:$PATH" > /etc/profile.d/02-istio.sh')
profilesh = open('/etc/profile.d/02-istio.sh', 'w')
content = ["export PATH=/usr/local/istio/bin:$PATH"]
profilesh.writelines(content)
profilesh.close()
##Cmd2('more', '/etc/profile.d/02-istio.sh')
##Cmd2('export', 'PATH=/usr/local/istio/bin:$PATH')
SetEnv()
##Cmd2('env', '-v')
##Cmd2('echo', '$PATH')
os.chdir(cwd)
os.getcwd()


## Set Up Kind
Cmd5('kind', 'create', 'cluster', '--name', 'seldon')
Cmd4('kubectl', 'cluster-info', '--context', 'kind-seldon')

## Install Cluster Ingress
Cmd5('istioctl', 'install', '--set', 'profile=demo', '-y')
##with  open('IstioGW.yaml','r') as istiogwyaml:
##  Cmd4('kubectl', 'apply', '-f', 'istiogwyaml')
Cmd4('kubectl', 'apply', '-f', 'IstioGW.yaml')
Cmd4('kubectl', 'create', 'namespace', 'seldon-system')
Scmd('helm install seldon-core seldon-core-operator --repo https://storage.googleapis.com/seldon-charts --set usageMetrics.enabled=true --set istio.enabled=true --namespace seldon-system')
##Scmd('kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80')
portn = PortNumber.input()
PortForward(portn)
output2=Cmd3('helm', 'list', '--all-namespaces')
print(output2)
output1=Cmd5('kubectl', 'get', 'pods', '-n', 'seldon-system')
print(output1)

# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
# sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
# sudo apt install docker-ce
# curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64
# chmod +x ./kind
# sudo mv ./kind /usr/local/bin/kind
# curl -fsSLo /etc/apt/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
# echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list
# curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
# sudo apt-get install apt-transport-https --yes
# echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
# sudo apt-get update
# sudo apt-get install helm
