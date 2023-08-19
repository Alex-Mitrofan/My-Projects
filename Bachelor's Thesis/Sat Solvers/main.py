from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, BooleanProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.graphics import Rectangle
from kivy.graphics import Ellipse
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image 
from kivy.uix.screenmanager import Screen, ScreenManager

import time
import ast
from CDCL import CDCL
from DPLL import DPLL
from WalkSAT import WalkSAT
import CDCL as vars
from clause import Clause
from implication_graph import ImplicationGraph
import buildGraphs
from dimacs_to_data import get_data

from kivy.config import Config             #Change the window size
Config.set('graphics', 'width', '1500')
Config.set('graphics', 'height', '760')

class WindowManager(ScreenManager):
    pass

class MenuWindow(Screen):
    pass

class CDCLWindow(Screen):
    pass

class HelpWindow(Screen):
    pass

class MainWidget(BoxLayout):
    pass

class MenuHeader(BoxLayout):
    def on_start_press(self):
        global cdcl, dpll, result, problem_data, C, A
        #Default settings
        A.root.get_screen('cdcl').ids.mainwidget.ids.tree.size_hint = (0.4,1)
        A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.size_hint = (0.4,1)
        A.root.get_screen('cdcl').ids.mainwidget.ids.walksat_data.text = ''

        #settings for each algorithm
        if A.algorithm == 'cdcl':
            cdcl = CDCL(A.formula, 12) 
            result, problem_data = cdcl.get_solution(A.formula, 12)
            print(result, len(problem_data))
            C = Clauses(cdcl.clauses)
            
            #reset graphs
            buildGraphs.build_decision_tree([], None)
            A.root.get_screen('cdcl').ids.mainwidget.ids.decision_tree_image.reload()
            buildGraphs.build_implication_graph({}, None)
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph_image.reload()
        
        elif A.algorithm == "dpll":
            #reset static data members of DPLL
            DPLL.all_decisions = []                   #list of dictionaries with all decisions; used for GUI; it is static
            DPLL.problem_data = []
            #create new instance of DPLL
            dpll = DPLL(A.formula, 12)
            result, problem_data = dpll.get_solution(A.formula, 12)
            print(result, len(problem_data))
            C = Clauses(dpll.clauses)
            

            #reset graphs
            buildGraphs.build_dpll_tree([], None)
            A.root.get_screen('cdcl').ids.mainwidget.ids.decision_tree_image.reload()
            #buildGraphs.build_implication_graph({}, None)
            #A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph_image.reload()
            #A.root.get_screen('cdcl').ids.mainwidget.ids.tree.remove_widget( A.root.get_screen('cdcl').ids.mainwidget.ids.decision_tree_image)

        elif A.algorithm == "walksat":
            #create new instance of walksat
            walksat = WalkSAT(A.formula)
            result, problem_data = walksat.get_solution(A.formula)
            print(result, len(problem_data))
            C = Clauses(walksat.clauses)

            buildGraphs.build_dpll_tree([], None)
            A.root.get_screen('cdcl').ids.mainwidget.ids.decision_tree_image.reload()
            buildGraphs.build_implication_graph({}, None)
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph_image.reload()

            A.root.get_screen('cdcl').ids.mainwidget.ids.tree.size_hint = (0.1,1)
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.size_hint = (0.7,1)

            state = problem_data[A.index]
            A.root.get_screen('cdcl').ids.mainwidget.ids.walksat_data.text = "Iteration: " + str(state["iteration"]) + "\nNr flips: " + str(state["nr_flips"]) + "\nProbability: " + str(state["probability"])

             

        #reset app variable
        A.clauses = C.clauses
        A.label_clauses = ""
        A.footer_text = ""
        A.index = 0   #state index in problem data

class MenuMain(BoxLayout):
    pass

class FormulaMenu(ScrollView):
    pass

