Sub StockMarket ()

Dim Ticker as string
Dim Yearly_Change as Double
Dim Open_value as Double
Dim Close_value as Double
Dim Percent_Change as Double
Dim Total as Double


Cells(1,9) = "Ticker"
Cells(1,10) = "Yearly Change"
Cells(1,11) = "Percent Change"
Cells(1,12) = "Total Stock Volume"

' Keep track of the locatoin for each ticker brand in the sumarry table
Dim Summary_Table_Row As Integer
Summary_Table_Row = 2

' Loop through all ticker'
Dim TotalRows as Long
TotalRows = Cells(Rows.Count, 1).End(xlUp).Row

Open_value = Cells(2,3)

For i = 2 to TotalRows

  ' Check if we are still within the same ticker, if it is not then...
    if Cells(i + 1, 1).Value <> Cells(i,1).Value Then

        ' Set the Brand name. Ticker is place holder 
        
        Ticker = Cells(i, 1)
        Total = Total + Cells( i, 7)
        
        'Set the yearly change, need to have a place holder to hold the value of initial value. 
        Close_value = Cells(i,6)
        Yearly_Change = Close_value - Open_value

        if  Open_value = 0 then
            Percent_Change = 0
        Else
            Percent_Change = Yearly_Change / Open_value * 100
        End if

        Range("I" & Summary_Table_Row).Value = Ticker

        Range("L" & Summary_Table_Row).Value = Total

        Range("J" & Summary_Table_Row).Value = Yearly_Change

        Range("K" & Summary_Table_Row).Value = (Percent_Change & "%")
 
        Total = 0
        Yearly_Change = 0
        Open_value = cells(i + 1, 3)

         If Range("J" & Summary_Table_Row).Value >= 0 Then
            Range("J" & Summary_Table_Row).Interior.ColorIndex = 4
         Else
            Range("J" & Summary_Table_Row).Interior.ColorIndex = 3
         End If 

        Summary_Table_Row = Summary_Table_Row + 1 

    Else 
       
        Total = Total + Cells(i, 7)


    End if 

next i 

End Sub