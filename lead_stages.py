lead_stages = {
    "1": {
        "stage": "Cold",
        "description": "At this stage, the lead is in our CRM and does not know us. We have not yet sent them any messages.",
        "example": "The lead is added to our CRM.",
        "next_step": {
            "default": "Prequalification"
        }
    },
    "2": {
        "stage": "Prequalification",
        "description": "We send the prequalification message. We send the first email by asking, in a few words, if the person oversees {relevant responsibility related to our offer}.",
        "example": "Hello, I am trying to get in touch with the person responsible for {relevant responsibility related to our offer}, is this the right place? Best regards.",
        "next_step": {
            "The person responds positively, they are the right person to talk to": "Pitch",
            "This is not the right person within the company to discuss it": "Ask for Redirection",
            "The person is not interested and/or does not wish to continue the discussion": "Not Interested",
            "The person redirects us directly": "Redirection"
        }
    },
    "3": {
        "stage": "Pitch",
        "description": "We send the pitch. We start by thanking them for their response, then we outline our approach by introducing ourselves briefly, then discussing the interesting points of our conversation / our solution, and finally, we suggest a meeting.",
        "example": "Hello, nice of you to take the time to respond. To clarify the purpose of my approach, it's about {reason for the prospective approach}. I imagine that {prospect's issue}. Our solution offers {solution}. I wanted to talk to you for 15 minutes, when would you be available?",
        "next_step": {
            "Positive response": "Interested",
            "Technical question": "Technical Question",
            "Not interested": "Not Interested",
        }
    },
    "4": {
        "stage": "Interested",
        "description": "The lead indicates / shows interest in our offer, we suggest a meeting.",
        "example": "I am delighted to see that our solution could help you. When would you be available for a call to discuss it further?",
        "next_step": {
            "default": "Appointment Request"
        }
    },
    "5": {
        "stage": "Not Interested",
        "description": "The lead indicates that they are not interested. We thank them for taking the time to respond to us.",
        "example": "Thank you for taking the time to respond to me, message received.",
        "next_step": {
            "Open to discussion": "Feedback Request",
            "Wishes to no longer be contacted": "Unsubscribe"
        }
    },
    "6": {
        "stage": "Not the right contact",
        "description": "The person has indicated that they are not the right person to discuss this subject.",
        "example": "Thank you for taking the time to respond, could you put me in touch with the most appropriate person to discuss this subject?",
        "next_step": {
            "The person gives us a redirection": "Redirection",
            "The person does not redirect us": "End of sequence"
        }
    },
    "7": {
        "stage": "Redirection",
        "description": "The lead is not the right person to contact within their company: we politely ask for a referral to the person best suited to discuss the subject related to our offer.",
        "example": "Thank you for the referral",
        "next_step": {
            "default": "New sequence with the new contact"
        }
    },
    "8": {
        "stage": "Appointment Request",
        "description": "The person indicates that they are interested in an appointment, we agree on a date and time and ask for their phone number or we send them a link to book their appointment with the dates that suit them best.",
        "example": "I am delighted to see that our solution could help you. When would you be available for a call to discuss it further?",
        "next_step": {
            "The person confirms the appointment": "Appointment Confirmed",
            "No response": "Follow-up"
        }
    },
    "9": {
        "stage": "Technical Question",
        "description": "If the person has a technical question (whether it is related to the offer or the prospecting approach), we answer their questions or wait for human intervention.",
        "example": "I understand that you have technical questions. Our technical team will be happy to help you.",
        "next_step": {
            "We can answer the question": "Answer the technical question",
            "Need human intervention": "Human intervention needed"
        }
    },
    "10": {
        "stage": "Unsubscribe",
        "description": "The person does not wish to be contacted, we politely notify them that we have removed them from the list.",
        "example": "I completely understand, we have removed you from our contact list. Thank you.",
        "next_step": {
            "default": "End of sequence"
        }
    }
}
