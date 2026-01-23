//go:build !windows

package portscan

func (p *PortScan) Scan() (ExcludePortArr, error) {
	return p.ExcludePorts, nil
}
