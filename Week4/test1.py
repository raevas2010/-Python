for i in range(0, len(data)):    
    word = data.iloc[i]

    if word["flag"] == True:
        words_in_line = data[(data["Y_a"] > word["Y_o"]) & (data["Y_c"] < word["Y_o"])].sort_values(['X_o'], ascending=[True])
        data.loc[list(words_in_line.index), "flag"] = False
        bbox = words_in_line.iloc[[0]]
        
        if len (words_in_line) > 1:
            margin_word = [0]            
            for j in range(1, len(words_in_line)):
                margin_word.append(max(words_in_line.iloc[j]["X_a"], words_in_line.iloc[j]["X_b"]) - 
                                   min(words_in_line.iloc[j - 1]["X_c"], words_in_line.iloc[j - 1]["X_d"]))    
                
            for j in range(1, len(words_in_line)):
                
                bbox = words_in_line.iloc[[j - 1]]
                
                if (margin_word[j] < Margin_Sens * words_in_line.iloc[j - 1]["symbol_width"]):                       
                    
                    bbox.at[bbox.index[0], 'word'] = bbox.at[bbox.index[0], 'word'] + ' ' + words_in_line.iloc[j]["word"]
                    bbox.at[bbox.index[0], 'X_a'] = min(bbox.at[bbox.index[0], 'X_a'], words_in_line.iloc[j]["X_a"])
                    bbox.at[bbox.index[0], 'X_c'] = max(bbox.at[bbox.index[0], 'X_c'], words_in_line.iloc[j]["X_c"])
                    bbox.at[bbox.index[0], 'Y_a'] = max(bbox.at[bbox.index[0], 'Y_a'], words_in_line.iloc[j]["Y_a"])
                    bbox.at[bbox.index[0], 'Y_c'] = min(bbox.at[bbox.index[0], 'Y_c'], words_in_line.iloc[j]["Y_c"])                                
                    
                    Boxes.update({number_box: bbox.to_dict('records')})                   
                                                                                      
                else:
                    bbox = words_in_line.iloc[[j]]
                    
                number_box += 1 
                    
               
            
        else:
            Boxes.update({number_box: bbox.to_dict('records')})
            number_box +=1
            #ass
            
        Boxes.update({number_box: bbox.to_dict('records')})       
        number_box +=1
    else:
        continue

#gaps_X = [x for range(3)]
                                                                   
                    
         