class ChooseFormula(BoxLayout):
    def on_path_validate(self, widget):
        path = widget.text 
        nvars, clauses = get_data(path)
        A.formula = clauses
        if A.algorithm != '': #if user chosed formula and algorithm
            A.root.get_screen('menu').ids.start_button.disabled = False  #enable start button
        C = Clauses(A.formula)
        A.label_clauses = ""
        A.clauses = C.clauses
        self.write_formula()
   


    def on_text_validate(self, widget):
        A.formula = ast.literal_eval(widget.text)  #convert string representation of list to list
        if A.algorithm != '': #if user chosed formula and algorithm
            A.root.get_screen('menu').ids.start_button.disabled = False  #enable start button
        C = Clauses(A.formula)
        A.label_clauses = ""
        A.clauses = C.clauses
        self.write_formula()


    def write_formula(self):
        for line in A.clauses:
            for i in range(len(line)-1):
                if line[i][1].startswith('x'):
                    A.label_clauses +=  line[i][1][0] + '[sub]' + line[i][1][1:]  + '[/sub]' + '[size=20dp]' + ' + ' + '[/size]'
                elif line[i][1].startswith('¬x'):
                        A.label_clauses += line[i][1][:2] + '[sub]' + line[i][1][2:] + '[/sub]' + '[size=20dp]' + ' + ' + '[/size]'
                    
            if line[len(line)-1][1].startswith('x'):
                    A.label_clauses += line[len(line)-1][1][0] + '[sub]' + line[len(line)-1][1][1:] + '[/sub]' + '\n'
            
            elif line[len(line)-1][1].startswith('¬x'):
                    A.label_clauses += line[len(line)-1][1][:2] + '[sub]' + line[len(line)-1][1][2:] + '[/sub]' + '\n'


    def on_ex1_press(self):
        A.formula = [[1, 4],
                    [1, -3, -8],
                    [1, 8, 12],
                    [2, 11],
                    [-7, -3, 9],
                    [-7, 8, -9],
                    [7, 8, -10],
                    [7, 10, -12],
                    [-1, 5],
                    [-1,-5]]
        if A.algorithm != '': #if user chosed formula and algorithm
            A.root.get_screen('menu').ids.start_button.disabled = False  #enable start button
        C = Clauses(A.formula)
        A.label_clauses = ""
        A.clauses = C.clauses
        self.write_formula()
        

    def on_ex2_press(self):
        A.formula = [[-1, -2],
                    [-1, 3],
                    [-3, -4],
                    [2, 4, 5],
                    [-5, 6, -7],
                    [2, 7, 8],
                    [-8, -9],
                    [-8, 10],
                    [9, -10, 11],
                    [-10, -12],
                    [-11, 12],]
        if A.algorithm != '': #if user chosed formula and algorithm
            A.root.get_screen('menu').ids.start_button.disabled = False  #enable start button
        C = Clauses(A.formula)
        A.label_clauses = ""
        A.clauses = C.clauses
        self.write_formula()
    
    def on_ex3_press(self):
        A.formula = [[1, -2, 3],
                    [-3, 4, -5],
                    [6, 7],
                    [-1, 2],
                    [3, 4, -6],
                    [-2, -4],
                    [5, -7],
                    [1, 2, -3],
                    [-2, 4],
                    [-5, 6, 7]]
        if A.algorithm != '': #if user chosed formula and algorithm
            A.root.get_screen('menu').ids.start_button.disabled = False  #enable start button
        C = Clauses(A.formula)
        A.label_clauses = ""
        A.clauses = C.clauses
        self.write_formula()
    
    def on_ex4_press(self):
        A.formula = [[-1, 2, 3],
                    [-1, -2, -3],
                    [1, 4],
                    [-4, 5],
                    [-1, 5],
                    [-2, -5],
                    [-3, -5],
                    [-4, -5]]
        if A.algorithm != '': #if user chosed formula and algorithm
            A.root.get_screen('menu').ids.start_button.disabled = False  #enable start button
        C = Clauses(A.formula)
        A.label_clauses = ""
        A.clauses = C.clauses
        self.write_formula()
    
    def on_ex5_press(self):
        A.formula = [[1, 2, 3],
                    [1, 2, -3],
                    [1, -2, 3],
                    [1, -2, -3],
                    [-1, 2, 3],
                    [-1, 2, -3],
                    [-1, -2, 3],
                    [-1, -2, -3]]
        if A.algorithm != '': #if user chosed formula and algorithm
            A.root.get_screen('menu').ids.start_button.disabled = False  #enable start button
        C = Clauses(A.formula)
        A.label_clauses = ""
        A.clauses = C.clauses
        self.write_formula()


