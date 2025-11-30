from flask import Flask, Response
from prometheus_client import start_http_server,Gauge, generate_latest, CONTENT_TYPE_LATEST
import calculate_cpu

#python class passes on values to prometheus
app = Flask(__name__)

#instantiate a guage object and pass on metrics later
cpu_percent_metric = Gauge("cpu_percent", "CPU usage percent")

@app.route("/metrics")
def metrics():
    percent_cpu=calculate_cpu.get_cpu_usage()
    try:
        value = float(percent_cpu)
    except Exception as e:
        print("error: ", e)
        return Response("bad output detected", status=500)
    
    cpu_percent_metric.set(value)
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__=='__main__':
    app.run(host="0.0.0.0", port=9000)
    