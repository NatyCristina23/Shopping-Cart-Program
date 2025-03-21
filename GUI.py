import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedWidget, QMainWindow, QListWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
import Cart


class ShoppingCart(QMainWindow):
    def __init__(self):
        super(ShoppingCart, self).__init__() #why add shopping cart?
        
        self.setWindowTitle("Shopping Cart")
        self.setFixedSize(900, 900)

        self.frame1 = QWidget()
        self.frame2 = QWidget()
        self.frame1UI()
        self.frame2UI()

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.frame1)
        self.stacked_widget.addWidget(self.frame2)
        self.setCentralWidget(self.stacked_widget)


    def frame1UI(self):
        self.title = QLabel("MENU", self)
        self.subtitle = QLabel("Choose your items:", self)
        self.pizza = QPushButton("PIZZA", self)
        self.meat = QPushButton("MEAT", self)
        self.veggie = QPushButton("VEGETABLES", self)
        self.fish = QPushButton("FISH", self)
        self.bread = QPushButton("BREAD", self)
        self.cont = QPushButton("CONTINUE", self)

        self.subtitle.setFixedHeight(50)
        self.title.setFixedHeight(100)

        frame1Layout = QVBoxLayout()
        frame1Layout.addWidget(self.title)
        frame1Layout.addWidget(self.subtitle)   
        grid = QGridLayout()
        grid.addWidget(self.pizza, 0 ,0)
        grid.addWidget(self.meat, 0, 1)
        grid.addWidget(self.veggie, 0, 2)
        grid.addWidget(self.fish, 1, 0)
        grid.addWidget(self.bread, 1, 2)
        grid.addWidget(self.cont, 1, 1)
        frame1Layout.addLayout(grid)
        self.frame1.setLayout(frame1Layout)

        self.title.setObjectName("title")
        self.subtitle.setObjectName("subtitle")
        self.pizza.setObjectName("pizza")
        self.meat.setObjectName("meat")
        self.veggie.setObjectName("veggie")
        self.fish.setObjectName("fish")
        self.bread.setObjectName("bread")
        self.cont.setObjectName("cont")

        self.setStyleSheet("""
            ShoppingCart {
                background-color: #D2B7DC;
            }
            QLabel#title {
                height: 50px;
                vertical-align: center;
                padding-left: 375px;
                font-size: 50px;
                margin: 10px;
            }

            QLabel#subtitle {
                height: 30px;
                padding-left: 325px;
                font-size: 30px;
                margin: 10px;
                background-color: white;
            }

            QPushButton#pizza, #meat, #veggie, #fish, #bread {
                height: 200px;
                width: 50px;
            }    
            
            QPushButton#cont {
                height: 60px;
            }
        """)

        self.pizza.clicked.connect(lambda: Cart.add("Pizza"))
        self.meat.clicked.connect(lambda: Cart.add("Meat"))
        self.veggie.clicked.connect(lambda: Cart.add("Vegetables"))
        self.fish.clicked.connect(lambda: Cart.add("Fish"))
        self.bread.clicked.connect(lambda: Cart.add("Bread"))
        self.cont.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.frame2))
        self.cont.clicked.connect(lambda: self.items.setText(Cart.display_items()))

    def frame2UI(self):
        self.items = QLabel(self)
        self.total = QLabel("Your total is: *total*", self)
        self.back = QPushButton("GO BACK", self)
        self.confirm = QPushButton("Confirm?", self)

        frame2Layout = QVBoxLayout()
        frame2Layout.addWidget(self.items)
        frame2Layout.addWidget(self.total)
        buttons = QHBoxLayout()
        buttons.addWidget(self.back)
        buttons.addWidget(self.confirm)
        frame2Layout.addLayout(buttons)
        self.frame2.setLayout(frame2Layout)

        self.back.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.frame1))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ShoppingCart()
    window.show()
    sys.exit(app.exec_())