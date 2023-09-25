"""
navhash is This program is a 32-bit encryption program and that yes unhackable hash :)
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import hashlib
class Main_navhash:
    def __init__(self):
        pass
        


    def mdnav(self,string): #baraye custom kardan str daryafti
        str=string
        if len(str)<2:
            str=";l'[DJI%$xlpw s]"+str*13+"4rsfc"
        if len(str)<3:
            str="bwqp$ dJID@o[]"+str*9+"wq dv9-"
        if len(str)<4:
            str="<nHGDYdg ;'[ddft>"+str*7+"`e 3ffu;"
        if len(str)<5:
            str="q45Kxo,h$%"+str*5+"lkqw231cv  .lj"
        if len(str)<6:
            str="089-_(&hdu)"+str*3+"'sd''\jvbe@&"

        def calculate_md5(input_string): #inja vorodi ro be md5 hash mikonam ta moshkel yeksan bodan ord bartaraf beshe!
            md5_hash = hashlib.md5()
            md5_hash.update(input_string.encode('utf-8'))
            return md5_hash.hexdigest()

        
        str = calculate_md5(str)


        list_str=list(str)
        #baraye tabdil tak betak eleman haye list be code ord batad az map() estefade konim be list tabdil mikonim chon garare estefade bokonim.
        code_str=list(map(ord,list_str))
        # print(code_str)
            
        sum_code_str=sum(code_str)
        
        n_list=[]
        for x in range((sum_code_str*len(str))//(len(str)*2)):  #yek range adad custom shode (shakhsi)
            #inja yek list khali ijad kardim va dakheli in list khali
            #item haye list str ke karbar vared kardaro ba moadeleye
            #amalyat= x%len(str) baes shodim jame ord haye item haye list_str
            #har chegadram ke bishtar bashe tagsim barlen(str)
            #bagi mandash be tedad item hate list str khahad bod
            #va ino be index list midim ta dartol amaliyat FOR
            #item haye str be sorat davarani be n_list ma ezafe beshe.
            #base code ine vali inja sar x balahayi avordim ta yekam custom beshe :)
            amaliyat=(((((x)*len(str))**4.5)/2.3)+0.5)%len(str)
            amaliyat=int(amaliyat)
            n_list.append(list_str[amaliyat])
        
        
        #hrof be dast amade ra ord mikonim
        code_n_list=list(map(ord,n_list))
        
        #dobare custom mikoim ta adad haye bozorgtari bedast biyad
        code_n_list2=[] 
        for index in range(len(code_n_list)):
            code_n_list2.append(int(code_n_list[index]+(index**3.8)))
        
        def hexx(n_list2): #in tabe tabdil be adad gabel tabdil be hex mikone
            return n_list2%16

        hex_n_list2=list(map(hexx,code_n_list2))  #az tabe bala estefade mikonim
        
        list_navhash=[]   #adad ro ash mikonim 
        for item in hex_n_list2:
            list_navhash.append((hex(item))[2:])
        str_navhash="".join(list_navhash)   #be str tabdil mikonim va boom!!!
        
        
        str_navhash2=str_navhash[:int(len(str_navhash)/10)]
        str_navhash2=str_navhash2[5:10]+str_navhash[-10:-20]+str_navhash2[:int(len(str_navhash)/11)]
        str_navhash2=str_navhash2[-10:]+str_navhash+str_navhash2[:10]
        str_navhash2=str_navhash2[20:52]
        
        
        return str_navhash2




passwd=Main_navhash()

# input_string=input("give me Password: ")
# # num=input_how_many=int(input("How many characters do you want?: "))
# n=passwd.mdnav(input_string)
# print("your strong Password is :",n)
# # print("Password with the number of characters you want! :",n[:num])

class navhas(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            "give me passwd: ",
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            "NavHash Generator",
            on_press=self.generator,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


     
     
    def generator(self,widget):
        n=passwd.mdnav(self.name_input.value)

                
        self.main_window.info_dialog("Congratulations, you have joined NavHash",
            f"your Hash is : {n} ")



    
def main():
    return navhas()
