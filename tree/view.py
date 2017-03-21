def textView(node,width,toStr):
    """ node struct should be
{
  value:
  children:[node ...],
}"""
    if not node:
        print("$")
        return
    print(toStr(node.value),end="-")
    if hasattr(node,"children"):
        for child in node.children:
            textView(child,width,toStr)
    else :
        print("*")
        return
