## Important Note
still maintenance because there is still an error due to update heroku from stack-18 to stack-20 where currently the code still can't be deployed to heroku
the web service can still be run manually, just download and run it via python on your pc

# MuhiqCov19Bot
this is place to save my ongoing project for humanity help world
and complete my study
https://mcov.herokuapp.com/

run app
```console
python app.py
```
open ngrok and write
```console
ngrok http 5000
```
then this code will be online

hook web from ngrok and open twilio then copy link to webhook and test app on your whatsapp
or we can host the app to heroku hosting

## HOW TO USE ONLINE
- deploy on heroku
- hook your heroku link to twilio
http://your_heroku_link/sms
- then whatsapp bot is online

## HOW TO USE THIS BOT ON PC 
Requirements  
- install Python 3.10.6
- install all requirements with command
```console
pip install requirements.txt
```
- run python webservice
```console
python app.py
```
- make webservice online on port 5000
```console
ngrok http 5000
```
- hook your ngrok link to twilio
http://your_ngrok_link/sms
- then whatsapp bot is online


### ALL COMMAND BOT 
- Menu 1-9
 1. Situasi COVID-19 Indonesia 
 2. Apa itu COVID-19 ? 
 3. Apa gejala COVID-19 ? 
 4. Cara melindungi diri dari COVID-19 
 5. Cara melindungi orang lain dari COVID-19? 
 6. Penggunaan Masker kain? 
 7. Rumah sakit Rujukan COVID-19 
 8. Edukasi test COVID-19
 9. SKRINING Mandiri COVID-19
 10. Pantau Vaksinasi

- text name province like Jawa Tengah to show case covid in your area and give you hospital covid info
- NEWS to show you realtime news about covid

### DATA 
all data is from official website covid like kawalcovid or covid19.go.id

 ## MIT License
 
 ```
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

Author : @muhiqsimui
