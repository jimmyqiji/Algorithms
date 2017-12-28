#lang racket

(provide my-sort)


(require "generate.rkt")

;=====================================

;; O(nlogn) because
;; each loops O(log n) and each loop takes O(n) time

;; the only purpose of this function is to pass the exploded list into function (mergeuntil) 
(define (my-sort l <)
  (generate
   l
   (lambda (x) true)
   (lambda (x) x)
   (lambda (x) (mergeuntil (explodelist l) <))))

;; takes in a list, then outputs the list with each of its elements wraped in a list
;; goes through each element in the list hence O(n)
(define (explodelist l)
  (generate
   (list l '())
   (lambda (x) (empty? (first x)))
   (lambda (x) (list (rest(first x)) (cons(list(first(first x))) (second x)))) ;; since we're only appending one thing, appened: O(1)
   (lambda (x) (second x))))


;; takes in the exploded list, then feeds it into mergesort until there's only 1 element in the list in which case, the sort is done
;; O(log n) time because we divide the list into 2s repeatedly
(define (mergeuntil lst <)
  (generate
   lst
   (lambda (x) (or (empty? x) (empty? (rest x))))
   (lambda (x) (mergesort x <))
   (lambda (x) (if (empty? x) x (first x)))))

;; repeatedly takes the first 2 elements(ordered) in the lst and put them in 1 list in order of < with the (merge) function
;; (mergesort) and (merge) together goes through every element in the list twice, hence
;; T : 2*n
;; which is still O(n)
(define (mergesort lst <)
  (generate
   (list lst '())
   (lambda (x) (or (empty? (first x)) (empty? (rest(first x))))) ;; stops if (first x) has less than 2 elements
   (lambda (x) (list (rest(rest (first x))) (cons(merge (first(first x)) (second(first x)) <) (second x)))) ;; merges the first 2 elements
   (lambda (x) (append (first x) (second x)))))


;; takes 2 lists ordered by < and group them in 1 list in order of <
(define (merge lsta lstb <)
  (generate
   (list lsta lstb '())
   (lambda (x) (or (empty? (first x)) (empty? (second x))))
   (lambda (x) (if (< (first(first x)) (first(second x))) (list (rest (first x)) (second x) (cons (first(first x)) (third x)))
                                                          (list (first x) (rest (second x)) (cons (first(second x)) (third x)))))
   (lambda (x) (cond
                 [(empty? (first x)) (reverse (everythingcons (second x) (third x)))]
                 [else (reverse (everythingcons (first x) (third x)))]))))

;; repeated cons the first element of the first list onto the second list (resulting in reversing the order)
(define (everythingcons lst1 lst2)
  (generate
   (list lst1 lst2)
   (lambda (x) (empty? (first x)))
   (lambda (x) (list (rest (first x)) (cons (first (first x)) (second x))))
   (lambda (x) (second x))))

