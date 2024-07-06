
def main(concatenated_string, integration_dir, 
         description='',
         delimiter=";"):
    print('____________________')
    link_label = integration_dir+': '+description
    url_hyperlink = '=HYPERLINK("'+concatenated_string+'"'+delimiter+'"'+link_label+'")'
    print(url_hyperlink)
    print('____________________')

if __name__ == "__main__":
    concatenated_string='https://adrianartacho.github.io/SALTA/?file=exp0b_SALTA.csv'
    integration_dir="exp0b_SALTA"
    description_text="Unaggregated"
    main(concatenated_string, integration_dir, description=description_text)

