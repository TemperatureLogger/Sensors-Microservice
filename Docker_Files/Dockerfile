FROM python:3
WORKDIR /usr/src/app

# Get adafruit library
# RUN echo "Getting Addafruit lib set-up"
# RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
# RUN cd Adafruit_Python_DHT; python3 setup.py install
# RUN echo "Done"
# Get python3
ENTRYPOINT ["python3"]

# Copy sources to docker
COPY . .

# Run data generating script
CMD ["data_generator.py"]