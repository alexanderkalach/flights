FROM logstash:5.2.1

COPY logstash.conf /usr/share/logstash/config/
RUN logstash-plugin install logstash-input-kafka

CMD ["-f", "/usr/share/logstash/config/logstash.conf"]