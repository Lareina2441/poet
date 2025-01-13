# 小诗：一个与长辈对话创作唐诗的AI助手  
**XiaoShi: An AI Assistant for Conversing and Composing Tang Poems with Elders**

这个项目创建了一个基于语音识别和GPT-4模型的对话式AI助手，用于与长辈互动，帮助他们创作和修改中国唐诗宋词。AI助手能够通过语音识别接收长辈的输入，通过GPT-4模型生成合适的诗歌内容，并以语音的形式输出回答。该项目主要面向长辈群体，帮助他们更好地理解和参与诗歌创作。  
This project creates a conversational AI assistant based on speech recognition and the GPT-4 model to interact with elders, helping them compose and modify Chinese Tang and Song poems. The AI assistant can receive input from elders through speech recognition, generate appropriate poetry content via the GPT-4 model, and output the response in the form of speech. This project is mainly aimed at the elderly, helping them better understand and engage in poetry creation.

## 功能介绍  
## Features

1. **语音识别**：通过麦克风实时接收长辈的语音输入，转换为文本。  
   **Speech Recognition**: Real-time speech input from the elder is captured via a microphone and converted into text.
   
2. **语音合成**：将ChatGPT的回答转换为语音，方便长辈听取。  
   **Text-to-Speech**: Converts ChatGPT's response into speech, making it easier for elders to listen.

3. **ChatGPT响应生成**：利用GPT-4模型生成对话内容，尤其在唐诗宋词创作上提供帮助。  
   **ChatGPT Response Generation**: Utilizes GPT-4 to generate conversational content, particularly helpful for creating Tang and Song poems.

4. **交互式提示**：通过语音播放简洁的提示，引导长辈使用该系统进行创作和互动。  
   **Interactive Prompts**: Provides simple voice prompts to guide elders in using the system for creation and interaction.

## 安装和使用  
## Installation and Usage

### 环境要求  
### Requirements

- Python 3.x
- `speech_recognition`：用于语音识别  
  **speech_recognition**: For speech recognition.
  
- `openai`：用于与ChatGPT交互  
  **openai**: For interacting with ChatGPT.
  
- `pyttsx3`：用于文本转语音  
  **pyttsx3**: For text-to-speech conversion.

### 安装依赖  
### Install Dependencies

1. 克隆该仓库：  
   Clone the repository:
   ```bash
   git clone https://github.com/Lareina2441/poet.git
   cd poetry-assistant
   ```

2. 安装所需的Python库：  
   Install the required Python libraries:
   ```bash
   pip install speech_recognition openai pyttsx3
   ```

### 配置API密钥  
### Configure API Key

你需要设置一个OpenAI API密钥，用于访问GPT-4模型：  
You need to set an OpenAI API key to access the GPT-4 model:

1. 在代码中找到以下行：  
   Find the following line in the code:
   ```python
   openai.api_key = 'your api here'
   ```
   
2. 将`'your api here'`替换为你的OpenAI API密钥。  
   Replace `'your api here'` with your OpenAI API key.

### 运行程序  
### Run the Program

在命令行中运行程序：  
Run the program in the command line:
```bash
python main.py
```

程序启动后，系统会播放欢迎语音提示，告诉长辈如何与AI助手互动。长辈可以通过语音与AI对话，AI将根据输入内容生成唐诗或宋词。  
Once the program starts, it will play a welcome voice prompt explaining how the elder can interact with the AI assistant. The elder can speak to the AI, which will generate Tang or Song poems based on their input.

## 使用示例  
## Example Usage

1. **长辈输入：** “你好小诗”  
   **Elder input:** "Hello XiaoShi"  
   - **AI输出：** “爷爷奶奶你好，我是小诗，擅长写中国唐诗宋词。我们可以一起创作诗歌。”  
   **AI output:** "Hello, grandpa and grandma, I am XiaoShi, good at composing Tang and Song poems. Let's create poetry together."
   
2. **长辈输入：** “我想写一首关于春天的诗”  
   **Elder input:** "I want to write a poem about spring"  
   - **AI输出：** “好的，让我们从‘春’字开始，我会帮助你一步步完成。‘春天来了，百花齐放’……”  
   **AI output:** "Okay, let's start with the word 'spring'. I will help you step by step. 'Spring has come, and flowers are blooming'…"

## 代码结构  
## Code Structure

- `get_chatgpt_response(conversation_history)`：与OpenAI的GPT-4模型进行交互，获取响应文本。  
  **Interacts with OpenAI's GPT-4 model to retrieve response text.**

- `text_to_speech(response_text)`：将文本转换为语音并播放。  
  **Converts text into speech and plays it.**

- `recognize_speech()`：识别长辈的语音输入并转换为文本。  
  **Recognizes speech input from the elder and converts it into text.**

- `play_prompt()`：播放初始的提示信息，帮助长辈理解系统的使用方法。  
  **Plays initial prompt to help the elder understand how to use the system.**

- `main()`：主程序，控制整个对话流程。  
  **Main program that controls the entire conversation flow.**

## 贡献  
## Contributions

欢迎提交Issue和Pull Request，如果你有任何想法或问题，随时与我们讨论。  
Feel free to submit Issues and Pull Requests. If you have any ideas or questions, don't hesitate to discuss them with us.

## 许可证  
## License

MIT许可证，详情请参阅 [LICENSE](LICENSE)。  
MIT License, see the [LICENSE](LICENSE) for details.
