# Taken from http://www.apohllo.pl/blog/virtuoso-installation-in-debian
# con retoques de aquí http://swebdev.wordpress.com/2012/10/01/loading-geonames-in-virtuoso/

$>isql-vt -U dba

SQL> load [path to]rdfloader.sql
SQL> ld_dir ('[path to without end slash]', '*.nt', 'http://rafco.jgsogo.es');
SQL> rdf_loader_run();


# VACIAR EL GRAFO:
$> isql-vt
SQL> log_enable(3,1);
SQL> SPARQL CLEAR GRAPH  <graph-name>; 
