from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title('Supermercado Mercadona - Natalia Ramírez')
#root.iconbitmap('C:\Users\natal\Desktop\DAM\Segundo\GEMP\Hitos\Supermercado\img\mercadona.ico')
root.geometry("1000x500")

# Database

# Producto

# Conectar a una base de datos
conn = sqlite3.connect('data.sqlite')

# Cursor
c = conn.cursor()

def query_database():
    # Conectar a una base de datos
    conn = sqlite3.connect('data.sqlite')
    # Cursor
    c = conn.cursor()
    c.execute("SELECT * FROM producto")
    records = c.fetchall()

    global count
    count = 0

    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[3], record[4], record[5]), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[3], record[4], record[5]), tags=('oddrow',))
        count += 1

    conn.commit()
    conn.close()


conn.commit()

conn.close()

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


# Crear Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")


# Añadimos cuadros para añadir productos
data_frame = LabelFrame(root, text="Añadir Productos")
data_frame.pack(fill="x", expand="yes", padx=20)

# ID Producto
idp_label = Label(data_frame, text="ID Producto")
idp_label.grid(row=0,column=0,padx=10, pady=10)
idp_entry = Entry(data_frame)
idp_entry.grid(row=0, column=1, padx=10, pady=10)

# Nombre
nombre_label = Label(data_frame, text="Nombre")
nombre_label.grid(row=0,column=2,padx=10, pady=10)
nombre_entry = Entry(data_frame)
nombre_entry.grid(row=0, column=3, padx=10, pady=10)

# ID Categoría
idc_label = Label(data_frame, text="ID Categoria")
idc_label.grid(row=0,column=4,padx=10, pady=10)
idc_entry = Entry(data_frame)
idc_entry.grid(row=0, column=5, padx=10, pady=10)

# Medida
medida_label = Label(data_frame, text="Medida")
medida_label.grid(row=1,column=0,padx=10, pady=10)
medida_entry = Entry(data_frame)
medida_entry.grid(row=1, column=1, padx=10, pady=10)

# Precio
precio_label = Label(data_frame, text="Precio")
precio_label.grid(row=1,column=2,padx=10, pady=10)
precio_entry = Entry(data_frame)
precio_entry.grid(row=1, column=3, padx=10, pady=10)

# Stock
stock_label = Label(data_frame, text="Stock")
stock_label.grid(row=1,column=4,padx=10, pady=10)
stock_entry = Entry(data_frame)
stock_entry.grid(row=1, column=5, padx=10, pady=10)

# Añadir Botones

button_frame = LabelFrame(root, text="Botones")
button_frame.pack(fill="x", expand="yes", padx=20)

# Eliminar texto de las cajas
def clear_entries():
    # Borrar datos
    idp_entry.delete(0, END)
    nombre_entry.delete(0, END)
    idc_entry.delete(0, END)
    medida_entry.delete(0, END)
    precio_entry.delete(0, END)
    stock_entry.delete(0, END)

# Mover Arriba
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)

# Mover Abajo
def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)

# Eliminar un registro
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

# Eliminar varios registros
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)

# Eliminar todos los registros
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

# Actualizar registro
def update_record():
    selected = my_tree.focus()
    my_tree.item(selected, text="", values=(idp_entry.get(), nombre_entry.get(), idc_entry.get(), medida_entry.get(), precio_entry.get(), stock_entry.get()))
    # Borrar datos
    idp_entry.delete(0, END)
    nombre_entry.delete(0, END)
    idc_entry.delete(0, END)
    medida_entry.delete(0, END)
    precio_entry.delete(0, END)
    stock_entry.delete(0, END)

select_record_button = Button(button_frame, text="Eliminar texto de las cajas", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

# Actualizar
update_button = Button(button_frame, text="Actualizar registro", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

# Añadir
add_button = Button(button_frame, text="Añadir registro")
add_button.grid(row=0, column=1, padx=10, pady=10)

# Eliminar todo
remove_all_button = Button(button_frame, text="Eliminar todo", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

# Eliminar un registro
remove_one_button = Button(button_frame, text="Eliminar uno", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

# Eliminar varios registros
remove_many_button = Button(button_frame, text="Eliminar varios", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

# Mover arriba
move_up_button = Button(button_frame, text="Mover arriba", command=up)
move_up_button.grid(row=0, column=5, padx=10, pady=10)

# Mover abajo
move_down_button = Button(button_frame, text="Mover abajo", command=down)
move_down_button.grid(row=0, column=6, padx=10, pady=10)

# Eliminar texto de las cajas
select_record_button = Button(button_frame, text="Eliminar texto de las cajas", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

# Elegir registro
def select_record(e):
    # Borrar datos
    idp_entry.delete(0, END)
    nombre_entry.delete(0, END)
    idc_entry.delete(0, END)
    medida_entry.delete(0, END)
    precio_entry.delete(0, END)
    stock_entry.delete(0, END)

    # Coger los datos del registro seleccionado
    selected = my_tree.focus()
    values = my_tree.item(selected, 'values')

    # Poner los valores en las cajas
    idp_entry.insert(0, values[0])
    nombre_entry.insert(0, values[1])
    idc_entry.insert(0, values[2])
    medida_entry.insert(0, values[3])
    precio_entry.insert(0, values[4])
    stock_entry.insert(0, values[5])


# Bind the treeview
my_tree.bind("<ButtonRelease-1>", select_record)

query_database()

root.mainloop()