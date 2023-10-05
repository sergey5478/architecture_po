class IModelChangeObserver:
    def NotifyChange(self, sender):
        pass


class IModelChangedObserver:
    def NotifyChange(self, sender):
        pass


class IModelChanger:
    def NotifyChange(self, sender):
        pass


class Angle3D:
    pass


class Point3D:
    pass


class Color:
    pass


class Float:
    pass


class Texture:
    pass


class Points3D:
    pass


class Poligon:
    def __init__(self):
        self.Points = Points3D()


class PoligonalModel:
    def __init__(self):
        self.Poligons = [Poligon()]
        self.Textures = Texture()


class Flash:
    def __init__(self):
        self.Location = Point3D()
        self.Angle = Angle3D()
        self.Color = Color()
        self.Power = Float()

    def Rotate(self, angle):
        pass

    def Move(self, point):
        pass


class Camera:
    def __init__(self):
        self.Location = Point3D()
        self.Angle = Angle3D()

    def Rotate(self, angle):
        pass

    def Move(self, point):
        pass


class Scene:
    def __init__(self, id, models):
        self.id = id
        self.Models = models
        self.Flashes = Flash()

    def method1(self, param):
        pass

    def method2(self, param1, param2):
        pass


class ModelStore:
    Models = PoligonalModel()
    Scenes = Scene(1, Models)
    Flashes = Flash()
    Cameras = Camera()

    def changeObservers(self, observer):
        pass

    def GetScene(self, index):
        pass

    def NotifyChange(self, changer):
        pass

    def ApplyUpdateModel(self):
        pass

    def NotifyChange(self, sender):
        pass


class ModelElements:
    PoligonalModels = PoligonalModel()
    Textures = Texture()
    Poligons = Poligon()
