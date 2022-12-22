try:
    blance=500
    my_num=613150013
    evc='y'
    while evc=='y':
        print("garaac *770# si aad uagshid evc_plus")
        evc1=input("soo gali evc\n")
        print(" ")
        if evc1== '*770#':
            account=input("account maleedahay yes or no\n") 
            print(" ")
            if account== 'n':
                account1=input("ma rabtaa in aad sameysatid account yes or no\n")
                if account1== 'y':
                    print(" ")
                    print("gali pin cusub")
                    print(" ")
                    while 'true':
                        pin = (input("soo gali 4 digit\n"))
                        print(" ")
                        if len (pin)!= 4:
                            print(" fadlan soo gali only 4 digit")
                            print(" ")
                        else :
                            password=open("evc.txt",'w') // file sameeso kuna qoro "evc.txt" wuxuu kuu keedina passwordka aad sameesatay.
                            password.write(str(pin))
                            password. close()
                            print(" ")
                            password1=(input("confirm password"))
                            if password1!=pin:
                                print(" ")
                                print("labadaada password isma laha please try again ")
                            else:
                                print(" hambalyo waxaad sameysatay account")
                                break
            
        
            elif account== 'y':
               
                    gali_pinkaaaga=input("gali pin_kaga") 
                    if len(gali_pinkaaaga)!=4:
                        print("passwordka aad galisay ma ahan mid jira") 
                        
                    else:
                        password= open ("evc.txt",'r')
                        pin1=password.readline()
                        password.close()
                        if gali_pinkaaaga!=pin1 :
                             print("pinka aad galisay ma ahan mid jira")
                      
                            
                        else:
                            print(" ")
                            print("EVCPLUS")
                            print(" ")
                            print("1.itus haraagaaga")
                            print("2.kaarka hadalka")
                            print("3.bixi biil")
                            print("4.uwareeji Evc_plus")
                            print("5.warbixin kooban")
                            print("6.salaam bank")
                            print("7.maareynta")
                            print("8.taaj")
                            print("9.bill payment")
                            print(" ")
                            users=int(input(" ")) 
                            print(" ")
                            def user1():
                                if users==1:
                                    print("[-EVCPLUS-] Haraagaga waa $",blance,sep="")
                            user1()   
                            def user2():
                                
                                if users==2:
                                    print("kaarka hadalka")
                                    print("1.ku shubo lacag\n2.ugu shub lacag\n3.ku shubo internet\n4.MIFI Package\n5.ugu shub qof kale(mmt)\n")
                                    two_evc=int(input(" "))
                                    if two_evc==1:
                                        lacagta=int (input("fadlan gali lacagta"))
                                        print("ma hubtaa inaad $",lacagta," ku shubtid undefined?\n")
                                        ma_hubta=int(input(" ""1.haa\n""2.maya\n"))
                                        if ma_hubta==1:
                                            lcg=lacagta
                                            summ1=blance-lcg
                                            
                                            print("wxad $",lcg," ugu shubtay ",my_num," haraagaga hada waa $",summ1,"\n",sep="")
                                        
                                    elif two_evc==2: 
                                        four=int (input("fadlan gali numberka\n"))
                                        three=int (input("fadlan gali lacagta\n"))
                                        print("ma hubtaa inaad ",three,"$ ugu shubtid",four)
                                        five=int(input("1.haa\n""2.maya\n"))
                                        if five==1:
                                            money=three
                                            summ3=blance-money
                                            print("$",money," ayaad ugu shubtay ",four," haraagaga waa ",summ3,sep="")  
                                    elif two_evc==3:
                                        print("fadlan dooro numberka aad ku shubeyso\n""1.maalinle\n""2.isbuucle\n""3.bille\n")
                                        maalin=int (input("mid dooro"))
                                        if maalin==1:
                                            codsi=float(input("gali lacagta"))
                                            print("ma hubtaa in inaad ku shubaneysid",codsi)
                                            gali=int(input("1.haa\n2.maya\n"))
                                            if gali==1:
                                                print("waxaad ku shubatay",codsi,"haraagaaga waa",codsi,"GB")
                                        elif isbuuc==2:
                                            codsi1=float(input("gali lacagta"))
                                            print("ma hubtaa in inaad ku shubaneysid",codsi1)
                                            gali1=int(input("1.haa\n2.maya\n"))
                                            if gali1==1:
                                                print("waxaad ku shubatay",codsi1,"haraagaaga waa",codsi1,"GB")
                                        elif bille==3:
                                            codsi2=float(input("gali lacagta"))
                                            print("ma hubtaa in inaad ku shubaneysid",codsi2,"GB")
                                            gali2=int(input("1.haa\n2.maya\n"))
                                            if gali==1:
                                                print("waxaad ku shubatay",codsi,"haraagaaga waa",codsi2,"GB")
                                        else:
                                            print("kuma jiro numbarka aad dooratay")
                                    elif two_evc==4: 
                                        mifi= int (input("1.ku shubo data MIFI"))
                                        mifi1=int (input("1.maalinle\n""2.isbuucle\n""3.bille\n"))
                                        if mifi1==1:
                                            bundle=int(input("fadlan dooro bundle ka\n""1.$1=2GB\n""2.$2=5GB\n"))
                                            if bundle==1:
                                                print("waxaad ku shubatay 2GB")
                                            elif bundle==2:
                                                 print("waxaad ku shubatay 5GB")
                                            else:
                                                print("numbarka aad dooratay ma ahan mid sax ah")
                                    
                                        elif mifi12==2:
                                            bundle2=int(input("fadlan dooro bundle ka\n""1.$1=2GB\n""2.$2=5GB\n"))
                                            if bundle2==1:
                                                print("waxaad ku shubatay 2GB")
                                            elif bundle==2:
                                                print("waxaad ku shubatay 5GB")
                                            else:
                                                print("numbarka aad dooratay ma ahan mid sax ah")
                  
                                        elif mifi13==3:
                                            bundle3=int(input("fadlan dooro bundle ka\n""1.$1=2GB\n""2.$2=5GB\n"))
                                            if bundle3==1:
                                                print("waxaad ku shubatay 2GB")
                                            elif bundle3==2:
                                                 print("waxaad ku shubatay 5GB")
                                            else:
                                                print("numbarka aad dooratay ma ahan mid sax ah")
                                    elif two_evc==5: 
                                        mmt=int(input("fadlan gali numberka aad ku shubeesid"))
                                        mmt1=int (input("fadlan gali lacagta"))
                                        print("waxaad ugu shubtay", mmt,"qiimo la eg",mmt1,"$", sep="")
                                    else:
                                        print("numbarka aad dooratay ma ahan mid jira")
                                
                                
                            user2()
                            
                            
                            def user3():
                                if users==3:
                                    print("bixi biil")
                                    paid=int(input("1.post paid\n2.ku iibso\n"))
                                    if paid==1:
                                        print("1.ogow biilka\n""2.bixi biil\n""3.ka bixi biil\n")
                                        dooro_number=int(input("dooro number\n"))
                                        if dooro_number==1:
                                            print("error occured,please try again later")
                                        elif dooro_number==2:
                                            number=int(input("fadlan gali lacgta"))
                                            print("ma hubtaa inaad bixisid biil lacgtiisu tahay $",number,"\n""1. haa\n""2.maya\n")
                                            number2= int (input("dooro"))
                                            if number2==1:
                                                print (" waxaad bixisay biil lacagtiisu la egtahay $",number, sep="")
                                            else:
                                                 print(" waad ka baxday")
                                        elif dooro_number==3:
                                            number3=int(input("fadlan gali mobelka\n"))
                                            number4=int(input("fadlan gali lacagta\n"))
                                            print("waxaad ka bixisay biilkaaga lacag dhan $",number4,"oo aad uga bixisay",number3)
                                            
                                        else:
                                            print("numberka aad dooratay ma ahan mid jira")
                   
                                    elif paid==2:
                                        fadlan=input("fadlan gali aqoonsiga ganacsiga")
                                        print(" partner doesnt exist(invalid)")
                                    else:
                                        print("numberka aad dooratay ma ahan mid saxan")
                            user3()    
                            def user4():
                                if users==4:
                                    print("uwareeji Evc_plus")
                                    num1=input("fadlan gali mobelka adigoo ka bilaabaya 61xxxxxxx:\n")
                                    if len (num1)!= 9:
                                        print(" fadlan soo gali only 9 digit")
                                    else :
                                        if num1[0]=='6' and num1[1]=='1':
                                            print(" ")
                                            lacag=float(input("fadlan gali lacgta\n"))
                                            if lacag<0:
                                                print('lacagta aad galisay ma ahan mida jira')
                                            else:
                                                outfile=open("lacagnum.txt",'w')
                                                line1 = outfile.write(str(num1+"\n"))
                                                line2 = outfile.write(str(lacag))
                                                outfile. close()
                                                print(" ")
                                                print("ma hubtaa inaad $" + str(format(lacag)) + " uwareejisid numberkaan ",num1, sep="")

                                                num3=int(input("1:haa\n2:maya\n"))
                                                if num3==1:
                                                    sub=blance-lacag
                                                    if blance<lacag:
                                                        print("haraagaga kuguma filna")

                                                    else:
                                                        print("$",lacag," ayaad u wareejisey numberkaan " + str(num1)+ " haraagaaga hada uwaa $",sub, sep="")


                                        else:
                                            print("kabilaaw 61")

                            user4()
                            def user5():
                                if users==5:
                                    print("war bixin kooban")
                                    last=int (input("1.last action\n""2.wareejintii udambeysay\n""3.iibsashadii udanbeysay\n""4.last 3 action\n"))
                                    if last==1:
                                        infile= open ("lacagnum.txt",'r')
                                        line1 = infile.readline()
                                        line2 = infile.readline()
                                        infile.close()
                                        print("$",line2," ayaad uwareejisay ",line1,",taarikh:18/12/2021",sep="")
                                        
                                        
                                        
                            user5()
                            def user7():
                                if users==7:
                                    print("maareynta")
                                    mareyn=int(input("1.bedel lambarka sirta ah\n""2.bedel luqada\n""3.wargalin mobile lumay\n""4.lacag xirasho\n""5.ucali lacag qaldantay\n""6.Enablemobilebanking\n"))
                                    if mareyn==1:
                                        print(" ")
                                        print("Fadlan Gali PIN-Kaaga cusub")
                                        print(" ")
                                        while 'true':
                                            pin = (input("soo gali 4 digit\n"))
                                            print(" ")
                                            if len (pin)!= 4:
                                                print(" fadlan soo gali only 4 digit")
                                                print(" ")
                                            else :
                                                password=open("evc.txt",'w')
                                                password.write(str(pin))
                                                password. close()
                                                print(" ")
                                                password1=(input("Hubi PIN_kaka cusub"))
                                                if password1!=pin:
                                                    print(" ")
                                                    print("labadaada password isma laha please try again ")
                                                else:
                                                    print(" hambalyo wad badalatay pinkaka")
                                                    break
                                    elif mareyn==2:
                                            luqad=int(input("fadlan dooro luqada\n""1.English\n""2.Somali\n"))
                                            if luqad==1:
                                                print("welcome english language")
                                            elif luqad==2:
                                                print("kusoo dhawaaw luqadaada hooyo")
                                            else:
                                                print("numberkaan ma ahan mid shaqeynaya")
                                
                            user7()
                            def user9():
                                
                                if users==9:
                                    print("bill payment")
                                    bill=int(input("1.itus haraaga bill ka\n""2.wada bixi bill ka\n""3.qeyb ka bixi bill ka\n"))
                                    if bill==1:
                                        bill1=int(input(" fadlan gali bill reference number\n"))
                                        print("some parameters are missing please check your request")
                                    elif bill==2: 
                                        bill2=int(input("fadlan gali bill reference number\n"))
                                        print("invalid input parameter")
                                    elif bill==3: 
                                        bill3=int(input("fadlan gali bill reference number\n"))
                                        print("invalid input parameter")
                                    else:
                                            print("numberka aad dooratay ma ahan mid jira")
                                
                                
                                
                                
                                
                                
                                
                                
                                
                            user9()
                            
                            
                        
               
            break
        elif evc!='*770#' :
                n=input("waxaad soo galisay waa qalad do you wanna try again y or n")
    
except Exception as e:
        print(e)