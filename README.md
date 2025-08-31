# Pebble-QA
**Petroleum Engineering Benchmarks for LLM Evaluation - Questions and Answers**

<img src="https://github.com/user-attachments/assets/96f8691b-b110-4d33-a100-2af976cd1810" alt="demo" width="500" height="500">



AI, particularly Large Language Models (LLMs) are revolutionizing the oil and gas industry (source). While LLMs on average have very good accuracy on answering general questions and on reasoning, their performance on oil and gas domain knowledge have not been evaluated. With 100+ different LLMs nowadays, we want to benchmark different LLMs and identify the top performing LLM on this domain knowledge. 

## 📱 Data and methodology

[SPE MCQ Dataset](https://huggingface.co/datasets/ynuwara/spe_mcq_dataset) is a dataset which consists of 100 multiple choice questions (MCQ) on different topics of petroleum engineering, such as general knowledge, reservoir engineering, drilling and wells, and production engineering. Some of the questions are easy, while some of them requires reasoning and calculations based on plot and tables.

Different LLMs that are currently deployed in [Ollama](https://ollama.com/) are used to answer the question and evaluation is carried out based on how many answers are incorrect. Moreover, the evaluation is done per topics of questions. 

## 🏅 Who are the winners? 

|Model|Parameter size|Score|Time taken to complete (hour)|Answer sheet|
|:---:|:---:|:---:|:---:|:--:|
|gpt-oss|20B||2.39|[gpt-oss](https://github.com/yohanesnuwara/Pebble-QA/blob/main/llm_result/gpt-oss_20b_answer.txt)|
