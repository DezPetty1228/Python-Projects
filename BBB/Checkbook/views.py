from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .models import Account, Transaction


# this function will render the home page when requested
def home(request):
    form = forms.TransactionForm(data=request.POST or None)  # Retrieve the Account Form
    # Checks if request method is POST
    if request.method == 'POST':
        pk = request.POST['account']  # if the form is submitted, retrieve which amount the user wants to view
        return balance(request, pk)  # call balance function to render that account's balance sheet
    content = {'form': form}  # pass content to the template in a dictionary
    # Adds content of form to page
    return render(request, 'checkbook/index.html', content)


# this function will render the Create New Account page when requested
def create_account(request):
    form = forms.AccountForm(data=request.POST or None)  # Retrieve the Account Form
    # Checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # Check to see if the submitted form is valid and if so, saves form
            form.save()  # Save New Account
            return redirect('index')  # returns user back to homepage
    # Pass content to the template in a dictionary
    content = {'form': form}  # Saves content to the template as a dictionary
    # Adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# this function will render the balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # retrieves the requested account using its primary key
    transactions = Transaction.Transaction.filter(account=pk)  # retrieves all the account transactions
    current_total = account.initial_deposit  # creates account total variable, starting with initial deposit
    table_contents = {}  # Create a dictionary into which transaction data will be placed
    for t in transactions:  # loop through transactions and determine which is a deposit and which is a withdrawal
        if t.type == 'Deposit':
            current_total += t.amount  # if deposit add amount to balance
            table_contents.update({t: current_total})  # Add transaction and total to the dictionary
        else:
            current_total -= t.amount  # if withdrawal subtract amount from balance
            table_contents.update({t: current_total})  # Add transaction and total to the dictionary
    # Pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# this function will render the transcripts page when requested
def transaction(request):
    form = forms.TransactionForm(data=request.POST or None)  # Retrieves the transaction form
    # Checks if requested method is post
    if request.method == 'POST':
        if form.is_valid():  # Check to see if form is valid if so saves the form
            pk = request.POST['account']  # Retrieves which amount the transaction was for
            form.save()  # Saves the Transaction Form
            return balance(request, pk)  # Renders balance of the accounts balance sheet
    # Pass content to the template in a dictionary
    content = {'form': form}
    # Adds content of the form page
    return render(request, 'checkbook/AddTransaction.html', content)
