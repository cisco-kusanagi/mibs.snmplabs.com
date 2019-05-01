#
# PySNMP MIB module CISCO-METRO-PHY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-METRO-PHY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:07:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, iso, ModuleIdentity, MibIdentifier, IpAddress, Integer32, TimeTicks, Counter32, ObjectIdentity, NotificationType, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "ModuleIdentity", "MibIdentifier", "IpAddress", "Integer32", "TimeTicks", "Counter32", "ObjectIdentity", "NotificationType", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
ciscoMetroPhyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 69))
ciscoMetroPhyMIB.setRevisions(('2005-09-02 00:00', '2004-11-19 00:00', '2003-08-25 00:00', '2003-01-08 00:00', '2002-05-14 00:00', '2001-08-31 00:00', '2001-04-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMetroPhyMIB.setRevisionsDescriptions(('Following objects have been added to cmPhyIfTable: cmPhyIfRate, cmPhyIfNegotiatedRate, cmPhyIfOverSubscription, cmPhyIfClientSubrate, cmPhyIfClientSubrateLock. Following Textual conventions have been added: CmRateType, CmNegotiatedRateType. ', "cmPhyIfTransType object has been added to cmPhyIfTable. 'e1', 't1', 'e3', 't3', 'dvb', 'sdi' and 'its' enumeration has been added to cmPhyIfProtocol object.", 'cmPhyIfAutoNegotiation object has been added to cmPhyIfTable.', 'cmPhyIfTxBufferSize object has been added to cmPhyIfTable.', 'The third revision of this MIB. The following new counters have been added - cmPhyRxCRC, cmPhyRxCRCOverflow, cmPhyHCRxCRC, cmPhyTxEncapFarEndPktErrors, cmPhyTxEncapFarEndPktErrOverflow, cmPhyHCTxEncapFarEndPktErrors The following objects have been deprecated - cmPhyIfLaserSafetyControl (moved to CISCO-OPTICAL-IF-EXTN-MIB), cmPhyIfForwardLaserControl (moved to CISCO-OPTICAL-IF-EXTN-MIB), cmPhyRxPower (moved to CISCO-OPTICAL-MONITOR-MIB), cmPhyRxHEC (moved to CISCO-CDL-MIB), cmPhyRxHECOverflow (moved to CISCO-CDL-MIB) and cmPhyHCRxHEC (moved to CISCO-CDL-MIB). ', 'The second revision of this MIB.', 'The initial revision of this MIB.',))
if mibBuilder.loadTexts: ciscoMetroPhyMIB.setLastUpdated('200509020000Z')
if mibBuilder.loadTexts: ciscoMetroPhyMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMetroPhyMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 Tel: +1 800 553-NETS E-mail: cs-dwdm@cisco.com')
if mibBuilder.loadTexts: ciscoMetroPhyMIB.setDescription('This MIB module defines the managed objects for physical layer related interface configurations and objects for the protocol specific error counters for DWDM optical switches. This MIB contains three groups. The first group, cmPhyIf group, handles the physical layer related interface configurations. The cmPhyIfTable has objects for configuring protocol, rate, error monitoring, loopback mode and safety features like OFC (Open Fibre Control), laser safety control and forward laser control. The second group, cmPhyStatistics group, represents the counters that collect error statistics on the received data traffic for all protocols except SONET. The error statistics for SONET are covered in the SONET-MIB. The third group, cmPhySonetSectionTrace group, provides objects for section trace monitoring on SONET/SDH interfaces. ')
class TransmissionType(TextualConvention, Integer32):
    description = "An integer value that identifies the physical layer medium used across an interface. The value 'unknown' indicates the physical layer medium is not known. The value 'copper' indicates the physical layer medium is copper. The value 'optical' indicates the physical layer medium is optical."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("unknown", 1), ("copper", 2), ("optical", 3))

class ProtocolType(TextualConvention, Integer32):
    description = "An integer value that identifies the protocol used across an interface. The value 'e1' indicates an interface that implements the physical layer of E1. The value 't1' indicates an interface that implements the physical layer of T1. The value 'e3' indicates an interface that implements the physical layer of E3. The value 't3' indicates an interface that implements the physical layer of T3. The value 'dvb' indicates an interface that implements the physical layer of DVB. The value 'sdi' indicates an interface that implements the physical layer of SDI. The value 'its' indicates an interface that implements the physical layer of ITS. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("gigabitEthernet", 3), ("tenGigabitEthernet", 4), ("fibreChannel", 5), ("ficon", 6), ("escon", 7), ("sonet", 8), ("sdh", 9), ("sysplexIscCompatibility", 10), ("sysplexIscPeer", 11), ("sysplexTimerEtr", 12), ("sysplexTimerClo", 13), ("fastEthernet", 14), ("fddi", 15), ("e1", 16), ("t1", 17), ("e3", 18), ("t3", 19), ("dvb", 20), ("sdi", 21), ("its", 22))

class TriValue(TextualConvention, Integer32):
    description = 'A three codepoint value.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("true", 1), ("false", 2), ("notApplicable", 3))

class CmRateType(TextualConvention, Integer32):
    description = "An integer value that identifies the rate of the interface. The value 'unknown' indicates the rate of the interface is not known. The value 'auto' indicates the rate of the interface is auto. The client interface will automatically negotiates its speed with its peer. The value 'oneGbps' indicates the rate of the interface is 1 Gigabits/sec. The value 'twoGbps' indicates the rate of the interface is 2 Gigabits/sec. The value 'fourGbps' indicates the rate of the interface is 4 Gigabits/sec. The value 'tenGbps' indicates the rate of the interface is 10 Gigabits/sec."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("auto", 2), ("oneGbps", 3), ("twoGbps", 4), ("fourGbps", 5), ("tenGbps", 6))

