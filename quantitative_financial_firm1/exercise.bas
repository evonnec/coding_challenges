Option Explicit

Sub task()

Dim Trades_FilePath, BlueChips_FilePath As String       'declare file paths

Trades_FilePath = Range("Trades_FilePath")              'range to take input of where filepaths exist
BlueChips_FilePath = Range("BlueChips_FilePath")

Range("num_of_orders").ClearContents                    'clear out old data
Range("shs_traded").ClearContents
Range("sum_CHF").ClearContents
Range("all_fees").ClearContents

Dim FileNum As Long
FileNum = FreeFile()                                    'bring in text or csv files as freefiles, declare as such

Dim trade_line As Variant, order_counter As Long        'dim each trade line, dim order counter

Dim stringdf, row_string As String                      'dim dataframe of string, each row as string    'for text
Dim BC_line As Variant                                  'dim each blue chip line

Dim trades_list As String
Dim row_counter

Dim shares_sum, per_trade_CHF, total_CHF, fixed_fees, vari_fees, total_vari_fees, all_fees As Double 'set up some variables as double
'variable descriptions:
'total number of shares traded, each trade's total CHF, total cumulative CHF, fixed fee of .01 CHF per trade
'variable fee per trade, total variable fees, both fixed and variable fees combined

shares_sum = 0                                          'set them to zero
total_CHF = 0
fixed_fees = 0
'vari_fees = 0                                          'needs to be reset each time, declared in code below to be reset
total_vari_fees = 0

Dim dOrderIDs As New Scripting.Dictionary               'make a dictionary for unique order IDs
Set dOrderIDs = CreateObject("Scripting.Dictionary")

'Dim dPerTradeCHF As New Scripting.Dictionary           'make a dictionary for unique CHF  'unused
'Set dPerTradeCHF = CreateObject("Scripting.Dictionary")

Dim dBlueChips As New Scripting.Dictionary              'make a dictionary of blue chip Swiss stocks
Set dBlueChips = CreateObject("Scripting.Dictionary")


Open BlueChips_FilePath For Input As #FileNum           'open Blue Chip file to identify and dictionary the Blue Chips
    Line Input #FileNum, row_string                     'skip header
    
    While Not EOF(FileNum)
        Line Input #FileNum, row_string                 'line by line stored into row_string variable
        stringdf = stringdf & row_string & vbCrLf       'accumulated lines put into stringdf variable
        BC_line = Split(row_string, ",")
        If Not dBlueChips.Exists(BC_line(0)) Then       'if it does not exist in blue chip dictionary, add blue chip stock name/sym to dictionary. (0) indicates first indexed element
            dBlueChips.Add BC_line(0), BC_line(0)       'generally, it would be prudent to have the code check if the stock listed is indeed a Blue Chip by checking the 4th column for TRUE, did not do that here as it wasn't needed
        End If
    Wend
        
Close #FileNum                                          'close BC file

stringdf = vbNullString                                 'reset text variables to null, possibly unnecessary
row_string = vbNullString
BC_line = vbNullString


Open Trades_FilePath For Input As #FileNum              'open trades file
    Line Input #FileNum, row_string                     'skip header row
    
    While Not EOF(FileNum)                              'alternative: Do Until EOF(FileNum)
        Line Input #FileNum, row_string                 'take line by line and store into row_string
        stringdf = stringdf & row_string & vbCrLf       'accumulated row_string lines are put into stringdf
        
        trade_line = Split(row_string, ",")             'split the array to take each field by indexing the array
        
        If Not dOrderIDs.Exists(trade_line(2)) Then     'add unique order IDs to dictionary. essentially, if it doesn't exist, add it.
            dOrderIDs.Add trade_line(2), trade_line(2)
        End If
        
        shares_sum = shares_sum + trade_line(3)         'sum the total shares traded
        
        per_trade_CHF = trade_line(3) * trade_line(4)   'sum the total CHF per trade
        total_CHF = total_CHF + per_trade_CHF           'sum total notional CHF traded
        
        vari_fees = 0                                   'per trade variable fees - set it back to zero for each line
        If dBlueChips.Exists(trade_line(0)) Then        'if trade_line symbol exists in Blue Chips dictionary
            vari_fees = per_trade_CHF * 0.0001          'give it per trade fees of 1 bp for Blue Chips
        Else                                            'else
