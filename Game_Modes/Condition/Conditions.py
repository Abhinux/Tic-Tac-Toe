def Comp_turn1():
    #first turn check
    if B5["text"]==" ":
        B5["text"]="X"
    #Offensive check
    elif (B2["text"]==B3["text"]=="X" or B7["text"]==B4['text']=="X" or B9["text"]==B5["text"]=="X") and B1["text"]==" ":
        B1["text"]="X"
    elif (B1["text"]==B3["text"]=="X" or B5["text"]==B8['text']=="X") and B2["text"]==" ":
        B2["text"]="X"
    elif (B1["text"]==B2["text"]=="X" or B9["text"]==B6['text']=="X" or B7["text"]==B5["text"]=="X") and B3["text"]==" ":
        B3["text"]="X"
    elif (B1["text"]==B7["text"]=="X" or B6["text"]==B5['text']=="X") and B4["text"]==" ":
        B4["text"]="X"
    elif (B3["text"]==B9["text"]=="X" or B4["text"]==B5['text']=="X") and B6["text"]==" ":
        B6["text"]="X"
    elif (B1["text"]==B4["text"]=="X" or B9["text"]==B8['text']=="X" or B3["text"]==B5["text"]=="X") and B7["text"]==" ":
        B7["text"]="X"
    elif (B7["text"]==B9["text"]=="X" or B2["text"]==B5['text']=="X") and B8["text"]==" ":
        B8["text"]="X"
    elif (B1["text"]==B5["text"]=="X" or B3["text"]==B6['text']=="X" or B7["text"]==B8["text"]=="X") and B9["text"]==" ":
        B9["text"]="X"
    #Defensive check
    elif (B2["text"]==B3["text"]=="O" or B7["text"]==B4['text']=="O" or B9["text"]==B5["text"]=="O") and B1["text"]==" ":
        B1["text"]="X"
    elif (B1["text"]==B3["text"]=="O" or B5["text"]==B8['text']=="O") and B2["text"]==" ":
        B2["text"]="X"
    elif (B1["text"]==B2["text"]=="O" or B9["text"]==B6['text']=="O" or B7["text"]==B5["text"]=="O") and B3["text"]==" ":
        B3["text"]="X"
    elif (B1["text"]==B7["text"]=="O" or B6["text"]==B5['text']=="O") and B4["text"]==" ":
        B4["text"]="X"
    elif (B3["text"]==B9["text"]=="O" or B4["text"]==B5['text']=="O") and B6["text"]==" ":
        B6["text"]="X"
    elif (B1["text"]==B4["text"]=="O" or B9["text"]==B8['text']=="O" or B3["text"]==B5["text"]=="O") and B7["text"]==" ":
        B7["text"]="X"
    elif (B7["text"]==B9["text"]=="O" or B2["text"]==B5['text']=="O") and B8["text"]==" ":
        B8["text"]="X"
    elif (B1["text"]==B5["text"]=="O" or B3["text"]==B6['text']=="O" or B7["text"]==B8["text"]=="O") and B9["text"]==" ":
        B9["text"]="X" 
    else:
        if B5["text"]=="X":
            if B7["text"]==" ":
                B7["text"]="X"
            elif B1["text"]==" ":
                B1["text"]="X"
            elif B9["text"]==" ":
                B9["text"]="X"
            elif B3["text"]==" ":
                B3["text"]="X"
            elif B8["text"]==" ":
                B8["text"]="X"
        else:
            if B4["text"]==" ":
                B4["text"]="X"
            elif B6["text"]==" ":
                B6["text"]="X"
            elif B2["text"]==" ":
                B2["text"]="X"
            elif B7["text"]==" ":
                B7["text"]="X"
            elif B1["text"]==" ":
                B1["text"]="X"
            elif B9["text"]==" ":
                B9["text"]="X"
            elif B3["text"]==" ":
                B3["text"]="X"
            elif B8["text"]==" ":
                B8["text"]="X"

