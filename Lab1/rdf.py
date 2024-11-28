from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, FOAF, XSD
import rdflib

EX = Namespace("http://example.org/")


g = Graph()

g.bind("foaf", FOAF)
g.bind("rdf", RDF)
g.bind("xsd", XSD)
g.bind("ex", EX)

kade = URIRef(EX.Kade)
emma = URIRef(EX.Emma)

g.add((kade, RDF.type, FOAF.Person))
g.add((kade, FOAF.name, Literal("Kade")))
g.add((kade, EX.address, Literal("1516 Henry Street, Berkeley, California 94709, USA")))
g.add((kade, EX.degree, Literal("Bachelor of Biology")))
g.add((kade, EX.almaMater, URIRef(EX.University_of_California)))
g.add((kade, EX.graduationYear, Literal("2011", datatype=XSD.gYear)))
g.add((kade, EX.interest, Literal("birds")))
g.add((kade, EX.interest, Literal("ecology")))
g.add((kade, EX.interest, Literal("environment")))
g.add((kade, EX.interest, Literal("photography")))
g.add((kade, EX.interest, Literal("traveling")))
g.add((kade, EX.traveledTo, URIRef(EX.Canada)))
g.add((kade, EX.traveledTo, URIRef(EX.France)))

g.add((emma, RDF.type, FOAF.Person))
g.add((emma, FOAF.name, Literal("Emma")))
g.add((emma, EX.address, Literal("Carrer de la Guardia Civil 20, 46020 Valencia, Spain")))
g.add((emma, EX.degree, Literal("Master of Chemistry")))
g.add((emma, EX.almaMater, URIRef(EX.University_of_Valencia)))
g.add((emma, EX.graduationYear, Literal("2015", datatype=XSD.gYear)))
g.add((emma, EX.knowledgeArea, Literal("waste management")))
g.add((emma, EX.knowledgeArea, Literal("toxic waste")))
g.add((emma, EX.knowledgeArea, Literal("air pollution")))
g.add((emma, EX.interest, Literal("cycling")))
g.add((emma, EX.interest, Literal("music")))
g.add((emma, EX.interest, Literal("traveling")))
g.add((emma, EX.traveledTo, URIRef(EX.Portugal)))
g.add((emma, EX.traveledTo, URIRef(EX.Italy)))
g.add((emma, EX.traveledTo, URIRef(EX.France)))
g.add((emma, EX.traveledTo, URIRef(EX.Germany)))
g.add((emma, EX.traveledTo, URIRef(EX.Denmark)))
g.add((emma, EX.traveledTo, URIRef(EX.Sweden)))

g.add((kade, FOAF.knows, emma))
g.add((kade, EX.metIn, Literal("Paris", lang="en")))
g.add((kade, EX.metOn, Literal("2014-08", datatype=XSD.gYearMonth)))

university_uc = URIRef(EX.University_of_California)
g.add((university_uc, RDF.type, EX.University))
g.add((university_uc, FOAF.name, Literal("University of California")))
g.add((university_uc, EX.country, URIRef(EX.USA)))

university_valencia = URIRef(EX.University_of_Valencia)
g.add((university_valencia, RDF.type, URIRef(EX.University)))
g.add((university_valencia, FOAF.name, Literal("University of Valencia")))
g.add((university_valencia, EX.country, URIRef(EX.Spain)))

countries = ["USA", "Spain", "Canada", "France", "Portugal", "Italy", "Germany", "Denmark", "Sweden"]
for country in countries:
    country_uri = URIRef(EX[country])
    g.add((country_uri, RDF.type, URIRef(EX.Country)))

g.serialize(destination="graph.rdf", format="xml")
g.serialize(destination="graph.ttl", format="turtle")
g.serialize(destination="graph.nt", format="nt")
g.serialize(destination="graph.json-ld", format="json-ld")

print("Graph serialized in formats: RDF/XML, Turtle, N-Triples, JSON-LD.")

g.serialize(destination="graph.ttl", format="turtle")
print("Graph written to 'graph.ttl' in Turtle format.")

print("\nAll triples in the graph:")
for s, p, o in g:
    print(f"({s}, {p}, {o})")

print("\nTriples related only to Emma:")
for p, o in g.predicate_objects(subject=emma):
    print(f"({emma}, {p}, {o})")

print("\nTriples that contain people's names:")
for s, p, o in g.triples((None, FOAF.name, None)):
    print(f"({s}, {p}, {o})")
