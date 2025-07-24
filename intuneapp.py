{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4ac834af",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from dotenv import load_dotenv\n",
    "load_dotenv()\n",
    "os.environ[\"LANGCHAIN_API_KEY\"]= os.getenv(\"LANGCHAIN_API_KEY\")\n",
    "os.environ[\"LANGCHAIN_TRACKING_V2\"] = \"true\"\n",
    "os.environ[\"LANGCHAIN_PROJECT\"] = os.getenv(\"LANGCHAIN_PROJECT\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a68d88fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain_community .llms import Ollama\n",
    "import streamlit as st\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "myenv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
