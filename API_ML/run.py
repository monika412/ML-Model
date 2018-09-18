from cassandra.cluster import Cluster
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from flask import Flask,jsonify
from models.CustomerSeg import CustomerSeg
from views.api import app

KEYSPACE = "fresco_seg"


#cluster = Cluster()
#session = cluster.connect(keyspace=KEYSPACE)


#session = cluster.connect()
# session.execute(
 # """
        # CREATE KEYSPACE IF NOT EXISTS %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 };
        # """ % KEYSPACE)


#    return app


#app = create_app()
#api = Api(app)

if __name__ == '__main__':
    ##connection.setup(['127.0.0.1'], "customer_segment", protocol_version=3)
    ##sync_table(CustomerSeg)
    app.run(host="0.0.0.0", port=8081,debug=True)
