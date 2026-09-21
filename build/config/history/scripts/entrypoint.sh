#!/bin/bash

set -e

echo "Iniciando Spark History Server..."

$SPARK_HOME/sbin/start-history-server.sh

tail -f /dev/null