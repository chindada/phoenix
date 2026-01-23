//go:build windows

package portscan

import (
	"strconv"
	"strings"

	"phoenix/processor/pkg/command"
)

func (p *PortScan) Scan() (ExcludePortArr, error) {
	args := []string{
		"interface", "ipv4", "show", "excludedportrange", "protocol=tcp",
	}
	cmd := command.NewCMD("netsh", args...)
	result, err := command.RunAndParse(cmd)
	if err != nil {
		return nil, err
	}

	var excludes ExcludePortArr
	for _, v := range result {
		split := strings.Fields(v)
		var startPort, endPort int64
		if count := len(split); count == 2 {
			for i := range count {
				n, errParse := strconv.ParseInt(split[i], 10, 64)
				if errParse != nil {
					break
				}

				switch i {
				case 0:
					startPort = n
				case 1:
					endPort = n
				}
			}
		}
		if startPort != 0 && endPort != 0 {
			excludes = append(excludes, ExcludePort{
				StartPort: startPort,
				EndPort:   endPort,
			})
		}
	}
	p.ExcludePorts = excludes
	return p.ExcludePorts, nil
}
