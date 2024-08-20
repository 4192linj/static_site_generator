
class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclass must implement to_html method")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join([f"{key}={value}" for key, value in self.props.items()])
    
    def __repr__(self):
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, value: str, tag: str = None, props: dict = None):
        super().__init__(tag = tag, value = value, props = props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value is required for all leaf nodes")
        if self.tag is None: # if no tag, then it should be returned as raw text
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
    

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag = tag, children = children, props = props)

    def to_html(self):
        if self.children is None:
            raise ValueError("children is required for all parent nodes")
        if self.tag is None:
            raise ValueError("tag is required for all parent nodes")
        if self.props is None:
            html_tag = f"<{self.tag}>{self.children}</{self.tag}>"
        else:
            html_tag = f"<{self.tag} {self.props_to_html()}>"
        for child in self.children:
            html_tag += child.to_html()
        html_tag += f"</{self.tag}>"
        return html_tag

