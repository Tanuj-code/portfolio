import streamlit as st
import smtplib as s
import os
import pandas as pd
import numpy as np
import time
from streamlit_option_menu import option_menu
st.set_page_config(
    page_title="Tanuj Choudhary",
    page_icon="fire",
    
    
)
st.header("Tanuj Choudhary")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown("""---""")
with st.sidebar: 
    ch=option_menu("Tanuj", ['Home', 'About Me', 'Experience', 'Projects', 'Contact Me'], 
            icons=['house', 'book', 'list-task', 'gear', 'envelope'], menu_icon="cast", default_index=0)    
if(ch=="Home"):
        st.write("### Home ", unsafe_allow_html=True)
        with st.expander("View Introduction"):
            st.markdown(' I am a <b> Computer Science Engineering </b> undergrad majoring in <b> Artificial Intelligence </b>, currently in my pre-final year of graduation. I have a strong interest in both programming and development. I have done projects related to Web and Mobile development as well as Machine learning, IoT and computer vision. I constantly look to improve my skills and devise new ways of solving problems through technology using my skillset and knowledge. <br> I have talked about my skills and projects in the following sections. I also have a strong interest in <b> Competitive programming </b>. I participate in coding contests on <b> Codechef </b> and <b> Codeforces </b> frequently. I strated competitive programming in January 2023 and in a matter of weeks I improved exponentially and was able to acheive milestones on these platforms in a quick fashion. My latest stats are: <br> <b> Codechef: </b>3 :star: (div 2) <br> <b> Codeforces: </b><b> Pupil </b> .<br> However I have a long way to go ahead and improve myself in this "mental sport". <br>', unsafe_allow_html=True)
            st.markdown(' Being a software student, I have till now explored various domains in the feild of computer science and have learnt a lot. Each of them will be discussed in this section and the projects developed through them are mentioned in a following section named <b> "Projects" which you must visit. </b> For convenience I shall be mapping my proficiency in each tech I know and have used on a scale of 10 . ', unsafe_allow_html=True)
        st.markdown("##### Programming Languages", unsafe_allow_html=True)
        oc=st.selectbox("", ("Bar Chart", "Line Chart", "Area Chart"))
        chart_data = pd.DataFrame(
        {
            "Proficiency":[10, 10, 9, 9, 8, 8],
            "Language":["C", "C++", "Java", "Python", "JavaScript", "TypeScript"]

            
        })
        if(oc=="Bar Chart"):
            st.bar_chart(chart_data, x="Language", y="Proficiency")

        elif(oc=="Line Chart"):
            st.line_chart(chart_data, x="Language", y="Proficiency")

        elif(oc=="Area Chart"):
            st.area_chart(chart_data, x="Language", y="Proficiency")
        st.markdown("##### Frameworks and other tools", unsafe_allow_html=True)
        co=st.selectbox("", ("MongoDB", "ExpressJs", "NodeJs", "ReactJS", "Tkinter", "Android Studio", "PyWeb", "Arduino", "Git", "Github", "Streamlit", "Heroku", "Linux", "Shell Scripting", "Firebase", "SQL", "NoSQL", "SQLite", "Wordpress", "Data Structures and Algorithms", "Jupyter", "HTML", "CSS", "Visual Studio", "PyCharm", "Sublime", "TailwindCSS", "Bootstrap", "Sklearn"))
        if(co=="MongoDB" or co=="ReactJS" or co=="NodeJs" or co=="StreamLit" or co=="Heroku" or co=="Streamlit" or co=="Sklearn"):
            st.info(co+": 8 out of 10")
        elif(co=="Tkinter" or co=="PyWeb" or co=="Android Studio" or co=="Firebase" or co=="SQLite" or co=="NoSQL" or co=="SQL" or co=="Git" or co=="Github" or co=="Data Structures and Algorithms" or co=="Wordpress" or co=="HTML" or co=="CSS" or co=="Jupyter" or co=="Arduino" or co=="Visual Studio" or co=="PyCharm" or co=="Sublime" or co=="TailwindCSS" or co=="Bootstrap"):
            st.success(co+": 9 out of 10")
        else:
            st.error(co+": 7 out of 10")

