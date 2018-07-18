#lang racket


(define (nat-to-blist num)
  (define toblist (quotient num 10000))
  (define remainder (- num (* toblist 10000)))
  ; (printf "~a ~a\n" toblist remainder)
  
  (cond
    [(= 0 num) '()]
    [(= 0 toblist) (cons remainder '())]
    [else 
      (cons remainder (nat-to-blist toblist))]))


(define (blist-to-nat blist)
  ; (printf "~a\n" blist)
  (if (empty? blist)
      0
      (+ (car blist) (* 10000 (blist-to-nat (rest blist))))))



(define (add a b)
   ;(printf "add ~a ~a\n" a b)
  
  (cond
    [(empty? a) b]
    [(empty? b) a]
    [(>= (+ (car a) (car b)) 10000) (cons (- (+ (car a) (car b)) 10000) (add '(1) (add (cdr a) (cdr b))))]
    [else (cons (+ (car a) (car b)) (add (cdr a) (cdr b)))]))

(define (mult a b)
  ; (printf "mult ~a ~a\n" a b)
  (cond
    [(or (empty? a) (empty? b)) '()]
    [else (add (scalmult (car a) b) (cons 0 (mult (cdr a) b)))]))

(define (scalmult scaler blist)
  ;(printf "scaler ~a ~a\n" scaler blist)
  
  (cond
    [(or (= 0 scaler) (empty? blist)) '()]
    [(>= (* scaler (car blist)) 10000) (cons (modulo (* scaler (car blist)) 10000) (add (cons (quotient (* scaler (car blist)) 10000) '()) (scalmult scaler (cdr blist))))]
    [else (cons (* scaler (car blist)) (scalmult scaler (cdr blist)))]))
    




(define (multtest n)
  (define l 11)
  (define a (random l))
  (define b (random l))
  (define c (+ 9995 (random l)))
  (define d (+ 9995 (random l)))
  
  
  (cond
    [(= n 3000000) (printf "error not found\n")]
    [(= (+ (* a c) (* b d)) (blist-to-nat (add (mult (nat-to-blist a) (nat-to-blist c)) (mult (nat-to-blist d) (nat-to-blist b))))) (multtest (add1 n))]
    [else (printf "~a ~a ~a ~a\n" a c d b)]))


(define (addtest n)
  (define l 11)
  (define a (random l))
  (define b (random l))
  (define c (+ 9995 (random l)))
  (define d (+ 9995 (random l)))
  
  
  (cond
    [(= n 3000000) (printf "error not found\n")]
    [(= (+ a b c d) (blist-to-nat (add(add (nat-to-blist d) (nat-to-blist c)) (add (nat-to-blist a) (nat-to-blist b))))) (addtest (add1 n))]
    [else (printf "~a ~a ~a ~a\n" d c a b)]))