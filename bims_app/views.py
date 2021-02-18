from django.shortcuts import render, redirect
from bims_app.models import Client, Loans, Group, Application
from datetime import date
from django.contrib import messages


# Create your views here.


def dashboard(request):
    no_of_clients = Client.objects.all().count()
    no_of_groups = Group.objects.all().count()
    no_of_loans = Loans.objects.all().count()
    no_of_applications = Application.objects.all().count()
    dict = {'m_clients':no_of_clients,
            'm_groups':no_of_groups,
            'm_loans':no_of_loans,
            'm_apps':no_of_applications}
    return render(request, 'bims_app/dashboard.html',dict)


def clientview(request):
    clients = Client.objects.all()
    dict = {'clients': clients}
    return render(request, 'bims_app/client.html', dict)


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
                return redirect('client')
            except Exception:
                messages.error(request, 'client not added')
                return redirect('client')

        else:
            pass

    else:
        return redirect('client')


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
            return redirect('client')
        else:
            messages.error(request, 'client not updated')
            return redirect('client')
    else:
        return redirect('client')


def deleteclientview(request, client_id):
    if request.method == 'POST':
        Client.objects.filter(id=client_id).delete()
        messages.success(request, 'delete!!')
        return redirect('client')
    else:
        messages.error(request, 'Not deleted')
        return redirect('cliens')


def groupview(request):
    groups = Group.objects.all()
    dict = {'groups': groups}
    return render(request, 'bims_app/group.html', dict)


def addgroupview(request):
    if request.method == 'POST':
        # check if data is not empty

        if (request.POST.get('NameOfTheGroup') and
                request.POST.get('ChairOfGroup') and
                request.POST.get('Treasurer') and
                request.POST.get('TPNumber') and
                request.POST.get('YOE')
        ):
            # if not empty grab data

            NOG = request.POST.get('NameOfTheGroup')
            COG = request.POST.get('ChairOfGroup')
            Treasure = request.POST.get('Treasurer')
            phone = request.POST.get('TPNumber')
            YEAR = request.POST.get('YOE')

            # instance of the group table

            group = Group()
            group.NameOfTheGroup = NOG
            group.ChairOfGroup = COG
            group.Treasurer = Treasure
            group.TPNumber = phone
            group.YOE = YEAR
            group.save()
            messages.success(request, 'group saved')
            return redirect('group')
        else:
            messages.error(request, 'group not saved')
            return redirect('group')

    else:
        return redirect('group')


def updategroupview(request, group_id):
    if request.method == 'POST':
        # check if all the fields have data
        if (
                request.POST.get('NameOfTheGroup') and
                request.POST.get('ChairOfGroup') and
                request.POST.get('Treasurer') and
                request.POST.get('TPNumber') and
                request.POST.get('YOE')
        ):
            # update
            Group.objects.filter(id=group_id).update(
                name=request.POST.get('NameOfTheGroup'),
                chair=request.POST.get('ChairOfGroup'),
                treasuer=request.POST.get('Treasurer'),
                phone=request.POST.get('TPNumber'),
                year=request.POST.get('YOE')
            )
            messages.success(request, 'updated successfully')
            return redirect('group')
        else:
            messages.error(request, 'not updated')
            return redirect('group')

    else:
        return redirect('group')


def deletegroupview(request, group_id):
    if request.method == 'POST':
        Group.objects.filter(id=group_id).delete()
        messages.success(request, 'deleted!')
        return redirect('group')
    else:
        messages.error(request, 'Group not deleted')
        return redirect('group')


def loansview(request):
    loan = Loans.objects.all()
    dict = {'loan': loan}
    return render(request, 'bims_app/loans.html', dict)


def createloansview(request):
    if request.method == 'POST':

        # check if the data not empty
        if (request.POST.get('Loan_Name') and
                request.POST.get('Loan_Duration') and
                request.POST.get('Amount')
        ):

            # if empty grab data
            name = request.POST.get('Loan_Name')
            duration = request.POST.get('Loan_Duration')
            amount = request.POST.get('Amount')

            # instance of the table
            loans = Loans()
            loans.Loan_Name = name
            loans.Loan_Duration = duration
            loans.Amount = amount
            loans.save()
            messages.success(request, 'loan saved')
            return redirect('loan')
        else:
            messages.error(request, 'something went wrong')
            return redirect('loan')

    else:
        return redirect('loan')


def updateloansview(request, loans_id):
    if request.method == 'POST':

        # check if all fields have data
        if (request.POST.get('Loan_Name') and
                request.POST.get('Loan_Duration') and
                request.POST.get('Amount')
        ):

            # update
            Loans.objects.filter(loans_id).update(
                name=request.POST.get('Loan_Name'),
                duration = request.POST.get('Loan_Duration'),
                amount = request.POST.get('Amount')
            )
            messages.success(request, 'updated successfully')
            return redirect('loans')
        else:
            messages.error(request, 'not updated')
            return redirect('loan')

    else:
        return redirect('loan')


def deleteloansview(request, loans_id):
    if request.method == 'POST':
        Loans.objects.filter(loans_id).delete()
        messages.success(request, 'deleted successfully')
        return redirect('loan')
    else:
        messages.error(request, 'not deleted')
        return redirect('loan')

def applicationsview(request):
    applications = Application.objects.all()
    dict = {'applications':applications}
    return render(request,'bims_app/application.html',dict)

# frontend views###

def homepageview(request):
    return render(request,'frontend/home.html')

def aboutpageview(request):
    return render(request,'frontend/about.html')