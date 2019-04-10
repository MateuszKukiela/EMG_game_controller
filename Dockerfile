FROM registry.gitlab.com/pierzchlewicz/tmsi-usb-docker

WORKDIR /EMG_controller



RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y libjack-jackd2-dev libportmidi-dev portaudio19-dev liblo-dev libsndfile-dev
RUN apt-get install -y python3-dev python3-tk python3-pil.imagetk python3-pip
RUN git clone https://github.com/belangeo/pyo.git
WORKDIR /EMG_controller/pyo
RUN python3 setup.py install --install-layout=deb --use-jack --use-double
WORKDIR /EMG_controller
RUN pip install setuptools
RUN pip3 install requests

RUN pip install -U \
    -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-16.04 \
    wxPython
RUN pip install PyQt5
RUN apt-get install -y python3-setuptools
RUN apt-get install -y python-setuptools
RUN pip install -U --ignore-installed setuptools

RUN pip install numpy scipy matplotlib pandas pyopengl pyglet pillow moviepy lxml openpyxl xlrd configobj pyyaml gevent greenlet msgpack-python psutil tables requests[security] pyosf cffi pysoundcard pysoundfile seaborn psychopy_ext python-bidi psychopy
RUN pip install pyserial pyparallel egi
RUN pip install pytest coverage sphinx

RUN apt-get install -y libgtk-3-0
RUN apt-get install -y libxxf86vm-dev
RUN apt-get install -y libsm-dev
RUN apt-get install -y python-qt4
RUN apt-get install -y freeglut3-dev

COPY test /EMG_controller/test
COPY src/calibration-session src/calibration-session
COPY src/classifier src/classifier
COPY src/client-app src/client-app
COPY src/app.py /EMG_controller/src
COPY index.py /EMG_controller
COPY src/dummy_classify.py /EMG_controller/src
COPY config.ini /EMG_controller
COPY config.ini /EMG_controller/src
COPY fitted_model /EMG_controller/fitted_model
