#
# PySNMP MIB module HM2-PLATFORM-QOS-COS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PLATFORM-QOS-COS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:32:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
hm2PlatformQoS, = mibBuilder.importSymbols("HM2-PLATFORM-QOS-MIB", "hm2PlatformQoS")
HmEnabledStatus, = mibBuilder.importSymbols("HM2-TC-MIB", "HmEnabledStatus")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, Integer32, ModuleIdentity, ObjectIdentity, Counter64, Gauge32, MibIdentifier, iso, NotificationType, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "Integer32", "ModuleIdentity", "ObjectIdentity", "Counter64", "Gauge32", "MibIdentifier", "iso", "NotificationType", "IpAddress", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hm2PlatformQosCos = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 3, 3))
hm2PlatformQosCos.setRevisions(('2011-10-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hm2PlatformQosCos.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: hm2PlatformQosCos.setLastUpdated('201110120000Z')
if mibBuilder.loadTexts: hm2PlatformQosCos.setOrganization('Hirschmann Automation and Control GmbH')
if mibBuilder.loadTexts: hm2PlatformQosCos.setContactInfo('Postal: Stuttgarter Str. 45-51 72654 Neckartenzlingen Germany Phone: +49 7127 140 E-mail: hac.support@belden.com')
if mibBuilder.loadTexts: hm2PlatformQosCos.setDescription('The Hirschmann Private Platform2 MIB for Quality of Service - CoS. Copyright (C) 2011. All Rights Reserved.')
class Percent(TextualConvention, Unsigned32):
    description = 'An unsigned integer representing a value expressed as a percentage with one percent increments.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

class Sixteenths(TextualConvention, Unsigned32):
    description = 'An unsigned integer representing the numerator of a value expressing a fraction in terms of sixteenths (0/16, 1/16, 2/16, up to 16/16).'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 16)

hm2AgentCosMapCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1))
hm2AgentCosMapIpPrecTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1), )
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecTable.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecTable.setDescription('A table mapping evaluated IP precedence to Traffic Class for a specific physical port. Traffic class is a number in the range (0..(dot1dPortNumTrafficClasses-1)).')
hm2AgentCosMapIpPrecEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1, 1), ).setIndexNames((0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIpPrecIntfIndex"), (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIpPrecValue"))
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecEntry.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecEntry.setDescription('IP Precedence to Traffic Class mapping for a port.')
hm2AgentCosMapIpPrecIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecIntfIndex.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecIntfIndex.setDescription('This is a unique index for an entry in the hm2AgentCosMapIpPrecTable. A non-zero value indicates the ifIndex for the corresponding interface entry in the ifTable. A value of zero represents global configuration, which in turn causes all interface entries to be updated for a set operation, or reflects the most recent global setting for a get operation.')
hm2AgentCosMapIpPrecValue = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecValue.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecValue.setDescription('The IP precedence value contained in the received frame. This value is only indicated in IP packets, but is independent of both media-type and frame tagging. Non-IP packets are handled in accordance with the dot1dPortDefaultUserPriority value of the ingress port.')
hm2AgentCosMapIpPrecTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecTrafficClass.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIpPrecTrafficClass.setDescription('Traffic class priority queue the received frame is mapped to. This represents the actual configuration setting the port is using.')
hm2AgentCosMapIpDscpTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2), )
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpTable.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpTable.setDescription('A table mapping evaluated IP DSCP to Traffic Class for a specific physical port. Traffic class is a number in the range (0..(dot1dPortNumTrafficClasses-1)).')
hm2AgentCosMapIpDscpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2, 1), ).setIndexNames((0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIpDscpIntfIndex"), (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIpDscpValue"))
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpEntry.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpEntry.setDescription('IP DSCP to Traffic Class mapping for a port.')
hm2AgentCosMapIpDscpIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpIntfIndex.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpIntfIndex.setDescription('This is a unique index for an entry in the hm2AgentCosMapIpDscpTable. A non-zero value indicates the ifIndex for the corresponding interface entry in the ifTable. A value of zero represents global configuration, which in turn causes all interface entries to be updated for a set operation, or reflects the most recent global setting for a get operation.')
hm2AgentCosMapIpDscpValue = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpValue.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpValue.setDescription('The IP DSCP value contained in the received frame. This value is only indicated in IP packets, but is independent of both media-type and frame tagging. Non-IP packets are handled in accordance with the dot1dPortDefaultUserPriority value of the ingress port.')
hm2AgentCosMapIpDscpTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpTrafficClass.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIpDscpTrafficClass.setDescription('Traffic class priority queue the received frame is mapped to.')
hm2AgentCosMapIntfTrustTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3), )
if mibBuilder.loadTexts: hm2AgentCosMapIntfTrustTable.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIntfTrustTable.setDescription('Specifies the interface trust mode of operation for a port. The trust mode setting determines which COS mapping table is used for directing ingress packets to a Traffic Class.')
hm2AgentCosMapIntfTrustEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3, 1), ).setIndexNames((0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosMapIntfTrustIntfIndex"))
if mibBuilder.loadTexts: hm2AgentCosMapIntfTrustEntry.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIntfTrustEntry.setDescription('COS interface trust mode.')
hm2AgentCosMapIntfTrustIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: hm2AgentCosMapIntfTrustIntfIndex.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIntfTrustIntfIndex.setDescription('This is a unique index for an entry in the hm2AgentCosMapIntfTrustTable. A non-zero value indicates the ifIndex for the corresponding interface entry in the ifTable. A value of zero represents global configuration, which in turn causes all interface entries to be updated for a set operation, or reflects the most recent global setting for a get operation.')
hm2AgentCosMapIntfTrustMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("untrusted", 1), ("trustDot1p", 2), ("trustIpPrecedence", 3), ("trustIpDscp", 4))).clone('trustDot1p')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosMapIntfTrustMode.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapIntfTrustMode.setDescription('The class of service trust mode of an interface. When set to a trusted mode, the appropriate COS mapping table is used as follows: trustDot1p(2) : dot1dTrafficClassTable trustIpPrecedence(3): hm2AgentCosMapIpPrecTable trustIpDscp(4): hm2AgentCosMapIpDscpTable For an untrusted(1) interface, packets are handled in accordance with the dot1dPortDefaultUserPriority value of the ingress port.')
hm2AgentCosMapUntrustedTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentCosMapUntrustedTrafficClass.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosMapUntrustedTrafficClass.setDescription('The traffic class (i.e. hardware queue) to which all untrusted traffic is assigned. This includes all traffic when the hm2AgentCosMapIntfTrustMode is set to untrusted(1), or just non-IP packets when in trustIpPrecedence(3) or trustIpDscp(4) modes. This is a read-only object that reflects the current setting of the dot1dPortDefaultUserPriority object as mapped to a traffic class through the dot1dTrafficClassEntry.')
hm2AgentCosQueueCfgGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2))
hm2AgentCosQueueNumQueuesPerPort = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentCosQueueNumQueuesPerPort.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueNumQueuesPerPort.setDescription('The number of configurable COS queues per port supported by the hardware device.')
hm2AgentCosQueueNumDropPrecedenceLevels = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentCosQueueNumDropPrecedenceLevels.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueNumDropPrecedenceLevels.setDescription('The number of distinct drop precedence levels per queue supported by the hardware device. These levels are typically used when configuring the queue management tail drop and WRED parameters.')
hm2AgentCosQueueControlTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3), )
if mibBuilder.loadTexts: hm2AgentCosQueueControlTable.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueControlTable.setDescription('Table of class-of-service queue configuration controls for the specified interface.')
hm2AgentCosQueueControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1), ).setIndexNames((0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIntfIndex"))
if mibBuilder.loadTexts: hm2AgentCosQueueControlEntry.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueControlEntry.setDescription('Provides a general control mechanism that affects all queues on a given interface.')
hm2AgentCosQueueIntfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: hm2AgentCosQueueIntfIndex.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueIntfIndex.setDescription('This is a unique index for an entry in the hm2AgentCosQueueControlTable, hm2AgentCosQueueTable, or hm2AgentCosQueueMgmtTable. A non-zero value indicates the ifIndex for the corresponding interface entry in the ifTable. A value of zero represents global configuration, which in turn causes all interface entries to be updated for a set operation, or reflects the most recent global setting for a get operation.')
hm2AgentCosQueueIntfShapingRate = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueIntfShapingRate.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueIntfShapingRate.setDescription('Maximum bandwidth allowed for this interface as a whole, typically used to shape the outbound transmission rate. The value is specified in terms of percentage of overall link speed for the port in 1% increments. A value of 0 means there is no maximum bandwidth limit in effect and that the interface is allowed to transmit up to its maximum line rate (i.e., work conserving method). The default value is 0. When set to a non-zero value, the interface is restricted to using at most the bandwidth specified in this object for the outbound transmission rate (i.e., non-work-conserving method). This bandwidth value is independent of any per-queue maximum bandwidth value(s) in effect for the interface, as specified in the hm2AgentCosQueueMaxBandwidth ohject, and should be considered as a second-level transmission rate control mechanism that regulates the output of the entire interface regardless of which queues originate the outbound traffic. Valid value ranges depend on the value returned by object hm2AgentCosQueueIntfShapingRateUnits. If that object returns percent(1), hm2AgentCosQueueIntfShapingRate accepts values 0..100. If that object returns kbps(2), hm2AgentCosQueueIntfShapingRate accepts values 0,64..4294967295.')
hm2AgentCosQueueMgmtTypeIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("taildrop", 1), ("wred", 2))).clone('taildrop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtTypeIntf.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtTypeIntf.setDescription('The management technique used for all queues on this interface. If taildrop(1), then all new packets presented to the queues are dropped based on some maximum threshold value(s). If wred(2), then an active queue management scheme is employed whereby packet drop precedence is considered during times of queue congestion using WRED parameters. The necessary queue management parameters are specified in the hm2AgentCosQueueMgmtTable for the corresponding hm2AgentCosQueueIntfIndex value. The default for this object is taildrop(1). Implementations that support this object but do not support weighted RED must return taildrop(1) for this value and must not allow a value of wred(2) to be set.')
hm2AgentCosQueueWredDecayExponent = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)).clone(9)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueWredDecayExponent.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueWredDecayExponent.setDescription('The decay exponent value used with the weighted random early discard (WRED) algorithm to determine how quickly the average queue length calculation reacts to the current length of the queue. A higher value produces a slower response, meaning previously sampled queue length values are factored into the calculation for a longer period of time. The default value is 9. Use caution when changing this value from its default. If set too low, short traffic bursts can cause WRED to drop too many packets. If set too high, WRED might not detect queue congestion in a timely manner and becomes ineffective. The default value should be sufficient for most users. This object value is only used when the hm2AgentCosQueueMgmtType is set to wred(2) and is otherwise ignored.')
hm2AgentCosQueueDefaultsRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 5), HmEnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueDefaultsRestore.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueDefaultsRestore.setDescription('Causes the default values to be restored for all COS queue objects defined for this interface. This includes objects in the following tables: hm2AgentCosQueueTable hm2AgentCosQueueMgmtTable This object always reads as disable(2). This object may only be set to enable(1), which immediately causes the default value restoration action as described above. In essence, this models a momentary-style push button switch that triggers a restoration of the original default values for all affected objects.')
hm2AgentCosQueueIntfShapingRateUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("percent", 1), ("kbps", 2))).clone('percent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentCosQueueIntfShapingRateUnits.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueIntfShapingRateUnits.setDescription('Gets the units of the threshold value to percentage of port speed or kilobits per second (kbps).')
hm2AgentCosQueueTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4), )
if mibBuilder.loadTexts: hm2AgentCosQueueTable.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueTable.setDescription('Table of class-of-service queue configuration parameters for the specified interface.')
hm2AgentCosQueueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1), ).setIndexNames((0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIntfIndex"), (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIndex"))
if mibBuilder.loadTexts: hm2AgentCosQueueEntry.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueEntry.setDescription("Each entry describes a single class-of-service (COS) queue for a given Interface Index. The number of configurable COS queues for an interface vary based on device capabilities. All objects defined for this table entry contain a default value corresponding to a typical, non-preferential treatment of packets traversing the interface's COS queues.")
hm2AgentCosQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hm2AgentCosQueueIndex.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueIndex.setDescription('The COS queue index, numbered 0 to (n-1), where n is the total number of configurable interface queues for the device as indicated by hm2AgentCosQueueNumQueuesPerPort. In general, a higher numbered queue index is used to support higher priority traffic, although actual operation may be altered via configuration through this table.')
hm2AgentCosQueueSchedulerType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("strict", 1), ("weighted", 2))).clone('strict')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueSchedulerType.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueSchedulerType.setDescription('The type of scheduling used for this queue. If strict(1), then all traffic placed on this queue is transmitted before any queue with a lower precedence (lower hm2AgentCosQueueIndex). A weighted(2) scheme gives this queue service relative to other weighted queues based on their relative hm2AgentCosQueueMinBandwidth object values. The default is strict(1).')
hm2AgentCosQueueMinBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 3), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMinBandwidth.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueMinBandwidth.setDescription('Minimum guaranteed bandwidth allotted to this queue. The value is specified in terms of percentage of overall link speed for the port in 1% increments. A value of 0 means there is no guaranteed minimum bandwidth in effect (best-effort service). The default value is 0. The sum of all hm2AgentCosQueueMinBandwidth object values for the queues on the same interface must not exceed 100%. If the hm2AgentCosQueueMaxBandwidth corresponding to the same hm2AgentCosQueueIndex on this interface is currently set to a non-zero value, then setting this object to a value greater than hm2AgentCosQueueMaxBandwidth automatically updates hm2AgentCosQueueMaxBandwidth to the same value to maintain a proper relationship between the minimum and maximum queue bandwidth specification. The value of this object is ignored when hm2AgentCosQueueSchedulerType is set to strict(1).')
hm2AgentCosQueueMaxBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 4), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMaxBandwidth.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueMaxBandwidth.setDescription('Maximum bandwidth allowed for this queue, typically used to shape the outbound transmission rate. The value is specified in terms of percentage of overall link speed for the port in 1% increments. A value of 0 means there is no maximum bandwidth limit in effect and that the queue is allowed to use any available excess bandwidth (i.e., work conserving method). The default value is 0. When set to a non-zero value, the queue is restricted to using at most the bandwidth specified in this object for the outbound transmission rate (i.e., non-work-conserving method). Any non-zero value set for this object must be equal to or greater than the value of hm2AgentCosQueueMinBandwidth for the same hm2AgentCosQueueIndex on this interface.')
hm2AgentCosQueueMgmtType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("taildrop", 1), ("wred", 2))).clone('taildrop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtType.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtType.setDescription('The queue depth management technique used when per-queue specification is supported. If taildrop(1), then all new packets presented to the queue are dropped based on some maximum threshold value(s). If wred(2), then an active queue management scheme is employed whereby packet drop precedence is considered during times of queue congestion using WRED parameters. The necessary queue management parameters are specified in the hm2AgentCosQueueMgmtEntry for the corresponding hm2AgentCosQueueIntfIndex and hm2AgentCosQueueIndex values. The default for this object is taildrop(1). Implementations that do not support weighted RED must return taildrop(1) for this value and must not allow a value of wred(2) to be set.')
hm2AgentCosQueueMgmtTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5), )
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtTable.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtTable.setDescription('Table of class-of-service queue drop precedence configuration parameters. The values in this table are used based on the hm2AgentCosQueueMgmtType for the corresponding hm2AgentCosQueueIntfIndex and hm2AgentCosQueueIndex values. These parameters are specified for each drop precedence level supported within a queue.')
hm2AgentCosQueueMgmtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1), ).setIndexNames((0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIntfIndex"), (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueIndex"), (0, "HM2-PLATFORM-QOS-COS-MIB", "hm2AgentCosQueueDropPrecIndex"))
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtEntry.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtEntry.setDescription("The individual objects in this table are specified for each drop precedence level supported within a particular queue on a given interface. Each object's usage is based on the current setting of the hm2AgentCosQueueMgmtType. See the individual object descriptions for details.")
hm2AgentCosQueueDropPrecIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hm2AgentCosQueueDropPrecIndex.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueDropPrecIndex.setDescription('The COS queue drop precedence level, numbered 1 to p, where p is the total number of drop precedences supported per queue, as indicated by hm2AgentCosQueueNumDropPrecedenceLevels. This is used as the minor index into the table. Each supported drop precedence level for a queue has its own set of configuration parameters. The actual number of drop precedence levels supported depends on the device characteristics. For example, some implementations may allow for three levels of drop precedence (1/2/3, sometimes referred to as green/yellow/red), some may support two levels (1/2, or high/low), while others only one. Some devices use the lowest (highest-numbered) drop precedence level to represent non-TCP traffic.')
hm2AgentCosQueueMgmtTailDropThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 2), Sixteenths()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtTailDropThreshold.setStatus('obsolete')
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtTailDropThreshold.setDescription('Tail drop queue threshold above which all packets are dropped for the current drop precedence level. The value specifies the threshold based on a fraction of the overall device queue size in terms of sixteenths (0/16, 1/16, 2/16, ... 16/16). Since device implementations vary, the actual value deployed may be rounded up or down accordingly. The default value is calculated from the hm2AgentCosQueueIndex and hm2AgentCosQueueDropPrecIndex as shown in the following table (values listed for drop precedence levels 1, 2, and 3, respectively): Queue Index 0: 16, 14, 12 Queue Index 1: 16, 14, 12 Queue Index 2: 16, 14, 12 Queue Index 3: 16, 14, 12 Queue Index 4: 16, 14, 12 Queue Index 5: 16, 14, 12 Queue Index 6: 16, 14, 12 Queue Index 7: 16, 14, 12 This object is only used when hm2AgentCosQueueMgmtType is set to taildrop(1).')
hm2AgentCosQueueMgmtWredMinThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 3), Sixteenths()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtWredMinThreshold.setStatus('obsolete')
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtWredMinThreshold.setDescription('Weighted RED minimum queue threshold, below which no packets are dropped for the current drop precedence level. The value specifies the threshold based on a fraction of the overall device queue size in terms of sixteenths (0/16, 1/16, 2/16, ... 16/16). Since device implementations vary, the actual value deployed may be rounded up or down accordingly. The default value is calculated from the hm2AgentCosQueueIndex and hm2AgentCosQueueDropPrecIndex as shown in the following table (values listed for drop precedence levels 1, 2, and 3, respectively): Queue Index 0: 8, 6, 4 Queue Index 1: 9, 7, 5 Queue Index 2: 10, 8, 6 Queue Index 3: 11, 9, 7 Queue Index 4: 12, 10, 8 Queue Index 5: 13, 11, 9 Queue Index 6: 14, 12, 10 Queue Index 7: 15, 13, 11 This object is only used when hm2AgentCosQueueMgmtType is set to wred(2). Any value set for this object must be equal to or less than the value of hm2AgentCosQueueMgmtWredMaxThreshold.')
hm2AgentCosQueueMgmtWredMaxThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 4), Sixteenths()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtWredMaxThreshold.setStatus('obsolete')
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtWredMaxThreshold.setDescription('Weighted RED maximum queue threshold, above which all packets are dropped for the current drop precedence level. The value specifies the threshold based on a fraction the overall device queue size in terms of sixteenths (0/16, 1/16, 2/16, ... 16/16). Since device implementations vary, the actual value deployed may be rounded up or down accordingly. The default value is calculated from the hm2AgentCosQueueIndex and hm2AgentCosQueueDropPrecIndex as shown in the following table (values listed for drop precedence levels 1, 2, and 3, respectively): Queue Index 0: 16, 14, 12 Queue Index 1: 16, 14, 12 Queue Index 2: 16, 14, 12 Queue Index 3: 16, 14, 12 Queue Index 4: 16, 14, 12 Queue Index 5: 16, 14, 12 Queue Index 6: 16, 14, 12 Queue Index 7: 16, 14, 12 This object is only used when hm2AgentCosQueueMgmtType is set to wred(2). Any value set for this object must be equal to or greater than the value of hm2AgentCosQueueMgmtWredMinThreshold.')
hm2AgentCosQueueMgmtWredDropProbScale = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtWredDropProbScale.setStatus('obsolete')
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtWredDropProbScale.setDescription('A scaling factor used for the WRED calculation to determine the packet drop probability for the current drop precedence level. The value is specified as a number S from 1-15 and is used in the formula: 1/(2** S), meaning one packet is dropped out of every (2** S). Packet dropping begins when hm2AgentCosQueueMgmtWredMinThreshold is reached and proceeds linearly up to the (2**S) value specified by this object until the hm2AgentCosQueueMgmtWredMaxThreshold is reached, beyond which all packets are dropped. Smaller values of S produce a steeper slope, hence a higher incidence of randomly dropped packets. The default value is 10, which corresponds to a drop rate of 1 out of every (2**10)=1024 packets. This object is only used when hm2AgentCosQueueMgmtType is set to wred(2).')
hm2AgentCosQueueMgmtPercentTailDropThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 6), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtPercentTailDropThreshold.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtPercentTailDropThreshold.setDescription('Tail drop queue threshold above which all packets are dropped for the current drop precedence level. The value specifies the threshold based on a percentage of the overall device queue size. Since device implementations vary, the actual value deployed may be rounded up or down accordingly. The default value, for all queues, is 100% for drop precedence 1 and non-TCP traffic, 90% and 80% for drop precedences 2 and 3. This object is only used when hm2AgentCosQueueMgmtType is set to taildrop(1).')
hm2AgentCosQueueMgmtPercentWredMinThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 7), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtPercentWredMinThreshold.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtPercentWredMinThreshold.setDescription('Weighted RED minimum queue threshold, below which no packets are dropped for the current drop precedence level. The value specifies the threshold based on a percentage of the overall device queue size. Since device implementations vary, the actual value deployed may be rounded up or down accordingly. The default value, for all queues, is 100% for non-TCP traffic, 40%, 30% and 20% for TCP drop precedences 1, 2 and 3. This object is only used when hm2AgentCosQueueMgmtType is set to wred(2). Any value set for this object must be equal to or less than the value of hm2AgentCosQueueMgmtPercentWredMaxThreshold.')
hm2AgentCosQueueMgmtPercentWredMaxThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 8), Percent()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtPercentWredMaxThreshold.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtPercentWredMaxThreshold.setDescription('Weighted RED maximum queue threshold, above which all packets are dropped for the current drop precedence level. The value specifies the threshold based on a percentage of the overall device queue size. Since device implementations vary, the actual value deployed may be rounded up or down accordingly. The default value, for all queues, is 100% for drop precedence 1 and non-TCP traffic, 90% and 80% for drop precedences 2 and 3. This object is only used when hm2AgentCosQueueMgmtType is set to wred(2). Any value set for this object must be equal to or greater than the value of hm2AgentCosQueueMgmtPercentWredMinThreshold.')
hm2AgentCosQueueMgmtWredDropProbability = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 3, 3, 2, 5, 1, 9), Percent().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtWredDropProbability.setStatus('current')
if mibBuilder.loadTexts: hm2AgentCosQueueMgmtWredDropProbability.setDescription('A scaling factor used for the WRED calculation to determine the packet drop probability for the current drop precedence level. Packet dropping begins when hm2AgentCosQueueMgmtWredMinThreshold is reached and proceeds linearly up to the percentage value specified by this object until the hm2AgentCosQueueMgmtWredMaxThreshold is reached, beyond which all packets are dropped. The default value is 10. This object is only used when hm2AgentCosQueueMgmtType is set to wred(2).')
mibBuilder.exportSymbols("HM2-PLATFORM-QOS-COS-MIB", hm2AgentCosMapIntfTrustTable=hm2AgentCosMapIntfTrustTable, hm2AgentCosQueueCfgGroup=hm2AgentCosQueueCfgGroup, hm2AgentCosMapIpPrecValue=hm2AgentCosMapIpPrecValue, hm2PlatformQosCos=hm2PlatformQosCos, hm2AgentCosQueueEntry=hm2AgentCosQueueEntry, hm2AgentCosQueueDropPrecIndex=hm2AgentCosQueueDropPrecIndex, hm2AgentCosQueueMgmtType=hm2AgentCosQueueMgmtType, hm2AgentCosMapUntrustedTrafficClass=hm2AgentCosMapUntrustedTrafficClass, hm2AgentCosQueueMgmtTailDropThreshold=hm2AgentCosQueueMgmtTailDropThreshold, hm2AgentCosQueueMgmtWredMaxThreshold=hm2AgentCosQueueMgmtWredMaxThreshold, Sixteenths=Sixteenths, hm2AgentCosQueueMinBandwidth=hm2AgentCosQueueMinBandwidth, hm2AgentCosQueueMaxBandwidth=hm2AgentCosQueueMaxBandwidth, hm2AgentCosQueueIntfShapingRate=hm2AgentCosQueueIntfShapingRate, hm2AgentCosMapIpDscpIntfIndex=hm2AgentCosMapIpDscpIntfIndex, hm2AgentCosQueueMgmtPercentWredMaxThreshold=hm2AgentCosQueueMgmtPercentWredMaxThreshold, hm2AgentCosQueueIntfShapingRateUnits=hm2AgentCosQueueIntfShapingRateUnits, hm2AgentCosMapIpPrecTrafficClass=hm2AgentCosMapIpPrecTrafficClass, hm2AgentCosMapIpDscpEntry=hm2AgentCosMapIpDscpEntry, PYSNMP_MODULE_ID=hm2PlatformQosCos, hm2AgentCosMapIpDscpValue=hm2AgentCosMapIpDscpValue, hm2AgentCosQueueWredDecayExponent=hm2AgentCosQueueWredDecayExponent, hm2AgentCosMapCfgGroup=hm2AgentCosMapCfgGroup, hm2AgentCosQueueIndex=hm2AgentCosQueueIndex, hm2AgentCosQueueDefaultsRestore=hm2AgentCosQueueDefaultsRestore, hm2AgentCosMapIpPrecTable=hm2AgentCosMapIpPrecTable, hm2AgentCosQueueMgmtTable=hm2AgentCosQueueMgmtTable, hm2AgentCosMapIpPrecIntfIndex=hm2AgentCosMapIpPrecIntfIndex, hm2AgentCosQueueIntfIndex=hm2AgentCosQueueIntfIndex, hm2AgentCosQueueMgmtWredDropProbScale=hm2AgentCosQueueMgmtWredDropProbScale, Percent=Percent, hm2AgentCosMapIpPrecEntry=hm2AgentCosMapIpPrecEntry, hm2AgentCosQueueMgmtWredDropProbability=hm2AgentCosQueueMgmtWredDropProbability, hm2AgentCosQueueMgmtPercentTailDropThreshold=hm2AgentCosQueueMgmtPercentTailDropThreshold, hm2AgentCosQueueNumQueuesPerPort=hm2AgentCosQueueNumQueuesPerPort, hm2AgentCosMapIpDscpTrafficClass=hm2AgentCosMapIpDscpTrafficClass, hm2AgentCosQueueMgmtWredMinThreshold=hm2AgentCosQueueMgmtWredMinThreshold, hm2AgentCosMapIntfTrustIntfIndex=hm2AgentCosMapIntfTrustIntfIndex, hm2AgentCosQueueSchedulerType=hm2AgentCosQueueSchedulerType, hm2AgentCosQueueControlTable=hm2AgentCosQueueControlTable, hm2AgentCosQueueMgmtEntry=hm2AgentCosQueueMgmtEntry, hm2AgentCosMapIntfTrustEntry=hm2AgentCosMapIntfTrustEntry, hm2AgentCosQueueNumDropPrecedenceLevels=hm2AgentCosQueueNumDropPrecedenceLevels, hm2AgentCosQueueMgmtPercentWredMinThreshold=hm2AgentCosQueueMgmtPercentWredMinThreshold, hm2AgentCosQueueMgmtTypeIntf=hm2AgentCosQueueMgmtTypeIntf, hm2AgentCosQueueControlEntry=hm2AgentCosQueueControlEntry, hm2AgentCosMapIpDscpTable=hm2AgentCosMapIpDscpTable, hm2AgentCosQueueTable=hm2AgentCosQueueTable, hm2AgentCosMapIntfTrustMode=hm2AgentCosMapIntfTrustMode)
