package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
	"time"
)

// GetBetweenDates 根据开始日期和结束日期计算出时间段内所有日期
// 参数为日期格式，如：2020-01-01
func GetBetweenDates(sdate, edate string) []string {
	d := []string{}
	timeFormatTpl := "2006-01-02 15:04:05"
	if len(timeFormatTpl) != len(sdate) {
		timeFormatTpl = timeFormatTpl[0:len(sdate)]
	}
	date, err := time.Parse(timeFormatTpl, sdate)
	if err != nil {
		// 时间解析，异常
		return d
	}
	date2, err := time.Parse(timeFormatTpl, edate)
	if err != nil {
		// 时间解析，异常
		return d
	}
	if date2.Before(date) {
		// 如果结束时间小于开始时间，异常
		return d
	}
	// 输出日期格式固定
	timeFormatTpl = "20060102"
	date2Str := date2.Format(timeFormatTpl)
	d = append(d, date.Format(timeFormatTpl))
	for {
		date = date.AddDate(0, 0, 1)
		dateStr := date.Format(timeFormatTpl)
		d = append(d, dateStr)
		if dateStr == date2Str {
			break
		}
	}
	return d
}

func main() {

	file, err := os.Open("Pi - Dec - Chudnovsky.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()
	content, err := ioutil.ReadAll(file)
	fmt.Println(len(content))

	//year := []string{"0"}
	stime := "1910-01-01"
	etime := "2021-12-31"
	daylist := GetBetweenDates(stime, etime)
	fmt.Println(len(daylist))

	result, err := os.OpenFile("result.txt", os.O_APPEND|os.O_CREATE, 0644)
	if err != nil {
		panic(err)
	}
	defer result.Close()
	sflag := "1899"
	for _, i := range daylist {
		tflag := i[:4]
		# 显示年份提示
		if tflag != sflag {
			# 检验（其实没必要）
			if strconv.Itoa(strings.Index(string(content), "19950701") - 1) != "73967554" {
				fmt.Println("Error!")
				break
			}
			fmt.Println(tflag)
			sflag = tflag
		}

		t := i + " " + strconv.Itoa(strings.Index(string(content), i) - 1) + "\n"
		n, err := result.Write([]byte(t))
		if err == nil && n < len(t) {
			panic(err)
		}
		//fmt.Println(t)
	}

	//fmt.Println("19950701 " + strconv.Itoa(strings.Index(string(content), "19950701") - 1))
	fmt.Println("Done!")
}