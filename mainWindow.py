import asyncio
import json
import random
import time
from PySide6.QtCore import QEasingCurve, QPoint, QPropertyAnimation, QRect, QTimer, Qt
from PySide6.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow
from WinnerDialog import WinnerDialog
from clickableLabel import ClicableLabel
from loseDialog import LoseDialog
from uiMainWindow import Ui_MainWindow



class MainWindow(QMainWindow):
    def __init__(self,gamemode:bool = True,turns:int = 0,app:QApplication=None):   #True - с таймером, False - без таймера
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.gamemode = gamemode
        self.timer = QTimer()
        self.time = float(0)
        self.app = app
        
        if gamemode:
            self.ui.saveGameButton.hide()
        else:
            self.ui.timer.hide()
        
        
        self.turns = turns
        self.ui.turns.setText("Количество ходов = "+ str(self.turns)) 
        
        self.blocked = True
        self.blockGui(True) 
        
        for i in range(4):
            for j in range(4):
                if(i==j==3):
                    continue
                self.ui.chips[i][j].clicked.connect(self.clicked)
        self.ui.shuffleButton.clicked.connect(lambda:asyncio.ensure_future(self.randomGenerate()))
        self.ui.saveGameButton.clicked.connect(self.saveGame)
        self.ui.backButton.clicked.connect(self.backButton)
        self.setFocusPolicy(Qt.StrongFocus)
        
   
    def animateSwap(self,label:ClicableLabel):
        emptyPos = self.findEmptyPos()
        labelPos = self.ui.area.getItemPosition(self.ui.area.indexOf(label))
        
        animeLabel = ClicableLabel(self.ui.centralwidget)
        animeLabel.setObjectName("ClicableLabel")
        animeLabel.setText(label.text())
        animeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        animeLabel.setGeometry(QRect(labelPos[0]+540,labelPos[1]+30,121,121))
        animeLabel.setStyleSheet(label.styleSheet())
        animeLabel.setAttribute(Qt.WA_TransparentForMouseEvents)
        animeLabel.show()
        
        self.app.setStyle(self.app.style())
        label.setStyleSheet(f"background-color: rgba(0, 0, 0,0.0);"
                            f"border: 0px solid rgba(0, 0, 0,0.0);"
                            f"color: rgba(0,0,0,0.0);")
        
        anim = QPropertyAnimation(animeLabel, b"pos", self)
        
        start = self.ui.area.cellRect(labelPos[0], labelPos[1]).topLeft()
        finish = self.ui.area.cellRect(emptyPos[0], emptyPos[1]).topLeft()
   
        anim.setDuration(75)
        anim.setStartValue(QPoint(start.x()+540,start.y()+30))
        anim.setEndValue(QPoint(finish.x()+540,finish.y()+30))
        anim.start()
        anim.finished.connect(lambda: (animeLabel.hide(),animeLabel.destroy(),label.setStyleSheet("")))
        
        self.ui.area.addWidget(label,emptyPos[0],emptyPos[1],1,1)                        #Анимация движения фишки
    def clicked(self):
        if(self.hasEmptyNear(self.sender())):
            self.move(self.sender())                                                #обработка нажатия на label
    def move(self,label:ClicableLabel):
        
        self.animateSwap(label)
        self.turns+=1
        self.ui.turns.setText("Количество ходов = "+ str(self.turns))
        
        if not(self.timer.isActive()) and self.gamemode:
            self.timer.start()
                
        if (self.isSolved()):
            self.timer.stop()
            self.winnerDialog = WinnerDialog(self.turns,self.time,self.gamemode)
            self.ui.saveGameButton.setEnabled(False)
            self.ui.saveGameButton.setStyleSheet("text-decoration: line-through")
            self.blockGui(True)
            return                              
        else:
            self.ui.saveGameButton.setEnabled(True)
            self.ui.saveGameButton.setStyleSheet("text-decoration: ")                               #Двигает фишку в пустоту     
    def hasEmptyNear(self,label:ClicableLabel):
        pos = self.ui.area.getItemPosition(self.ui.area.indexOf(label))[:2]
        empty = self.findEmptyPos()
        match pos:
            case [0,0]:
                if([1,0] == empty or [0,1] == empty):
                    return True
            case [3,3]:
                if([2,3] == empty or [3,2] == empty):
                    return True
            case [0,3]:
                if ([1,3] == empty or [0,2] == empty):
                    return True
            case [3,0]:
                if([2,0] == empty or [3,1] == empty):
                    return True
            case [0,x]:
                if([1,x] == empty or [0,x+1] == empty or [0,x-1]== empty):
                    return True
            case [3,x]:
                if([2,x] == empty or [3,x+1] == empty or [3,x-1] == empty):
                    return True
            case [x,0]:
                if([x,1]==empty or [x+1,0] == empty or [x-1,0]==empty):
                    return True
            case [x,3]:
                if([x,2]==empty or [x+1,3] == empty or [x-1,3]==empty):
                    return True
            case[x,y]:
                if([x+1,y] == empty or [x-1,y]==empty or [x,y+1] == empty or [x,y-1] == empty):
                    return True
            case _:
                return False                       #Проверяет есть ли рядом пустая клетка
    def findEmptyPos(self):
        for row in range(4):
            for col in range(4):
                widget = self.ui.area.itemAtPosition(row, col)
                if widget is None:
                    return([row,col])                                           #Находит координаты пустой клетки
    async def randomGenerate(self):
        self.ui.turns.setText("Количество ходов = 0")
        self.turns = 0
        
        self.ui.saveGameButton.setEnabled(True)
        self.ui.saveGameButton.setStyleSheet("text-decoration: line-through")
        self.ui.shuffleButton.blockSignals(True)
        self.ui.shuffleButton.setStyleSheet("text-decoration: line-through")
        
        if self.gamemode:
            self.ui.timer.setText("Оставшееся время = 60s")
            self.initTimer()
        
        self.blockGui(True)
        self.moveEmptyToPos([3,3])
        for i in range(0,50):
            await asyncio.sleep(0.03)
            a = random.randint(0,14)
            b = random.randint(0,14)
            self.swap(self.ui.chips[a//4][a%4],self.ui.chips[b//4][b%4])
        flag = self.solvable()
        while not(flag):
            await asyncio.sleep(0.03)
            a = random.randint(0,14)
            b = random.randint(0,14)
            self.swap(self.ui.chips[a//4][a%4],self.ui.chips[b//4][b%4])  
            flag = self.solvable()
            
        self.ui.saveGameButton.blockSignals(False)
        self.ui.saveGameButton.setStyleSheet("text-decoration:")
        self.ui.shuffleButton.setStyleSheet("text-decoration:")
        self.ui.shuffleButton.blockSignals(False)
        self.blockGui(False)                                   #Случайным образом заполняет поле
    def swap(self,label1:ClicableLabel,label2:ClicableLabel):
         pos1 = self.ui.area.getItemPosition(self.ui.area.indexOf(label1))
         pos2 = self.ui.area.getItemPosition(self.ui.area.indexOf(label2))
         self.ui.area.removeWidget(label1)
         self.ui.area.removeWidget(label2)
         self.ui.area.addWidget(label1,pos2[0],pos2[1],pos2[2],pos2[3])
         self.ui.area.addWidget(label2,pos1[0],pos1[1],pos1[2],pos1[3])         #Меняет местами две фишки
    def solvable(self):
         inversions = 1
         flatteredchips = [item for sublist in self.ui.chips for item in sublist]
         for i in range(len(flatteredchips)):
            pos1 = self.ui.area.getItemPosition(self.ui.area.indexOf(flatteredchips[i]))[:2]
            for j in range(i + 1, len(flatteredchips)):
                pos2 = self.ui.area.getItemPosition(self.ui.area.indexOf(flatteredchips[j]))[:2]
                if(int(flatteredchips[(pos1[0])*4+pos1[1]].text())<int(flatteredchips[(pos2[0])*4+pos2[1]].text())):
                    inversions+=1     
         return inversions%2==0                                               #Проверяет решаема ли данная ситуация на доске
    def isSolved(self):
        for i in range(0,4):
            for j in range(0,4): 
                 if(i==j==3):
                     continue
                 pos = self.ui.area.getItemPosition(self.ui.area.indexOf(self.ui.chips[i][j]))[:2] 
                 if not(pos[0]==i and pos[1]==j):
                     return False
        return True                                               #Проверяет решена ли головоломка прямо сейчас
    def blockGui(self,b:bool):
        for i in range(4):
            for j in range(4):
                if(i==j==3):
                    continue
                self.ui.chips[i][j].blockSignals(b)
        self.blocked = b                                        #Блокирует Гуи
    def moveEmptyToPos(self,pos):
        empty = self.findEmptyPos()
        if (empty == pos):
            return
        label = self.ui.area.itemAtPosition(pos[0],pos[1]).widget()
        self.ui.area.removeWidget(label)
        self.ui.area.addWidget(label,empty[0],empty[1],1,1)                                     #Переносит пустую фишку в правый угол
    def timeUpdate(self):
        self.time -= 0.1
        self.time = round(self.time,1)
        self.ui.timer.setText("Оставшееся время = "+str(self.time)+" s")
        
        if (self.time <=0):
            self.loseWindow = LoseDialog(self.turns)
            asyncio.ensure_future(self.randomGenerate())                                             #Обновляет таймер каждые 100ms
    def initTimer(self):
        self.timer = QTimer()
        self.ui.timer.setText("Оставшееся время = 60s")
        self.ui.timer.setStyleSheet(f'color: ')
        self.timer.setInterval(100)
        self.time = 60
        self.timer.timeout.connect(self.timeUpdate)                                              #Инициализация таймера 
    def saveGame(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Grid State', '', 'JSON Files (*.json)')
        if file_path:
            state = {'turns': self.turns, 'grid_state': []}
            for row in range(4):
                for column in range(4):
                    item = self.ui.area.itemAtPosition(row, column)
                    if item is not None:
                        widget = item.widget()
                        if widget is not None:
                            state['grid_state'].append({'row': row, 'column': column, 'widget_text': widget.text()})
                    if item is None:
                        state['grid_state'].append({'row': row, 'column': column, 'widget_text': 0})
            with open(file_path, 'w') as file:
                json.dump(state, file)                                               #Сохранение игры
    def keyPressEvent(self, event):
        key = event.key() 
        empty = self.findEmptyPos()
        if self.blocked:
            return
        match key:
            case 16777234:
                if (empty[1]+1!=4):
                    label = self.ui.area.itemAtPosition(empty[0],empty[1]+1)
                    self.move(label.widget())
                   
            case 16777236: 
                if (empty[1]-1!=-1):
                    label = self.ui.area.itemAtPosition(empty[0],empty[1]-1)
                    self.move(label.widget())
            case 16777235: 
                if (empty[0]+1 !=4):
                    label = self.ui.area.itemAtPosition(empty[0]+1,empty[1])
                    self.move(label.widget())
            case 16777237:
                if (empty[0]-1 !=-1):
                    label = self.ui.area.itemAtPosition(empty[0]-1,empty[1])
                    self.move(label.widget())                                   #Управление на стрелочки                                                                            
    async def fillBoardFromJson(self,saved_area_state):
  
        self.blocked = True
        self.blockGui(True) 
        
        self.ui.shuffleButton.blockSignals(True)
        self.ui.shuffleButton.setStyleSheet("text-decoration: line-through")
        self.ui.saveGameButton.blockSignals(False)
        self.ui.saveGameButton.setStyleSheet("text-decoration:")
        for i in range(0,16):
            await asyncio.sleep(0.03)
            item = self.ui.area.itemAtPosition(saved_area_state[i]['row'],saved_area_state[i]['column'])
            if (saved_area_state[i]['widget_text']==0):
                emptypos = [saved_area_state[i]['row'],saved_area_state[i]['column']]
                continue
            newindex = int(saved_area_state[i]['widget_text'])-1
            if (item is not(None)):   
                widget = item.widget()
                self.swap(widget,self.ui.chips[newindex//4][newindex%4])
        await asyncio.sleep(0.03)
        self.moveEmptyToPos(emptypos) 
        self.ui.shuffleButton.blockSignals(False)
        self.ui.shuffleButton.setStyleSheet(("text-decoration: "))
        self.blocked = False
        self.blockGui(False)               #Заполнение доски с словаря saved_area_state
    def backButton(self):
        from startDialog import StartDialog
        self.startDialog = StartDialog(self.app)
        self.destroy()                                             #Возврат на стартовое окно
    def showEvent(self, event):
        self.setWindowOpacity(0.0) 
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(100)
        self.animation.setStartValue(0.0)
        self.animation.setEndValue(1.0)
        self.animation.setEasingCurve(QEasingCurve.OutQuad)
        self.animation.start()                                       #Плавное появленик окна