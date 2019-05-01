#
# PySNMP MIB module CISCO-ENTITY-PFE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-PFE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:57:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
PhysicalIndex, entPhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex", "entPhysicalIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Unsigned32, TimeTicks, Gauge32, Counter32, IpAddress, ObjectIdentity, ModuleIdentity, Counter64, NotificationType, iso, MibIdentifier, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Gauge32", "Counter32", "IpAddress", "ObjectIdentity", "ModuleIdentity", "Counter64", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp")
ciscoEntityPfeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 265))
ciscoEntityPfeMib.setRevisions(('2002-11-27 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEntityPfeMib.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEntityPfeMib.setLastUpdated('200211271600Z')
if mibBuilder.loadTexts: ciscoEntityPfeMib.setOrganization('Cisco System, Inc.')
if mibBuilder.loadTexts: ciscoEntityPfeMib.setContactInfo('Postal: Cisco Systems, Inc. 170 West Tasman Drive San Jose, CA 95134-1706 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEntityPfeMib.setDescription('The Packet Forwarding Engine technology are Cisco developed Network Processors, which accelerates certain features in order to provide better network performance. An agent uses this MIB to monitor the performance history on any active PFE pipeline listed in the ENTITY-MIB (RFC 2737) entPhysicalTable. This monitoring is via measurement periods of actual, 1-minute, 5-minutes and 15-minutes. For the 1-minute and 5-minute measurement periods, perfor- mance statistics are calculated and displayed based on pre- vious 1 minute and 5 minute respectively. For the 15-minute period, the performance statistics are accumulated in fifteen minute intervals. At any one time, an agent maintains one current (incomplete) interval and up to 96 completed intervals (24 hours worth). Fewer than 96 intervals of data will be available if the agent has been restarted within the last 24 hours. In addition, there is a rolling 24-hour total of each performance statistic. There is no requirement for an agent to ensure fixed rela- tionship between the start of a fifteen minute interval and any wall clock; however some agents may align the fifteen minute intervals with quarter hours.')
class CurrentUtilization(TextualConvention, Gauge32):
    description = 'A percentage value that represent the actual utilization performance measurement.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class CurrentEfficiency(TextualConvention, Gauge32):
    description = 'A percentage value that represents the actual efficiency performance measurement.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class IntervalUtilization(TextualConvention, Gauge32):
    description = 'A percentage value that represents the utilization perfor- mance measurement in a previous 15 minute measurement interval. In the case where the agent has no valid data available for a particular interval the corresponding object instance is not available and upon a retrieval request a corresponding error message shall be returned to indicate that this instance does not exist (for example, a noSuchObject error for SNMPv1 and a noSuchInstance for SNMPv2 GET operation). In a system supporting a history of n intervals with IntervalUtilization(1) and IntervalUtilization(n) the most and least recent intervals respectively, the following proce- dure is used to update the intervals at end of a 15 minute interval: - discard the value of IntervalUtilization(n) - the value of IntervalUtilization(i) becomes that of IntervalUtilization(i-1) for n >= i > 1 - the value of IntervalUtilization(1) becomes that of current 15-minute %utilization.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class IntervalEfficiency(TextualConvention, Gauge32):
    description = 'A percentage value that represents the efficiency performance measurement in a previous 15 minute measurement interval. In the case where the agent has no valid data available for a particular interval the corresponding object instance is not available and upon a retrieval request a corresponding error message shall be returned to indicate that this instance does not exist (for example, a noSuchObject error for SNMPv1 and a noSuchInstance for SNMPv2 GET operation). In a system supporting a history of n intervals with IntervalEfficiency(1) and IntervalEfficiency(n) the most and least recent intervals respectively, the following procedure is used to update the intervals at end of a 15 minute inter- val: - discard the value of IntervalEfficiency(n) - the value of IntervalEfficiency(i) becomes that of IntervalEfficiency(i-1) for n >= i > 1 - the value of IntervalEfficiency(1) becomes that of currente 15-minute %efficiency.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class TotalUtilization(TextualConvention, Gauge32):
    description = 'A percentage value that represents the total running utili- zation performance measurements.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class TotalEfficiency(TextualConvention, Gauge32):
    description = 'A percentage value that represents the total running Effi- ciency performance measurements.'
    status = 'current'
    subtypeSpec = Gauge32.subtypeSpec + ValueRangeConstraint(0, 100)

class Percentage(TextualConvention, Unsigned32):
    description = 'A percentage value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

class EventType(TextualConvention, Integer32):
    description = "Type of action to execute when an event occurs. 'none' Neither log an entry in the cePfeHistTable, nor sent out an SNMP notification. 'log' Create a cePfeHistTable entry, but do not sent out an SNMP notification. 'notify' Sent out an SNMP notification, but do not create a log entry in the cePfeHistTable. 'logAndNotify' Both create a log entry in the cePfeHistTable and sent out an SNMP notification."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("log", 2), ("notify", 3), ("logAndNotify", 4))

class HistEventType(TextualConvention, Integer32):
    description = "Type of event that has occurred. 'thldUtilizationEvent' This event is generated if the cePfePerfCurrentUtilization, at the time of sampling, becomes greater than or equal to the cePfePerfThldUtilization. 'thldEfficiencyEvent' This event is generated if the cePfePerfCurrentEfficiency, at the time of sampling, becomes less than or equal to the cePfePerfThldEfficiency. 'thld1MinUtilizationEvent' This event is generated if the cePfePerfCurrent1MinUtilization, at the time of sampling, becomes greater than or equal to the cePfePerfThld1MinUtilization. 'thld1MinEfficiencyEvent' This event is generated if the cePfePerfCurrent1MinEfficiency, at the time of sampling, becomes less than or equal to the cePfePerfThld1MinEfficiency. 'thld5MinUtilizationEvent' This event is generated if the cePfePerfCurrent5MinUtilization, at the time of sampling, becomes greater than or equal to the cePfePerfThld5MinUtilization. 'thld5MinEfficiencyEvent' This event is generated if the cePfePerfCurrent5MinEfficiency, at the time of sampling, becomes less than or equal to the cePfePerfThld5MinEfficiency. 'restartEvent' This event is generated every time the processor gets restarted."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("thldUtilizationEvent", 1), ("thldEfficiencyEvent", 2), ("thld1MinUtilizationEvent", 3), ("thld1MinEfficiencyEvent", 4), ("thld5MinUtilizationEvent", 5), ("thld5MinEfficiencyEvent", 6), ("restartEvent", 7))

cePfeMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 0))
cePfeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 1))
cePfeMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 2))
cePfePerformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1))
cePfeHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2))
cePfePerfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1), )
if mibBuilder.loadTexts: cePfePerfConfigTable.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigTable.setDescription('This table contains configuration information on a PFE pipeline.')
cePfePerfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cePfePerfConfigEntry.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigEntry.setDescription('An entry will exist for each entry in the entPhysicalTable that correspond to an active PFE pipeline.')
cePfePerfConfigTimeElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 899))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfConfigTimeElapsed.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigTimeElapsed.setDescription("The number of seconds that have elapsed since the beginning of the current 15 min interval. If for some reason, such as an adjustment in the system's time-of-day clock, the current interval exceeds the maximum value, the agent will return the maximum value.")
cePfePerfConfigValidIntervals = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 96))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfConfigValidIntervals.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigValidIntervals.setDescription('The number of completed 15 min intervals for which valid PFE performance data has been collected. The value will be 96 unless the interface was brought online within the last 24 hours, in which case the value will be the number of completed 15 minute intervals since the PFE pipeline has been online.')
cePfePerfConfigThldUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 3), Percentage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThldUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigThldUtilization.setDescription("This object contains the threshold value for the cePfePerfCurrentUtilization object. If during the last 5 second measurement period the cePfePerfCurrentUtilization object becomes greater than or equal to this threshold value, an event of type 'thldUtilizationEvent' will be genera- ted. Value of zero indicates that no comparison is being made between the cePfePerfCurrentUtilization object value and the threshold value, therefore no event action will be gene- rated.")
cePfePerfConfigThldEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 4), Percentage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThldEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigThldEfficiency.setDescription("This object contains the threshold value for the cePfePerfCurrentEffciency object. If during the last 5 second measurement period the cePfePerfCurrentEfficiency object becomes less than or equal to this threshold value, an event of type 'thldEfficiencyEvent' will be genera- ted. Value of zero indicates that no comparison is being made between the cePfePerfCurrentEfficiency object value and the threshold value, therefore no event action will be gene- rated.")
cePfePerfConfigThld1MinUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 5), Percentage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThld1MinUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigThld1MinUtilization.setDescription("This object contains the threshold value for the cePfePerfCurrent1MinUtilization object. If during the last 1 minute measurement period the cePfePerfCurrent1MinUtilization object becomes greater than or equal to this threshold value, an event of type 'thld1MinUtilizationEvent' will be genera- ted. Value of zero indicates that no comparison is being made between the cePfePerfCurrent1MinUtilization object value and the threshold value, therefore no event action will be gene- rated.")
cePfePerfConfigThld1MinEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 6), Percentage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThld1MinEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigThld1MinEfficiency.setDescription("This object contains the threshold value for the cePfePerfCurrent1MinEfficiency object. If during the last 1 minute measurement period the cePfePerfCurrent1MinEfficiency object becomes less than or equal to this threshold value, an event of type 'thld1MinEfficiencyEvent' will be genera- ted. Value of zero indicates that no comparison is being made between the cePfePerfCurrent1MinEfficiency object value and the threshold value, therefore no event action will be gene- rated.")
cePfePerfConfigThld5MinUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 7), Percentage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThld5MinUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigThld5MinUtilization.setDescription("This object contains the threshold value for the cePfePerfCurrent5MinUtilization object. If during the last 5 minute measurement period the cePfePerfCurrent5MinUtilization object becomes greater than or equal to this threshold value, an event of type 'thld5MinUtilizationEvent' will be genera- ted. Value of zero indicates that no comparison is being made between the cePfePerfCurrent5MinUtilization object value and the threshold value, therefore no event action will be gene- rated.")
cePfePerfConfigThld5MinEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 1, 1, 8), Percentage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfePerfConfigThld5MinEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfConfigThld5MinEfficiency.setDescription("This object contains the threshold value for the cePfePerfCurrent5MinEfficiency object. If during the last 5 minute measurement period the cePfePerfCurrent5MinEfficiency object becomes less than or equal to this threshold value, an event of type 'thld5MinEfficiencyEvent' will be genera- ted. Value of zero indicates that no comparison is being made between the cePfePerfCurrent5MinEfficiency object value and the threshold value, therefore no event action will be gene- rated.")
cePfePerfCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2), )
if mibBuilder.loadTexts: cePfePerfCurrentTable.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrentTable.setDescription('This table maintains PFE current running performance, which are collected at various measurement periods.')
cePfePerfCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1), )
cePfePerfConfigEntry.registerAugmentions(("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrentEntry"))
cePfePerfCurrentEntry.setIndexNames(*cePfePerfConfigEntry.getIndexNames())
if mibBuilder.loadTexts: cePfePerfCurrentEntry.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrentEntry.setDescription('An entry containing performance information applicable to a particular PFE pipeline.')
cePfePerfCurrentUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 1), CurrentUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrentUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrentUtilization.setDescription('This object provides the actual PFE percentage utilization. It is determined by the number of new work contexts + feedback contexts divided by total number of contexts that can be supported by the PFE pipeline.')
cePfePerfCurrentEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 2), CurrentEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrentEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrentEfficiency.setDescription('This object provides the actual PFE percentage efficiency. It is determined by the total number of contexts per second divided by maximum theoretical contexts per second supported by the PFE pipeline. Under normal conditions, this number will be 100 and when efficiency starts degrading, it will start going down until it reaches zero.')
cePfePerfCurrent1MinUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 3), CurrentUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrent1MinUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrent1MinUtilization.setDescription('This object provides the PFE percentage utilization over the previous 1 minute period. It is determined by the number of new work contexts + feedback contexts divided by total number of contexts that can be supported by the PFE pipeline.')
cePfePerfCurrent1MinEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 4), CurrentEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrent1MinEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrent1MinEfficiency.setDescription('This object provides the PFE percentage efficiency over the previous 1 minute period. It is determined by the totalnumber of contexts per second divided by maximum theoretical contexts per second supported by the PFE pipeline. Under normal conditions, this number will be 100 and when efficiency starts degrading, it will start going down until it reaches zero.')
cePfePerfCurrent5MinUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 5), CurrentUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrent5MinUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrent5MinUtilization.setDescription('This object provides the PFE percentage utilization over the previous 5 minutes period. It is determined by the number of new work contexts + feedback contexts divided by total number of contexts that can be supported by the PFE pipeline.')
cePfePerfCurrent5MinEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 2, 1, 6), CurrentEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfCurrent5MinEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfCurrent5MinEfficiency.setDescription('This object provides the PFE percentage efficiency over the previous 5 minutes period. It is determined by the total number of contexts per second divided by maximum theoretical contexts per second supported by the PFE pipeline. Under normal conditions, this number will be 100 and when efficiency starts degrading, it will start going down until it reaches zero.')
cePfePerfIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3), )
if mibBuilder.loadTexts: cePfePerfIntervalTable.setStatus('current')
if mibBuilder.loadTexts: cePfePerfIntervalTable.setDescription('This table contains performance statistics for completed 15 minutes intervals, specifically up to 96 such intervals over a 24 hours of operation.')
cePfePerfIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-PFE-MIB", "cePfePerfIntervalNumber"))
if mibBuilder.loadTexts: cePfePerfIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: cePfePerfIntervalEntry.setDescription('An entry containing performance information applicable to a particular PFE pipeline at a specific interval.')
cePfePerfIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 96)))
if mibBuilder.loadTexts: cePfePerfIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: cePfePerfIntervalNumber.setDescription('An interval number between 1 and 96, where 1 is the most recently completed 15 min interval and 96 is the 15 min interval completed 23 hours and 45 minutes prior to interval 1.')
cePfePerfIntervalUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1, 2), IntervalUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfIntervalUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfIntervalUtilization.setDescription('The percentage of processor utilization by the PFE pipeline during this completed 15 min interval.')
cePfePerfIntervalEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 3, 1, 3), IntervalEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfIntervalEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfIntervalEfficiency.setDescription('The percentage of processor efficiency by the PFE pipeline during this completed 15 min interval. Under normal conditions, this number will be 100 and when efficiency starts degrading, it will start going down until it reaches zero.')
cePfePerfTotalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4), )
if mibBuilder.loadTexts: cePfePerfTotalTable.setStatus('current')
if mibBuilder.loadTexts: cePfePerfTotalTable.setDescription('This table contains the running utilization and efficiency of the PFE pipeline for the 24 hour period preceding the current interval. If the agent was restarted less than 24 hours ago, i.e., when there are less than 96 intervals in the cePfePerfIntervalTable, it will contain the running utiliza- tion and efficiency up to the last collected 15 minute inter- val.')
cePfePerfTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cePfePerfTotalEntry.setStatus('current')
if mibBuilder.loadTexts: cePfePerfTotalEntry.setDescription('An entry containing performance information applicable to a particular PFE pipeline at the end of each interval in the cePfePerfIntervalTable.')
cePfePerfTotalUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4, 1, 1), TotalUtilization()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfTotalUtilization.setStatus('current')
if mibBuilder.loadTexts: cePfePerfTotalUtilization.setDescription('The running utilization by the PFE pipeline for the prece- ding 24 hrs.')
cePfePerfTotalEfficiency = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 1, 4, 1, 2), TotalEfficiency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfePerfTotalEfficiency.setStatus('current')
if mibBuilder.loadTexts: cePfePerfTotalEfficiency.setDescription('The running efficiency by the PFE pipeline for the preceding 24 hrs. Under normal conditions, this number will be 100 and when efficiency starts degrading, it will start going down until it reaches zero.')
cePfeHistNotifiesEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 1), EventType().clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfeHistNotifiesEnable.setStatus('current')
if mibBuilder.loadTexts: cePfeHistNotifiesEnable.setDescription('This object indicates what type of action should be taken by the agent when a event is generated.')
cePfeHistTableSize = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cePfeHistTableSize.setStatus('current')
if mibBuilder.loadTexts: cePfeHistTableSize.setDescription("This object specifies the number of entries that the cePfeHistTable can contain. When a event is generated, and the capacity of the cePfeHistTable has reached the value specified by this object, then the agent deletes the oldest entity in order to accommodate the new entry. A value of '0' prevents any history from being retained.")
cePfeHistTableLastIndex = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistTableLastIndex.setStatus('current')
if mibBuilder.loadTexts: cePfeHistTableLastIndex.setDescription('This object specifies the value of the cePfeHistIndex object corresponding to the last entry added to the table by the agent. It will return zero if there are no entries in the table. If the management client uses the notifications defined by this module, then it can poll this object to determine whether it has missed a notification sent by the agent.')
cePfeHistTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4), )
if mibBuilder.loadTexts: cePfeHistTable.setStatus('current')
if mibBuilder.loadTexts: cePfeHistTable.setDescription('This table contains a history of events generated by the agent.')
cePfeHistEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1), ).setIndexNames((0, "CISCO-ENTITY-PFE-MIB", "cePfeHistIndex"))
if mibBuilder.loadTexts: cePfeHistEntry.setStatus('current')
if mibBuilder.loadTexts: cePfeHistEntry.setDescription("An entry will exist for each event that has occured while cePfeHistNotifiesEnable object is set to 'log(2)' or 'logAndNotify(4)'.")
cePfeHistIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: cePfeHistIndex.setStatus('current')
if mibBuilder.loadTexts: cePfeHistIndex.setDescription("An integer value uniquely identifying the entry in the table. The value of this object starts at '1' and monotonically increases for each event condition transition monitored by the agent. If the value of this object is '4294967295', the agent will reset the index to '1' upon monitoring the next event condition transition.")
cePfeHistEntPhysIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 2), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistEntPhysIndex.setStatus('current')
if mibBuilder.loadTexts: cePfeHistEntPhysIndex.setDescription('The value in this object is equal to the value of the entPhysicalIndex, from the Physical Entity Table (RFC 2037), that is associated with the PFE pipeline that has caused this event.')
cePfeHistType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 3), HistEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistType.setStatus('current')
if mibBuilder.loadTexts: cePfeHistType.setDescription('This object describes the type of event that has occurred.')
cePfeHistThld = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 4), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistThld.setStatus('current')
if mibBuilder.loadTexts: cePfeHistThld.setDescription('The configured value of the specific threshold.')
cePfeHistValue = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 5), Percentage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistValue.setStatus('current')
if mibBuilder.loadTexts: cePfeHistValue.setDescription('The actual value of the specific performance objects, at the time of the sample, which is related to the threshold event.')
cePfeHistRestartReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistRestartReason.setStatus('current')
if mibBuilder.loadTexts: cePfeHistRestartReason.setDescription('The reason for which the PFE pipeline has restarted.')
cePfeHistTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 265, 1, 2, 4, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cePfeHistTimeStamp.setStatus('current')
if mibBuilder.loadTexts: cePfeHistTimeStamp.setDescription('This object specifies the value of the sysUpTime object at the time the event was generated.')
cePfeHistThldEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 265, 0, 1)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistEntPhysIndex"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistType"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistThld"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistValue"))
if mibBuilder.loadTexts: cePfeHistThldEvent.setStatus('current')
if mibBuilder.loadTexts: cePfeHistThldEvent.setDescription("This notification is generated when a threshold event has occurred and the cePfeHistNotifiesEnable is set to 'notify (3)' or 'logAndNotify(4)'. After generating this notification, another such notifica- tion will not be sent out until the sample value has fallen below the threshold value.")
cePfeHistRestartEvent = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 265, 0, 2)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistEntPhysIndex"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistRestartReason"))
if mibBuilder.loadTexts: cePfeHistRestartEvent.setStatus('current')
if mibBuilder.loadTexts: cePfeHistRestartEvent.setDescription("This notification is generated when a restart event has occurred and the cePfeHistNotifiesEnable is set to 'notifyp (3)' or 'logAndNotify(4)'.")
cePfeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 1))
cePfeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2))
cePfeMIBPerformanceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 1, 1)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeMIBPerformanceGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBCurrentGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBHistGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBHistEventGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBIntervalGroup"), ("CISCO-ENTITY-PFE-MIB", "cePfeMIBTotalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBPerformanceCompliance = cePfeMIBPerformanceCompliance.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBPerformanceCompliance.setDescription('An Entity-MIB implementation can implement this module to provide PFE pipeline performance history.')
cePfeMIBPerformanceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 1)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistTableSize"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistTableLastIndex"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistNotifiesEnable"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigTimeElapsed"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigValidIntervals"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThldUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThldEfficiency"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld1MinUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld1MinEfficiency"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld5MinUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfConfigThld5MinEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBPerformanceGroup = cePfeMIBPerformanceGroup.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBPerformanceGroup.setDescription('The collection of objects which are used to manage the per- formance history of the PFE pipeline.')
cePfeMIBCurrentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 2)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrentUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrentEfficiency"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent1MinUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent1MinEfficiency"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent5MinUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfCurrent5MinEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBCurrentGroup = cePfeMIBCurrentGroup.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBCurrentGroup.setDescription("The collection of objects which are used to maintain the PFE processor's performance history over a 24 hour of operation.")
cePfeMIBIntervalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 3)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfePerfIntervalUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfIntervalEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBIntervalGroup = cePfeMIBIntervalGroup.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBIntervalGroup.setDescription("The collection of objects which are used to maintain the PFE processor's performance history over a 24 hour of operation.")
cePfeMIBTotalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 4)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfePerfTotalUtilization"), ("CISCO-ENTITY-PFE-MIB", "cePfePerfTotalEfficiency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBTotalGroup = cePfeMIBTotalGroup.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBTotalGroup.setDescription('The collection of objects which are used to manage the threshold configuration for the PFE pipeline performance.')
cePfeMIBHistGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 5)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistEntPhysIndex"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistType"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistThld"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistValue"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistRestartReason"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBHistGroup = cePfeMIBHistGroup.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBHistGroup.setDescription('The collection of objects which are used to manage the threshold configuration for the PFE pipeline performance.')
cePfeMIBHistEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 265, 2, 2, 6)).setObjects(("CISCO-ENTITY-PFE-MIB", "cePfeHistThldEvent"), ("CISCO-ENTITY-PFE-MIB", "cePfeHistRestartEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cePfeMIBHistEventGroup = cePfeMIBHistEventGroup.setStatus('current')
if mibBuilder.loadTexts: cePfeMIBHistEventGroup.setDescription('The collection of objects which are used to generate a threshold event for the PFE pipeline performance.')
mibBuilder.exportSymbols("CISCO-ENTITY-PFE-MIB", CurrentEfficiency=CurrentEfficiency, IntervalUtilization=IntervalUtilization, cePfeHistory=cePfeHistory, cePfePerfIntervalUtilization=cePfePerfIntervalUtilization, CurrentUtilization=CurrentUtilization, Percentage=Percentage, cePfeHistTimeStamp=cePfeHistTimeStamp, cePfeMIBGroups=cePfeMIBGroups, cePfePerfConfigThld1MinEfficiency=cePfePerfConfigThld1MinEfficiency, cePfeHistType=cePfeHistType, cePfePerfConfigEntry=cePfePerfConfigEntry, cePfePerfCurrent1MinUtilization=cePfePerfCurrent1MinUtilization, cePfeMIBPerformanceCompliance=cePfeMIBPerformanceCompliance, cePfeMIBPerformanceGroup=cePfeMIBPerformanceGroup, PYSNMP_MODULE_ID=ciscoEntityPfeMib, cePfeHistTableLastIndex=cePfeHistTableLastIndex, cePfePerfCurrent5MinUtilization=cePfePerfCurrent5MinUtilization, cePfeMIBHistEventGroup=cePfeMIBHistEventGroup, cePfePerfConfigTable=cePfePerfConfigTable, cePfePerfTotalTable=cePfePerfTotalTable, cePfeMIBTotalGroup=cePfeMIBTotalGroup, cePfePerfCurrent5MinEfficiency=cePfePerfCurrent5MinEfficiency, cePfePerfCurrentEfficiency=cePfePerfCurrentEfficiency, cePfePerfConfigThldEfficiency=cePfePerfConfigThldEfficiency, cePfeHistThld=cePfeHistThld, cePfeMIBNotifications=cePfeMIBNotifications, cePfeHistEntPhysIndex=cePfeHistEntPhysIndex, cePfePerfTotalEfficiency=cePfePerfTotalEfficiency, cePfeMIBHistGroup=cePfeMIBHistGroup, HistEventType=HistEventType, cePfePerfIntervalNumber=cePfePerfIntervalNumber, cePfePerfConfigValidIntervals=cePfePerfConfigValidIntervals, cePfePerfConfigThld1MinUtilization=cePfePerfConfigThld1MinUtilization, cePfePerfTotalEntry=cePfePerfTotalEntry, cePfeMIBConformance=cePfeMIBConformance, TotalEfficiency=TotalEfficiency, cePfeHistRestartReason=cePfeHistRestartReason, cePfeHistThldEvent=cePfeHistThldEvent, cePfePerfConfigThldUtilization=cePfePerfConfigThldUtilization, cePfePerformance=cePfePerformance, ciscoEntityPfeMib=ciscoEntityPfeMib, cePfePerfConfigThld5MinEfficiency=cePfePerfConfigThld5MinEfficiency, TotalUtilization=TotalUtilization, cePfePerfIntervalTable=cePfePerfIntervalTable, cePfePerfTotalUtilization=cePfePerfTotalUtilization, cePfeHistNotifiesEnable=cePfeHistNotifiesEnable, cePfePerfCurrentUtilization=cePfePerfCurrentUtilization, cePfeHistTable=cePfeHistTable, cePfePerfConfigThld5MinUtilization=cePfePerfConfigThld5MinUtilization, cePfeHistIndex=cePfeHistIndex, cePfeHistValue=cePfeHistValue, cePfeMIBCurrentGroup=cePfeMIBCurrentGroup, cePfeHistEntry=cePfeHistEntry, IntervalEfficiency=IntervalEfficiency, cePfePerfIntervalEfficiency=cePfePerfIntervalEfficiency, cePfePerfCurrent1MinEfficiency=cePfePerfCurrent1MinEfficiency, cePfePerfConfigTimeElapsed=cePfePerfConfigTimeElapsed, cePfePerfCurrentEntry=cePfePerfCurrentEntry, cePfePerfIntervalEntry=cePfePerfIntervalEntry, cePfeHistRestartEvent=cePfeHistRestartEvent, EventType=EventType, cePfeMIBCompliances=cePfeMIBCompliances, cePfeHistTableSize=cePfeHistTableSize, cePfePerfCurrentTable=cePfePerfCurrentTable, cePfeMIBIntervalGroup=cePfeMIBIntervalGroup, cePfeMIBObjects=cePfeMIBObjects)