class CmNegotiatedRateType(TextualConvention, Integer32):
    description = "An integer value that identifies the current rate of the interface after the auto negotiation. The value 'notApplicable' indicates this object is not applicable for the interface. The value 'negotiating' indicates the interface is in the process of negotiating its speed with its peer. The value 'oneGbps' indicates the rate of the interface is 1 Gigabits/sec after auto negotiation. The value 'twoGbps' indicates the rate of the interface is 2 Gigabits/sec after auto negotiation. The value 'fourGbps' indicates the rate of the interface is 4 Gigabits/sec after auto negotiation. The value 'tenGbps' indicates the rate of the interface is 10 Gigabits/sec after auto negotiation."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notApplicable", 1), ("negotiating", 2), ("oneGbps", 3), ("twoGbps", 4), ("fourGbps", 5), ("tenGbps", 6))

ciscoMetroPhyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 1))
cmPhyIf = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1))
cmPhyStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2))
cmPhySonetSectionTrace = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3))
cmPhyIfTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1), )
if mibBuilder.loadTexts: cmPhyIfTable.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfTable.setDescription('This table allows physical layer related interface configurations on an interface.')
cmPhyIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cmPhyIfEntry.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfEntry.setDescription('A collection of objects for configuration on an interface.')
cmPhyIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mode2R", 1), ("mode3R", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfMode.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfMode.setDescription('This object allows the management client to configure the mode of operation for the client interface modules. When in 2R mode, there is no protocol type, clock rate or monitoring to be configured i.e. the next three objects would be read-only. When in 3R mode, monitoring can be enabled or disabled and the clock rate and protocol should be configured.')
cmPhyIfProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 2), ProtocolType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfProtocol.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfProtocol.setDescription("This object is used to specify the protocol of the data carried over the client side interface. This object applies to linecards which support a variety of protocols and allow dynamic configuration of the specific protocol to be monitored on the interface. The ifType value for such interfaces remains fixed. The agent may use this object to identify the protocol to be monitored (see the cmPhyIfMonitor object), to set the clock rate for the interface (see the cmPhyIfClockRate object), or to enable or disable functionality related to the protocol, for example OFC (see the cmPhyIfOFC object). The value of this object cannot be modified when the cmPhyIfMonitor object is set to 'true' for that interface. Also, this object does not apply to the trunk side interfaces.")
cmPhyIfClockRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10312000))).setUnits('kHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfClockRate.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfClockRate.setDescription("This object allows the management client to set the clock rate across the client side interface. Due to hardware limitations, all values may not be supported. The default value of this object depends on the value of the cmPhyIfProtocol object. When the value of the cmPhyIfProtocol object is reset, the value of this object will be automatically set to the default for that protocol. In case of protocols that support multiple rates, the default value of this object will be the lowest rate possible for that protocol. For example, if the value of cmPhyIfProtocol is set to 'sonet', the default value of cmPhyIfClockRate is set to the OC-3 rate of 155520 kHz. If a non-default value is desired, then this object must be set after the cmPhyIfProtocol object has been reset. This object must be set to a supported clock rate when setting cmPhyIfProtocol to 'unknown'. In 2R mode of operation, this object is not applicable and will have a default value of 0. The value of this object cannot be modified when the cmPhyIfMonitor object is set to 'true' for that interface. Also, this object is not applicable to trunk side interfaces.")
cmPhyIfMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfMonitor.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfMonitor.setDescription("This object allows the management client to enable monitoring of the error counters on an interface, by writing a value of 'true' to this object. To bypass the monitoring hardware, a value of 'false' must be written to this object. Monitoring does not apply when the value of cmPhyIfProtocol is 'unknown'.")
cmPhyIfLoopback = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noLoop", 1), ("diagnosticLoop", 2), ("lineLoop", 3), ("otherLoop", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfLoopback.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfLoopback.setDescription("This object allows the management client to configure loopback for the client side or trunk side interfaces. 'noLoop' - No Loopback present. 'diagnosticLoop' - This is an internal loopback, where the data stream is looped from the transmit to receive section. It is used for hardware debug, bring-up and diagnostics. 'lineLoop' - In this mode, the receive data stream is looped back to the transmit side. 'otherLoop' - This indicates loopbacks not defined here. The default value of this object will be 'noLoop'.")
cmPhyIfOFC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfOFC.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfOFC.setDescription("This object allows the management client to enable OFC(Open Fibre Control) safety protocol for the client side interfaces, by writing a 'true' value to this object. A 'false' value would disable OFC. The default value of this object varies depending on the value of cmPhyIfProtocol and cmPhyIfClockRate. When cmPhyIfProtocol or cmPhyIfClockRate is reset, then the value of this object is automatically reset to the default value for that protocol or rate. If non-default OFC behavior is desired, then this object should be set after cmPhyIfProtocol or cmPhyIfClockRate has been reset. This object is not applicable to trunk side interfaces.")
cmPhyIfLaserSafetyControl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfLaserSafetyControl.setStatus('deprecated')
if mibBuilder.loadTexts: cmPhyIfLaserSafetyControl.setDescription("This object allows the management client to enable laser safety control feature on the trunk side interfaces by writing a true value to this object. If laser safety control is enabled, the transmit laser on the trunk side is shut when the receive signal is not available on the fiber. A 'false' value disables this feature and is the default value assigned to this object. Laser safety control would not apply in case of splitter protection on the optical switch.")
cmPhyIfForwardLaserControl = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfForwardLaserControl.setStatus('deprecated')
if mibBuilder.loadTexts: cmPhyIfForwardLaserControl.setDescription("This object allows the management client to enable forward laser control on the client or trunk side interfaces by writing a true value to this object. If forward laser control is enabled, the transmit laser is shut when the cross-connect receive port on the switch is in alarm condition. A 'false' value disables this feature and is the default value assigned to this object.")
cmPhyIfTxBufferSize = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65536))).setUnits('bytes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfTxBufferSize.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfTxBufferSize.setDescription('This object applies when circuit emulation of the client protocol is used. It allows the management client to configure the size of the transmit buffer on the client port. A value of 0 implies that this object does not apply to this interface. Controlling the size of the transmit buffer on a client port may be essential in scenarios where packet streams from various client ports are aggregated onto a single trunk port. The latency associated with an elementary stream received on a client port, from the trunk port is influenced by the nature of other elementary streams in the aggregate. For example, a giant packet in one stream will increase latency in processing packets in other elementary streams. The size of the transmit buffer on the client port must be configured proportional to this expected latency. Increasing the buffer size when latency is higher helps in reassembly of fragmented packets before transmitting them to the client device. Note that increasing the buffer size results in higher latency even when the elementary packet stream is not subject to high jitters. Refer to the platform specific documentation for guidelines on configuring this buffer size.')
cmPhyIfAutoNegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 10), TriValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfAutoNegotiation.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfAutoNegotiation.setDescription("This object allows the management client to enable auto negotiation signaling on the client side interface, by writing a 'true' value to this object. A 'false' value would disable auto negotiation. Setting the value 'notApplicable' to this object will not change the existing value in this object. Auto negotiation is applicable only for a few client protocols such as gigabitEthernet. If the client interface does not support 'auto negotiation' feature, then this object has the value of 'notApplicable' and the value will not be changed via a set operation.")
cmPhyIfTransType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 11), TransmissionType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyIfTransType.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfTransType.setDescription("This object is used to identify the physical layer medium used for carrying data. For non-relevant interfaces, this value is 'unknown'.")
cmPhyIfRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 12), CmRateType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfRate.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfRate.setDescription("This object is used to specify the rate of the interface. The value of 'unknown' implies that this object does not apply to this interface.")
cmPhyIfNegotiatedRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 13), CmNegotiatedRateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyIfNegotiatedRate.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfNegotiatedRate.setDescription("This object is used to identify the current rate of the interface after the auto negotation. This object is valid only if the object cmPhyIfRate is configured as 'auto'.")
cmPhyIfOverSubscription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 14), TriValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfOverSubscription.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfOverSubscription.setDescription("Oversubscription allows the user to carry multiple clients over the trunk to efficiently utilize the trunk bandwidth. This object allows the management client to enable over subscription on an interface by setting a value of 'true' to this object. A 'false' value would disable over subscription. Setting the value 'notApplicable' to this object is not allowed. The value of 'notApplicable' implies that this object does not apply to this interface.")
cmPhyIfClientSubrate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4240))).setUnits('mega-bytes-per-second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfClientSubrate.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfClientSubrate.setDescription('This object allows the management client to specify the subrate bandwidth of the oversubscribed trunk which carries this client. A value of 0 implies that this object does not apply to this interface.')
cmPhyIfClientSubrateLock = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 16), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhyIfClientSubrateLock.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfClientSubrateLock.setDescription("This object allows the management client to lock the subrate bandwidth on an interface, by writing a value of 'true' to this object. A 'false' value would disable the bandwidth lock. If the clients bandwidth is locked then this client will not share its bandwidth with the other clients on the same oversubscribed trunk. SubrateLock does not apply when the value of cmPhyIfClientSubrate is zero.")
cmPhyStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1), )
if mibBuilder.loadTexts: cmPhyStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: cmPhyStatisticsTable.setDescription('This table contains the cumulative error statistics being collected for the different medium types, except SONET, on the client side and an object for the optical power level on the trunk side. The error statistics for SONET are covered by the sonetSectionCurrentTable and the sonetSectionIntervalTable in the RFC1595-MIB.')
cmPhyStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cmPhyStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: cmPhyStatisticsEntry.setDescription('An entry in the cmPhyStatisticsTable.')
cmPhyRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-4000, 0))).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxPower.setStatus('deprecated')
if mibBuilder.loadTexts: cmPhyRxPower.setDescription('This object gives the optical power level received on the trunk side interface. The actual value of the power level received on the interface is the value of this object divided by 100. This object is not applicable to client side interfaces. This object has been deprecated since a similar object has been defined in the CISCO-OPTICAL-MONITOR-MIB.')
cmPhyRxCVRD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxCVRD.setStatus('current')
if mibBuilder.loadTexts: cmPhyRxCVRD.setDescription('This object represents the lower word value of the counter associated with the number of code violations and running disparity errors encountered, in the receive direction. NOTE: The object cmPhyRxCVRDOverflow contains the higher 32 bits of this counter value. SNMP v2c or v3 managers can use the cmPhyHCRxCVRD object directly which is a 64 bit counter.')
cmPhyRxCVRDOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxCVRDOverflow.setStatus('current')
if mibBuilder.loadTexts: cmPhyRxCVRDOverflow.setDescription('This object represents the high word value of the counter associated with the number of code violations and running disparity errors encountered, in the receive direction. NOTE: The object cmPhyRxCVRD contains the lower 32 bits of this counter value. If the error count is greater than 4,294,967,295 the higher word value will be stored in this object. SNMP v2c or v3 managers can use the cmPhyHCRxCVRD object directly which is a 64 bit counter.')
cmPhyHCRxCVRD = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyHCRxCVRD.setStatus('current')
if mibBuilder.loadTexts: cmPhyHCRxCVRD.setDescription('This object represents the counter associated with the number of code violations and running disparity errors encountered, in the receive direction. This is a High Capacity (64 bit) version of the cmPhyRxCVRD counter.')
cmPhyRxHEC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxHEC.setStatus('deprecated')
if mibBuilder.loadTexts: cmPhyRxHEC.setDescription('This object represents the lower word value of the counter associated with the number of CDL HEC errors encountered, in the receive direction. This object has a valid value only if the protocol type is gigabitEthernet/ tenGigabitEthernet. For all other protocols, this object is not applicable. NOTE: The object cmPhyRxHECOverflow contains the higher 32 bits of this counter value. SNMP v2c or v3 managers can use the cmPhyHCRxHEC object directly which is a 64 bit counter. This object has been deprecated since a similar object has been defined in the CISCO-CDL-MIB.')
cmPhyRxHECOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxHECOverflow.setStatus('deprecated')
if mibBuilder.loadTexts: cmPhyRxHECOverflow.setDescription('This object represents the high word value of the counter associated with the number of CDL HEC errors encountered, in the receive direction. This object has a valid value only if the protocol type is gigabitEthernet/ tenGigabitEthernet. For all other protocols, this object is not applicable. NOTE: The object cmPhyRxHEC contains the lower 32 bits of this counter value. If the error count is greater than 4,294,967,295 the higher word value will be stored in this object. SNMP v2c or v3 managers can use the cmPhyHCRxHEC object directly which is a 64 bit counter. This object has been deprecated since a similar object has been defined in the CISCO-CDL-MIB.')
cmPhyHCRxHEC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyHCRxHEC.setStatus('deprecated')
if mibBuilder.loadTexts: cmPhyHCRxHEC.setDescription('This object represents the counter associated with the number of CDL HEC errors encountered, in the receive direction. This object has a valid value only if the medium type is gigabitEthernet/ tenGigabitEthernet. For all other media, this object is not applicable. This is a High Capacity (64 bit) version of the cmPhyRxHEC counter. This object has been deprecated since a similar object has been defined in the CISCO-CDL-MIB.')
cmPhyRxCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxCRC.setStatus('current')
if mibBuilder.loadTexts: cmPhyRxCRC.setDescription('This object represents the lower word value of the counter associated with CRC errors. This object has a valid value only for interfaces that provide CRC error monitoring. NOTE: The object cmPhyRxCRCOverflow contains the higher 32 bits of this counter value. SNMP v2c or v3 managers can use the cmPhyHCRxCRC object directly which is a 64 bit counter.')
cmPhyRxCRCOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyRxCRCOverflow.setStatus('current')
if mibBuilder.loadTexts: cmPhyRxCRCOverflow.setDescription('This object represents the higher word value of the counter associated with CRC errors. This object has a valid value only for interfaces that provide CRC error monitoring. NOTE: The object cmPhyRxCRC contains the lower 32 bits of this counter value. If the error count is greater than 4,294,967,295 the higher word value will be stored in this object. SNMP v2c or v3 managers can use the cmPhyHCRxCRC object directly which is a 64 bit counter.')
cmPhyHCRxCRC = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyHCRxCRC.setStatus('current')
if mibBuilder.loadTexts: cmPhyHCRxCRC.setDescription('This object represents the counter associated with CRC errors. This object has a valid value only for interfaces that provide CRC error monitoring. This is a High Capacity (64 bit) version of the cmPhyRxCRC counter.')
cmPhyTxEncapFarEndPktErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyTxEncapFarEndPktErrors.setStatus('current')
if mibBuilder.loadTexts: cmPhyTxEncapFarEndPktErrors.setDescription('This object represents the lower word value of the counter associated with ingress error indications from the far end of an Ethernet network, where an ESCON stream is encapsulated in Ethernet packets. This counter is incremented whenever an ESCON packet or control character has 8b/10b code violations or running disparity errors in the ingress direction at the far end of the Ethernet network. This object has a valid value only for ESCON interfaces where Ethernet encapsulation is performed. NOTE: The object cmPhyTxEncapFarEndPktErrOverflow contains the higher 32 bits of this counter value. SNMP v2c or v3 managers can use the cmPhyHCTxEsconPktInd object directly which is a 64 bit counter.')
cmPhyTxEncapFarEndPktErrOverflow = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyTxEncapFarEndPktErrOverflow.setStatus('current')
if mibBuilder.loadTexts: cmPhyTxEncapFarEndPktErrOverflow.setDescription('This object represents the higher word value of the counter associated with ingress error indications from the far end of an Ethernet network, where an ESCON stream is encapsulated in Ethernet packets. This counter is incremented whenever an ESCON packet or control character has 8b/10b code violations or running disparity errors in the ingress direction at the far end of the Ethernet network. This object has a valid value only for ESCON interfaces where Ethernet encapsulation is performed. NOTE: The object cmPhyTxEncapFarEndPktErrors contains the lower 32 bits of this counter value. SNMP v2c or v3 managers can use the cmPhyHCTxEsconPktInd object directly which is a 64 bit counter.')
cmPhyHCTxEncapFarEndPktErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhyHCTxEncapFarEndPktErrors.setStatus('current')
if mibBuilder.loadTexts: cmPhyHCTxEncapFarEndPktErrors.setDescription('This object represents the counter associated with ESCON ingress error indications from the far end of an Ethernet network, where an ESCON stream is encapsulated in Ethernet packets. This counter is incremented whenever an ESCON packet or control character has 8b/10b code violations or running disparity errors in the ingress direction at the far end of the Ethernet network. This object has a valid value only for ESCON interfaces where Ethernet encapsulation is performed. This is a High Capacity (64 bit) version of the cmPhyTxEncapFarEndPktErrors counter.')
cmPhySonetSectionTraceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3, 1), )
if mibBuilder.loadTexts: cmPhySonetSectionTraceTable.setStatus('current')
if mibBuilder.loadTexts: cmPhySonetSectionTraceTable.setDescription('This table provides objects for monitoring the J0 bytes of a SONET or SDH section.')
cmPhySonetSectionTraceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cmPhySonetSectionTraceEntry.setStatus('current')
if mibBuilder.loadTexts: cmPhySonetSectionTraceEntry.setDescription("An entry in the cmPhySonetSectionTraceTable is created when the value of the cmPhyIfProtocol object is set to 'sonet' and the value of cmPhyIfMonitor is set to 'true'.")
cmPhySonetSectionTraceReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), ValueSizeConstraint(64, 64), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmPhySonetSectionTraceReceived.setStatus('current')
if mibBuilder.loadTexts: cmPhySonetSectionTraceReceived.setDescription('This object displays the SONET or SDH section trace bytes received at the interface.')
cmPhySonetSectionTraceExpected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3, 1, 1, 2), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), ValueSizeConstraint(64, 64), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmPhySonetSectionTraceExpected.setStatus('current')
if mibBuilder.loadTexts: cmPhySonetSectionTraceExpected.setDescription('This object defines the SONET or SDH section trace bytes to be expected at the interface. The default value of this object will be a zero length string.')
ciscoMetroPhyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 3))
ciscoMetroPhyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1))
ciscoMetroPhyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2))
cmPhyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 1)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyStatisticsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyMIBCompliance = cmPhyMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: cmPhyMIBCompliance.setDescription('The compliance statement for platforms that monitor the operating status with respect to error counters, for the physical layer.')
cmPhyMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 2)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIf2Group"), ("CISCO-METRO-PHY-MIB", "cmPhyCVRDErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyCRCErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyEncapFarEndPktErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyMIBCompliance2 = cmPhyMIBCompliance2.setStatus('deprecated')
if mibBuilder.loadTexts: cmPhyMIBCompliance2.setDescription('The compliance statement for platforms that monitor the operating status with respect to error counters, for the physical layer.')
cmPhyMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 3)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIf2Group"), ("CISCO-METRO-PHY-MIB", "cmPhyCVRDErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyCRCErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyEncapFarEndPktErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfTxBufferSizeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyMIBCompliance3 = cmPhyMIBCompliance3.setStatus('deprecated')
if mibBuilder.loadTexts: cmPhyMIBCompliance3.setDescription('The compliance statement for platforms that monitor the operating status with respect to error counters, for the physical layer.')
cmPhyMIBComplianceRev4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 4)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIf2Group"), ("CISCO-METRO-PHY-MIB", "cmPhyCVRDErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyCRCErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyEncapFarEndPktErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfTxBufferSizeGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfAutoNegGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyMIBComplianceRev4 = cmPhyMIBComplianceRev4.setStatus('deprecated')
if mibBuilder.loadTexts: cmPhyMIBComplianceRev4.setDescription('The compliance statement for platforms that monitor the operating status with respect to error counters, for the physical layer.')
cmPhyMIBComplianceRev5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 5)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIf2Group"), ("CISCO-METRO-PHY-MIB", "cmPhyCVRDErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyCRCErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyEncapFarEndPktErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfTxBufferSizeGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfAutoNegGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyMIBComplianceRev5 = cmPhyMIBComplianceRev5.setStatus('deprecated')
if mibBuilder.loadTexts: cmPhyMIBComplianceRev5.setDescription('The compliance statement for platforms that monitor the operating status with respect to error counters, for the physical layer.')
cmPhyMIBComplianceRev6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 6)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIf2Group"), ("CISCO-METRO-PHY-MIB", "cmPhyCVRDErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyCRCErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyEncapFarEndPktErrorsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfTxBufferSizeGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfAutoNegGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfGroupSup1"), ("CISCO-METRO-PHY-MIB", "cmPhyIfRateGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfClientOvsGroup"), ("CISCO-METRO-PHY-MIB", "cmPhyIfClientSubrateGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyMIBComplianceRev6 = cmPhyMIBComplianceRev6.setStatus('current')
if mibBuilder.loadTexts: cmPhyMIBComplianceRev6.setDescription('The compliance statement for platforms that monitor the operating status with respect to error counters, for the physical layer.')
cmPhyIfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 1)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfMode"), ("CISCO-METRO-PHY-MIB", "cmPhyIfProtocol"), ("CISCO-METRO-PHY-MIB", "cmPhyIfClockRate"), ("CISCO-METRO-PHY-MIB", "cmPhyIfMonitor"), ("CISCO-METRO-PHY-MIB", "cmPhyIfLoopback"), ("CISCO-METRO-PHY-MIB", "cmPhyIfOFC"), ("CISCO-METRO-PHY-MIB", "cmPhyIfLaserSafetyControl"), ("CISCO-METRO-PHY-MIB", "cmPhyIfForwardLaserControl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfGroup = cmPhyIfGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cmPhyIfGroup.setDescription('The collection of objects to allow configurations and give information related to the physical layer characteristics of an interface.')
cmPhyStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 2)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyRxPower"), ("CISCO-METRO-PHY-MIB", "cmPhyRxCVRD"), ("CISCO-METRO-PHY-MIB", "cmPhyRxCVRDOverflow"), ("CISCO-METRO-PHY-MIB", "cmPhyHCRxCVRD"), ("CISCO-METRO-PHY-MIB", "cmPhyRxHEC"), ("CISCO-METRO-PHY-MIB", "cmPhyRxHECOverflow"), ("CISCO-METRO-PHY-MIB", "cmPhyHCRxHEC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyStatisticsGroup = cmPhyStatisticsGroup.setStatus('deprecated')
if mibBuilder.loadTexts: cmPhyStatisticsGroup.setDescription('The collection of objects used to monitor the protocol error counters on the client side and the power level received on the trunk side.')
cmPhySonetSectionTraceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 3)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceReceived"), ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceExpected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhySonetSectionTraceGroup = cmPhySonetSectionTraceGroup.setStatus('current')
if mibBuilder.loadTexts: cmPhySonetSectionTraceGroup.setDescription('The objects used for monitoring the SONET section trace bytes.')
cmPhyIf2Group = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 4)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfMode"), ("CISCO-METRO-PHY-MIB", "cmPhyIfProtocol"), ("CISCO-METRO-PHY-MIB", "cmPhyIfClockRate"), ("CISCO-METRO-PHY-MIB", "cmPhyIfMonitor"), ("CISCO-METRO-PHY-MIB", "cmPhyIfLoopback"), ("CISCO-METRO-PHY-MIB", "cmPhyIfOFC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIf2Group = cmPhyIf2Group.setStatus('current')
if mibBuilder.loadTexts: cmPhyIf2Group.setDescription('The collection of objects to allow configurations and give information related to the physical layer characteristics of an interface.')
cmPhyCVRDErrorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 5)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyRxCVRD"), ("CISCO-METRO-PHY-MIB", "cmPhyRxCVRDOverflow"), ("CISCO-METRO-PHY-MIB", "cmPhyHCRxCVRD"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyCVRDErrorsGroup = cmPhyCVRDErrorsGroup.setStatus('current')
if mibBuilder.loadTexts: cmPhyCVRDErrorsGroup.setDescription('The collection of objects used to monitor the code violation and running disparity error counters.')
cmPhyCRCErrorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 6)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyRxCRC"), ("CISCO-METRO-PHY-MIB", "cmPhyRxCRCOverflow"), ("CISCO-METRO-PHY-MIB", "cmPhyHCRxCRC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyCRCErrorsGroup = cmPhyCRCErrorsGroup.setStatus('current')
if mibBuilder.loadTexts: cmPhyCRCErrorsGroup.setDescription('The collection of objects used to monitor CRC error counters.')
cmPhyEncapFarEndPktErrorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 7)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyTxEncapFarEndPktErrors"), ("CISCO-METRO-PHY-MIB", "cmPhyTxEncapFarEndPktErrOverflow"), ("CISCO-METRO-PHY-MIB", "cmPhyHCTxEncapFarEndPktErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyEncapFarEndPktErrorsGroup = cmPhyEncapFarEndPktErrorsGroup.setStatus('current')
if mibBuilder.loadTexts: cmPhyEncapFarEndPktErrorsGroup.setDescription('The collection of objects used to monitor the far end ingress error indication counters for Ethernet- encapsulated ESCON streams.')
cmPhyIfTxBufferSizeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 8)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfTxBufferSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfTxBufferSizeGroup = cmPhyIfTxBufferSizeGroup.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfTxBufferSizeGroup.setDescription('The collection of objects used to control size of transmit buffer.')
cmPhyIfAutoNegGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 9)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfAutoNegotiation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfAutoNegGroup = cmPhyIfAutoNegGroup.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfAutoNegGroup.setDescription('The collection of objects used to control auto negotiation behavior.')
cmPhyIfGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 10)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfTransType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfGroupSup1 = cmPhyIfGroupSup1.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfGroupSup1.setDescription('The object that gives information related to transmission types on the client interface.')
cmPhyIfRateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 11)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfRate"), ("CISCO-METRO-PHY-MIB", "cmPhyIfNegotiatedRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfRateGroup = cmPhyIfRateGroup.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfRateGroup.setDescription('The collection of objects that are used to retrieve and configure the various interface rates.')
cmPhyIfClientOvsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 12)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfOverSubscription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfClientOvsGroup = cmPhyIfClientOvsGroup.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfClientOvsGroup.setDescription('The collection of objects to allow the oversubscription configurations on an interface.')
cmPhyIfClientSubrateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 13)).setObjects(("CISCO-METRO-PHY-MIB", "cmPhyIfClientSubrate"), ("CISCO-METRO-PHY-MIB", "cmPhyIfClientSubrateLock"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmPhyIfClientSubrateGroup = cmPhyIfClientSubrateGroup.setStatus('current')
if mibBuilder.loadTexts: cmPhyIfClientSubrateGroup.setDescription('The collection of objects to allow the configurations related to the subrating on an interface.')
mibBuilder.exportSymbols("CISCO-METRO-PHY-MIB", cmPhyIfClientSubrateGroup=cmPhyIfClientSubrateGroup, ciscoMetroPhyMIBConformance=ciscoMetroPhyMIBConformance, cmPhyIfTxBufferSize=cmPhyIfTxBufferSize, cmPhyStatisticsTable=cmPhyStatisticsTable, cmPhyMIBCompliance=cmPhyMIBCompliance, cmPhyRxCVRDOverflow=cmPhyRxCVRDOverflow, cmPhyRxHECOverflow=cmPhyRxHECOverflow, cmPhyRxCVRD=cmPhyRxCVRD, CmRateType=CmRateType, cmPhyIfClientSubrateLock=cmPhyIfClientSubrateLock, cmPhyMIBCompliance2=cmPhyMIBCompliance2, cmPhyEncapFarEndPktErrorsGroup=cmPhyEncapFarEndPktErrorsGroup, cmPhyIfRateGroup=cmPhyIfRateGroup, cmPhyIfMonitor=cmPhyIfMonitor, cmPhyStatisticsEntry=cmPhyStatisticsEntry, cmPhyHCRxCRC=cmPhyHCRxCRC, ciscoMetroPhyMIBGroups=ciscoMetroPhyMIBGroups, cmPhyIfGroup=cmPhyIfGroup, cmPhySonetSectionTrace=cmPhySonetSectionTrace, cmPhyIfAutoNegGroup=cmPhyIfAutoNegGroup, cmPhyHCTxEncapFarEndPktErrors=cmPhyHCTxEncapFarEndPktErrors, cmPhyStatistics=cmPhyStatistics, cmPhyIfLoopback=cmPhyIfLoopback, cmPhyIfTransType=cmPhyIfTransType, cmPhyRxCRCOverflow=cmPhyRxCRCOverflow, cmPhyTxEncapFarEndPktErrors=cmPhyTxEncapFarEndPktErrors, PYSNMP_MODULE_ID=ciscoMetroPhyMIB, cmPhyMIBComplianceRev6=cmPhyMIBComplianceRev6, cmPhyIfOverSubscription=cmPhyIfOverSubscription, cmPhyHCRxCVRD=cmPhyHCRxCVRD, cmPhyRxCRC=cmPhyRxCRC, cmPhyIf=cmPhyIf, cmPhySonetSectionTraceExpected=cmPhySonetSectionTraceExpected, cmPhyIfClientOvsGroup=cmPhyIfClientOvsGroup, cmPhyStatisticsGroup=cmPhyStatisticsGroup, cmPhyRxPower=cmPhyRxPower, cmPhyIfClockRate=cmPhyIfClockRate, cmPhyIfForwardLaserControl=cmPhyIfForwardLaserControl, cmPhyIfTxBufferSizeGroup=cmPhyIfTxBufferSizeGroup, ProtocolType=ProtocolType, CmNegotiatedRateType=CmNegotiatedRateType, ciscoMetroPhyMIBObjects=ciscoMetroPhyMIBObjects, cmPhyCVRDErrorsGroup=cmPhyCVRDErrorsGroup, cmPhySonetSectionTraceTable=cmPhySonetSectionTraceTable, cmPhyIfAutoNegotiation=cmPhyIfAutoNegotiation, cmPhyIfEntry=cmPhyIfEntry, ciscoMetroPhyMIB=ciscoMetroPhyMIB, ciscoMetroPhyMIBCompliances=ciscoMetroPhyMIBCompliances, cmPhyRxHEC=cmPhyRxHEC, cmPhyMIBComplianceRev4=cmPhyMIBComplianceRev4, cmPhySonetSectionTraceReceived=cmPhySonetSectionTraceReceived, cmPhyHCRxHEC=cmPhyHCRxHEC, TransmissionType=TransmissionType, cmPhySonetSectionTraceEntry=cmPhySonetSectionTraceEntry, TriValue=TriValue, cmPhyMIBComplianceRev5=cmPhyMIBComplianceRev5, cmPhyIf2Group=cmPhyIf2Group, cmPhyCRCErrorsGroup=cmPhyCRCErrorsGroup, cmPhyIfNegotiatedRate=cmPhyIfNegotiatedRate, cmPhyIfClientSubrate=cmPhyIfClientSubrate, cmPhyIfRate=cmPhyIfRate, cmPhyIfTable=cmPhyIfTable, cmPhyIfGroupSup1=cmPhyIfGroupSup1, cmPhySonetSectionTraceGroup=cmPhySonetSectionTraceGroup, cmPhyIfMode=cmPhyIfMode, cmPhyIfProtocol=cmPhyIfProtocol, cmPhyTxEncapFarEndPktErrOverflow=cmPhyTxEncapFarEndPktErrOverflow, cmPhyIfLaserSafetyControl=cmPhyIfLaserSafetyControl, cmPhyMIBCompliance3=cmPhyMIBCompliance3, cmPhyIfOFC=cmPhyIfOFC)
