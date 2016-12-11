#!/bin/python

import json
import sys
import os

def loadJSON(jsonFile):
	with open(jsonFile) as fid:
		graph = json.load(fid)
	return graph

def buildVertexIndex(graph):
	n = len(graph["vertices"])
	vertexNames = [v["name"] for v in graph["vertices"]]
	map1 = {key:val for key, val in zip(vertexNames, range(n))}
	return map1

def checkGraph(graph, file):
	def fail(str):
		print str
		sys.exit(1)
	if not graph.get("vertices"):
		fail("file '%s' has no entry with key 'vertices'" % file)
	if not graph.get("edges"):
		fail("file '%s' has no entry with key 'edges'" % file)
	vertices = [v["name"] for v in graph["vertices"]]
	if len(vertices) != len(set(vertices)):
		fail("file '%s' has multiple vertices with the same name" % file)

def loadTemplates(tempDirFull):
	templates = {}
	for file in os.listdir(tempDirFull):
		fullFile = os.path.join(tempDirFull, file)
		with open(fullFile) as fid:
			tempName = file.replace(".v", "")
			templates[tempName] = fid.read()
	return templates

def generate(workDirFull = "example1"):
	tempDir = "templates"
	graphFile = "graph1.json"
	graphFileFull = os.path.join(workDirFull, graphFile)
	tempDirFull = os.path.join(workDirFull, tempDir)
	graph = loadJSON(graphFileFull)
	checkGraph(graph, graphFileFull)
	map1 = buildVertexIndex(graph)
	templates = loadTemplates(tempDirFull)
	print json.dumps(templates, indent=4)

generate()
