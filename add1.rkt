#lang lazy









((λ(f) ((λ(x)(f (x x)))(λ(x)(f (x x))))) ;; Y combinator, pass ADD1 to itself
 (λ (ADD1) 
   (λ (n) 
     (((n (λ (idk) (λ(wtf) (λ (f) (λ (ff) ff))))) ;; if n is empty
       (λ(cons) ((cons (λ (t) (λ (tt) t))) (λ (x) (λ (t) (λ (tt) t)))))) ;; then make it 1
      (((n (λ (t) (λ (tt) t))) ;; otherwise n is not empty and last digit is 1
        (λ (cons) ((cons (λ (f) (λ (ff) ff))) (ADD1 (n (λ (f) (λ (ff) ff))))))) ;; the last digit becomes 0 and the others inherit 1
       (λ (cons) ((cons (λ (t) (λ (tt) t))) (n (λ (f) (λ (ff) ff))))))))) ;; otherwise if last digit is 0, make that 1
 )











