

def numbers(n,l):
    
    display = [["###",
                "# #",
                "# #",
                "# #",
                "###"],
                ["#  ",
                "#  ",
                "#  ",
                "#  ",
                "#  "],
                ["###",
                "  #",
                "###",
                "#  ",
                "###"],
                ["###",
                "  #",
                "###",
                "  #",
                "###"],
                ["# #",
                "# #",
                "###",
                "  #",
                "  #"],
                ["###",
                "#  ",
                "###",
                "  #",
                "###"],
                ["###",
                "#  ",
                "###",
                "# #",
                "###"],
                ["###",
                "  #",
                "  #",
                "  #",
                "  #"],
                ["###",
                "# #",
                "###",
                "# #",
                "###"],
                ["###",
                "# #",
                "###",
                "  #",
                "###"]]
    # print("len",len(display))
    # print("reng",len(display[0]))
    return display[n][l]
   


def display(num):
    try:
        
        assert  num.isalnum() and int(num) >=0
        
        for lin in range (5):
            reng = ""
            for n in num:
                n= int(n)
                reng += numbers(n,lin)
                reng += " "
            print(reng)
        
    except AssertionError:
        print("ingrese numero valido")

#print(numbers(1,3))
display("7185")