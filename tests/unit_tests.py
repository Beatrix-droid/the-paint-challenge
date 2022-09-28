
import sys
import os

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

from app import app
import unittest

class FlaskTests(unittest.TestCase):

    #check that flask was set up correctly:
    def test_index(self):
        tester = app.test_client(self)
        response =tester.get("/", content_type="html/text")
        self.assertEqual(response.status_code,200)

    #test that page loads correctly:
    def test_title_(self):
        tester = app.test_client(self)
        response =tester.get("/", content_type="html/text")
        self.assertTrue(b'<h1>Welcome to the Paint Calculator</h1>' in response.data)

    def test_no_walls_input(self):
        tester = app.test_client(self)
        response =tester.get("/", content_type="html/text")
        self.assertTrue(b'<label class="dynamic">Enter number of walls you wish to paint <input type="number" min="1" name="" id="num" placeholder="enter number of walls"></label>' in response.data)

    def test_javascript_gen_input_button(self):
        tester = app.test_client(self)
        response =tester.get("/", content_type="html/text")
        self.assertTrue(b'<button class="dynamic-button" onclick="func()">click</button>' in response.data)
    
    def test_javascript_gen_input_button(self):
        tester = app.test_client(self)
        response =tester.get("/", content_type="html/text")
        self.assertTrue(b'<div id="inputs"></div>' in response.data)

    def test_javascript(self):
        tester = app.test_client(self)
        response =tester.get("/", content_type="html/text")
        self.assertTrue(b"""<script>
    function func(){
        var num = document.getElementById("num").value
        for (i=0; i<num ;i++){
            document.getElementById("inputs").innerHTML +='<label>Enter Wall Width:<input required type="number" min="0" name="width" placeholder="wall width in meters"></label> <br>';
            document.getElementById("inputs").innerHTML +='<label>Enter Wall Length:<input required type="number" min="0" name="length" placeholder=" wall length in meters"></label><br>';
            document.getElementById("inputs").innerHTML +='<label>Enter Obstacle Width (0 by default):<input required type="number" value=0 min="0" name="obstacle_width" placeholder="obstacle width in meters"></label><br>' ;   
            document.getElementById("inputs").innerHTML +='<label>Enter Obstacle Length (0 by default):<input required type="number" value=0 min="0" name="obstacle_length" placeholder=" obstacle length in meters"></label><br>';
        }""" in response.data)

    def test_basecoat(self):
        tester = app.test_client(self)
        response = tester.get("/", content_type="html/text")
        self.assertTrue(b'<label>Do you want to include a base coat?</label><input type="radio" class="inline" name="base_options" checked value="yes" id="option1">Yes<input type="radio" name="base_options" value="no" id="option2">No</label>' in response.data)

    def base_coat(self):
        tester = app.test_client(self)
        response = tester.get("/", content_type="html/text")
        self.assertTrue(b'<label>Do you want to include a top coat?</label><input type="radio" class="inline" name="top_options" checked value="yes" id="option1">Yes<input type="radio" name="top_options" value="no" id="option2">No</label>' in response.data)

    
    def test_javascript_gen_input_button(self):
        tester = app.test_client(self)
        response =tester.get("/", content_type="html/text")
        self.assertTrue(b'<input type="submit" value="submit">' in response.data)


        
        
    

    
if __name__ == "__main__":
    unittest.main()