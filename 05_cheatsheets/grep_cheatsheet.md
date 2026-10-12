# Шпаргалка з grep

## Найважливіші прапорці
| Прапорець | Призначення | Приклад |
|---|---|---|
| `-E` | Extended Regex (підтримка `+`, `?`, `|`, `()` без екранування) | `grep -E "error|fail" file.log` |
| `-P` | Perl-Compatible Regex (підтримка `\d`, `\s`, lookarounds) | `grep -P "(?<=\$)\d+" file.txt` |
| `-i` | Нечутливість до регістру (case-insensitive) | `grep -i "warning" app.log` |
| `-v` | Інверсія пошуку (показати рядки, що НЕ збігаються) | `grep -v "^#" config.conf` |
| `-n` | Виводити номери рядків у файлі | `grep -n "TODO" main.py` |
| `-c` | Підрахувати кількість збігів | `grep -c "404" access.log` |
| `-o` | Виводити ТІЛЬКИ ту частину, що збіглась | `grep -oE "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+" access.log` |
| `-w` | Пошук цілого слова (word match) | `grep -w "db" code.py` |
| `-r` / `-R` | Рекурсивний пошук у директоріях | `grep -rn "FIXME" ./src/` |
| `-l` | Вивести тільки назви файлів зі збігами | `grep -rl "secret" ./codebase/` |
| `-L` | Вивести назви файлів БЕЗ збігів | `grep -rL "license" ./codebase/` |
| `-A <N>` | Показати N рядків ПІСЛЯ збігу (After) | `grep -A 3 "ERROR" app.log` |
| `-B <N>` | Показати N рядків ДО збігу (Before) | `grep -B 2 "Exception" app.log` |
| `-C <N>` | Показати N рядків контексту (Before + After) | `grep -C 2 "CRITICAL" app.log` |
| `--include` | Обмежити пошук певними файлами | `grep -rn --include="*.py" "import" .` |
