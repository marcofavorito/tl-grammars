FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y \ 
  pandoc               \
  make                 \
  pandoc-citeproc      \
  latexmk              \ 
  texlive-xetex


