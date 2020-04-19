__pragma__('alias', 'S', '$')

from model import Model
from view import View

class Presenter:
    # コンストラクタ
    def __init__(self):
        self._model = Model()
        self._view = View()
        self._bind()

    # イベントをバインドする
    def _bind(self):
        S('body').on('todos-updated', self._on_todos_updated)
        S('#input-form').on('show.bs.modal', self._on_show_modal)
        S('#register-button').on('click', self._on_click_register)
        S('#todo-list').on('click', '.toggle-checkbox', self._on_click_checkbox)
        S('#todo-list').on('click', '.delete-button', self._on_click_delete)

    # 初期表示処理
    def start(self):
        self._model.load_all_todos()
