import os
import sys

# Get the root project directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

# Append the src directory to sys.path
src_path = os.path.join(project_root, 'src')
sys.path.append(src_path)

from math_utils import add

def test_addition():
    assert add(2,3)==5