class PluginBase:
    """
    Базовый класс для абстрактных классов, для которых могут быть плагины.
    Каждый плагинный абстрактный класс должен содержать plugins = [] на уровне класса и
     наследоваться от PluginBase с ключевым аргументом abstract=True
    """
    def __init_subclass__(cls, **kwargs):
        """ Перехватывает процесс наследования  """
        abstract = kwargs.get('abstract', False)
        if abstract:
            kwargs.pop('abstract')

        super().__init_subclass__(**kwargs)

        if hasattr(cls, 'plugins') and not abstract:
            cls.plugins.append(cls)
