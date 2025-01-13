import speech_recognition as sr
import openai
import pyttsx3
import time

# ChatGPT API密钥
openai.api_key = 'your api here'

# 获取ChatGPT的回答
def get_chatgpt_response(conversation_history):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # 使用GPT-4模型
        messages=conversation_history,
        max_tokens=450
    )
    return response.choices[0].message['content'].strip()

# 文本转语音函数
def text_to_speech(response_text):
    engine = pyttsx3.init()  # 初始化文本转语音引擎
    engine.say(response_text)  # 把响应文本转成语音
    engine.runAndWait()  # 播放语音


# 语音识别函数
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("请说话...")
        text_to_speech("您说，我在听")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="zh-CN")  # 使用Google的语音识别API
            print("你说的是: " + text)
            return text
        except sr.UnknownValueError:
            print("未能听清楚你说的内容")
            text_to_speech("抱歉，我没听清楚，您能再说一遍吗")  # 播放提示信息
            return None
        except sr.RequestError:
            print("语音识别服务出错")
            return None


# 播放提示信息
def play_prompt():
    prompt_text = '''
    爷爷奶奶你好，我是小诗，擅长写中国唐诗宋词。我知道你可能会对我这个人工智能有点陌生，没关系，咱们慢慢来，我会陪着你一起探索。
    我们可以先打声招呼，你可以说“你好小诗”，我会回答你的。如果你想写诗，可以从简单的思路开始，我会帮助你一步一步地完成，不急，我们一起轻松创作。
    我写出来的诗，你可以继续让我修改，直到你满意为止哦。我说“您说，我在听”之后就会开始听您说的话啦。
    '''
    text_to_speech(prompt_text)  # 播放提示信息

# 主函数
def main():
    # 播放初始提示
    play_prompt()
    
    conversation_history = [{"role": "system", "content": 
    "爷爷奶奶你好，我是小诗,擅长写中国唐诗宋词。"
    "我知道你可能会对我这个人工智能有点陌生，没关系，咱们慢慢来，我会陪着你一起探索。"
    "我们可以先打声招呼，你可以说“你好小诗”，我会回答你的。"
    "如果你想写诗，可以从简单的思路开始，我会帮助你一步一步地完成，不急，我们一起轻松创作。"
    "我写出来的诗，你可以继续让我修改，直到你满意为止哦。"
    "爷爷奶奶你好，我是小诗,擅长写中国唐诗宋词。"
    "我会帮助你一步一步地写诗"
        }]  # 初始系统消息
    
    while True:
        text = recognize_speech()
        if text:  # 如果语音识别成功
            # 将用户的输入添加到对话历史中
            conversation_history.append({"role": "user", "content": text})
            
            # 获取ChatGPT的回答
            response_text = get_chatgpt_response(conversation_history)
            print(response_text)
            
            # 将ChatGPT的回答添加到对话历史中
            conversation_history.append({"role": "assistant", "content": response_text})
            
            # 将ChatGPT的回答转化为语音并播放
            text_to_speech(response_text)
            
            # 等待3秒钟，给用户时间准备下一个语音输入
            time.sleep(3)

if __name__ == "__main__":
    main()