elif(ch=="About Me"):
    st.write("### About Me", unsafe_allow_html=True)    
    st.markdown('This section consists mainly of my background and other related information. Besides, I will be beginning this section with my background now. <br> ', unsafe_allow_html=True)
    st.write("##### Background")
    with st.expander("View Details"):
        st.markdown(' I have been pursuing my education from Pune, Maharshtra, India. I am good at science since childhood and as a result I have chosen to pursue my career in the field. My stats of secondary and higher secondary  education are as: <br> <b> Secondary (i.e. 10th) : 93% </b> <br> <b> Higher Secondary (i.e. 12th)  : 74%  </b> <br>', unsafe_allow_html=True)
    st.markdown('##### Current')
    with st.expander("View Details"):
        st.markdown('Currently I am pursuing my Bachelor of Technology from Dr.BA Technological University in Computer Science Engineering with specialization in Artificial Intelligence. ')
    st.write("You can view my academic performance pictorially through different charts. You can do so by choosing a specific chart from the dropdwn below.")
    oc=st.selectbox("", ("Bar Chart", "Line Chart", "Area Chart"))
    chart_data = pd.DataFrame(
        {
            "SGPA":[9.4, 9.2, 9.0, 9.1, 8.89],
            "Semester":[1,2,3,4,5]

            
        })
    if(oc=="Bar Chart"):
        st.bar_chart(chart_data, x="Semester", y="SGPA")

    elif(oc=="Line Chart"):
        st.line_chart(chart_data, x="Semester", y="SGPA")

    elif(oc=="Area Chart"):
        st.area_chart(chart_data, x="Semester", y="SGPA")
    st.markdown('##### Hobbies and Interests')
    with st.expander("View Details"):
        st.markdown('I am an avid reader and love reading especially mythological and thrillers. I also love outdoor sports, watching movies and web series and working out. Another hobby of mine which developed recently is <b> competitive programming and problem solving (i.e. solving twisted dsa problems) </b> which I love doing daily and rarely miss it any day. ', unsafe_allow_html=True)
elif(ch=="Experience"):
    st.write("### Experience", unsafe_allow_html=True)  
    st.markdown('##### GeeksforGeeks', unsafe_allow_html=True)
    st.markdown('<b> Technical Content Engineer: Aug, 2022 - Present.</b>', unsafe_allow_html=True)
    with st.expander("View Details"):
        st.markdown(' Working on digital written technical content.<br> I write, edit, publish articles and make corrections in published ones and in those which are queued for review before getting published. <br>', unsafe_allow_html=True)
    st.markdown('##### LetsGrowMore', unsafe_allow_html=True)
    st.markdown('<b> Web Development Intern: Oct, 2022 - Nov, 2022.</b>', unsafe_allow_html=True)
    with st.expander("View Details"):
        st.markdown('Completed assigned tasks. Worked with <b>MERN</b> stack. <br>', unsafe_allow_html=True)
        st.markdown('Also received a Letter of Recommendation. <br>', unsafe_allow_html=True)
    st.markdown('##### Dolphin Labs', unsafe_allow_html=True)
    st.markdown('<b> Automation Intern: Oct, 2021 - Nov, 2021.</b>', unsafe_allow_html=True)
    with st.expander("View Details"):
        st.markdown('Worked on projects under the domain of <b>IoT</b> using <b>arduino</b>. <br>', unsafe_allow_html=True)
        st.markdown('Also made personal projects using it such as relay lights and computer operated car. <br>', unsafe_allow_html=True)
