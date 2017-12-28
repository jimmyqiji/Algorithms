;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname Quicksort) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define-struct node (left right key))

;;(define (test (shuffle (range 1 11 1))))


(define (take lst n)
  (cond
    ;[(empty? lst) lst]
    [(zero? n) empty]
    ;[(= n 1) (cons (first lst) empty)]
    [else  (cons (first lst) (take (rest lst) (sub1 n)))]))


(define (drop lst n)
  (cond
    ;[(empty? lst) lst]
    [(zero? n) lst]
    ;[(= n 1) (rest lst)]
    [else (drop (rest lst) (sub1 n))]))

(define (swap lst pos1 pos2) ;pos1<pos2
  (append (take lst pos1) (list (list-ref lst pos2)) (drop (take lst pos2) (add1 pos1)) (list (list-ref lst pos1)) (drop lst (add1 pos2))))
(define (order2 lst)
  (cond
    [(< (second lst) (first lst)) (cons (second lst) (cons (first lst) '()))]
    [else lst]))


(define (quicksort lst)
  (cond
    [(empty? lst) lst]
    [(= (length lst) 1) lst]
    [(= (length lst) 2) (order2 lst)]
    [else (iter lst 1 (sub1 (length lst)) 0)]))
(define (iter lst l r pivot)
  (cond
    [(> l r) (append (quicksort (drop (take lst l) 1)) (list (first lst)) (quicksort (drop lst (add1 r))))]
    [(< (list-ref lst l) (list-ref lst pivot)) (iter lst (add1 l) r pivot)]
    [(> (list-ref lst l) (list-ref lst pivot)) (iter-r lst l r pivot)]
    [else (append (quicksort (take lst r)) (drop lst r))]))


(define (iter-r lst l r pivot)
  (cond
    [(> l r) (append (quicksort (drop (take lst l) 1)) (list (first lst)) (quicksort (drop lst (add1 r))))]
    [(> (list-ref lst r) (list-ref lst pivot)) (iter-r lst l (sub1 r) pivot)]
    [(< (list-ref lst r) (list-ref lst pivot)) (iter (swap lst r l) l r pivot)]
    [else (cons (first lst) (quicksort (rest lst)))]))

