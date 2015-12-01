package ts2

type options struct {
	TrackCircuitBased       bool           `json:"trackCircuitBased"`
	CurrentScore            int            `json:"currentScore"`
	CurrentTime             Time           `json:"currentTime"`
	DefaultDelayAtEntry     DelayGenerator `json:"defaultDelayAtEntry"`
	DefaultMaxSpeed         float64        `json:"defaultMaxSpeed"`
	DefaultMinimumStopTime  DelayGenerator `json:"defaultMinimumStopTime"`
	DefaultSignalVisibility float64        `json:"defaultSignalVisibility"`
	Description             string         `json:"description"`
	TimeFactor              int            `json:"timeFactor"`
	Title                   string         `json:"title"`
	Version                 string         `json:"version"`
	WarningSpeed            float64        `json:"warningSpeed"`
}