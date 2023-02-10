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
    def __init__(self, cmd, arg1):
        super().__init__(cmd, arg1,
                         'apt-transport-https ca-certificates curl software-properties-common gpg-agent')
        print("[+] Installation of the prerequisite packages is starting:")
        for self.items in self.arg2.split():
            self.command = str(self.cmd) + '\n' + \
                str(self.arg1) + '\n' + str(self.items)
            subprocess.run(self.command.split())
            print("\[+] Package {} Installed".format(str(self.items)))


class GPGpub(Install):
    def __init__(self, cmd, arg1, arg2, arg3, arg4, arg5):
        super().__init__(cmd, arg1, arg2)
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.arg5 = arg5
        curld = subprocess.run([cmd, self.arg1, self.arg2],
                               check=True, capture_output=True)
        subprocess.run([self.arg3, self.arg4, self.arg5],
                       input=curld.stdout, check=True)
        print("\[+] GPG pub key {} added")


class GPGpub2(Install):
    def __init__(self, cmd, arg1, arg2, arg3):
        super().__init__(cmd, arg1, arg2)
        self.arg2 = arg2
        self.arg3 = arg3
        curld = subprocess.run(
            [cmd, self.arg1], check=True, capture_output=True)
        subprocess.run([self.arg2, self.arg3], input=curld.stdout, check=True)
        print("\[+] GPG pub key", arg1, "added")