class ChooseAlgorithm(BoxLayout):
    def on_button_cdcl_press(self):
        A.algorithm = 'cdcl'
        A.root.get_screen('menu').ids.cdcl_button.disabled = True  #disable algorithm buttons
        A.root.get_screen('menu').ids.dpll_button.disabled = True
        A.root.get_screen('menu').ids.walksat_button.disabled = True
        print("cdcl")

        if A.formula != '': #if user chosed formula and algorithm
            A.root.get_screen('menu').ids.start_button.disabled = False  #enable start button



    def on_button_dpll_press(self):
        A.algorithm = 'dpll'
        A.root.get_screen('menu').ids.cdcl_button.disabled = True  #disable algorithm buttons
        A.root.get_screen('menu').ids.dpll_button.disabled = True
        A.root.get_screen('menu').ids.walksat_button.disabled = True
        print("dpll")

        if A.formula != '': #if user chosed formula and algorithm
            A.root.get_screen('menu').ids.start_button.disabled = False  #enable start button

    def on_button_walksat_press(self):
        A.algorithm = 'walksat'
        A.root.get_screen('menu').ids.cdcl_button.disabled = True  #disable algorithm buttons
        A.root.get_screen('menu').ids.dpll_button.disabled = True
        A.root.get_screen('menu').ids.walksat_button.disabled = True
        print("walksat")

        if A.formula != '': #if user chosed formula and algorithm
            A.root.get_screen('menu').ids.start_button.disabled = False  #enable start button

