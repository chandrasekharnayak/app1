import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct path to 'utils' folder
src_path = os.path.join(current_dir, 'src')
# Add it to sys.path so Python can find it
sys.path.append(src_path)

from src.math_utils import add

def test_addition():
    assert add(2,3)==5