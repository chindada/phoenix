package portscan

import "strconv"

type ExcludePort struct {
	StartPort int64
	EndPort   int64
}

type ExcludePortArr []ExcludePort

func (e ExcludePortArr) IsExcluded(port string) bool {
	n, err := strconv.ParseInt(port, 10, 64)
	if err != nil {
		return false
	}
	for _, v := range e {
		if v.StartPort <= n && n <= v.EndPort {
			return true
		}
	}
	return false
}

type PortScan struct {
	ExcludePorts ExcludePortArr
}

func NewPortScan() *PortScan {
	return &PortScan{}
}
