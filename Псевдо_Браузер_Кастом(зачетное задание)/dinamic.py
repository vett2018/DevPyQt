import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


#class TabContainer(QtGui.QWidget):
class TabContainer(QWidget):
  def __init__(self):
    super(TabContainer, self).__init__()
    self.next_item_is_table = False
    self.initUI()

  def initUI(self):
    self.setGeometry(150, 150, 650, 350)
    self.tabwidget = QTabWidget(self)
    vbox = QVBoxLayout()
    vbox.addWidget(self.tabwidget)
    self.setLayout(vbox)
    self.pages = []
    self.add_page()
    self.show()

  def create_page(self, *contents):
    page = QWidget()
    vbox = QVBoxLayout()
    for c in contents:
        vbox.addWidget(c)

    page.setLayout(vbox)
    return page

  def create_table(self):
    rows, columns = random.randint(2,5), random.randint(1,5)
    table = QTableWidget( rows, columns )
    for r in range(rows):
        for c in range(columns):
            table.setItem( r, c, QTableWidgetItem(str(random.randint(0,10) ) ) )
    return table

  # def create_list(self):
  #   list = QListWidget()
  #   columns = random.randint(2,5)
  #   for c in range(columns):
  #       QListWidgetItem( str( random.randint(0,10) ), list )
  #
  #   return list

  def create_new_page_button(self):
    btn = QPushButton('Create a new page!')
    btn.clicked.connect(self.add_page)
    return btn

  def add_page(self):
    if self.next_item_is_table:
        self.pages.append( self.create_page( self.create_table(), self.create_new_page_button() ) )
        self.next_item_is_table = False
    else:
        self.pages.append( self.create_page( self.create_list(), self.create_new_page_button() ) )
        self.next_item_is_table = True

    self.tabwidget.addTab( self.pages[-1] , 'Page %s' % len(self.pages) )
    self.tabwidget.setCurrentIndex( len(self.pages)-1 )

app = QApplication(sys.argv)
ex = TabContainer()
sys.exit(app.exec_())