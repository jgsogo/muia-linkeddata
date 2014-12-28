# Taken from http://www.apohllo.pl/blog/virtuoso-installation-in-debian
# con retoques de aquí http://swebdev.wordpress.com/2012/10/01/loading-geonames-in-virtuoso/

$>isql-vt -U dba
SQL> load [path to]rdfloader.sql
SQL> ld_dir ('[path to without end slash]', '*.nt', 'http://rafco.jgsogo.es');
SQL> rdf_loader_run();


# EN CASO DE QUE NO FUNCIONE LA IMPORTACION
#   comando mágicos para resetear el asuto
SQL> drop table load_list;
SQL> drop table ldlock;


# VACIAR EL GRAFO:
$> isql-vt
SQL> log_enable(3,1);
SQL> SPARQL CLEAR GRAPH  <graph-name>; 
