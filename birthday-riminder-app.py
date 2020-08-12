dict={}
while True:
     print("**********BIRTHDAY RIMINDER**********")
     print("1.Show Birthday Riminder")
     print("2.Add to  Brithday List")
     print("3. Exit")
     choice=int(input("Enter the choice"))
     if choice==1:
         if len(dict.keys())==0:
             print("nothing to show")
         else:
             name=input("Enter name to looking for a BIRTHDAY:")
             birthday=dict.get(name,"No data found")
             print(birthday)
     elif choice==2:
          name=input("Enter friends name:")
          date= input("Enter  BIRTHDAT:")
          dict[name]=date

          print("BIRTHDAY Added secsessfully")
     elif choice==3:
         break
     else:
         print("please chooose a valid no.")