elif(ch=="Projects"):
    st.write("### Projects", unsafe_allow_html=True)
    st.markdown('##### Moviz ', unsafe_allow_html=True)
    st.markdown("<a href='https://github.com/tansrh/MOVIZZ'>Link to github repository</a><br>", unsafe_allow_html=True)
    with st.expander("View Details"):
        st.write("Moviz is a website that recommends movies. This is a full stack machine learning project made using Django. The site has three tabs: Home, Top, Contact. Home tab does the recommendation. It uses techniques of both collaborative and content based filtering to recommend movies. Recommendation is also done on the basis of actors, actresses, genres. The top tab provides top 50 movies. The contact page lets you contact with us. You details are mailed to us provided you enter a legit and existing email in the email input.Basically it is a ready to use web app. Earlier the database was postgres but due to hosting issues it was removed. The site had been deployed at railway. But because of financial constraints it has been removed. <br>", unsafe_allow_html=True)
        st.markdown('##### Booker ', unsafe_allow_html=True)
    st.markdown("<a href='https://github.com/tansrh/Booker.com'>Link to github repository</a><br><a href='https://tanuj-code.github.io/Themer-React-Editor/'>Use the online hosted editor now</a><br>", unsafe_allow_html=True)
    with st.expander("View Details"):
        st.write("Booker is a website that searches for available books. This project provides the list of available books based on the searched keywords . It uses google api to do so. Frontend has been designed using streamlit which is a python framework.<br>", unsafe_allow_html=True)
    st.markdown('##### Student Management Application ', unsafe_allow_html=True)
    st.markdown("<a href='https://github.com/tansrh/Student-Management-Application'>Link to github repository</a><br>", unsafe_allow_html=True)
    with st.expander("View Details"):
        st.write("This is an android application to monitor student records. All requirements from attendance to exam score maintenance have been served through special features. This application eases a teacher's hectic of managing student record and makes it easy enough to manage it at fingertips. Also anyone i.e. any teacher or organization can login to his/her account from any device and use the app. Firebase has been used as backend and database while Java has been used for frontend. You can download and install the apk file of the app from the repository link above and use the app for free. <br>", unsafe_allow_html=True)
    st.markdown('##### Audiopad ', unsafe_allow_html=True)
    st.markdown("<a href='https://github.com/tansrh/PythonAudioPad'>Link to github repository</a><br>", unsafe_allow_html=True)
    with st.expander("View Details"):
        st.write("It's a Notepad with audio feature made using python. Tkinter has been the library used specifically for this purpose. It's a mini notepad which enables one to write, read, create, delete text files along with another additional option of getting the files read. It provides every option and feature that one needs to read, write and manage files on an operating system. It consumes less memory as compared to Notepad and the audio option provides an audiobook like experience.<br> ", unsafe_allow_html=True)
    st.markdown('##### Tic-Tac-Toe Application')
    st.markdown("<a href='https://github.com/tansrh/Android-TIC_TAC_TOE-GAME'>Link to github repository</a><br>", unsafe_allow_html=True)
    with st.expander("View Details"):
        st.write("Android tic-tac-toe application which lets you play the game where you will be competing against a smart opponent (i.e. computer) which makes every attempt to ruin your strategy. It's a single player application. However, a multiplayer application has also been developed and its apk has also been provided along with the single player application's apk in the repository link above. Visit the link and download and install the respective apk as per your choice and enjoy. Java has been used as the primary language for developing this application.", unsafe_allow_html=True)
    st.markdown('##### Themer Editor ', unsafe_allow_html=True)
    st.markdown("<a href='https://github.com/tansrh/Themer-React-Editor'>Link to github repository</a><br><a href='https://tanuj-code.github.io/Themer-React-Editor/'>Use the online hosted editor now</a><br>", unsafe_allow_html=True)
    with st.expander("View Details"):
        st.write("This editor has been made using React. It is a very attractive and interesting editor which lets you enjoy while typing through it interactive and smooth interface. It has some other exciting features too which you will be able to use after visiting the site. Its direct link has also been provided above which you can check for quick use.<br> ", unsafe_allow_html=True)
    st.write("Besides these I have made other projects too which you can view by visiting<a href='https://github.com/tansrh'> my github profile</a> and checking the repositories. ", unsafe_allow_html=True)
elif(ch=="Contact Me"):
    st.write("### Contact Me", unsafe_allow_html=True)
    with st.form("Getintouch", clear_on_submit=True):
        
        pas="pihllwkbblbyaaiq"
        email=st.text_input(label="", placeholder="Enter your email")
        name=st.text_input(label="", placeholder="Enter your full name")
        sub=st.text_input(label="", placeholder="Enter the subject of your message")
        body=st.text_area(label="", placeholder="Write your message")
        send = st.form_submit_button(label="Send Message")
        if send:
            tmp=st.empty()
            tmp.info("Please wait.")
            time.sleep(2)
            connection=s.SMTP('smtp.gmail.com', 587)
            connection.starttls()
            sendto="tanc16h@gmail.com"
            connection.login(sendto, pas)
            
            message="\n\nName:{}\n\nEmail:{}\n\nSubject:{}\n\nBody:{}".format(name, email, sub, body)
            if (email=="" or sub=="" or name=="" or body=="" or ".com" not in email):
                tmp.error("Please fill all the fields with valid credentials.")                
                time.sleep(2)
                tmp.empty()            
            else:
                a=os.system("ping www.google.com.")
                if a==1:                    
                    tmp.error("Please connect to the internet.")
                    time.sleep(2)
                    tmp.empty()
                else:
                    connection.sendmail(sendto, sendto, message)
                    connection.quit()
                    tmp.success("Message sent!")
                    time.sleep(2)
                    tmp.empty()

                
               
                
        
          
                






   

