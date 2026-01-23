package command

import (
	"bufio"
	"bytes"
	"os/exec"
)

func RunAndParse(c *exec.Cmd) ([]string, error) {
	output, err := c.Output()
	if err != nil {
		return nil, err
	}

	var result []string
	scanner := bufio.NewScanner(bytes.NewReader(output))
	for scanner.Scan() {
		result = append(result, scanner.Text())
	}

	if scanErr := scanner.Err(); scanErr != nil {
		return nil, scanErr
	}

	return result, nil
}
