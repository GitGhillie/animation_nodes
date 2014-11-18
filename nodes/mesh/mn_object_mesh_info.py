import bpy
from bpy.types import Node
from mn_node_base import AnimationNode
from mn_execution import nodePropertyChanged, allowCompiling, forbidCompiling

class mn_ObjectMeshInfo(Node, AnimationNode):
	bl_idname = "mn_ObjectMeshInfo"
	bl_label = "Object Mesh Info"
	
	def init(self, context):
		forbidCompiling()
		self.inputs.new("mn_ObjectSocket", "Object").showName = False
		self.outputs.new("mn_VertexListSocket", "Vertices")
		self.outputs.new("mn_PolygonListSocket", "Polygons")
		allowCompiling()
		
	def getInputSocketNames(self):
		return {"Object" : "object"}
	def getOutputSocketNames(self):
		return {"Vertices" : "vertices",
				"Polygons" : "polygons"}
		
	def useInLineExecution(self):
		return True
	def getInLineExecutionString(self, outputUse):
		codeLines = []
		codeLines.append("$vertices$ = []")
		codeLines.append("$polygons$ = []")
		codeLines.append("try:")
		codeLines.append("    for vertex in %object%.data.vertices:")
		codeLines.append("        $vertices$.append([vertex.co, vertex.normal, vertex.index, %object%])")
		codeLines.append("    for polygon in %object%.data.polygons:")
		codeLines.append("        $polygons$.append([polygon.center, polygon.normal, polygon.area, polygon.material_index, %object%])")
		codeLines.append("except: pass")
		return "\n".join(codeLines)
		