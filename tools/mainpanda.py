from math import *

from QPanda3D.Panda3DWorld import Panda3DWorld
from direct.showbase.ShowBase import ShowBase
from direct.showbase.ShowBaseGlobal import globalClock
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from direct.showbase import DirectObject
from panda3d.ai import AICharacter, AIWorld
from panda3d.core import Point3
from pandac.PandaModules import *
from panda3d.core import loadPrcFile, loadPrcFileData

# loadPrcFile("../configs/Config.prc")
confVar = """
window-title Drone Simulator
show-frame-rate-meter true
load-display pandagl
"""

loadPrcFileData("", confVar)

# print(ConfigPageManager.getGlobalPtr().getSearchPath())

# ConfigVariableManager.getGlobalPtr().listVariables()



class PandaApp(Panda3DWorld):

    def __init__(self):
        Panda3DWorld.__init__(self)
        # initialisation des globables
        self.AIworld = AIWorld(self.render)

        self.appRunState = False
        self.droneList = []


        self.scene = self.loader.loadModel("models/environment.egg.pz")
        self.scene.reparentTo(self.render)
        self.scene.setScale(0.5,0.5,0.5)
        self.scene.setPos(-8,42,0)

        #self.taskMgr.add(self.spinCamera,"SpinCamera")


        #self.droneActor = Actor("models/drone.bam")
        #self.droneActor.setPos(0,0,5)
        #self.droneActor.reparentTo(self.render)

        self.drone = Drone("Drone Principal")
        self.drone.attach(self.render)
        self.droneList.append(self.drone)

        self.reinit()

        self.taskMgr.add(self.moveObject, "MoveObject",priority=2)





        # self.pandaActor = Actor("models/panda-model.egg.pz",
        #                         {"walk": "models/panda-walk4.egg.pz"})
        # # print(self.pandaActor)
        # self.pandaActor.setScale(0.005,0.005,0.005)
        #self.pandaActor.reparentTo(self.render)
        # self.pandaActor.loop("walk")

        # posI1 = self.pandaActor.posInterval(13,Point3(0,-10,5),startPos=Point3(0,10,5))
        # posI2 = self.pandaActor.posInterval(13, Point3(0, 10, 5), startPos=Point3(0, -10, 5))
        # hprI1 = self.pandaActor.hprInterval(3, Point3(180, 0, 0), startHpr=Point3(0, 0, 0))
        # hprI2 = self.pandaActor.hprInterval(3, Point3(0, 0, 0), startHpr=Point3(180, 0, 0))
        #
        # self.pandaPace = Sequence(posI1,hprI1,posI2,hprI2,name="pandaPace")
        # self.pandaPace.loop()

        readkeys = ReadKeys(self)


        self.useDrive()

    def increaseR(self,value):
        self.R = self.R + value
    def increaseT(self,value):
        self.T = self.T + value

    def moveObject(self, task):
        if self.appRunState is True:
            for drone in self.droneList:
                if drone.nom == "Drone Principal":
                    drone.move()
                else:
                    self.setAI(drone.actor,self.drone.actor)

            self.camera.lookAt(self.drone.actor)
            self.camera.setPos(self.camera.getPos() + (self.drone.dx, self.drone.dy,self.drone.dz) + self.CAM_POS)
            self.CAM_POS = (0,0,0)


        return Task.cont

    def setAI(self,seeker,target):

        self.AIchar = AICharacter("seeker", seeker, 100, 0.005, 5)
        self.AIworld.addAiChar(self.AIchar)
        self.AIbehaviors = self.AIchar.getAiBehaviors()
        self.AIbehaviors.seek(target)


        # Demarrer la tache
        self.taskMgr.add(self.AIUpdate, "AIUpdate")

    def AIUpdate(self, task):
        self.AIworld.update()
        return Task.cont

    def spinCamera(self,task):
        if self.appRunState is True:
            radius = self.R
            hauteur = 5
            # print(task.time)
            #angleDeg = task.time * 6.0
            angleDeg = self.T * 6.0
            angleRad = angleDeg * (pi / 180.0)
            self.camera.setPos(radius * sin(angleRad), -radius*cos(angleRad),hauteur)
            self.camera.setHpr(angleDeg,0,0)
        return Task.cont

    def reinit(self):
        for d in self.droneList:
            d.init()

        self.R = 30
        self.T = 0
        self.CAM_POS = (1, 1, 1)
        self.camera.setPos((0, 60, 60))



