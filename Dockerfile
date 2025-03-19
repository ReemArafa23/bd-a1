FROM ubuntu

RUN apt-get update && apt-get install -y python3 python3-pip

# Use the flag to bypass the externally managed environment issue
RUN pip3 install --break-system-packages pandas numpy seaborn matplotlib scikit-learn scipy

RUN mkdir -p /home/doc-bd-a1/

COPY movies.csv /home/doc-bd-a1/
COPY ratings.csv /home/doc-bd-a1/

WORKDIR /home/doc-bd-a1/

CMD ["bash"]
