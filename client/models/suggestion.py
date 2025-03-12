class Suggestion:
    def __init__(self, message, action=None, params=None):
        self.message = message
        self.action = action
        self.params = params if params else {}
        
    def to_dict(self):
        return {
            'message': self.message,
            'action': self.action,
            'params': self.params
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            message=data.get('message', ''),
            action=data.get('action'),
            params=data.get('params', {})
        )

def filter_suggestions(suggestions, max_count=5):
    if len(suggestions) <= max_count:
        return suggestions
    
    return suggestions[:max_count]