class GPGpub3(Install):
    def __init__(self, cmd, arg1, arg2, arg3, arg4, arg5):
        super().__init__(cmd, arg1, arg2)
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4
        self.arg5 = arg5
        curld = subprocess.run(
            [cmd, self.arg1], check=True, capture_output=True)
        gpg = subprocess.run(
            [self.arg2, self.arg3], input=curld.stdout, check=True, capture_output=True)
        subprocess.run([self.arg4, self.arg5], input=gpg.stdout, check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print("\[+] GPG pub key", arg1, "added")


class AddRpstr(Install):
    def __init__(self, cmd):
        super().__init__(
            cmd, 'deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable', '')
        subprocess.run([self.cmd, self.arg1,], check=True)


class DebPkg(Install):
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


class Cmd5(Install):
    def __init__(self, cmd, arg1, arg2, arg3, arg4):
        print("[+] Run a command:", cmd, arg1, arg2, arg3, arg4)
        subprocess.run([cmd, arg1, arg2, arg3, arg4], check=True)


class Istio(Install):
    def __init__(self, cmd, arg1, arg2, arg3, arg4):
        print("[+] Run a command:", cmd, arg1, arg2, arg3, arg4)
        curld = subprocess.run(
            [cmd, arg1, arg2], check=True, capture_output=True)
        subprocess.run([arg3, arg4], input=curld.stdout, check=True)
        print("\[+] Istio installed")


class SetEnv:
    def __init__(self):
        os.environ["PATH"] += os.pathsep + os.pathsep.join(["/usr/local/istio/bin/"])
        print(os.environ["PATH"])
        print("\[+] PATH set")


class Scmd(Install):
    def __init__(self, cmd):
        self.cmd = cmd
        super().__init__(self.cmd, '', '')
        splitcmd = subprocess.Popen(self.cmd.split(), stdout=subprocess.PIPE)
        splitcmd.communicate()
        print("\[+] Helm setup")


class PortNumber:
    def input():
        while True:
            try:
                portn = int(input("Enter port number (between 26-65535) "))
                print("Port number = ", portn)
                try:
                    pattern = re.compile(
                        "([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$")
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
        return portn

class PortForward(Install):
    def __init__(self, portn):
        self.arg2 = '-n'
        self.arg3 = 'istio-system'
        self.arg4 = 'svc/istio-ingressgateway'
        super().__init__('kubectl', 'port-forward', self.arg2)
        self.portnf = str(portn) + ":80"
        print("[+] Run a command:", self.cmd, self.arg1, self.arg2,
              self.arg3, self.arg4, self.portnf)
        self.command = str(self.cmd) + '\n' + str(self.arg1) + '\n' + str(self.arg2) + '\n' + str(self.arg3) + '\n' + str(self.arg4) + '\n' + str(self.portnf) + '\n' + '&'
        subprocess.run(self.command.split())
        print('\n', "!!!kubectl port-forward is now running in background on port",
              portn, "!!!")


# Prerequisite packages
DebPkgPr('apt-get', 'install -yq --no-install-recommends')

# Docker-ce
GPGpub('curl', '-vfsSL', 'https://download.docker.com/linux/ubuntu/gpg',
       'apt-key', 'add', '-')
AddRpstr('add-apt-repository')
DebPkg('apt', 'install', '-y', 'docker-ce')

# Kind
if os.path.isfile('/usr/local/bin/kind') == False:
    Cmd4('curl', '-Lo', '/tmp/kind',
         'https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64')
if os.path.isfile('/tmp/kind'):
    Cmd3('chmod', '+x', '/tmp/kind')
    Cmd3('mv', '/tmp/kind', '/usr/local/bin/kind')

# Kubectl
if os.path.isdir('/etc/apt/keyrings') == False:
    Cmd3('mkdir', '-p', '/etc/apt/keyrings')
Cmd4('curl', '-fsSLo', '/etc/apt/keyrings/kubernetes-archive-keyring.gpg',
     'https://packages.cloud.google.com/apt/doc/apt-key.gpg')
GPGpub2('echo', 'deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main',
        'tee', '/etc/apt/sources.list.d/kubernetes.list')
Cmd3('apt-get', '-q', 'update')
DebPkg('apt', 'install', '-y', 'kubectl')

# Helm
GPGpub3('curl', 'https://baltocdn.com/helm/signing.asc', 'gpg',
        '--dearmor', 'tee', '/usr/share/keyrings/helm.gpg')
GPGpub2('echo', 'deb [arch=amd64 signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main',
        'tee', '/etc/apt/sources.list.d/helm-stable-debian.list')
Cmd3('apt-get', '-q', 'update')
DebPkg('apt', 'install', '-y', 'helm')


# Istio
cwd = os.getcwd()
os.chdir('/tmp')
if os.path.isdir('/usr/local/istio') == False:
    Istio('curl', '-L', 'https://istio.io/downloadIstio', 'sh', '-')
    cwd2 = os.getcwd()
    print("Current working directory: {0}".format(cwd2))
    print("os.getcwd() returns an object of type: {0}".format(type(cwd)))
    istiofd = [istiofd for istiofd in os.listdir(
        '/tmp') if re.match(r"^istio*", istiofd)]
    if istiofd:
        print(istiofd[0])
        Cmd3('mv', istiofd[0], '/usr/local/istio')
Cmd2('touch', '/etc/profile.d/02-istio.sh')
profilesh = open('/etc/profile.d/02-istio.sh', 'w')
content = ["export PATH=/usr/local/istio/bin:$PATH"]
profilesh.writelines(content)
profilesh.close()
SetEnv()
os.chdir(cwd)
os.getcwd()


# Set Up Kind
Cmd5('kind', 'create', 'cluster', '--name', 'seldon')
Cmd4('kubectl', 'cluster-info', '--context', 'kind-seldon')

# Install Cluster Ingress
Cmd5('istioctl', 'install', '--set', 'profile=demo', '-y')
Cmd4('kubectl', 'apply', '-f', 'IstioGW.yaml')
Cmd4('kubectl', 'create', 'namespace', 'seldon-system')
Scmd('helm install seldon-core seldon-core-operator --repo https://storage.googleapis.com/seldon-charts --set usageMetrics.enabled=true --set istio.enabled=true --namespace seldon-system')
portn = PortNumber.input()
PortForward(portn)
