guestList = ["John Petrucci","Andy James","Paul Gilbert"];
for person in guestList:
    print("Dear "+ person + ", I would like to invit to have a dinner comingi firday night.")

absencePerson = guestList[1];


print(absencePerson);

guestList[1]="John Mayer";
guestList.insert(0,"Mike Portnoy");
guestList.insert(3,"Taylor Swift");
guestList.append("50 cent");

guestList.pop();
guestList.pop();
guestList.pop();
guestList.pop();

del guestList[:];
print(guestList);