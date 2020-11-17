from random import sample
from tkinter import Tk
def creategrid(h,w):
    grid=[]
    for row in range(h):
        grid.append([])
        for col in range(w):
            grid[row].append("#")
    return grid

def printgrid(grid):
    for row in grid:
        text=""
        for cell in row:
            text+=cell
        print(text)

def calculatefill(h,w):
    cell=h*w
    return cell//2

def firstfill(h,w):
    x=sample(range(w),1)[0]
    y=sample(range(h),1)[0]
    return([y,x])

def findfillers(fillnum):
    colors=["#FF0000","#800000","#FFFF00","#808000","#00FF00","#008000","#00FFFF","#008080","#0000FF","#000080","#FF00FF","#800080"]
    filler=[]
    for i in range(fillnum):
        filler.append(colors[i])
    return filler

def fillgrid(grid, filler, locs):
    count=0
    for loc in locs:
        y=loc[0]
        x=loc[1]
        grid[y][x]=filler[count]
        count+=1
    return grid

def randfillgridloc(h,w,fill):
    locs=[]
    locs.append(firstfill(h,w))
    for i in range(fill-1):
        while True:
            chosen=sample(locs,1)[0]
            ychange=sample([-1,0,1],1)[0]
            xchange=sample([-1,0,1],1)[0]
            y=chosen[0]+ychange
            x=chosen[1]+xchange
            if y<0 or x<0 or y>(h-1) or x>(w-1):
                continue
            if [y,x] not in locs:
                locs.append([y,x])
                break
    return locs

def createfilledgrid():
    height=5
    weight=5
    grid = creategrid(height,weight)

    fillnum = calculatefill(height,weight)

    fill_locs = randfillgridloc(height, weight, fillnum)

    fillers = findfillers(fillnum)

    grid = fillgrid(grid,fillers,fill_locs)

    return grid 

def configure_window():
    root.geometry("500x500")
    root.configure(background="#b3ffff")

grid=createfilledgrid()

printgrid(grid)

root = Tk()

root.mainloop()