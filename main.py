from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Supermercado Mercadona - Natalia Ramírez')
#root.iconbitmap('C:\Users\natal\Desktop\DAM\Segundo\GEMP\Hitos\Supermercado\img\mercadona.ico')
root.geometry("1000x500")

# Añadir un estilo
style = ttk.Style()

# Elegir un estilo
style.theme_use('default')

# Configuramos los colores del TreeView
style.configure("TreeView",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

# Cambiar el color el color de los elementos seleccionados de la tabla
style.map('TreeView',
          background=[('selected', "#347083")])

# Creamos un frame para el TreeView
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Creamos la ScrollBar del TreeView
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Creamos el TreeView
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Configurar la Scrollbar
tree_scroll.config(command=my_tree.yview)

# Definir nuestras columnas
my_tree['columns'] = ["ID Producto", "Nombre", "ID Categoria", "Medida", "Precio", "Stock"]

# Formatear las columnas
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID Producto", anchor=CENTER, width=100)
my_tree.column("Nombre", anchor=W, width=140)
my_tree.column("ID Categoria", anchor=CENTER, width=100)
my_tree.column("Medida", anchor=CENTER, width=140)
my_tree.column("Precio", anchor=CENTER, width=140)
my_tree.column("Stock", anchor=CENTER, width=140)

# Creamos los Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID Producto", text="ID Producto", anchor=CENTER)
my_tree.heading("Nombre", text="Nombre", anchor=W)
my_tree.heading("ID Categoria", text="ID Categoria", anchor=CENTER)
my_tree.heading("Medida", text="Medida", anchor=CENTER)
my_tree.heading("Precio", text="Precio", anchor=CENTER)
my_tree.heading("Stock", text="Stock", anchor=CENTER)

# Add Fake Data

data = [
	["John", "Elder", "123 Elder St.", "Las Vegas", "NV", "89137"],
	["Mary", "Smith", "435 West Lookout", "Chicago", "IL", "60610"],
	["Tim", "Tanaka", "246 Main St.", "New York", "NY", "12345"],
	["Erin", "Erinton", "333 Top Way.", "Los Angeles", "CA", "90210"],
	["Bob", "Bobberly", "876 Left St.", "Memphis", "TN", "34321"],
	["Steve", "Smith", "1234 Main St.", "Miami", "FL", "12321"],
	["Tina", "Browne", "654 Street Ave.", "Chicago", "IL", "60611"],
	["Mark", "Lane", "12 East St.", "Nashville", "TN", "54345"],
	["John", "Smith", "678 North Ave.", "St. Louis", "MO", "67821"],
	["Mary", "Todd", "9 Elder Way.", "Dallas", "TX", "88948"],
	["John", "Lincoln", "123 Elder St.", "Las Vegas", "NV", "89137"],
	["Mary", "Bush", "435 West Lookout", "Chicago", "IL", "60610"],
	["Tim", "Reagan", "246 Main St.", "New York", "NY", "12345"],
	["Erin", "Smith", "333 Top Way.", "Los Angeles", "CA", "90210"],
	["Bob", "Field", "876 Left St.", "Memphis", "TN", "34321"],
	["Steve", "Target", "1234 Main St.", "Miami", "FL", "12321"],
	["Tina", "Walton", "654 Street Ave.", "Chicago", "IL", "60611"],
	["Mark", "Erendale", "12 East St.", "Nashville", "TN", "54345"],
	["John", "Nowerton", "678 North Ave.", "St. Louis", "MO", "67821"],
	["Mary", "Hornblower", "9 Elder Way.", "Dallas", "TX", "88948"]
	
]

# Crear Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Añadir nuestros datos a la pantalla
global count
count = 0

for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]), tags=('oddrow',))
    # incrementar el contador
    count += 1
