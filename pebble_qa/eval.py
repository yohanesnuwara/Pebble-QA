import subprocess
import os
from PIL import Image
import io

def save_image(df, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for index, row in df.iterrows():
        if row['figure'] is not None:
            image_bytes = row['figure']['bytes']
            image = Image.open(io.BytesIO(image_bytes))
            filename = f"Q{row['number']}.png"
            filepath = os.path.join(output_dir, filename)
            image.save(filepath, 'PNG')
            print(f"Saved {filename}")

def generate_image_path(df_row, folder_path):
    question_no = df_row['number']
    image_path = os.path.join(folder_path, f"Q{question_no}.png")
    return image_path

def download_model(model):
    result = subprocess.run(
        ["ollama", "pull", model],
        text=True,
        capture_output=True
    )
    print(f'{model} is finished downloaded.')

def list_models():
    result = subprocess.run(
        ["ollama", "list"],
        text=True,
        capture_output=True
    )
    return result.stdout

def answer(question, model="gemma3"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=question,
        text=True,
        capture_output=True
    )
    return result.stdout

def answer_all_questions(df, model="gemma3", limit_question=2):
    # Define log output filename
    log_output = f"{model}_answer.txt"

    answers = []

    # Write output into text file
    with open(log_output, 'w') as f:

        # Iterate through every question
        for i in range(limit_question):
            # Define question
            question = f"""
            {df.iloc[i,:].question}
            A. {df.iloc[i,:].A}
            B. {df.iloc[i,:].B}
            C. {df.iloc[i,:].C}
            D. {df.iloc[i,:].D}
            """

            # Print question
            print(f"QUESTION NO. {i+1}\n")
            print(question + "\n")
            print(f"CORRECT ANSWER  : {df.iloc[i,:].correct_answer}\n")

            # Write question to file
            f.write(f"QUESTION NO. {i+1}\n")
            f.write(question + "\n")
            f.write(f"CORRECT ANSWER  : {df.iloc[i,:].correct_answer}\n")

            # Decide if question includes image
            fig = df.iloc[i,:].figure
            
            if fig is None:
                # Prompt only consist of text
                # Generate question
                prompt = f"""You are an expert in petroleum engineering. Answer the following multiple choice question. Think carefully before answering.

                {question}

                Write answer in JSON

                {{
                    'answer': 'A',
                    'explanation': '...'
                }}
                """

            if fig is not None:
                # Prompt consists of text and image

                # Generate filepath to image
                image_path = generate_image_path(df.iloc[i,:], folder_path='/content/figures')

                # Generate question
                prompt = f"""You are an expert in petroleum engineering. Answer the following multiple choice question. Think carefully before answering.

                {question}

                Write answer in JSON

                {{
                    'answer': 'A',
                    'explanation': '...'
                }}

                Image: {image_path}
                """

            # Answer question
            ans = answer(prompt, model=model)

            print(f"LLM ANSWER      : {ans}\n")
            print("--------------------------------------------------\n")

            f.write(f"LLM ANSWER      : {ans}\n")
            f.write("--------------------------------------------------\n")

            answers.append(ans)
