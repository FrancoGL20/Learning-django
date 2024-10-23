from django.shortcuts import render

# Create your views here.
def index(request):
    list_articles=[
        {
            "title":"Tesla muestra su robot Optimus y anticipa que será el nuevo C-3PO",
            "image":"https://i0.wp.com/imgs.hipertextual.com/wp-content/uploads/2024/10/Tesla-Bot-Optimus_00.jpg?resize=1200%2C675&quality=70&strip=all&ssl=1",
            "author":"Luis Miranda"
        },
        {
            "title":"Los mejores memes del robot optimus de Tesla",
            "image":"https://www.infobae.com/resizer/v2/Z4SF367WAFEEFEVRKQFYBSM2P4.jpg?auth=75011353f63d2781ed8ebda426ad351c4ac41130df234fb9d9e38ee084a0d911&smart=true&width=992&height=558&quality=85",
            "author":"Olivia Vázquez Herrera"
        },
        {
            "title":"Los robots ‘Optimus’ de Tesla estaban teledirigidos por humanos",
            "image":"https://imagenes.elpais.com/resizer/v2/JU67TFBLHKCN537ECIG3PWSFXE.jpg?auth=1143d9eba12762836eabf8c00e154bccbc4dd5748d04bdf6897a1c6de9d2e94d&width=1200",
            "author":"Miguel Jiménez"
        },
    ]
    
    context={
        "articles":list_articles
    }
    
    return render(request,'blog/index.html',context)