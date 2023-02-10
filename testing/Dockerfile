FROM ubuntu:20.04

RUN apt-get update  \
    && apt-get install -yq --no-install-recommends python3
#    && rm -rf /var/lib/apt/lists/*

RUN apt-get install -yq --no-install-recommends apt-transport-https ca-certificates curl software-properties-common
RUN apt-get install -yq --no-install-recommends gpg-agent
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
RUN apt install -y docker-ce

# Install Kind
RUN curl -Lo /tmp/kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64
RUN chmod +x /tmp/kind
RUN mv /tmp/kind /usr/local/bin/kind

# Install kubectl
RUN mkdir -p /etc/apt/keyrings
RUN curl -fsSLo /etc/apt/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
RUN echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | tee /etc/apt/sources.list.d/kubernetes.list
RUN apt-get -q update
RUN apt install -y kubectl

# Install Helm
RUN curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | tee /usr/share/keyrings/helm.gpg > /dev/null
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | tee /etc/apt/sources.list.d/helm-stable-debian.list
RUN apt-get -q update
RUN apt install -y helm

# Create directories
RUN mkdir -p /home/script

WORKDIR /home/script

# Download Isitio
RUN curl -L https://istio.io/downloadIstio | sh -
RUN mv istio* /usr/local/istio
#RUN mkdir /etc/environment.d/
RUN touch /etc/profile.d/02-istio.sh
RUN echo "export PATH=/usr/local/istio/bin:$PATH" > /etc/profile.d/02-istio.sh
ENV PATH="${PATH}:/usr/local/istio/bin"
#RUN rm /bin/sh && ln -s /bin/bash /bin/sh
#RUN source /etc/profile.d/02-istio.sh
#RUN echo ${PATH}
#RUN export PATH=/usr/local/istion/bin:${PATH}
#RUN echo ${PATH}
#RUN PATH=/usr/local/istion/bin:${PATH}
#RUN echo ${PATH}

# chmod +x ./kind
#  mv ./kind /usr/local/bin/kind


# Copy script
COPY ./skb.py /home/script/
COPY ./IstioGW.yaml /home/script/

#ENTRYPOINT nohup dockerd >/dev/null 2>&1 & sleep 1 && /home/script/skb.py

# Run the script
#RUN /home/script/skb.py
#CMD /home/script/skb.py
CMD nohup dockerd >/dev/null 2>&1 & sleep 1 && /home/script/skb.py
