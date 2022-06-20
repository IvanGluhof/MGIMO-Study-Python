# mgimo-university-task-1
This is a repo dedicated to completing a university exam task dedicated to proving that I know how to use git.

## Недочеты

В коде почти нет никаких проверок и контроля ошибок.

## Как запустить

В данной репозитории находятся исходник (`main.go`) и кросскомпилированные версии для Windows (`main_win64.exe`), macOS (`main_darwin_x86-64`) и Linux (`main_linux_x86-64`).

При желании скомпилировать данный код самостоятельно, необходимо установить Golang (Go) версии не ниже 1.15 и запустить в данной директории следующую команду:

```
go build main.go
```

Как альтернатива, можно запустить без компиляции:

```
go run main.go
```