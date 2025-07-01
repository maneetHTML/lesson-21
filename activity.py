import tkinter as tk
import requests
url="https://uselessfacts.jsph.pl/random.json?language=en"
def get_random_technology_fact():
    try:
        response = requests.get(url)
        if response.status_code==200:
            fact_data=response.json()
            fact_text.set(f"Did you know?\n\n{fact_data['text']}")
        else:
            fact_text.set('Failed to fetch fact.')
    except Exception as e:
        fact_text.set(f"Error:{str(e)}")
root =tk.Tk()
root.title('Random fact')
root.geometry('500x300')
fact_text=tk.StringVar()
fact_label=tk.Label(root,textvariable=fact_text,wraplength=450,justify='left',font=('Arial',12))
fact_label.pack(pady=20)
fetch_button=tk.Button(root,text='Get Fact',command=get_random_technology_fact,font=('Arial',12,'bold'))
fetch_button.pack(pady=10)
quit_button=tk.Button(root,text='Quit',command=root.quit,font=('Arial',12))
quit_button.pack(pady=5)
root.mainloop()