class Header(BoxLayout):
    def on_button_next_press(self):
        A.index += 1
        if A.index > 0:
            button = A.root.get_screen('cdcl').ids.mainwidget.ids.header.ids.back  #enable back button
            button.disabled = False
        if A.index == len(problem_data) - 1:
            button = A.root.get_screen('cdcl').ids.mainwidget.ids.header.ids.next  #disable next button
            button.disabled = True

        state = problem_data[A.index]
        action = state["action"]
        A.update(action)
        if A.algorithm != 'walksat':         #walksat do not have decisions
            decisions = state["decisions"]
        if A.algorithm == "cdcl":
            back_jump_level = state["back_jump_level"]
            A.root.get_screen('cdcl').ids.mainwidget.ids.tree.draw_decision_tree(decisions, back_jump_level)
            graph = state["graph"].graph
            conflict = state["conflict"]
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.draw_implication_graph(graph, conflict)

        elif A.algorithm == "dpll":
            A.root.get_screen('cdcl').ids.mainwidget.ids.tree.draw_decision_tree(decisions, None)
            graph = state["graph"].graph
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.draw_implication_graph(graph, None)

        elif A.algorithm == "walksat":
            graph = state["graph"]
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.draw_implication_graph(graph, None)
            state = problem_data[A.index]
            A.root.get_screen('cdcl').ids.mainwidget.ids.walksat_data.text = "Iteration: " + str(state["iteration"]) + "\nNr flips: " + str(state["nr_flips"]) + "\nProbability: " + str(state["probability"])


    def on_button_back_press(self):
        A.index -= 1
        if A.index < len(problem_data) - 1:
            button = A.root.get_screen('cdcl').ids.mainwidget.ids.header.ids.next  #enable next button
            button.disabled = False
        if A.index == 0:
            button = A.root.get_screen('cdcl').ids.mainwidget.ids.header.ids.back  #disable back button
            button.disabled = True
            
        state = problem_data[A.index]
        action = state["action"]
        A.update(action)
        if A.algorithm != 'walksat':         #walksat do not have decisions
            decisions = state["decisions"]
        if A.algorithm == "cdcl":
            back_jump_level = state["back_jump_level"]
            A.root.get_screen('cdcl').ids.mainwidget.ids.tree.draw_decision_tree(decisions, back_jump_level)
            graph = state["graph"].graph
            conflict = state["conflict"]
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.draw_implication_graph(graph, conflict)
        
        elif A.algorithm == "dpll":
            A.root.get_screen('cdcl').ids.mainwidget.ids.tree.draw_decision_tree(decisions, None)
            graph = state["graph"].graph
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.draw_implication_graph(graph, None)
            
        elif A.algorithm == "walksat":
            graph = state["graph"]
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.draw_implication_graph(graph, None)
            state = problem_data[A.index]
            A.root.get_screen('cdcl').ids.mainwidget.ids.walksat_data.text = "Iteration: " + str(state["iteration"]) + "\nNr flips: " + str(state["nr_flips"]) + "\nProbability: " + str(state["probability"])


    def on_button_final_press(self):
        A.index = len(problem_data) - 1
        A.root.get_screen('cdcl').ids.mainwidget.ids.header.ids.next.disabled = True   #disable next button
        A.root.get_screen('cdcl').ids.mainwidget.ids.header.ids.back.disabled = False  #enable back button
                 
        state = problem_data[A.index]
        action = state["action"]
        A.update(action)

        if A.algorithm != 'walksat':         #walksat do not have decisions
            decisions = state["decisions"]
        if A.algorithm == "cdcl":
            back_jump_level = state["back_jump_level"]
            A.root.get_screen('cdcl').ids.mainwidget.ids.tree.draw_decision_tree(decisions, back_jump_level)
            graph = state["graph"].graph
            conflict = state["conflict"]
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.draw_implication_graph(graph, conflict)
        
        elif A.algorithm == "dpll":
            A.root.get_screen('cdcl').ids.mainwidget.ids.tree.draw_decision_tree(decisions, None)
            graph = state["graph"].graph
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.draw_implication_graph(graph, None)
            
        elif A.algorithm == "walksat":
            graph = state["graph"]
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.draw_implication_graph(graph, None)
            state = problem_data[A.index]
            A.root.get_screen('cdcl').ids.mainwidget.ids.walksat_data.text = "Iteration: " + str(state["iteration"]) + "\nNr flips: " + str(state["nr_flips"]) + "\nProbability: " + str(state["probability"])


    def on_button_reset_press(self):
        A.index = 0
        A.root.get_screen('cdcl').ids.mainwidget.ids.header.ids.next.disabled = False   #enable next button
        A.root.get_screen('cdcl').ids.mainwidget.ids.header.ids.back.disabled = True    #disable back button
           
        state = problem_data[A.index]
        action = state["action"]
        A.update(action)

        if A.algorithm != 'walksat':         #walksat do not have decisions
            decisions = state["decisions"]
        if A.algorithm == "cdcl":
            back_jump_level = state["back_jump_level"]
            A.root.get_screen('cdcl').ids.mainwidget.ids.tree.draw_decision_tree(decisions, back_jump_level)
            graph = state["graph"].graph
            conflict = state["conflict"]
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.draw_implication_graph(graph, conflict)
        
        elif A.algorithm == "dpll":
            A.root.get_screen('cdcl').ids.mainwidget.ids.tree.draw_decision_tree(decisions, None)
            graph = state["graph"].graph
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.draw_implication_graph(graph, None)
            
        elif A.algorithm == "walksat":
            #A.root.get_screen('cdcl').ids.mainwidget.ids.tree.draw_decision_tree(None, None)
            graph = state["graph"]
            A.root.get_screen('cdcl').ids.mainwidget.ids.implication_graph.draw_implication_graph(graph, None)
            state = problem_data[A.index]
            A.root.get_screen('cdcl').ids.mainwidget.ids.walksat_data.text = "Iteration: " + str(state["iteration"]) + "\nNr flips: " + str(state["nr_flips"]) + "\nProbability: " + str(state["probability"])

    
    def on_exit_press(self):
        button = A.root.get_screen('cdcl').ids.mainwidget.ids.header.ids.next  #enable next button
        button.disabled = False
       
        button = A.root.get_screen('cdcl').ids.mainwidget.ids.header.ids.back  #disable back button
        button.disabled = True

        #reset formula and algorithm
        A.formula = ''
        A.algorithm = ''
        A.root.get_screen('menu').ids.start_button.disabled = True #disable start button
        #enable algortihm buttons
        A.root.get_screen('menu').ids.cdcl_button.disabled = False
        A.root.get_screen('menu').ids.dpll_button.disabled = False
        A.root.get_screen('menu').ids.walksat_button.disabled = False
        A.label_clauses = ''

