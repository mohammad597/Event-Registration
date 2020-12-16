##########
# EVENT REGISTRATION  Task
# author : Mohammad Saleem
# email : mohammadsaleem597@gmail.com
##########

class Registrant:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class ContactsList(Registrant):
    pass


class LeadList(Registrant):
    pass


contacts_list = []
lead_list = []

# ADD Contacts Provided
contacts_list.append(ContactsList('Alice Brown', None, 1231112223))
contacts_list.append(ContactsList('Bob Crown', 'bob@crowns.com', None))
contacts_list.append(ContactsList('Carlos Drew', 'carl@drewess.com', 3453334445))
contacts_list.append(ContactsList('Doug Emerty', None, 4564445556))
contacts_list.append(ContactsList('Egan Fair', 'eg@fairness.com', 5675556667))

# ADD Leads Provided
lead_list.append(LeadList(None, 'kevin@keith.com', None))
lead_list.append(LeadList('Lucy', 'lucy@liu.com', 3210001112))
lead_list.append(LeadList('Mary Middle', 'mary@middle.com', 3331112223))
lead_list.append(LeadList(None, None, 4442223334))
lead_list.append(LeadList(None, 'ole@olson.com', None))

first_register = {
    "registrant":
        {
            "name": "Lucy Liu",
            "email": "lucy@liu.com",
            "phone": None,
        }
}

second_register = {
    "registrant":
        {
            "name": "Doug",
            "email": "doug@emmy.com",
            "phone": "4564445556",
        }
}

third_register = {
    "registrant":
        {
            "name": "Uma Thurman",
            "email": "uma@thurs.com",
            "phone": None,
        }
}


# Method To Check the New Registrant

def check_registrant(new_register):
    registrant = new_register['registrant']
    name = registrant['name']
    email = registrant['email']
    phone = registrant['phone']

    # Firstly Check From Contacts List
    for contact in contacts_list:

        # Email Validate
        if contact.email and email and email == contact.email:

            # update phone number if equal to None and registered phone number is valid
            if not contact.phone and phone and len(phone) == 10:

                phone_number = int(phone)
                if str(phone_number).isdigit():
                    contact.__setattr__('phone', phone_number)
                    return
        elif contact.phone and phone and len(phone) == 10 and contact.phone == int(phone):

            # update email if equal to None and registered email is not None
            if not contact.email:
                contact.__setattr__('email', email)
                return

    # Secondly Check From Lead List
    lead_updated = False
    lead_index = None
    lead_item = False
    for lead in lead_list:
        if lead.email and email and lead.email == email:
            lead_updated = True
            lead_index = lead_list.index(lead)
            if name:
                l_name = name
            else:
                l_name = lead.name
            if phone:
                l_phone = phone
            else:
                l_phone = lead.phone
            if email:
                l_email = email
            else:
                l_email = lead.email
            lead_item = LeadList(l_name, l_email, l_phone)

            # update lead name
            if name:
                lead.__setattr__('name', name)

            # update lead phone if None
            if not lead.phone and phone and len(phone) == 10:
                lead.__setattr__('phone', int(phone))
        elif lead.phone and phone and len(phone) == 10 and lead.phone == int(phone):
            lead_updated = True
            lead_index = lead_list.index(lead)
            lead_item = lead
            if not lead.name:
                lead.__setattr__('name', name)
            if not lead.email and email:
                lead.__setattr__('email', email)
    if lead_updated and lead_item and lead_index:
        lead_list.pop(lead_index)
        new_contact = ContactsList(lead_item.name, lead_item.email, lead_item.phone)
        contacts_list.append(new_contact)
        return
    else:
        new_contact = ContactsList(name, email, phone)
        contacts_list.append(new_contact)


check_registrant(first_register)
check_registrant(second_register)
check_registrant(third_register)

####### Show Results
#
## LeadList
print("New Lead List")
for lead in lead_list:
    print("Lead Item : ", lead.name, " / ", lead.email, " / ", lead.phone)

print("New Contacts List")
## ContactsList
for contact in contacts_list:
    print("Contact Item : ", contact.name, " / ", contact.email, " / ", contact.phone)

