
#Generado de certificado para el cliente 
openssl req -newkey dsa:dsaparams.pem -keyout dsakey.pem -new -days 365 -out dsareq.pem
#Expedicion del certificado 
openssl x509 -days 180 -CA rootcert.pem -CAkey dsarootket.pem -req -CAcreateserial -CAserial ca.srl -in dsareq.pem -out newcert.pem
#examinando el certificado emitido
openssl x509 -text -in newcert.pem  | more 
openssl asn1parse -in newcert.pem | more 
#verificacion del certificado 
openssl verify - CAfile rootcert.pem newcert.pem



