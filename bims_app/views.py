from django.shortcuts import render, redirect
from bims_app.models import Client, Business, Loans, Group
from datetime import date
from django.contrib import messages


# Create your views here.


def dashboard(request):
    return render(request, 'Bimsapp/dashboard.html')


def clientview(request):
    clients = Client.objects.all()
    dict = {'clients':clients}
    return render(request, 'Bimsapp/client.html',dict)


def addclientview(request):
    if request.method == 'POST':
        # check if data is not empty
        if (request.POST.get('First_Name') and
                request.POST.get('Last_Name') and
                request.POST.get('Surname') and
                request.POST.get('Phone_Number') and
                request.POST.get('PoBox') and
                request.POST.get('Residence') and
                request.POST.get('Email') and
                request.POST.get('Id_No') and
                request.POST.get('DOB') and
                request.POST.get('Occupation')
        ):
            # if not empty grab the

            fname = request.POST.get('First_Name')
            lname = request.POST.get('Last_Name')
            sname = request.POST.get('Surname')
            phone = request.POST.get('Phone_Number')
            pbox = request.POST.get('PoBox')
            residence = request.POST.get('Residence')
            email = request.POST.get('Email')
            idno = request.POST.get('Id_No')
            dob = request.POST.get('DOB')
            occupation = request.POST.get('Occupation')

            # GENERATE MEMBERS ACCOUNT NUMBER ##  MEL/2021/1

            year = date.today().year
            # check id of the last client to be added
            lastClient = Client.objects.last()  # get the last item in the client table

            # check if last client was found
            if lastClient:
                newClientId = lastClient.id + 1

            else:
                newClientId = 1

            # ACC no
            accno = "MEL/" + str(year) + '/' + str(newClientId)

            # instace of the client table
            try:
                client = Client()
                client.Acc_No = accno
                client.First_Name = fname
                client.Last_Name = lname
                client.Surname = sname
                client.Phone_Number = phone
                client.PoBox = pbox
                client.Residence = residence
                client.Email = email
                client.Id_No = idno
                client.DOB = dob
                client.Occupation = occupation
                client.save()
                messages.success(request, 'client added successfully')
                return redirect('clients')
            except Exception:
                messages.error(request, 'client not added')
                return redirect('clients')

        else:
            pass

    else:
        return redirect('clients')


def updateclientview(request, client_id):
    if request.method == 'POST':
        # check if all fields have data
        if (
                request.POST.get('First_Name') and
                request.POST.get('Last_Name') and
                request.POST.get('Surname') and
                request.POST.get('Phone_Number') and
                request.POST.get('PoBox') and
                request.POST.get('Residence') and
                request.POST.get('Email') and
                request.POST.get('Id_No') and
                request.POST.get('DOB') and
                request.POST.get('Occupation')
        ):
            # update
            Client.objects.filter(id=client_id).update(
                First_Name=request.POST.get('First_Name'),
                Last_Name=request.POST.get('Last_Name'),
                Surname=request.POST.get('Surname'),
                Phone_Number=request.POST.get('Phone_Number'),
                PoBox=request.POST.get('PoBox'),
                Residence=request.POST.get('Residence'),
                Email=request.POST.get('Email'),
                Id_No=request.POST.get('Id_No'),
                DOB=request.POST.get('DOB'),
                Occupation=request.POST.get('Occupation')
            )
            messages.success(request, 'client updated')
            return redirect('clients')
        else:
            messages.error(request, 'client not updated')
            return redirect('clients')
    else:
        return redirect('clients')


def deleteclientview(request, client_id):
    if request.method == 'POST':
        Client.objects.filter(id=client_id).delete()
        messages.success(request, 'delete!!')
        return redirect('clients')
    else:
        messages.error(request, 'Not deleted')
        return redirect('clients')


def businessview(request):
    return render(request, 'Bimsapp/business.html')


def loansview(request):
    return render(request, 'Bimsapp/loans.html')


def groupview(request):
    return render(request, 'Bimsapp/group.html')
