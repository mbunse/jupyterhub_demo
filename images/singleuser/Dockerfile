# Based on https://github.com/jupyterhub/zero-to-jupyterhub-k8s/blob/v0.6/images/singleuser-sample/Dockerfile 
FROM jupyter/base-notebook:27ba57364579
# See https://github.com/jupyter/docker-stacks/blob/master/base-notebook/Dockerfile

# conda/pip/apt install additional packages here, if desired.

# pin jupyterhub to match the Hub version
# set via --build-arg in Makefile
ARG JUPYTERHUB_VERSION=0.8
RUN pip install --no-cache jupyterhub==$JUPYTERHUB_VERSION
