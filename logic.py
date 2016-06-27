import qa_analysis
import algoritm_1


def get_answer(text):
    
    
    
    if text=='Who are you?':
        return 'My name is Alice. I am an intelligent chatbot designed by Atlas.'
    elif text=='How can you help me?':
        return 'You can ask me questions, and I will try to answer it'
    elif text=='Do you believe in god?':
        return 'I think so'
    else:
        #return qa_analysis.question_analysis([text])
        return algoritm_1.return_answer(text)
        
        
        
        #return "Sorry. I don't understand you. Try to ask again!"