class Main(BoxLayout):
    pass

class Footer(BoxLayout):
    pass

class ClausesPanel(ScrollView): 
    font_size = "27dp"
 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for line in A.clauses:
            for i in range(len(line)-1):
                if line[i][1].startswith('x'):
                    A.label_clauses +=  line[i][1][0] + '[sub]' + line[i][1][1:]  + '[/sub]' + '[size=20dp]' + ' + ' + '[/size]'
                elif line[i][1].startswith('¬x'):
                        A.label_clauses += line[i][1][:2] + '[sub]' + line[i][1][2:] + '[/sub]' + '[size=20dp]' + ' + ' + '[/size]'
                    
            if line[len(line)-1][1].startswith('x'):
                    A.label_clauses += line[len(line)-1][1][0] + '[sub]' + line[len(line)-1][1][1:] + '[/sub]' + '\n'
            
            elif line[len(line)-1][1].startswith('¬x'):
                    A.label_clauses += line[len(line)-1][1][:2] + '[sub]' + line[len(line)-1][1][2:] + '[/sub]' + '\n'

            
    def update_colors(self):
        #UPDATE COLORS IN VARIABLE A.clauses
        list_of_clauses = problem_data[A.index]["literals_values"]
        list_of_values = []
        for clause in list_of_clauses:
            list_of_values.append(clause.literals_values)
        for i in range(len(list_of_values)):
            for j in range(len(list_of_values[i])):
                if list_of_values[i][j] == 0:
                    A.clauses[i][j][2] = "B"
                elif list_of_values[i][j] == 1:
                    A.clauses[i][j][2] = "G"
                elif list_of_values[i][j] == -1:
                    A.clauses[i][j][2] = "R"

         
        #print(problem_data[A.index]["decisions"])
        #print()
        #print(problem_data[A.index]["graph"].graph)
        #print()
        #print(problem_data[A.index]["graph"].graph.keys())
        #print("----------------------------------")
        #UPDATE COLORS IN GUI    
        for line in A.clauses:
            for i in range(len(line)-1):
                if line[i][1].startswith('x'):
                    if line[i][2] == 'B': #Black color 
                        A.label_clauses +=  '[color=#000000]' + line[i][1][0]
                        A.label_clauses +=  '[sub]' + line[i][1][1:]  + '[/sub]' + '[/color]' + '[size=20dp]' + ' + ' + '[/size]'
                    elif line[i][2] == 'G': #Green color 
                        A.label_clauses +=  '[color=#25DD2D]' + line[i][1][0]
                        A.label_clauses +=  '[sub]' + line[i][1][1:]  + '[/sub]' + '[/color]' + '[size=20dp]' + ' + ' + '[/size]'
                    elif line[i][2] == 'R': #Red color 
                        A.label_clauses +=  '[color=#EC2C11]' + line[i][1][0]
                        A.label_clauses +=  '[sub]' + line[i][1][1:]  + '[/sub]' + '[/color]' + '[size=20dp]' + ' + ' + '[/size]'

                elif line[i][1].startswith('¬x'):
                    if line[i][2] == 'B': #Black color 
                        A.label_clauses += '[color=#000000]' + line[i][1][:2]
                        A.label_clauses += '[sub]' + line[i][1][2:] + '[/sub]' +  '[/color]' + '[size=20dp]' + ' + ' + '[/size]'
                    elif line[i][2] == 'G': #Green color 
                        A.label_clauses += '[color=#25DD2D]' + line[i][1][:2]
                        A.label_clauses += '[sub]' + line[i][1][2:] + '[/sub]' +  '[/color]' + '[size=20dp]' + ' + ' + '[/size]'
                    elif line[i][2] == 'R': #Red color 
                        A.label_clauses +=  '[color=#EC2C11]' + line[i][1][:2]
                        A.label_clauses +=  '[sub]' + line[i][1][2:]  + '[/sub]' + '[/color]' + '[size=20dp]' + ' + ' + '[/size]'
                    
            if line[len(line)-1][1].startswith('x'):
                if line[len(line)-1][2] == 'B': #Black color 
                    A.label_clauses += '[color=#000000]' + line[len(line)-1][1][0] + '[sub]' + line[len(line)-1][1][1:] + '[/sub]' + '[/color]' + '\n'
                elif line[len(line)-1][2] == 'G': #Green color   
                    A.label_clauses += '[color=#25DD2D]' + line[len(line)-1][1][0] + '[sub]' + line[len(line)-1][1][1:] + '[/sub]' + '[/color]' + '\n' 
                elif line[len(line)-1][2] == 'R': #Red color   
                    A.label_clauses += '[color=#EC2C11]' + line[len(line)-1][1][0] + '[sub]' + line[len(line)-1][1][1:] + '[/sub]' + '[/color]' + '\n' 
            
            elif line[len(line)-1][1].startswith('¬x'):
                if line[len(line)-1][2] == 'B': #Black color 
                    A.label_clauses += '[color=#000000]' + line[len(line)-1][1][:2] + '[sub]' + line[len(line)-1][1][2:] + '[/sub]' + '[/color]' + '\n'
                if line[len(line)-1][2] == 'G': #Green color 
                    A.label_clauses += '[color=#25DD2D]' + line[len(line)-1][1][:2] + '[sub]' + line[len(line)-1][1][2:] + '[/sub]' + '[/color]' + '\n'
                if line[len(line)-1][2] == 'R': #Red color 
                    A.label_clauses += '[color=#EC2C11]' + line[len(line)-1][1][:2] + '[sub]' + line[len(line)-1][1][2:] + '[/sub]' + '[/color]' + '\n'

  
    
        

