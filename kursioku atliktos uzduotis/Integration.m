function Integration

% 1. PATEIKIAMI DUOMENYS
    f = @(x) 3.*x.^3 - x + 2; % Funkcija
    a = 1; b = 3; % intervalas
    n_max = 1024; % intervalu skaicius
    n = 1;

% 2. TIKSLUS SPRENDINYS
    ats = integral(f, a, b);
    disp(['Tikslus atsakymas: ', num2str(ats)]);
    
% 3. APYTIKSLE PAKLAIDA

    function uncertainty = get_uncertainty(h, a, b)
        M = 0;
        uncertainty = M * (b-a)/180 * h^4;
    end
    
    
% 4. SIMPSONO METODAS

    disp("Intervalo dydis             |    Tarpinis rezultatas    |    Sanktikine paklaida");
    disp("--------------------------------------------------------------------------------");
    mistake = Inf; Sn = Inf; 
    mistake_vector = [];
    level = 0;
    while (n <= n_max && mistake > 10^-6)
        level = level + 1;
        h = (b - a)/n;
        xVector = a:h:b;
    
        Sn_new = h./3 .* ...
             (f(xVector(1)) + f(xVector(end))...
             + 4 * sum(f(xVector(2:2:end-1))) ...
             + 2 * sum(f(xVector(3:2:end-2))));
         mistake = abs(Sn - Sn_new);
         fprintf('intervalo dydis = %.3f \t|\t rezultatas = %.3f \t|\t santikine paklaida = %.6f\n', h, Sn_new, mistake);
         mistake_vector( end+1, : ) = [level, mistake]; 
         Sn = Sn_new;
         n = n * 2;
    end   
    disp("---------------------------------------------------------------------");
    fprintf('\t rezultatas = %.3f \t|\t santikine paklaida = %.6f\n', Sn_new, mistake);
    disp(['APYTIKSLE PAKLAIDA ', num2str(get_uncertainty(h, a, b)) ]);
    
    
% 3. GRAFIKAS  
    plot(mistake_vector(:,1), mistake_vector(:,2));
    grid on;
    xlabel('x asis');
    ylabel('y asis');
    title(['Santikiniu paklaidu grafikas']);
end