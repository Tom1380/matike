FROM python

RUN apt update -y && apt upgrade -y
RUN apt install -y libcairo2-dev libpango1.0-dev ffmpeg texlive texlive-latex-extra texlive-fonts-extra \
	texlive-latex-recommended texlive-science texlive-fonts-extra tipa

RUN mkdir /input

WORKDIR /input

COPY requirements.txt .

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install -r requirements.txt

COPY scene.py .

WORKDIR /output

CMD [ "manim", "/input/scene.py", "Matike", "-qh" ]