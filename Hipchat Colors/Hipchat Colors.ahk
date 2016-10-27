Random_Choice(Choices*){
	Random,Index,1,% Choices.MaxIndex()
	Return,Choices[Index]
}


^!t:: ;<-- ctrl-alt-t activates the event
lastword = init
send {#}%lastword%{enter}
Loop, 30
{
    newword := Random_Choice("ff0000", "00FF00", "0000ff", "008000", "00FFFF", "008080", "ECFF33", "F633FF", "FF3393", "FFAA00", "9B00FF", "B9FF00", "FF6100") ;
    Send, {s}{/}%lastword%{/}%newword%{enter} ;
    lastword := newword
    Sleep, 200
}
Return ;<-- end of routine


