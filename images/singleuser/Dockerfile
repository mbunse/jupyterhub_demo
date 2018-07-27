# Based on https://github.com/jupyterhub/zero-to-jupyterhub-k8s/blob/v0.6/images/singleuser-sample/Dockerfile 
FROM jupyter/base-notebook:27ba57364579
# See https://github.com/jupyter/docker-stacks/blob/master/base-notebook/Dockerfile

# conda/pip/apt install additional packages here, if desired.

# pin jupyterhub to match the Hub version
# set via --build-arg in Makefile
USER root
#RUN apt-get update \
#&& apt-get -y install build-essential
ARG JUPYTERHUB_VERSION=0.8
COPY requirements.txt $HOME/.
RUN conda install --yes --file requirements.txt && \
    conda install xorg-libxrender xorg-libxpm && \
    conda clean -tipsy && \
    pip install --no-cache jupyterhub==$JUPYTERHUB_VERSION twitter && \
    fix-permissions $CONDA_DIR 
COPY datalab_ws.tar.gz $HOME/.
RUN tar -xzvf datalab_ws.tar.gz && \
    rm datalab_ws.tar.gz && \
    fix-permissions /home/$NB_USER
USER $NB_UID
