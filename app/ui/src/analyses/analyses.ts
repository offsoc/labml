import {Analysis} from "./types"

import stdOutAnalysis from "./experiments/stdout"
import stderrAnalysis from "./experiments/stderror"
import loggerAnalysis from "./experiments/logger"
import runConfigsAnalysis from "./experiments/configs"

import cpuAnalysis from './sessions/cpu'
import diskAnalysis from './sessions/disk'
import {gpuMemoryAnalysis, gpuPowerAnalysis, gpuTempAnalysis, gpuUtilAnalysis} from './sessions/gpu'
import memoryAnalysis from './sessions/memory'
import networkAnalysis from './sessions/network'
import processAnalysis from './sessions/process'
import batteryAnalysis from './sessions/battery'
import sessionConfigsAnalysis from "./sessions/configs"
import metricsAnalysis from "./experiments/metrics";
import comparisonAnalysis from "./experiments/comparison";

let metricAnalyses: Analysis[] = [
    metricsAnalysis,
    comparisonAnalysis
]

let experimentAnalyses: Analysis[] = [
    stdOutAnalysis,
    stderrAnalysis,
    runConfigsAnalysis,
    loggerAnalysis
]

let sessionAnalyses: Analysis[] = [
    cpuAnalysis,
    processAnalysis,
    memoryAnalysis,
    diskAnalysis,
    gpuUtilAnalysis,
    gpuTempAnalysis,
    gpuMemoryAnalysis,
    gpuPowerAnalysis,
    batteryAnalysis,
    networkAnalysis,
    sessionConfigsAnalysis,
]

export {
    experimentAnalyses,
    sessionAnalyses,
    metricAnalyses
}