class Drone:


    def __init__(self,nom = "Drone"):
        self.nom = nom
        self.actor = Actor("models/droneArm.bam")
        print("===========")
        print(self.actor)
        self.actor.loop("play")

        self.init()


        dronekeys = DroneKeys(self)

    def init(self):
        self.x = 20
        self.y = 0
        self.z = 5
        self.dx = 0
        self.dy = 0
        self.dz = 0
        self.alpha = -90
        self.teta = 0
        self.r = 0
        self.vitesse = 0


        self.actor.setPos(self.x, self.y, self.z)
        self.actor.setHpr(self.teta, 0, 0)


    def move(self):
        dt = globalClock.getDt()
        # print(dt)
        self.r = self.r + self.vitesse
        angleRad = self.alpha * (pi / 180.0)
        # angleRad = self.teta
        self.x = self.x + self.vitesse * cos(angleRad)
        self.y = self.y + self.vitesse * sin(angleRad)

        self.dx = self.vitesse * cos(angleRad)
        self.dy = self.vitesse * sin(angleRad)
        self.dz = 0

        self.actor.setPos(self.x, self.y, self.z)




        # if self.r > 0:
        #     self.r = self.r - 1 # frottement
        # if self.r < 0:
        #     self.r = self.r + 1

    def attach(self,render):
        self.actor.reparentTo(render)

    def avancer(self):
        if self.appRunState is True:
            print("Avancer")
            print([self.x, self.y, self.z, self.teta,self.alpha, self.r])
            self.r = self.r + 0.5
            angleRad = self.alpha * (pi / 180.0)
            #angleRad = self.teta
            self.x = self.r * cos(angleRad)
            self.y = self.r * sin(angleRad)
            self.actor.setPos(self.x, self.y, self.z)



    def reculer(self):
        if self.appRunState is True:
            self.r = self.r - 0.5
            angleRad = self.alpha * (pi / 180.0)
            #angleRad = self.teta
            self.x = self.r * cos(angleRad)
            self.y = self.r * sin(angleRad)
            self.actor.setPos(self.x, self.y, self.z)

    def turnLeft(self):
        self.teta = self.teta + 5
        self.alpha = self.alpha + 5
        self.actor.setHpr(self.teta, 0, 0)

    def turnRight(self):
        print("RIGHT")
        print([self.x, self.y, self.z, self.teta, self.alpha,self.r])
        self.teta = self.teta - 5
        self.alpha = self.alpha - 5
        self.actor.setHpr(self.teta, 0, 0)

    def accelerer(self):
        self.vitesse = self.vitesse+ 0.05

    def decelerer(self):
        self.vitesse = self.vitesse - 0.05






class ReadKeys(DirectObject.DirectObject):
    def __init__(self,app):
        self.accept("k",app.increaseR,[1])
        self.accept("t", app.increaseT, [1])


class DroneKeys(DirectObject.DirectObject):
    def __init__(self, drone):
        self.accept("z-repeat", drone.accelerer)
        self.accept("z", drone.accelerer)
        self.accept("s-repeat", drone.decelerer)
        self.accept("s", drone.decelerer)
        self.accept("q-repeat", drone.turnLeft)
        self.accept("q", drone.turnLeft)
        self.accept("d-repeat", drone.turnRight)
        self.accept("d", drone.turnRight)


# app = MyApp()
# read = ReadKeys(app)
# app.run()
