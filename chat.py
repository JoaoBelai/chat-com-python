import flet as ft

def main(page):
    title = ft.Text("Chat")  

    windowTitle = ft.Text("Bem vindo ao Chat")
    userNameField = ft.TextField(label="Escreva seu nome no chat")

    def sendMessage (evento):
        text = f"{userNameField.value}: {messageText.value}"

        page.pubsub.send_all(text)

        messageText.value = ""
        page.update()

    messageText = ft.TextField(label="Digite sua mensagem", on_submit=(sendMessage))
    sendButton = ft.ElevatedButton("Enviar", on_click=(sendMessage))

    chat = ft.Column()

    messageRow = ft.Row([messageText, sendButton])

    def enterChat(evento):
        page.remove(title)
        page.remove(startButton)
        modal.open = False

        page.add(chat)
        page.add(messageRow)

        enterChatText = f"{userNameField.value} entrou no chat"
        page.pubsub.send_all(enterChatText)

        page.update()

    enterButton = ft.ElevatedButton("Entrar no chat", on_click=(enterChat))


    modal = ft.AlertDialog(
        title=windowTitle,
        content=userNameField,
        actions=[enterButton]
    )

    def openModal(event):
        page.dialog = modal
        modal.open = True
        page.update()


    startButton = ft.ElevatedButton("Iniciar Chat", on_click=(openModal))

    page.add(title)
    page.add(startButton)
    
    def sendTunnelMessage(message):
        chat.controls.append(ft.Text(message))

        page.update()

    page.pubsub.subscribe(sendTunnelMessage)

ft.app(main, view=ft.WEB_BROWSER)