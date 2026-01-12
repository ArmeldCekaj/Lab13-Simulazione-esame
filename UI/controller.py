import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleDDYearSelection(self, e):
        pass

    def handleCreaGrafo(self,e):
        year = self._view._ddAnno.value
        if year == "" or year is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Attenzione selezionare un anno."))
            return

        self._model.buildGraph(year)
        nNodes, nEdges = self._model.getGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo Correttamente creato "))
        self._view.txt_result.controls.append(ft.Text(f"N nodi  {nNodes}"))
        self._view.txt_result.controls.append(ft.Text(f"N archi {nEdges}"))

        topPilota = self._model.analyze()
        self._view.txt_result.controls.append(ft.Text(f"Miglior pilota:  {topPilota[0]} con punteggio {topPilota[1]}"))



        self._view.update_page()

    def handleCerca(self, e):
        pass

    def fillDDYear(self):
        years = self._model.getYear()
        for y in years:
            self._view._ddAnno.options.append(ft.dropdown.Option(str(y), data=y))
        self._view.update_page()


