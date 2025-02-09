
class CuentaBancaria:
    def __init__(self,saldo,cliente):
        self.saldo=saldo
        self.cliente=cliente
        print (f"Cuenta '{self.cliente}' creada. Saldo = {self.saldo}€")

    def ObtenerSaldo(self):
        print (f"Saldo de la cuenta '{self.cliente}' = {self.saldo}€")
    
    def Depositar(self,cantidad):
        self.saldo+=cantidad
        print (f"Depósito de {cantidad}€ completado")

    def Retirar(self,cantidad):
        if cantidad > self.saldo:
            print (f"Retiro interrumpido: La cuenta '{self.cliente}' solo tiene un saldo de {self.saldo}€")
        else:
            self.saldo-=cantidad
            print (f"Retiro de {cantidad}€ completado")
        
    def Transferir(self,cantidad, cuenta_destino):
        print("Iniciando Transferencia...")
        if cantidad > self.saldo:
            print (f"Transferencia fallida: La cuenta '{self.cliente}' solo tiene un saldo de {self.saldo}€")
        else:
            self.Retirar(cantidad)
            self.ObtenerSaldo()
            cuenta_destino.Depositar(cantidad)
            cuenta_destino.ObtenerSaldo()
            print (f"Transferencia de {cantidad}€ a la cuenta '{cuenta_destino.cliente}' completada")

class CuentaRecompensas(CuentaBancaria): #Una subclase de CuentaBancaria que proporciona una recompensa de interés del 5% en los depósitos que hayan ingresado.
    def Depositar(self,cantidad):
        cantidad2=5*cantidad/100
        self.saldo+=cantidad2+cantidad
        print (f"Depósito de {cantidad}€ completado con recompensas de interés")

class CuentaAhorros(CuentaBancaria): #Una subclase de CuentaBancaria que agrega una tarifa de retiro de 5€ en cada transacción de retiro.
    def Retirar(self,cantidad):
        cantidad2=cantidad+5
        if cantidad > self.saldo:
            print (f"Retiro interrumpido: La cuenta '{self.cliente}' solo tiene un saldo de {self.saldo}€")
        else:
            self.saldo-=cantidad2
            print (f"Retiro de {cantidad}€ completado")
        

print(' --- CUENTA Cliente1 ---')
input("Presiona ENTER para continuar...")
Cuenta1=CuentaBancaria(1000,"Cliente1")
Cuenta1.ObtenerSaldo()
Cuenta1.Retirar(10000)
Cuenta1.Retirar(10)

print ("")
print(' --- CUENTA Cliente2 ---')
input("Presiona ENTER para continuar...")
Cuenta2=CuentaBancaria(2000, "Cliente2")
Cuenta2.ObtenerSaldo()
Cuenta2.Depositar(500)
Cuenta2.ObtenerSaldo()


print(' --- TRANSFERENCIA DE 1 A 2 ---')
input("Presiona ENTER para continuar...")
Cuenta1.Transferir(10000, Cuenta2)


print(' --- TRANSFERENCIA DE 2 A 1 ---')
input("Presiona ENTER para continuar...")
Cuenta2.Transferir(100, Cuenta1)

print("")

print(' --- CUENTA CON RECOMPENSAS ---')
input("Presiona ENTER para continuar...")
CuentaInteres = CuentaRecompensas(1000, "CuentaInteres")
CuentaInteres.ObtenerSaldo()
CuentaInteres.Depositar(100)
CuentaInteres.ObtenerSaldo()

print(' --- CUENTA AHORROS ---')
input("Presiona ENTER para continuar...")
CuentaAhorros1 = CuentaAhorros(1000, "CuentaAhorros")
CuentaAhorros1.ObtenerSaldo()
CuentaAhorros1.Depositar(100)
CuentaAhorros1.ObtenerSaldo()
CuentaAhorros1.Transferir(10000, Cuenta2)
CuentaAhorros1.Transferir(1000, Cuenta2)
