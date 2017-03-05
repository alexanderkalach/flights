FROM logstash:5.2.1

COPY logstash.conf /usr/share/logstash/config/
RUN logstash-plugin install logstash-input-kafka
RUN logstash-plugin install logstash-input-stdin
RUN logstash-plugin install logstash-output-elasticsearch
RUN logstash-plugin install logstash-output-stdout

CMD ["-f", "/usr/share/logstash/config/logstash.conf"]