class Clauses():
    def __init__(self, clauses):
        self.nvars = cdcl.nvars
        self.clauses = []
        for clause in clauses:
            line = [] #a line is a clause
            for c in clause:
                if c > 0:  #if literal is not negated
                    line.append([c, "x" + str(c), "B"]) #c = value, "x"+c = text in GUI, "B"=color black (possible colors: "B"=black, "R"=red, "G"=green)
                else:
                    line.append([c, "¬x" + str(-c), "B"]) #c = value, "x"+c = text in GUI, "B"=color black (possible colors: "B"=black, "R"=red, "G"=green)
            self.clauses.append(line)
 
class BinaryTree(ScrollView):
    def draw_decision_tree(self, decisions, back_jump_level):
        if A.algorithm == 'cdcl':
            buildGraphs.build_decision_tree(decisions, back_jump_level)
            self.parent.parent.ids.decision_tree_image.reload()
        elif A.algorithm == 'dpll':
            buildGraphs.build_dpll_tree(decisions, None)
            self.parent.parent.ids.decision_tree_image.reload()
        elif A.algorithm == 'walksat':
            pass

class ImplicationGraph(BoxLayout):
    def draw_implication_graph(self, graph, conflict):
        if A.algorithm != "walksat":
            buildGraphs.build_implication_graph(graph, conflict)
            self.parent.parent.ids.implication_graph_image.reload()
        else:
            buildGraphs.show_walksat_graph(graph)
            self.parent.parent.ids.implication_graph_image.reload()
         