'            If 0.01 + per_trade_CHF * 0.0002 < 1 Then       'if 2 bps charge is less than 1 CHF
'                vari_fees = 1                               'give it per trade fees of 1 CHF
'            Else                                            'else
'                vari_fees = per_trade_CHF * 0.0002          'give it 2 bps charge per trade
'            End If                                          'so this didn't work for non-blue chips as it needs to sumif across order IDs, commented section out.
        End If                                               'don't know how to handle sumifs within/across VBA dictionaries, so handled it below.
        total_vari_fees = total_vari_fees + vari_fees   'total fees = add per trade variable fees and sum them
    
    Wend                                                'alternative: Loop
    
Close #FileNum                                          'close file
    
stringdf = vbNullString                                 'reset text variables back to null
row_string = vbNullString
trade_line = vbNullString



'i imagine sumif across dictionaries exists easily in python
'handle sumifs across a dictionary in free file in VBA would be cleaner

row_counter = 0

With Application
    .ScreenUpdating = False
    .Calculation = xlCalculationManual

    Open Trades_FilePath For Input As #FileNum              'open trades file
    '    trades_list = Input$(LOF(1), 1)                    'this populates strange, threw it out
        Line Input #FileNum, row_string                     'skip header row
    
        While Not EOF(FileNum)                              'alternative: Do Until EOF(FileNum)
            Line Input #FileNum, row_string                 'take line by line and store into row_string
            stringdf = stringdf & row_string & vbCrLf       'accumulated row_string lines are put into stringdf
    
            trade_line = Split(row_string, ",")             'split the array to take each field by indexing the array
            
            If Not dBlueChips.Exists(trade_line(0)) Then    'look at non Blue Chips here only to determine their variable costs
                Range("scratch").Offset(row_counter, 0) = trade_line(0) 'there are 7 fields, use array index to populate these
                Range("scratch").Offset(row_counter, 1) = trade_line(1)
                Range("scratch").Offset(row_counter, 2) = trade_line(2)
                Range("scratch").Offset(row_counter, 3) = trade_line(3)
                Range("scratch").Offset(row_counter, 4) = trade_line(4)
                Range("scratch").Offset(row_counter, 5) = trade_line(5)
                Range("scratch").Offset(row_counter, 6) = trade_line(6)
                Range("scratch").Offset(row_counter, 7) = trade_line(3) * trade_line(4) 'per trade CHF amt
                Range("scratch").Offset(row_counter, 8).FormulaR1C1 = _
                    "=IF(SUMIF(C[-6],RC[-6],C[-1])*0.0002+0.01<1,1,0.0002*RC[-1])"
                        'sum if per order CHF: if 2 bps charge on CHF amt per order plus 0.01 - is less than 1 CHF, give it 1 CHF,
                        'otherwise charge 2 bps on CHF amt for entire order's CHF amt executed
                        'a row needs to be deleted to avoid duplication
                row_counter = row_counter + 1
            End If
        Wend
    Close #FileNum

    .Calculation = xlCalculationAutomatic
    .ScreenUpdating = True
End With


'after sheet calculates, sum variable costs for non Blue Chips, add it to existing variable fees total/sum
    row_counter = 0
    Do While Range("scratch").Offset(row_counter, 0) <> vbNullString
    
        total_vari_fees = total_vari_fees + Range("scratch").Offset(row_counter, 8).Value
        row_counter = row_counter + 1

    Loop
    
'clear out scratch work
    Range(Range("scratch"), Range("scratch").Offset(0, 8)).Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.ClearContents
    Cells(4, 2).Activate
    
'set some variables up with their appropriate numbers
    order_counter = dOrderIDs.Count
    fixed_fees = 0.01 * order_counter                         'fixed fees
    all_fees = fixed_fees + total_vari_fees             'all fees include variable fees per trade
    
'show a pop up with results
    MsgBox ("order count: " & Format(order_counter, "#,###") & vbCrLf & _
            "shares total: " & Format(shares_sum, "#,###") & vbCrLf & _
            "total CHF traded: " & Format(total_CHF, "#,###.####") & vbCrLf & _
            "total trading fees: " & Format(all_fees, "#,###.####"))
    
'print on sheet with results
    Range("num_of_orders") = Format(order_counter, "#,###")
    Range("shs_traded") = Format(shares_sum, "#,###")
    Range("sum_CHF") = Format(total_CHF, "#,###.####")
    Range("all_fees") = Format(all_fees, "#,###.####")
    

Set dOrderIDs = Nothing                                 'kill dictionaries
Set dBlueChips = Nothing

End Sub
