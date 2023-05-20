from django.shortcuts import render, redirect
import ibm_db
from django.contrib.auth.decorators import login_required

def connect_db():
    conn_str = "database=bludb;hostname=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud; port=30426; uid = gtp43134;password = WrqarQrbVYVcaCA8;security =SSL;sslcertificate = SSL_Certificate.crt "
    conn = ibm_db.connect(conn_str, '', '')
    return conn

def pet_list(request):
    conn = connect_db()
    query = "SELECT * FROM petapp_pet WHERE available = 1"
    stmt = ibm_db.exec_immediate(conn, query)
    pets = []
    row = ibm_db.fetch_assoc(stmt)
    while row:
        pets.append(row)
        row = ibm_db.fetch_assoc(stmt)
    print(pets)
    ibm_db.close(conn)
    return render(request, 'petapp/pet_list.html', {'pets': pets})

def buy_pet(request, pet_id):
    conn = connect_db()
    query = f"UPDATE petapp_pet SET available = 0 WHERE id = {pet_id}"
    stmt = ibm_db.exec_immediate(conn, query)
    ibm_db.close(conn)
    return redirect('gallery')

def sell_pet(request):
    if request.method == 'POST':
        name = request.POST['name']
        species = request.POST['species']
        price = request.POST['price']
        url = request.POST['url']
        conn = connect_db()
        query = f"INSERT INTO petapp_pet (name, species, price, available, url) VALUES ('{name}', '{species}', {price}, TRUE, '{url}')"
        stmt = ibm_db.exec_immediate(conn, query)
        ibm_db.close(conn)
        return redirect('gallery')
    return render(request, 'petapp/sell_pet.html')


def pet_home(request):
    return render(request,"pet_temp/index.html")

@login_required(login_url='login')
def gallery(request):
    conn = connect_db()
    query = "SELECT * FROM petapp_pet WHERE available = 1"
    stmt = ibm_db.exec_immediate(conn, query)
    pets = []
    row = ibm_db.fetch_assoc(stmt)
    while row:
        pets.append(row)
        row = ibm_db.fetch_assoc(stmt)
    print(pets)
    ibm_db.close(conn)
    return render(request,"pet_temp/gallery.html",{'pets': pets})

@login_required(login_url='login')
def buyed(request):
    conn = connect_db()
    query = "SELECT * FROM petapp_pet WHERE available = 0"
    stmt = ibm_db.exec_immediate(conn, query)
    pets = []
    row = ibm_db.fetch_assoc(stmt)
    while row:
        pets.append(row)
        row = ibm_db.fetch_assoc(stmt)
    print(pets)
    ibm_db.close(conn)
    return render(request,"pet_temp/buyed.html",{'pets': pets})

def about(request):
    return render(request,"pet_temp/about.html")

def sale(request):
    return render(request,"pet_temp/contact.html")

def services(request):
    return render(request,"pet_temp/services.html")
