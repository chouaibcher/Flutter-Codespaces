FROM dart

RUN apt-get update
RUN apt-get install -y curl git unzip xz-utils zip libglu1-mesa

RUN apt-get clean

RUN git clone https://github.com/flutter/flutter.git -b stable --depth 1 /flutter
ENV PATH="/flutter/bin:$PATH"
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \ 
    wget \
# later --installing jdk8 + jdk 17  + downloading sdk + set path