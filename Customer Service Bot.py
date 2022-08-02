def greeting():
    name = input('Thank you for contacting Tiny Space! May I have your name? ')
    print(f'Thanks, {name}!')
    return

def select_category():
    category = input('What are you inquiring about today? Enter "1" for Store location and hours. "2" for Order Status,' \
        '"3" for Issue with order, "4" for Design Services, and "5" for other. ')
    #Create a list of functions that can be created later for each category 
    if category == '1':
        store_location_hours()
        return

    if category == '2':
        order_status()
        return

    if category == '3':
        order_issue()
        return

    if category == '4':
        design_services()
        return

    if category == '5':
        other()
        return
#All you have to do now is to define each function
def store_location_hours():
    hours = "Monday - Saturday 10 a.m. - 6 p.m"
    location = '2300 Riverdale Lane, Boston, MA 02101'
    print(f'Tiny space is located at {location}. The store is open from {hours}.')
    addition_comments = input('May I help you with anything else [yes/no] ').lower()
    if addition_comments == 'yes':
        select_category()
    elif addition_comments == 'no':
        print('Thank you for contacting Tiny Space!')
    return

def order_status():
    print("Sure, I can help you with that.")
    name_on_order = input('Elliot: May I have the full name on the order. ')
    order_number = input('Elliot: May I have the order number. ')
    transfer_Elliot() #this is a function that will be defined later
    return

def order_issue():
    print("Chrissa: I'm sorry that you're experiencing issues with your order.")
    name_on_order = input('Chrissa: May I have the full name on the order. ')
    order_number = input('Chrissa: May I have the order number. ')
    issue = input('Chrissa: Could you please describe the issue with your product. ')
    transfer_Chrissa() #this is a function that will be defined later
    return

def design_services():
    print("Ramon: I can definetly help you with your design questions! ")
    transfer_Ramon()
    return

def other():
    transfer_Trinity()
    return

def transfer_Elliot():
    print('Elliot: Thank you, I will check the status of your order now.')
    return

def transfer_Chrissa():
    print('Chrissa: Thank you, I will look into your issue right now.')

def transfer_Ramon():
    design_question = input('Ramon: Hello, what kind of questions do you have? ')
    return

def transfer_Trinity():
    other_inquiry = input("Trinity: Please describe to me how I may be of assistance. ")
    return

greeting()
select_category()
