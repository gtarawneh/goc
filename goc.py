#!/bin/python

import json
import sys


def loadJSON(jsonFile):
	with open(jsonFile) as fid:
		graph = json.load(fid)
	return graph

def buildVertexIndex(graph):
	n = len(graph["vertices"])
	vertexNames = [v["name"] for v in graph["vertices"]]
	map1 = {key:val for key, val in zip(vertexNames, range(n))}
	return map1

def checkGraph(graph):
	if not graph.get("vertices"):
		yield "no entry with key 'vertices'"
		raise StopIteration
	if not graph.get("edges"):
		yield "no entry with key 'edges'"
		raise StopIteration
	vertices = [v["name"] for v in graph["vertices"]]
	if len(vertices) != len(set(vertices)):
		yield "multiple vertices with the same name"

def generate():
	graphFile = "graph1.json"
	graph = loadJSON(graphFile)
	errors = [err for err in checkGraph(graph)]
	if errors:
		print "Found one or more errors while loading '%s':" % graphFile
		for e in errors:
			print "  * %s" % e
		sys.exit(1)
	map1 = buildVertexIndex(graph)
	print json.dumps(map1, indent=4)

generate()
