from dotenv import load_dotenv
load_dotenv() 
import streamlit as st
import os
import pathlib
import textwrap
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
import pickle







def preprocess_string(string):
    # This is a placeholder function for any string preprocessing you might want to do
    # For example, you might want to remove stop words, perform stemming or lemmatization, etc.
    return string

def process_string(model, string):
    # This is a placeholder function for processing the string using the model
    # For example, you might want to use the model to extract features from the string, etc.
    return model.predict([string])

def generate_input_string(salary, expense, home_value, to_buy_in_years, occupation, skillset, disease):
    # Generate a longer and more complex string using the input parameters
    input_string = f"The individual in question has a salary of {salary}, with expenses that amount to {expense} annually. The home of this individual is valued at {home_value}. The individual has plans to make a significant purchase within the next {to_buy_in_years} years. In terms of occupation, the individual works as a {occupation}. The individual's skillset includes {skillset}. Unfortunately, the individual is affected by {disease}. This information provides a comprehensive overview of the individual's financial situation, career, and health status."
    return input_string

def predict_output(salary, expense, home_value, to_buy_in_years, occupation, skillset, disease):
    # Load the models
    # with open('result_model.pkl', 'rb') as file:
    #     result_model = pickle.load(file)
    # with open('result_model.pkl', 'rb') as file:
    # chat_model = pickle.load(file)

    # Define the prompt template
    prompt_template = """Goal: Purchase a home worth INR {:.0f} in three years with a monthly salary of INR {:.0f} and monthly expenses of INR {:.0f}.
    \nAssumptions:\n\nDown payment: {:.0f}% (INR {:.0f})\nLoan amount: INR {:.0f}\nInterest rate: {:.1f}% per annum\nLoan term: {} years
    \n7-Steps to Achieve Home Ownership:\n\n1. Determine Monthly Savings Target:\n\nCalculate the monthly mortgage payment: INR {:.0f}\nSubtract current expenses: INR {:.0f}\nMonthly savings target: INR {:.0f}
    \n2. Create a Budget and Track Expenses:\n\nUse a budgeting app or spreadsheet to track income and expenses.\nIdentify areas where spending can be reduced to increase savings.
    \n3. Increase Income (Optional):\n\nDue to TB disease, exploring side hustles may not be feasible. Consider alternative ways to supplement income, such as overtime within your government role or a part-time job.
    \n4. Save Consistently:\n\nSet up automatic transfers to a dedicated savings account for your down payment and closing costs.\nConsider using a high-yield savings account to maximize interest earned.
    \n5. Reduce Debt:\n\nPay off any outstanding debts, such as credit card balances, to reduce financial obligations and improve your credit score.
    \n6. Explore Government Assistance Programs:\n\nResearch government programs that provide financial assistance for first-time homebuyers, such as down payment assistance or closing cost grants.
    \n7. Get Pre-Approved for a Mortgage:\n\nObtain a mortgage pre-approval to determine your borrowing capacity and strengthen your position when making an offer on a home.
    \nConclusion:\n\nAchieving homeownership with a monthly salary of INR {:.0f} and monthly expenses of INR {:.0f} requires careful financial planning and discipline. By following these steps, you can save consistently, reduce debt, and position yourself to purchase a home worth INR {:.0f} in three years."""

    # Define input values
    input_values = [
        (2215740, 45544, 458, 20, 443148, 1772592, 7, 20),
        # Add more input value tuples as needed
    ]

    # Generate text for each input value
    for i, input_value in enumerate(input_values, start=1):
        # Unpack input values
        home_value, salary, expenses, down_payment_percentage, down_payment, loan_amount, interest_rate, loan_term = input_value
        
        # Format prompt with input values
        prompt = prompt_template.format(home_value, salary, expenses, down_payment_percentage, down_payment, loan_amount, interest_rate, loan_term,
                                        (loan_amount*interest_rate/12/100)/(1-(1+interest_rate/12/100)**(-loan_term*12)),
                                        expenses, (salary-expenses), salary)
        
        # Generate text using the chat model with the prompt
        generated_text = chat_model(prompt)
        
        # Print generated text
        print(f"Generated Text {i}:")
        print(generated_text)
        print("\n" + "=" * 50 + "\n")

        with open('final_model.pkl', 'rb') as file:
            final_model = pickle.load(file)

        # Generate the input string
        input_string = generate_input_string(salary, expense, home_value, to_buy_in_years, occupation, skillset, disease)

        # Preprocess the input string
        preprocessed_string = preprocess_string(input_string)

        # Process the preprocessed string using the result_model
        processed_string = process_string(result_model, preprocessed_string)

        # Use the final_model to generate the output
        output = final_model.predict(processed_string)

        return output[0]







def get_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text



st.set_page_config(page_title="PADHLE...")

st.write('<h1 style="font-family: cursive; font-size: 36px; color: #4CAF50; text-shadow: 2px 2px 4px rgba(0,0,0,0.4);">Get all your answers here.......</h1>', unsafe_allow_html=True)

input1=st.text_input("Subject ",key="input1")
input2=st.text_input("Put your Doubt",key="input2")
input3=st.text_input("Preferred Language",key="input3")
# input4=st.text_input("To buy house in how many years",key="input4")
# # input5=st.text_input("occupation",key="input5")
# options = ['NA', 'Engineering', 'Government Service', 'CA', 'Lawyer', 'Defence', 'Business', 'Others']
# input5 = st.selectbox("Occupation", options, key="input5")
# # input6=st.text_input("Skillset",key="input6")
# opt = ['NA', 'Software Developer', 'Accounting', 'Mathematics', 'Designing', 'Economics', 'Others']
# input6 = st.selectbox("Skillset", opt , key="input6")
# input7=st.text_input("Disease",key="input7")

# input = f"Give me optimize financial plan to buy home of value {input3}INR in {input4} years with current salary of {input1}INR and expense of {input2}INR monthly.My occupation is {input5} And Myskillsets are {input6} for side hustling plan to earn extra with {input7} disease give output in whose sequence should look like this goal , assumption , 7-steps to acheive home using financial planning , occupation ,  skillset conclusion"
input = f"In the context of {input1} please solve this doubt {input2} so that i can understand easily in {input3} language"

submit=st.button("Click To resolve Doubt..")

## If ask button is clicked


st.write('<h1 style="color:goldenrod; font-size: 24px; text-align: center;">First of all be positive you are going to achieve a large milestone in the future and it\'s just a small doubt....We will resolve it!</h1>', unsafe_allow_html=True)
if submit:
    
    response=get_response(input)
    st.subheader("Here it goes")
    st.write('<p style="color:red; font-size:16px; font-weight:bold; padding:10px;">***Disclaimer: The information provided here is for educational and information purposes only.</p>', unsafe_allow_html=True)
    st.write(response)

st.write('<h1 style="color:silver; font-size: 18px;">Now go champ and make it</h1>', unsafe_allow_html=True)




# to run      streamlit run app1.py --server.port 8080