def infinito(**kargs):
    for karg in kargs:
        print(karg, '---->', kargs[karg])

infinito(a="Hola", b=20, c=["Maria", "Pedro", "Jose"])