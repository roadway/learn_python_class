# -*- coding: utf-8 -*-
Class cFish:
    Sub Swim() 
        print("海阔凭鱼跃")
    End Sub
End Class

Class cBird:
    Sub Fly() 
        print("天高任鸟飞")
    End Sub
End Class

Class Animal: 
    Dim Fish 
    Dim Bird 
     
    Private Sub Class_Initialize() 
        Set Fish = New cFish 
        Set Bird = New cBird 
    End Sub
     
    Private Sub Class_Terminate() 
        Set Fish = Nothing
        Set Bird = Nothing
    End Sub
End Class

Dim objAnimal 
Set objAnimal = New Animal 
objAnimal.Fish.Swim() 
objAnimal.Bird.Fly() 
Set objAnimal = Nothing