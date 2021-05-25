# Imagem oficial que servirá de base
FROM python:3

#VOLUME app
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8

# Define o diretório /home/app como um working directory
WORKDIR /app

# Copia o arquivo requirements do diretório atual para o diretório /home/app do container
COPY ./requirements.txt ./

# Instala libs necessárias
RUN pip3 install -r ./requirements.txt

# Remove arquivo requirements do diretório /home/app do container
RUN rm requirements.txt

#Copia o app para dentro do container
COPY ./ /app

# Remove pacotes não utilizados
RUN apt-get autoclean && apt-get autoremove