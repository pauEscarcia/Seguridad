#certificados 
openssl dsaparam 2048 -out dsaparams.pem
openssl gendsa -out dsarootkey.pem dsaparams.pem
openssl req -newkey dsa:dsaparams.pem -keyout dsarootket.pem -new -x509 -days 365 -out rootcert.pem;
openssl x509 -text -in rootcert.pem | more
openssl asn1parse -in rootcert.pem | more 
