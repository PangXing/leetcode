# coding:utf-8
'''
【1014. 最佳观光组合】
给定正整数数组 A，A[i] 表示第 i 个观光景点的评分，并且两个景点 i 和 j 之间的距离为 j - i。
一对景点（i < j）组成的观光组合的得分为（A[i] + A[j] + i - j）：景点的评分之和减去它们两者之间的距离。
返回一对观光景点能取得的最高分。

示例：
输入：[8,1,5,2,6]
输出：11
解释：i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
 
提示：
2 <= A.length <= 50000
1 <= A[i] <= 1000

'''
class Solution(object):
    def maxScoreSightseeinPair1(self, A):
        dp = list()
        for row in range(len(A)):
            dp.append(list())
            for col in range(len(A)):
                dp[row].append(0)

        max_score = 0
        for row in range(len(A)):
            for col in range(row+1, len(A)):
                dp[row][col] = max(dp[row][col-1], A[row]+A[col]+row - col)
                if dp[row][col] > max_score:
                    max_score = dp[row][col]
        return max_score

    def maxScoreSightseeinPair(self, A):
        '''
        pre_max = A[i] + i 
        score = pre_max + A[j] - j
        '''
        pre_max = A[0] + 0
        res = 0
        for j in range(1, len(A)):
            res = max(res, pre_max + A[j] - j)
            pre_max = max(pre_max, A[j]+j)
        return res