class CDCL_GUI_APP(App):
    label_clauses = StringProperty("")
    footer_text = StringProperty("")
    index = 0   #state index in problem data
    algorithm = ''  #what algorithm to use when solve the problem
    formula = ''    #formula chosed by user in menu screen
 
    with open("text_data/help.txt", "r") as file:
        help_content = file.read()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.clauses = C.clauses

        
    def update(self, action):
        #print(action)
        self.update_footer_text(action)

        clauses = problem_data[A.index]["clauses"]
        C.__init__(clauses)
        self.clauses = C.clauses
        self.label_clauses = ""
        
        #print(A.clauses)
        A.root.get_screen('cdcl').ids.mainwidget.ids.clausesPanel.update_colors()
        

    def update_footer_text(self, action):
        if action == "Init":
            self.footer_text = ""
        elif action == "UnitPropagation":
            self.footer_text = "Apply unit propagation and find the new implication graph."
        elif action == "AddNewClause":
            new_clause = problem_data[A.index]["new_clause"]
            string_clause = ""
            for i in range(len(new_clause) - 1):
                if new_clause[i] > 0:
                    string_clause = string_clause + "X" + str(new_clause[i]) + " + "
                else:
                    string_clause = string_clause + "¬X" + str(-new_clause[i]) + " + "
            if new_clause[len(new_clause) -1 ] > 0:
                string_clause = string_clause + "X" + str(new_clause[len(new_clause) -1 ])
            else: 
                string_clause = string_clause + "¬X" + str(-new_clause[len(new_clause) -1 ])
            self.footer_text = "Add new clause " + string_clause
            #print(new_clause)
        elif action == "BackJump":
            back_jump = problem_data[A.index]["back_jump_level"]
            conflict = problem_data[A.index]["conflict"]
            if conflict < 0:
                conflict = "¬X" + str(-conflict)
            else:
                conflict = "X" + str(conflict)
            self.footer_text = "Conflict for node: " + str(conflict) + ". Back jump to level " + str(back_jump)
        elif action == "AddAlreadyExistingClause":
            self.footer_text = "Tried to add already existing clause, that means formula is UNSAT."

        elif action == "ConstructFormula":
            self.footer_text = "Construct formula according to back jump level"

        elif action == "PickBranchingVariable":
            variable = problem_data[A.index]["variable"]
            assignment = problem_data[A.index]["assignment"]
            if assignment == 1:
                assignment = "True"
            else:
                assignment = "False"
            self.footer_text = "Arbitrarily pick branching variable X" + str(variable) + " and assign value " + assignment
        
        elif action == "PureLiteralElimination":
            self.footer_text = "Apply Pure Literal Elimination."

        elif action == "SAT":
            self.footer_text = "Formula is SAT."
        elif action == "UNSAT":
            self.footer_text = "Formula is UNSAT."
        elif action == "Init WalkSAT":
            self.footer_text = "WalkSAT"
        elif action == "RandomAssignment":
            self.footer_text = "Random assignment for all variables."
        elif action == "FlipVariable max":
            self.footer_text = "Iteration: " + str(problem_data[A.index]["iteration"]) + ". Flip variable X" + str(abs(problem_data[A.index]["variable"])) + " with maximum break-count."
        elif action == "FlipVariable min":
            self.footer_text = "Iteration: " + str(problem_data[A.index]["iteration"]) + ". Flip variable X" + str(abs(problem_data[A.index]["variable"])) + " with minimum break-count."
        elif action == "SAT walksat":
            self.footer_text = "Iteration: " + str(problem_data[A.index]["iteration"]) + ". Formula is SAT."
        elif action == "UNSAT walksat":
            self.footer_text = "Iteration: " + str(problem_data[A.index]["iteration"]) + ". Formula is UNSAT."

 
if __name__ == "__main__": 
    global cdcl, result, problem_data, C, formula
    #default example of formula
    formula = [[1, 4],
                [1, -3, -8],
                [1, 8, 12],
                [2, 11],
                [-7, -3, 9],
                [-7, 8, -9],
                [7, 8, -10],
                [7, 10, -12],
                [-1, 5],
                [-1,-5]]
    
    cdcl = CDCL(formula, 12) 
    #result, problem_data = cdcl.get_solution(formula, 12)
    #print(result, len(problem_data))
   
    
    dpll = DPLL(formula, 12) 
    walksat = WalkSAT(formula) 
    #result, problem_data = dpll.get_solution(formula, 12)
    #print(result, len(problem_data))
    C = Clauses(dpll.clauses)
    

    A = CDCL_GUI_APP()
    A.clauses = ''

    buildGraphs.build_decision_tree([], None)
    buildGraphs.build_dpll_tree([], None)
    buildGraphs.build_implication_graph({}, None)
    
    A.run()
   


