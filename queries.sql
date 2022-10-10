------------------------------------------------------------------------------------------------
--Qual foi o total de casos de covid por região?

SELECT
	regiao,
    SUM(casos_acumulados) as total_casos
FROM
	covid_regiao_periodo
GROUP BY
	regiao
ORDER BY
	SUM(casos_acumulados) DESC;
	
------------------------------------------------------------------------------------------------
--Qual UF foi mais impactada por novos casos de covid em Agosto de 2020?

SELECT 
    t1.uf,
    SUM(t2.casos_novos) as novos_casos
FROM
	regiao as t1
JOIN
	historico_covid as t2
WHERE 
	t2.cod_uf = t1.codigo_uf and
	YEAR(data) = 2020 and
    MONTH(data) = 08
GROUP BY
	t1.uf
ORDER BY
	SUM(t2.casos_novos) DESC

------------------------------------------------------------------------------------------------
--Quais regiões tiveram as maiores quantidade de óbitos em Setembro de 2020?

SELECT
    regiao,
    SUM(obitos_acumulados) as obitos_acumulados
FROM
	covid_regiao_periodo
WHERE 
	YEAR(data) = 2020 and
    MONTH(data) = 09
GROUP BY
	regiao
ORDER BY
	SUM(obitos_acumulados) DESC;

------------------------------------------------------------------------------------------------
--Qual foi o ranking de novos casos por governador no 4T de 2020?

SELECT 
    t1.governador,
	SUM(t2.casos_novos) as novos_casos
FROM
	regiao as t1
JOIN
	historico_covid as t2
WHERE 
	t2.cod_uf = t1.codigo_uf and
	YEAR(data) = 2020 and
    MONTH(data) in (10,11,12)
GROUP BY
	t1.governador
ORDER BY
	SUM(t2.casos_novos) DESC;

------------------------------------------------------------------------------------------------
--Qual está sendo a 3a Região mais afetada por novos óbitos em 2021?

SELECT 
    t2.regiao,
    SUM(t2.obitos_novos) as novos_obitos
FROM
	regiao as t1
JOIN
	historico_covid as t2
WHERE 
	t2.cod_uf = t1.codigo_uf and
	YEAR(data) = 2021
GROUP BY
	t2.regiao
ORDER BY
	SUM(t2.obitos_novos) DESC
limit 2,1;
------------------------------------------------------------------------------------------------