if __name__ == '__main__':
    solution = Solution()
    A = [627,377,25,528,925,381,126,887,296,105,90,189,750,821,798,543,767,825,473,517,381,804,498,753,750,865,894,843,
         919,897,602,527,753,66,990,536,254,162,619,82,975,582,591,459,281,641,353,802,455,492,646,164,563,242,820,931,
         852,513,786,641,820,287,804,785,797,597,791,690,110,448,176,688,119,931,878,811,486,685,129,195,551,724,889,986,
         168,295,140,446,267,660,874,665,396,847,306,764,994,652,17,235,270,692,39,91,876,459,836,323,120,401,842,355,111,
         230,47,365,755,856,348,753,317,325,359,608,949,282,409,300,292,961,689,439,748,936,212,834,314,436,135,414,804,349,820,115,284,781,714,384,971,820,899,19,248,279,260,816,309,712,709,231,199,244,718,450,763,292,33,322,319,436,206,293,594,488,245,160,223,447,373,845,338,708,705,136,908,201,893,674,312,380,729,575,680,886,486,337,310,689,62,186,469,257,855,548,590,918,533,208,787,394,647,696,834,564,965,290,443,167,62,364,252,765,200,358,241,379,616,876,43,656,434,508,756,450,226,882,575,650,803,552,313,300,932,188,418,352,215,512,741,996,440,759,485,799,357,783,19,502,461,25,349,102,372,534,591,180,16,388,971,731,618,438,509,916,367,219,751,920,693,731,932,497,327,753,636,89,338,873,776,61,405,353,272,258,562,726,231,868,623,302,97,35,66,341,336,529,975,876,590,59,47,363,404,903,314,671,323,582,397,529,393,734,529,440,116,851,283,600,461,400,258,489,551,136,270,694,176,184,383,119,837,163,738,993,146,331,329,438,68,618,741,974,421,662,436,168,279,886,53,871,758,521,921,533,513,222,467,819,17,437,707,667,4,495,484,262,831,996,425,577,4,555,542,831,275,105,67,927,465,756,668,495,962,343,105,428,980,711,461,480,56,487,98,377,164,32,823,516,441,668,269,932,961,796,68,758,614,617,323,114,659,902,142,456,822,456,659,726,113,490,878,985,904,473,302,905,396,156,544,868,431,204,300,306,633,368,131,471,505,12,151,898,109,620,475,405,734,674,128,384,943,670,647,853,356,99,667,381,531,713,987,321,604,96,781,123,970,889,315,638,430,957,972,579,695,219,87,573,223,937,387,305,581,753,228,200,70,642,689,916,666,691,278,155,274,697,983,188,268,406,836,731,156,692,779,348,769,148,495,309,891,65,227,332,514,609,555,782,500,662,731,393,385,487,266,490,328,319,301,902,610,606,593,282,366,742,749,21,25,894,482,45,208,720,198,544,681,228,885,674,843,322,907,503,911,249,835,751,479,268,347,428,616,883,519,453,307,703,34,382,685,62,299,807,468,211,900,803,789,76,511,711,522,789,714,842,246,475,617,550,247,311,883,798,144,339,385,999,45,840,170,38,340,480,43,219,122,939,308,908,924,765,970,357,418,452,676,975,983,94,433,310,667,993,462,690,106,187,179,108,803,596,625,185,962,215,630,692,4,564,658,65,7,967,485,658,579,213,887,783,535,25,853,223,551,734,207,323,517,325,762,647,574,477,690,953,506,269,101,63,341,822,632,774,169,217,815,86,365,764,235,558,328,253,12,113,400,74,924,785,654,297,833,42,844,733,675,398,258,224,656,765,197,905,276,155,610,530,875,700,718,972,900,391,402,465,794,162,466,981,969,706,734,856,759,635,318,958,421,111,602,998,405,257,71,41,39,565,80,733,465,955,237,164,433,380,651,868,144,776,63,313,264,541,398,386,68,414,995,756,711,44,24,855,241,483,956,464,506,477,613,741,978,717,830,933,216,148,554,57,438,657,307,564,605,668,120,799,418,100,548,641,293,104,612,380,277,537,822,145,876,9,968,302,35,258,779,209,823,506,769,238,597,337,576,482,128,176,549,242,926,533,674,460,526,449,121,427,162,189,347,254,259,679,363,885,50,108,109,301,60,883,243,35,836,988,493,776,205,909,731,794,867,135,104,449,455,863,381,996,339,966,850,290,347,195,327,366,837,100,31,293,280,820,411,712,437,736,362,177,767,294,731,364,339,168,77,718,870,63,221,331,800,270,271,49,511,429,245,519,798,845,783,542,778,330,489,835,248,657,735,355,985,168,547,135,366,488,714,279,986,370,734,903,760,915,428,749,371,576,959,794,226,781,26,329,998,698,604,264,775,213,977,309,558,92,31,885,291,608,695,852,690,975,665,997,49,461,445,639,976,531,238,223,223,276,454,996,491,622,767,106,554,205,694,57,992,425,225,214,502,407,449,698,784,242,16,542,5,815,473,885,985,391,322,565,807,444,142,288,816,158,323,230,276,907,864,941,73,580,801,818,436,484,892,350,989,316,818,6,312,196,276,993,737,161,399,994,56,481,812,483,280,662,303,523,958,69,611,53,573,744,208,2,872,718,702,495,907,522,959,277,985,466,298,291,225,574,126,261,837,384,781,298,867,381,588,550,413,177,281,812,622,987,347,177,2,585,962,633,863,439,798,825,586,8,545,646,813,159,449,126,950,671,723,610,883,77,61,220,721,451,506,765,642,699,432,870,109,410,956,578,380,724,598,42,856,239,808,881,657,799,467,992,174,826,41,727,823,835,715,838,859,265,10,414,213,335,75,54,842,773,38,759,446,962,96,877,335,655,236,434,213,437,931,630,227,358,572,739,745,398,439,664,782,908,36,228,679,464,100,497,555,797,943,154,818,993,102,149,779,672,787,791,731,560,315,436,70,971,999,807,971,699,402,426,209,796,48,895,467,482,703,561,215,532,966,24,4,10,40,321,993,192,495,998,839,124,966,579,52,984,893,953,288,545,750,825,247,184,950,786,160,262,65,594,509,280,255,962,85,500,486,144,217,831,4,944,720,74,689,704,111,396,239,901,203,21,940,358,428,321,586,192,770,288,306,484,122,584,402,422,159,381,138,477,276,95,331,542,1000,402,789,358,745,538,307,77,40,826,323,129,817,567,473,482,42,344,823,1,701,496,905,693,62,66,293,296,472,906,948,949,853,596,360,724,188,329,591,481,569,320,54,985,134,12,72,653,263,189,637,931,683,632,33,98,134,460,729,283,897,407,82,365,522,164,641,528,500,620,863,12,12,611,89,628,687,203,861,126,341,514,541,114,279,439,501,551,62,458,858,39,107,821,716,22,174,165,335,480,722,979,307,127,179,142,627,500,438,292,259,913,993,295,394,959,711,877,958,113,566,417,19,573,995,13,592,379,640,115,324,746,420,15,712,314,901,618,287,560,306,258,663,812,528,647,89,534,943,523,622,100,261,581,695,163,807,456,525,363,698,293,436,724,359,305,231,75,847,897,845,150,10,842,355,883,614,670,354,702,901,778,322,370,568,682,605,170,284,99,1,719,446,926,336,280,1,967,168,436,763,853,805,275,24,929,852,636,531,410,628,300,517,453,143,715,275,451,592,879,153,805,470,78,703,793,725,993,694,407,615,658,559,169,853,122,590,305,301,43,821,822,18,757,637,572,825,131,261,799,231,665,186,611,758,116,16,509,478,481,840,954,923,553,472,455,655,273,527,345,462,540,77,472,475,758,631,585,205,128,308,64,355,220,710,338,441,561,469,107,197,330,609,193,925,410,572,670,947,311,317,60,791,941,540,627,924,671,26,564,235,460,953,137,733,237,738,771,607,411,480,36,119,406,813,609,770,252,114,817,785,874,116,725,703,769,68,156,34,61,273,768,260,77,77,245,27,192,755,202,559,486,50,921,509,304,417,794,655,881,86,638,576,653,461,472,861,939,980,821,530,584,306,186,737,660,538,616,221,255,653,115,755,389,64,847,54,385,209,721,251,771,622,839,846,68,388,966,589,529,578,278,678,728,888,804,386,723,431,847,202,708,106,214,580,143,925,41,595,521,601,209,261,14,216,760,995,812,538,389,365,930,931,850,628,408,590,372,193,176,28,717,552,759,500,250,957,342,803,831,878,726,850,825,282,637,1000,236,227,646,118,71,624,195,779,702,821,695,70,320,750,231,639,222,567,763,693,19,560,800,864,645,826,984,719,752,993,548,348,935,770,133,16,670,406,494,135,431,779,234,721,105,557,767,934,153,788,868,275,295,683,420,766,393,319,952,448,731,849,47,729,3,633,598,499,777,906,933,910,663,27,14,575,916,881,517,478,763,630,26,198,4,436,815,735,290,942,760,395,299,721,674,916,287,121,793,59,980,932,202,945,618,598,413,468,58,605,653,298,858,528,971,685,378,970,343,270,777,74,74,230,123,567,752,558,935,243,312,216,174,413,577,541,126,703,276,288,374,339,67,469,296,622,118,669,314,874,386,306,199,168,259,589,983,729,340,82,321,266,239,316,943,849,403,369,406,88,990,189,123,966,410,832,669,836,701,274,263,484,595,515,468,703,328,740,672,84,311,378,631,716,31,410,127,511,65,909,332,852,434,847,356,100,454,176,712,711,992,760,284,239,508,122,23,674,800,374,251,283,777,430,906,932,498,270,392,568,679,285,997,931,236,187,586,109,353,531,690,644,666,512,337,717,955,751,99,501,743,332,383,652,885,996,428,281,2,902,890,175,885,901,818,670,160,253,624,619,424,657,306,348,744,389,569,90,116,854,766,240,693,770,614,652,312,291,701,769,297,199,180,970,18,741,75,23,111,110,43,471,510,980,250,922,971,330,843,451,301,731,878,12,902,785,604,808,455,322,388,820,56,353,755,727,643,292,560,258,206,728,613,323,287,947,314,337,843,52,18,999,488,560,445,360,58,266,21,91,44,158,79,94,15,848,252,834,695,286,317,562,266,184,42,889,502,473,617,189,796,274,849,559,639,470,123,549,257,44,914,576,235,897,543,654,597,837,174,57,431,332,787,243,574,649,881,873,525,154,761,63,316,781,988,261,893,401,759,805,29,675,557,977,938,47,538,354,973,190,710,695,928,619,736,933,442,583,436,902,754,869,11,122,353,873,981,439,970,263,995,364,115,780,314,446,219,626,425,945,437,49,253,192,63,487,204,429,722,610,759,722,829,666,312,229,80,528,241,936,4,459,326,35,775,604,552,592,92,107,204,398,307,205,649,480,236,22,795,79,403,263,456,228,604,449,224,303,196,291,155,1000,148,183,615,300,841,144,199,860,187,66,875,75,812,903,660,108,110,65,693,472,916,416,583,481,900,412,995,904,744,127,189,670,792,358,47,325,39,126,661,609,220,436,579,290,77,732,475,650,339,824,596,362,229,690,644,302,283,323,792,802,124,879,124,189,326,402,356,836,583,819,812,4,226,193,721,253,695,616,765,908,172,338,999,692,789,607,661,785,780,936,751,421,581,337,821,38,163,939,7,991,705,95,40,268,366,125,754,949,287,372,20,596,120,983,408,905,548,318,890,464,920,226,503,417,2,886,70,765,301,652,182,632,422,196,331,85,688,561,590,387,775,567,107,147,457,647,302,235,702,344,928,913,59,795,292,877,439,93,636,104,978,172,36,699,29,364,613,489,562,305,25,277,704,224,682,237,873,753,706,998,9,995,588,681,518,734,619,981,420,708,832,486,107,495,105,36,243,947,864,284,821,486,622,789,169,920,436,148,87,352,476,526,459,268,453,591,921,255,644,299,145,547,898,54,299,598,164,479,670,482,919,840,640,120,426,514,347,632,551,131,372,811,782,511,241,719,28,609,553,619,672,308,270,122,633,9,664,870,885,755,313,315,982,774,645,828,363,875,557,278,254,216,993,65,766,891,816,70,902,372,497,934,209,459,989,25,244,838,939,459,575,256,259,158,576,705,27,756,600,838,660,672,163,480,702,385,151,549,211,540,13,527,976,730,691,454,560,813,962,438,958,433,197,89,457,242,185,761,49,409,855,353,989,846,141,778,274,46,219,504,592,643,637,643,168,55,246,594,778,319,818,834,911,560,811,986,710,971,474,990,742,876,624,577,99,281,316,454,609,642,128,223,966,745,930,784,23,940,426,763,515,239,836,359,862,347,537,737,231,616,382,869,894,598,422,984,986,252,801,683,440,971,440,189,754,141,412,562,202,993,538,602,783,192,514,912,438,273,187,536,825,637,845,663,818,514,767,638,121,728,60,460,679,205,256,645,411,298,295,938,345,958,348,438,290,573,13,751,207,947,684,850,376,828,988,559,820,590,816,9,268,676,907,223,45,569,636,543,942,378,332,247,113,821,632,921,135,149,135,800,308,19,626,156,977,450,611,895,139,806,84,985,584,808,724,664,98,151,408,225,824,834,847,690,998,978,916,611,291,15,124,207,613,217,404,198,268,625,94,741,90,510,182,603,247,265,400,916,546,708,767,45,578,683,338,100,889,840,666,981,840,977,956,526,992,261,638,260,578,491,444,296,897,868,71,748,533,988,743,775,735,626,714,875,902,927,816,798,422,258,690,361,976,615,982,311,277,714,961,452,916,245,413,499,225,836,285,987,931,933,365,387,916,884,726,350,851,949,909,297,706,748,987,569,612,877,480,25,930,833,570,100,475,256,884,946,646,320,550,496,687,84,757,8,798,674,343,22,790,685,205,726,165,108,139,885,83,178,809,174,384,298,95,63,340,366,519,862,628,280,405,259,710,202,207,988,601,444,384,883,414,883,24,249,790,53,220,545,668,425,76,968,179,269,673,264,197,794,150,116,262,245,671,184,140,196,594,389,616,615,678,287,876,667,910,881,274,809,857,398,905,152,507,688,223,292,562,304,583,571,987,552,789,191,19,997,195,296,982,907,653,295,59,427,732,657,479,705,424,162,181,652,271,995,60,131,17,801,886,697,559,956,235,447,73,600,356,895,196,729,656,875,537,171,530,814,461,470,557,841,965,554,812,73,206,302,350,667,947,18,975,617,999,224,548,461,742,80,666,289,198,37,828,307,782,607,40,563,210,122,204,392,922,557,629,71,717,763,910,270,345,597,416,771,872,779,756,250,49,441,5,560,368,275,16,175,848,679,903,889,350,542,803,151,971,480,178,265,116,829,954,438,597,967,158,794,555,51,975,755,253,472,356,793,288,540,414,570,215,314,518,681,36,546,193,795,100,798,196,899,795,156,992,212,911,336,241,608,51,774,450,571,881,548,696,549,944,986,533,814,684,148,600,602,264,364,699,344,552,397,430,750,497,194,131,915,541,61,704,691,265,825,112,611,742,646,211,393,419,275,411,402,920,47,783,415,775,814,268,504,634,14,594,415,759,685,3,33,304,854,161,121,268,143,694,177,862,684,527,195,985,431,812,848,339,515,546,684,501,935,531,35,921,725,484,714,503,14,188,925,208,309,862,933,167,96,120,655,325,167,733,696,174,976,292,285,543,767,5,925,253,623,416,681,848,504,922,34,226,59,768,108,421,779,901,379,335,4,896,565,530,907,702,928,610,829,563,834,802,618,950,859,628,747,66,656,888,789,416,489,661,56,453,154,318,456,386,132,708,122,493,810,515,489,317,220,717,936,573,159,646,94,152,847,37,602,525,155,866,527,71,851,929,463,113,472,859,866,994,287,729,232,830,970,240,585,654,174,931,275,612,820,532,849,335,374,967,553,495,158,932,211,694,913,125,937,322,200,78,603,263,286,523,993,183,943,884,759,581,923,722,882,220,114,507,734,119,368,411,462,901,129,45,875,297,403,824,177,483,790,704,979,112,543,501,749,296,966,664,984,145,899,440,232,513,965,204,521,95,432,597,435,972,820,299,497,58,571,185,29,474,1000,391,940,589,739,543,673,833,95,720,625,702,722,16,839,593,627,233,523,105,689,879,779,669,514,594,333,943,547,464,576,843,633,214,375,556,775,615,608,304,973,436,93,759,528,68,412,227,181,360,696,965,362,64,186,446,480,180,297,593,614,140,939,699,408,247,723,343,213,689,557,700,235,485,830,321,836,853,967,695,602,295,858,470,914,981,705,696,160,46,638,320,795,619,714,459,720,523,732,402,473,897,585,695,610,64,500,886,50,899,596,291,917,960,693,617,756,244,178,75,719,992,416,879,938,706,231,738,583,526,877,705,204,800,225,887,567,518,297,358,803,713,830,134,415,293,891,888,697,383,639,778,732,187,861,573,949,726,223,266,92,633,836,335,226,117,623,209,954,261,277,107,729,859,766,550,494,626,433,149,36,278,62,178,936,743,102,745,97,189,571,456,973,765,355,267,795,866,882,549,984,56,786,434,687,246,256,144,913,334,587,939,869,161,772,49,472,940,703,937,198,971,871,115,636,48,167,300,112,764,774,799,637,174,39,828,264,78,458,47,99,614,650,395,650,352,753,335,563,96,675,720,846,230,99,396,38,286,136,603,198,432,959,754,194,846,643,661,869,852,299,43,34,829,265,495,10,123,517,342,73,699,134,483,407,186,902,346,120,148,793,840,115,390,145,508,180,554,846,551,461,520,165,84,204,876,657,858,338,85,387,585,956,355,334,343,702,970,455,923,116,208,92,790,726,33,689,973,353,50,867,406,634,279,705,507,917,889,651,226,781,108,506,33,544,233,679,572,137,515,275,367,434,418,514,740,642,230,82,66,219,289,615,121,251,475,769,485,754,582,144,948,542,663,558,948,52,237,1000,890,979,853,155,539,493,971,955,161,628,644,164,563,290,266,409,860,857,3,794,882,314,45,537,642,316,799,690,218,989,886,128,995,602,494,997,734,697,536,805,550,232,64,615,807,725,450,869,600,322,616,444,307,854,303,118,168,644,62,610,165,884,611,30,778,404,959,3,534,123,7,627,164,8,687,841,54,703,471,461,550,865,101,843,89,542,893,884,664,994,931,357,923,298,509,370,727,258,525,520,659,860,240,280,406,217,688,166,685,798,232,650,277,358,261,392,880,653,936,129,424,441,277,478,731,905,640,937,788,982,604,391,60,411,315,185,213,373,400,178,708,983,8,82,886,304,567,947,328,538,45,315,810,192,648,994,778,590,796,19,730,942,768,950,641,268,217,796,159,122,327,765,245,560,832,463,544,352,718,227,264,276,385,184,940,528,704,302,680,228,504,838,509,767,970,724,416,539,206,875,150,360,679,747,76,600,709,225,890,551,73,950,109,721,666,468,703,920,218,823,660,353,156,263,168,925,549,436,759,238,695,353,617,200,484,35,329,416,438,928,314,816,62,881,454,35,929,751,547,624,33,330,559,925,511,304,836,460,500,274,147,817,811,494,938,526,876,711,822,237,224,330,831,341,165,47,420,597,105,655,997,58,321,619,370,681,439,914,875,597,939,745,196,7,279,852,49,514,785,918,259,342,945,259,629,37,148,90,357,796,301,436,97,849,856,669,145,677,361,219,99,852,865,203,446,670,73,288,544,730,13,826,982,548,934,657,99,63,365,21,530,53,360,249,392,260,914,717,934,365,850,306,812,434,104,598,839,474,547,186,585,622,844,240,666,810,888,187,609,428,695,11,455,863,284,809,571,594,986,664,170,69,381,154,30,499,573,304,684,15,180,586,54,906,525,582,124,195,677,204,242,327,30,724,809,825,47,265,211,929,411,912,913,839,1,173,854,650,801,929,791,90,912,853,282,908,72,797,561,718,289,758,840,211,525,791,14,195,723,655,431,441,37,652,209,646,849,424,270,571,116,525,931,701,40,798,794,731,739,800,146,374,972,578,142,282,466,825,603,5,194,792,157,775,233,356,931,360,897,559,378,22,457,478,335,643,849,640,806,250,504,592,521,811,221,31,999,742,877,827,658,653,500,939,557,266,493,452,34,133,626,106,264,193,148,287,867,231,850,910,66,416,864,789,994,725,570,674,132,739,861,736,317,394,75,587,736,281,978,687,584,707,646,22,516,637,402,54,213,252,756,98,51,338,328,985,222,214,998,197,534,89,18,799,191,211,3,897,669,728,98,47,132,990,277,820,557,268,699,839,824,462,737,110,63,322,846,835,792,150,44,153,756,389,323,532,846,931,973,49,510,386,121,401,190,366,958,700,172,418,253,19,519,677,317,176,197,961,5,485,721,246,544,385,352,650,101,416,693,113,702,488,996,266,270,73,416,166,2,300,568,367,16,460,502,46,77,808,457,437,685,707,859,296,854,916,980,24,692,432,198,405,901,286,291,578,232,590,411,651,261,169,109,326,825,98,422,920,497,131,146,45,235,193,213,261,174,496,228,163,361,449,47,680,172,333,636,878,871,619,907,272,396,325,110,168,708,683,766,694,899,912,565,199,945,562,317,732,681,426,220,534,171,187,504,239,817,532,522,77,955,85,406,453,749,494,239,388,511,396,152,808,588,896,221,548,39,118,483,130,398,146,376,284,941,473,851,687,485,410,933,60,458,926,908,339,447,348,502,406,166,768,713,674,357,173,189,101,622,124,740,182,514,304,852,580,272,435,381,207,611,145,529,957,41,831,883,41,989,532,231,614,368,139,865,601,196,56,585,502,487,500,412,508,444,984,369,519,115,701,791,834,198,697,344,720,369,197,186,987,357,101,770,143,721,361,138,669,764,84,783,588,8,618,432,661,626,351,207,727,908,541,909,406,186,120,898,724,247,618,504,595,761,693,789,648,345,848,238,954,924,692,123,837,701,745,467,460,612,765,558,381,225,48,157,771,765,719,200,342,447,503,41,847,506,811,655,916,534,637,475,879,68,918,85,669,118,360,815,128,860,5,424,203,586,199,124,321,359,687,250,403,30,805,601,127,520,708,215,59,187,32,788,595,521,211,988,715,47,865,861,769,673,657,943,959,206,621,451,861,423,375,61,219,34,892,493,708,618,636,470,63,525,855,729,791,379,664,157,104,398,261,321,121,131,927,663,947,696,945,552,663,601,537,578,135,437,396,557,655,930,366,706,937,855,523,265,268,313,16,496,813,752,337,654,80,793,977,373,233,682,722,921,504,706,903,302,147,182,920,154,907,84,82,772,923,568,969,917,121,808,36,932,327,214,593,158,874,889,45,86,462,456,752,359,522,759,614,10,440,832,868,720,988,427,366,325,378,728,229,910,792,77,388,183,462,469,93,575,47,33,628,26,975,287,711,913,397,474,495,797,611,827,973,533,93,480,637,850,611,557,249,972,890,309,840,568,655,288,910,563,569,778,675,214,692,748,332,901,892,421,661,648,936,201,819,778,65,537,407,896,102,321,796,715,256,526,508,977,292,821,557,913,798,54,695,690,990,749,963,170,266,379,403,957,585,569,812,601,721,254,5,325,400,812,16,618,660,770,415,624,493,177,320,692,206,417,156,84,448,355,247,752,281,799,599,477,537,698,817,196,638,163,56,682,549,13,193,855,773,213,946,381,721,163,778,106,743,97,240,278,361,402,715,973,931,643,107,517,351,645,968,308,349,592,324,637,846,986,515,191,838,141,122,555,126,46,673,425,726,307,381,119,186,80,378,729,25,32,470,2,52,545,979,219,56,274,97,228,263,644,114,412,617,219,586,454,939,488,139,151,717,353,999,501,627,825,796,132,746,188,259,530,606,168,988,222,955,172,59,869,747,959,115,510,84,921,343,915,686,309,915,657,931,881,567,772,479,217,531,134,597,863,627,99,554,457,383,271,507,383,218,660,338,496,601,48,683,36,736,911,332,530,209,661,690,250,737,2,145,598,291,332,77,305,966,655,145,484,689,659,60,675,713,73,43,826,688,612,649,872,739,551,791,941,162,630,109,146,8,422,597,119,425,287,222,673,934,434,117,900,850,241,194,182,515,258,13,352,558,507,659,164,998,794,940,857,111,220,470,49,684,446,448,927,897,191,548,697,385,700,738,357,425,275,500,231,298,220,743,16,160,329,787,563,385,304,764,567,807,437,427,547,17,591,466,674,210,751,234,111,801,726,814,390,682,949,638,345,985,588,752,232,88,979,165,677,839,128,965,783,52,30,737,456,594,321,205,891,728,178,751,313,925,575,102,889,91,908,398,539,477,169,797,384,103,375,848,998,901,682,218,22,207,935,385,629,951,967,22,561,101,601,419,157,213,231,760,821,653,182,577,747,887,680,898,621,372,510,635,302,11,48,860,678,546,995,632,385,541,802,641,252,539,226,358,942,112,277,328,517,449,606,451,414,132,269,687,869,237,956,371,269,456,164,389,710,95,578,489,224,15,280,738,121,431,104,632,705,112,788,445,139,645,924,51,955,191,610,829,732,45,9,431,10,187,269,778,531,664,362,73,818,909,896,473,702,49,904,212,120,244,656,27,163,221,100,794,860,606,330,213,327,577,330,664,500,986,102,692,717,749,358,825,306,118,803,914,350,632,564,943,690,199,109,226,867,764,236,314,896,916,181,631,392,659,409,739,747,32,833,736,881,132,190,723,771,402,917,826,618,164,952,178,24,537,853,835,408,462,387,162,96,276,602,418,494,722,876,877,798,487,112,99,842,453,967,210,195,176,31,386,839,259,816,753,698,407,824,508,568,863,279,588,918,3,433,836,174,16,737,435,117,428,259,962,80,530,8,712,421,542,987,180,270,400,467,220,181,763,864,164,980,696,92,770,924,573,709,811,120,466,107,824,917,686,274,106,590,614,685,890,310,878,408,337,212,28,454,596,365,690,257,940,296,51,572,635,948,856,447,595,976,354,872,96,724,635,778,823,181,974,79,452,721,685,687,767,840,156,759,373,940,615,999,720,844,341,131,726,983,377,889,282,204,742,679,354,711,284,902,707,20,179,94,932,238,739,105,65,550,917,51,953,432,721,618,493,929,239,612,30,949,888,474,212,802,592,623,891,749,99,573,995,888,127,184,944,223,204,822,647,548,301,34,526,485,498,834,672,105,778,186,396,18,982,368,410,311,440,926,540,775,207,627,335,60,448,574,574,572,428,386,288,420,877,55,382,912,706,455,510,423,124,14,867,691,851,269,422,520,937,759,342,16,846,543,603,790,121,395,377,601,599,214,210,572,14,516,399,597,303,327,307,619,95,312,762,892,53,139,315,170,105,323,409,410,123,697,266,783,574,873,934,758,152,800,716,159,158,717,142,615,264,393,179,41,10,431,132,461,649,499,281,456,797,812,654,900,775,335,874,710,668,770,643,211,364,996,231,840,573,937,723,732,798,254,71,141,316,982,172,621,740,929,552,210,912,857,896,260,972,839,389,717,575,532,721,290,555,273,673,937,639,904,30,885,375,697,684,732,811,921,162,67,417,397,159,422,193,648,640,138,412,682,823,598,907,364,120,863,801,692,675,926,158,621,590,735,670,743,134,661,245,336,543,194,813,324,567,402,742,106,698,421,780,939,765,303,706,212,144,17,484,463,166,897,206,397,636,277,845,475,320,261,664,758,699,748,769,259,559,571,522,393,721,298,848,10,625,417,962,269,280,1,320,963,502,339,534,921,395,67,211,909,94,584,1000,176,532,193,846,575,562,194,993,402,790,499,465,284,706,361,173,66,882,723,101,47,221,878,536,64,491,628,839,52,803,815,649,951,464,242,790,473,830,5,497,185,267,764,459,604,994,878,115,355,680,588,785,201,510,20,207,777,961,309,975,269,987,360,140,490,785,385,446,901,568,820,566,419,372,877,278,253,110,576,72,967,100,341,402,373,329,547,875,903,538,98,784,112,327,613,507,870,796,189,208,554,586,445,736,854,284,676,691,813,739,241,776,551,700,841,495,815,333,543,26,20,153,490,690,822,159,140,982,294,839,193,417,483,510,462,607,939,640,897,898,186,102,36,632,667,57,740,676,725,640,82,79,460,99,61,645,655,793,681,150,148,397,568,631,375,58,59,464,766,785,920,289,161,850,87,975,105,861,469,944,270,426,461,820,805,74,498,603,800,758,349,848,432,579,337,490,230,979,123,524,880,554,431,703,619,266,408,789,537,322,838,216,680,146,566,507,108,830,484,688,907,6,170,342,538,528,446,403,335,369,426,924,114,530,790,542,317,572,976,559,242,798,108,425,366,596,355,488,87,973,879,169,109,395,275,609,243,343,570,518,20,346,552,522,226,723,874,896,893,708,187,807,888,711,252,258,613,113,151,39,421,975,89,557,149,127,396,840,972,681,71,101,323,156,588,801,554,805,90,949,173,427,71,406,433,58,976,682,372,379,171,566,586,317,898,493,129,477,87,304,627,240,794,598,221,176,136,458,756,831,745,28,154,998,960,337,441,683,528,196,307,117,17,969,365,81,282,957,731,761,814,398,87,194,170,321,724,554,328,181,828,432,531,883,695,88,875,946,608,495,547,744,302,614,531,572,667,859,64,857,163,131,554,161,689,556,596,687,173,510,748,221,258,966,684,14,679,394,174,95,868,602,763,997,79,876,176,165,769,38,517,701,674,678,421,728,137,427,161,907,995,772,792,269,455,766,163,170,252,384,241,844,638,397,919,77,353,424,19,402,472,314,976,785,363,715,276,884,953,444,346,474,591,550,596,211,318,883,755,162,909,866,252,265,660,447,912,915,41,199,300,978,910,529,313,616,334,957,246,120,180,648,684,238,347,460,394,402,623,679,291,323,882,421,178,489,715,646,432,503,254,39,214,773,967,334,95,126,286,370,476,549,814,16,126,573,156,436,774,736,166,60,991,43,777,934,577,35,976,327,723,390,89,755,122,906,407,186,734,404,926,481,614,264,723,461,903,943,494,687,442,50,202,837,858,630,215,94,418,260,337,966,237,847,437,516,694,265,533,43,396,606,909,921,632,621,72,884,463,650,153,908,953,596,536,137,708,53,182,91,551,391,358,279,603,212,773,830,977,435,814,62,349,332,348,174,681,149,27,53,66,655,421,630,661,448,712,446,145,882,192,500,483,568,624,508,79,656,367,896,731,853,891,94,870,295,926,464,605,972,52,852,258,98,762,360,179,917,146,585,24,340,359,686,812,927,16,112,676,839,435,17,400,199,817,870,802,439,369,660,241,992,662,373,225,396,792,630,484,285,27,210,780,829,542,977,512,543,370,995,498,311,134,180,554,606,156,18,236,692,667,737,990,617,311,610,536,471,837,642,719,761,715,580,955,602,283,830,295,279,13,78,543,665,942,155,598,210,994,484,641,179,760,306,357,443,100,419,234,572,347,785,381,550,415,668,74,898,68,927,913,118,268,545,939,330,81,838,243,797,644,1000,53,888,14,809,820,563,640,387,342,523,630,462,462,633,707,999,847,891,23,942,670,862,864,905,418,204,283,124,520,527,896,384,575,681,596,698,848,556,792,400,570,51,531,127,180,433,439,89,676,487,631,14,200,393,911,850,931,616,144,963,281,280,645,474,999,684,983,526,929,700,38,184,15,342,284,781,992,710,218,553,101,898,355,845,476,712,349,879,991,764,944,258,704,148,884,834,862,947,344,481,369,566,206,464,194,32,76,881,296,708,163,983,393,920,541,434,626,739,972,928,963,721,427,294,262,225,266,93,881,449,911,873,792,244,147,295,97,848,686,468,780,73,479,842,481,714,357,170,254,86,183,584,593,490,870,105,372,440,318,102,556,314,61,419,350,985,714,141,704,508,133,669,380,620,144,543,365,848,169,724,998,627,932,977,516,612,392,47,213,248,260,434,53,973,720,819,332,936,30,225,287,31,538,584,313,818,460,196,309,881,502,83,310,721,664,10,550,875,798,68,172,197,271,657,680,323,668,146,116,460,845,131,490,246,571,946,962,531,304,795,353,344,442,463,240,579,846,578,448,657,546,236,510,665,315,740,335,944,734,198,534,217,711,60,856,956,917,526,655,241,741,229,66,298,241,4,13,510,658,15,126,669,79,377,426,148,764,305,879,252,730,458,657,26,839,992,24,431,193,185,251,987,264,691,166,213,669,96,623,718,893,547,674,494,274,248,800,836,626,886,97,459,801,645,475,397,541,910,415,687,623,29,213,939,481,717,997,458,858,453,673,956,456,648,379,710,927,575,922,356,795]
    print solution.maxScoreSightseeinPair(A)