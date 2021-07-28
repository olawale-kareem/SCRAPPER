from user import User
from url import Url
from soup import Soup
from processed import WordRefine
from plots import Plot


   

def operation_choice():

    new_user_website = User('new_user').user_operation()
    if new_user_website == False:
        User('new_user').toggle_off()
    else:
        server_response  = Url(new_user_website).url_processing()
        if server_response == False:
            print('Status:404 Connection Error, Enter the format (https://wwww.<domain_name>.com) or (http://wwww.<domain_name>.com) ')
            operation_choice()
        else:
            site_body = Soup(server_response).get_url()
            refined_word = WordRefine(site_body).processed_word()
            keys, values , top_word = WordRefine(site_body).most_common_words(site_body,refined_word,10)
            print(f'The top word is: {top_word}')
            plotter = Plot(keys, values)
            plotter.plot_bar_chart()
            plotter.plot_pie_chart()
            
            operation_choice()
    
   
    




