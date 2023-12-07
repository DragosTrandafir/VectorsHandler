import sys
sys.path.append(r"D:\seminar8")
from logic.vector_repo import vectorRepoInitial
from console.ui import VectorUI


vR=vectorRepoInitial
user=VectorUI(vR)
user.start()