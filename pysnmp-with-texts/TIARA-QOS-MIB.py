#
# PySNMP MIB module TIARA-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-QOS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Bits, Counter64, TimeTicks, MibIdentifier, NotificationType, IpAddress, ObjectIdentity, Integer32, Unsigned32, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Counter64", "TimeTicks", "MibIdentifier", "NotificationType", "IpAddress", "ObjectIdentity", "Integer32", "Unsigned32", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
tiaraIpIfIndex, = mibBuilder.importSymbols("TIARA-IP-MIB", "tiaraIpIfIndex")
tiaraMgmt, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt")
tiaraQosMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 17))
tiaraQosMib.setRevisions(('1900-02-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tiaraQosMib.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: tiaraQosMib.setLastUpdated('0006100000Z')
if mibBuilder.loadTexts: tiaraQosMib.setOrganization('Tiara Networks Inc.')
if mibBuilder.loadTexts: tiaraQosMib.setContactInfo('Tiara Networks Customer Support 525 Race Street, Suite 100, San Jose, CA 95126 USA Tel: +1 408-216-4700 Fax: +1 408-216-4701 E-mail: support@tiaranetworks.com')
if mibBuilder.loadTexts: tiaraQosMib.setDescription('QoS MIB for configuring Quality of Service parameters on a WAN interface.')
tiaraRedConfigTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 17, 1), )
if mibBuilder.loadTexts: tiaraRedConfigTable.setStatus('current')
if mibBuilder.loadTexts: tiaraRedConfigTable.setDescription('This table consists of all parameters that are needed to configure RED on a WAN interface.')
tiaraRedConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1), ).setIndexNames((0, "TIARA-IP-MIB", "tiaraIpIfIndex"))
if mibBuilder.loadTexts: tiaraRedConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tiaraRedConfigEntry.setDescription('Describes an entry in the RED configuration table.')
redTxMaxThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redTxMaxThreshold.setStatus('current')
if mibBuilder.loadTexts: redTxMaxThreshold.setDescription('This is the upper limit for the average queue size for a given WAN interface. If the average queue size exceeds this value, RED drops all packets that are destined for that WAN interface. When a WAN interface is created, the maximum threshold is initialized to three times the minimum threshold. Setting maximum threshold to greater than two times minimum threshold is recommended for proper operation.')
redTxMinThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redTxMinThreshold.setStatus('current')
if mibBuilder.loadTexts: redTxMinThreshold.setDescription('This is the threshold at which RED begins dropping packets. When the average queue size for a WAN interface increases above the minimum threshold, RED drops packets with a certain probability that increases linearly as the average queue size increases from the minimum to the maximum threshold. Below the minimum threshold, RED allows all packets. When a WAN interface is created, the minimum threshold is initialized to a value that is dependent on the bandwidth of the interface. Setting the minimum threshold to less than this value may cause unnecessary packet drops at close to 100% utilization.')
redTxWqBiasFactor = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redTxWqBiasFactor.setStatus('current')
if mibBuilder.loadTexts: redTxWqBiasFactor.setDescription('This is the exponential weighting/bias factor used to calculate the moving average of the queue size. A higher value smooths out the peaks and troughs in the instantaneous queue size and, hence, better accomodates bursts. A lower value is more responsive to changes in queue size. It is important to select the optimum value. Using the default of 5 is recommended.')
redTxEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: redTxEnable.setStatus('current')
if mibBuilder.loadTexts: redTxEnable.setDescription('This is used to enable or disable RED on a WAN interface. RED is enabled by default.')
tiaraRedStatTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2), )
if mibBuilder.loadTexts: tiaraRedStatTable.setStatus('current')
if mibBuilder.loadTexts: tiaraRedStatTable.setDescription('This table gives RED statistics for a given WAN interface.')
tiaraRedStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1), ).setIndexNames((0, "TIARA-IP-MIB", "tiaraIpIfIndex"))
if mibBuilder.loadTexts: tiaraRedStatEntry.setStatus('current')
if mibBuilder.loadTexts: tiaraRedStatEntry.setDescription('Describes an entry in the RED statistics table.')
redTxLoanedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxLoanedCount.setStatus('current')
if mibBuilder.loadTexts: redTxLoanedCount.setDescription('This is the instantaneous queue size measured by RED for a given WAN interface.')
redTxMaxLoanedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxMaxLoanedCount.setStatus('current')
if mibBuilder.loadTexts: redTxMaxLoanedCount.setDescription('This is the maximum instantaneous queue size seen on a given WAN interface. In other words, it is the maximum number of packets that had been queued for transmission on the WAN interface.')
redTxAvgQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxAvgQueueSize.setStatus('current')
if mibBuilder.loadTexts: redTxAvgQueueSize.setDescription('This is the current value of the average queue size on a given WAN interface and is a measure of congestion on that interface. RED attempts to keep this value between the minimum and maximum thresholds.')
redTxMaxAvgQueueSize = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxMaxAvgQueueSize.setStatus('current')
if mibBuilder.loadTexts: redTxMaxAvgQueueSize.setDescription('This is the maximum value that the average queue size on a given WAN interface has reached.')
redTxDropRate = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxDropRate.setStatus('current')
if mibBuilder.loadTexts: redTxDropRate.setDescription('This is the rate at which RED drops packets when the average queue size is between the minimum and maximum thresholds. A value of N indicates that one out of N packets will be dropped.')
redTxMinThresholdSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxMinThresholdSuccess.setStatus('current')
if mibBuilder.loadTexts: redTxMinThresholdSuccess.setDescription('This is the number of packets allowed by RED while the average queue size (for a given WAN interface) is below the minimum threshold.')
redTxMaxThresholdFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxMaxThresholdFailure.setStatus('current')
if mibBuilder.loadTexts: redTxMaxThresholdFailure.setDescription('This is the number of packets dropped by RED when the average queue size exceeds the maximum threshold.')
redTxMinMaxRangeSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxMinMaxRangeSuccess.setStatus('current')
if mibBuilder.loadTexts: redTxMinMaxRangeSuccess.setDescription('This is the number of packets allowed by RED while the average queue size is between the minimum and maximum thresholds.')
redTxMinMaxRangeFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxMinMaxRangeFailure.setStatus('current')
if mibBuilder.loadTexts: redTxMinMaxRangeFailure.setDescription('This is the number of packets dropped by RED while the average queue size is between the minimum and maximum thresholds.')
redTxControlSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: redTxControlSuccess.setStatus('current')
if mibBuilder.loadTexts: redTxControlSuccess.setDescription('This is the number of control packets (for e.g., routing updates) that need to be dropped, but are allowed by RED. Routing updates are detected by RED and are not dropped.')
tiaraCbqConfigTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3), )
if mibBuilder.loadTexts: tiaraCbqConfigTable.setStatus('current')
if mibBuilder.loadTexts: tiaraCbqConfigTable.setDescription('This table consists of all the parameters required to configure a CBQ traffic class on an interface.')
tiaraCbqConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1), ).setIndexNames((0, "TIARA-IP-MIB", "tiaraIpIfIndex"), (0, "TIARA-QOS-MIB", "cbqClassIndex"))
if mibBuilder.loadTexts: tiaraCbqConfigEntry.setStatus('current')
if mibBuilder.loadTexts: tiaraCbqConfigEntry.setDescription('Describes an entry in the CBQ config table.')
cbqClassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassIndex.setStatus('current')
if mibBuilder.loadTexts: cbqClassIndex.setDescription('')
cbqClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassName.setStatus('current')
if mibBuilder.loadTexts: cbqClassName.setDescription('')
cbqClassParentName = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassParentName.setStatus('current')
if mibBuilder.loadTexts: cbqClassParentName.setDescription('')
cbqClassBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassBandwidth.setStatus('current')
if mibBuilder.loadTexts: cbqClassBandwidth.setDescription('')
cbqClassBurstTolerance = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassBurstTolerance.setStatus('current')
if mibBuilder.loadTexts: cbqClassBurstTolerance.setDescription('')
cbqClassKeyType = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("cbqClassifyTypeNotSet", 1), ("cbqClassifySrcIp", 2), ("cbqClassifyDestIp", 3), ("cbqClassifySrcPort", 4), ("cbqClassifyDestPort", 5), ("cbqClassifyProtocolType", 6), ("cbqClassifyVlanId", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyType.setStatus('current')
if mibBuilder.loadTexts: cbqClassKeyType.setDescription('')
cbqClassIsDefault = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassIsDefault.setStatus('current')
if mibBuilder.loadTexts: cbqClassIsDefault.setDescription('')
cbqClassAverageBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassAverageBandwidth.setStatus('current')
if mibBuilder.loadTexts: cbqClassAverageBandwidth.setDescription('')
tiaraCbqClassKeyTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4), )
if mibBuilder.loadTexts: tiaraCbqClassKeyTable.setStatus('current')
if mibBuilder.loadTexts: tiaraCbqClassKeyTable.setDescription('')
tiaraCbqClassKeyTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1), ).setIndexNames((0, "TIARA-IP-MIB", "tiaraIpIfIndex"), (0, "TIARA-QOS-MIB", "cbqClassIndex"), (0, "TIARA-QOS-MIB", "cbqClassKeyIndex"))
if mibBuilder.loadTexts: tiaraCbqClassKeyTableEntry.setStatus('current')
if mibBuilder.loadTexts: tiaraCbqClassKeyTableEntry.setDescription('')
cbqClassKeyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyIndex.setStatus('current')
if mibBuilder.loadTexts: cbqClassKeyIndex.setDescription('')
cbqKeyClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqKeyClassName.setStatus('current')
if mibBuilder.loadTexts: cbqKeyClassName.setDescription('')
cbqClassKeyVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyVlanId.setStatus('current')
if mibBuilder.loadTexts: cbqClassKeyVlanId.setDescription('')
cbqClassKeyIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyIpAddress.setStatus('current')
if mibBuilder.loadTexts: cbqClassKeyIpAddress.setDescription('')
cbqClassKeyIpNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyIpNetMask.setStatus('current')
if mibBuilder.loadTexts: cbqClassKeyIpNetMask.setDescription('')
cbqClassKeyPort = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyPort.setStatus('current')
if mibBuilder.loadTexts: cbqClassKeyPort.setDescription('')
cbqClassKeyProtocolType = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassKeyProtocolType.setStatus('current')
if mibBuilder.loadTexts: cbqClassKeyProtocolType.setDescription('')
tiaraCbqStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5), )
if mibBuilder.loadTexts: tiaraCbqStatsTable.setStatus('current')
if mibBuilder.loadTexts: tiaraCbqStatsTable.setDescription("This table gives CBQ's traffic class statistics for a given TIARA interface.")
tiaraCbqStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1), ).setIndexNames((0, "TIARA-IP-MIB", "tiaraIpIfIndex"), (0, "TIARA-QOS-MIB", "cbqClassIndex"))
if mibBuilder.loadTexts: tiaraCbqStatsEntry.setStatus('current')
if mibBuilder.loadTexts: tiaraCbqStatsEntry.setDescription("Describes an entry in the CBQ's statistics table.")
cbqStatsClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqStatsClassName.setStatus('current')
if mibBuilder.loadTexts: cbqStatsClassName.setDescription('')
cbqClassPacketsForwarded = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassPacketsForwarded.setStatus('current')
if mibBuilder.loadTexts: cbqClassPacketsForwarded.setDescription('')
cbqClassBytesForwarded = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassBytesForwarded.setStatus('current')
if mibBuilder.loadTexts: cbqClassBytesForwarded.setDescription('')
cbqClassPacketsDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassPacketsDropped.setStatus('current')
if mibBuilder.loadTexts: cbqClassPacketsDropped.setDescription('')
cbqClassBytesDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassBytesDropped.setStatus('current')
if mibBuilder.loadTexts: cbqClassBytesDropped.setDescription('')
cbqClassBurstExceedCount = MibTableColumn((1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cbqClassBurstExceedCount.setStatus('current')
if mibBuilder.loadTexts: cbqClassBurstExceedCount.setDescription('')
mibBuilder.exportSymbols("TIARA-QOS-MIB", tiaraCbqClassKeyTable=tiaraCbqClassKeyTable, tiaraRedConfigEntry=tiaraRedConfigEntry, tiaraCbqConfigEntry=tiaraCbqConfigEntry, cbqClassKeyIpNetMask=cbqClassKeyIpNetMask, redTxDropRate=redTxDropRate, cbqClassPacketsForwarded=cbqClassPacketsForwarded, cbqStatsClassName=cbqStatsClassName, redTxAvgQueueSize=redTxAvgQueueSize, redTxControlSuccess=redTxControlSuccess, cbqClassKeyVlanId=cbqClassKeyVlanId, redTxEnable=redTxEnable, tiaraCbqStatsEntry=tiaraCbqStatsEntry, redTxMinThresholdSuccess=redTxMinThresholdSuccess, cbqClassBandwidth=cbqClassBandwidth, cbqClassBurstTolerance=cbqClassBurstTolerance, cbqClassKeyPort=cbqClassKeyPort, cbqClassPacketsDropped=cbqClassPacketsDropped, redTxMinThreshold=redTxMinThreshold, cbqClassAverageBandwidth=cbqClassAverageBandwidth, cbqClassIsDefault=cbqClassIsDefault, tiaraQosMib=tiaraQosMib, redTxMinMaxRangeSuccess=redTxMinMaxRangeSuccess, redTxMaxThresholdFailure=redTxMaxThresholdFailure, tiaraRedStatEntry=tiaraRedStatEntry, cbqClassIndex=cbqClassIndex, cbqClassParentName=cbqClassParentName, cbqClassKeyIndex=cbqClassKeyIndex, cbqKeyClassName=cbqKeyClassName, tiaraCbqClassKeyTableEntry=tiaraCbqClassKeyTableEntry, cbqClassBurstExceedCount=cbqClassBurstExceedCount, redTxMaxThreshold=redTxMaxThreshold, redTxLoanedCount=redTxLoanedCount, cbqClassBytesForwarded=cbqClassBytesForwarded, tiaraRedStatTable=tiaraRedStatTable, redTxMaxLoanedCount=redTxMaxLoanedCount, cbqClassBytesDropped=cbqClassBytesDropped, redTxWqBiasFactor=redTxWqBiasFactor, tiaraCbqConfigTable=tiaraCbqConfigTable, redTxMinMaxRangeFailure=redTxMinMaxRangeFailure, tiaraRedConfigTable=tiaraRedConfigTable, cbqClassKeyProtocolType=cbqClassKeyProtocolType, tiaraCbqStatsTable=tiaraCbqStatsTable, PYSNMP_MODULE_ID=tiaraQosMib, redTxMaxAvgQueueSize=redTxMaxAvgQueueSize, cbqClassName=cbqClassName, cbqClassKeyType=cbqClassKeyType, cbqClassKeyIpAddress=cbqClassKeyIpAddress)
