import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

class Farmacia:
    def __init__(self, root):
        self.root = root
        self.root.title("Farmacia Moab")
        self.root.geometry("900x600")

        # Inicialización de datos
        self.productos = {}
        self.proveedores = {}
        self.clientes = {}
        self.recetas = {}
        self.ventas = []

        # Tabs
        self.tab_control = ttk.Notebook(root)
        self.tab_productos = ttk.Frame(self.tab_control)
        self.tab_proveedores = ttk.Frame(self.tab_control)
        self.tab_clientes = ttk.Frame(self.tab_control)
        self.tab_recetas = ttk.Frame(self.tab_control)
        self.tab_ventas = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_productos, text="Productos")
        self.tab_control.add(self.tab_proveedores, text="Proveedores")
        self.tab_control.add(self.tab_clientes, text="Clientes")
        self.tab_control.add(self.tab_recetas, text="Recetas")
        self.tab_control.add(self.tab_ventas, text="Ventas")
        self.tab_control.pack(expand=1, fill="both")

        # Configuración de cada pestaña
        self.configurar_tab_productos()
        self.configurar_tab_proveedores()
        self.configurar_tab_clientes()
        self.configurar_tab_recetas()
        self.configurar_tab_ventas()

    def configurar_tab_productos(self):
        ttk.Label(self.tab_productos, text="Nombre:").grid(row=0, column=0)
        self.entry_nombre = ttk.Entry(self.tab_productos)
        self.entry_nombre.grid(row=0, column=1)

        ttk.Label(self.tab_productos, text="Precio:").grid(row=1, column=0)
        self.entry_precio = ttk.Entry(self.tab_productos)
        self.entry_precio.grid(row=1, column=1)

        ttk.Label(self.tab_productos, text="Cantidad:").grid(row=2, column=0)
        self.entry_cantidad = ttk.Entry(self.tab_productos)
        self.entry_cantidad.grid(row=2, column=1)

        ttk.Button(self.tab_productos, text="Agregar", command=self.agregar_producto).grid(row=3, columnspan=2)
        self.tree_productos = ttk.Treeview(self.tab_productos, columns=("Nombre", "Precio", "Cantidad"), show='headings')
        self.tree_productos.heading("Nombre", text="Nombre")
        self.tree_productos.heading("Precio", text="Precio")
        self.tree_productos.heading("Cantidad", text="Cantidad")
        self.tree_productos.grid(row=4, columnspan=2)

    def agregar_producto(self):
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        cantidad = self.entry_cantidad.get()

        if nombre and precio.isdigit() and cantidad.isdigit():
            self.productos[nombre] = {'precio': precio, 'cantidad': cantidad}
            self.tree_productos.insert("", "end", values=(nombre, precio, cantidad))
            messagebox.showinfo("Éxito", "Producto agregado")
        else:
            messagebox.showerror("Error", "Datos inválidos")

    def configurar_tab_proveedores(self):
        ttk.Label(self.tab_proveedores, text="Nombre:").grid(row=0, column=0)
        self.entry_proveedor = ttk.Entry(self.tab_proveedores)
        self.entry_proveedor.grid(row=0, column=1)
        ttk.Button(self.tab_proveedores, text="Agregar", command=self.agregar_proveedor).grid(row=1, columnspan=2)
        self.tree_proveedores = ttk.Treeview(self.tab_proveedores, columns=("Nombre"), show='headings')
        self.tree_proveedores.heading("Nombre", text="Nombre")
        self.tree_proveedores.grid(row=2, columnspan=2)

    def agregar_proveedor(self):
        nombre = self.entry_proveedor.get()
        if nombre:
            self.proveedores[nombre] = {}
            self.tree_proveedores.insert("", "end", values=(nombre,))
            messagebox.showinfo("Éxito", "Proveedor agregado")

    def configurar_tab_clientes(self):
        ttk.Label(self.tab_clientes, text="Nombre:").grid(row=0, column=0)
        self.entry_cliente = ttk.Entry(self.tab_clientes)
        self.entry_cliente.grid(row=0, column=1)
        ttk.Button(self.tab_clientes, text="Agregar", command=self.agregar_cliente).grid(row=1, columnspan=2)
        self.tree_clientes = ttk.Treeview(self.tab_clientes, columns=("Nombre"), show='headings')
        self.tree_clientes.heading("Nombre", text="Nombre")
        self.tree_clientes.grid(row=2, columnspan=2)

    def agregar_cliente(self):
        nombre = self.entry_cliente.get()
        if nombre:
            self.clientes[nombre] = {}
            self.tree_clientes.insert("", "end", values=(nombre,))
            messagebox.showinfo("Éxito", "Cliente agregado")

    def configurar_tab_recetas(self):
        ttk.Label(self.tab_recetas, text="Receta:").grid(row=0, column=0)
        self.entry_receta = ttk.Entry(self.tab_recetas)
        self.entry_receta.grid(row=0, column=1)
        ttk.Button(self.tab_recetas, text="Agregar", command=self.agregar_receta).grid(row=1, columnspan=2)
        self.tree_recetas = ttk.Treeview(self.tab_recetas, columns=("Receta"), show='headings')
        self.tree_recetas.heading("Receta", text="Receta")
        self.tree_recetas.grid(row=2, columnspan=2)

    def agregar_receta(self):
        receta = self.entry_receta.get()
        if receta:
            self.recetas[receta] = {}
            self.tree_recetas.insert("", "end", values=(receta,))
            messagebox.showinfo("Éxito", "Receta agregada")

    def configurar_tab_ventas(self):
        ttk.Button(self.tab_ventas, text="Registrar Venta", command=self.registrar_venta).pack()
        self.tree_ventas = ttk.Treeview(self.tab_ventas, columns=("Venta"), show='headings')
        self.tree_ventas.heading("Venta", text="Venta")
        self.tree_ventas.pack()

    def registrar_venta(self):
        self.ventas.append("Venta registrada")
        self.tree_ventas.insert("", "end", values=("Venta registrada",))
        messagebox.showinfo("Éxito", "Venta registrada")

if __name__ == "__main__":
    root = tk.Tk()
    app = Farmacia(root)
    root.mainloop()
