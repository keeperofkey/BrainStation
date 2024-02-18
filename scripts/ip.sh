#! /bin/bash
echo "Website:" 
echo $1
echo "IP Address(es)"
dig $1 +short
