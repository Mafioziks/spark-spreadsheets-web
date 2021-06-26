function getChildElementsByClassName (parent, className) {
  const nodes = []
  for (let i = 0; i < parent.childNodes.length; i++) {
    const childNode = parent.childNodes[i]

    if (childNode.className === className) {
      nodes.push(childNode)
    }

    if (childNode.childNodes.length > 0) {
      getChildElementsByClassName(childNode, className).forEach(element => {
        nodes.push(element)
      })
    }
  }

  return nodes
}

function simulateClick (node) {
  const event = new MouseEvent('click', {
    bubbles: true,
    cancelable: true,
    view: window
  })

  node.dispatchEvent(event)
}

function isEmpty (object) {
  return object === undefined ||
    (
      typeof object === 'object' &&
      Object.entries(object).length === 0
    )
}

module.exports = { getChildElementsByClassName, simulateClick, isEmpty }
