from flask import Flask


app= Flask(__name__)

@app.route('/cToFConvertter')
def cToFConvertter():
    
    while True:
                
        cTemp = input("Please enter C degree: ")
        if cTemp:
            fTemp = round(9* float(cTemp)/5 + 32, 1)

            
            return (f'{cTemp}C is converted to {fTemp}F')
        
            break
        else:
            print('cTemp is empty')
            continue
  




def main():
    cToFConvertter ()
    app.run() 


if __name__ == "__main__":
    main()
    