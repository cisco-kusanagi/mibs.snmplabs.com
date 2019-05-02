#
# PySNMP MIB module ENTERASYS-LINK-FLAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-LINK-FLAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:03:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ifIndex, ifName = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifName")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, ModuleIdentity, Counter32, Gauge32, Bits, ObjectIdentity, iso, TimeTicks, Unsigned32, IpAddress, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "ModuleIdentity", "Counter32", "Gauge32", "Bits", "ObjectIdentity", "iso", "TimeTicks", "Unsigned32", "IpAddress", "MibIdentifier", "Counter64")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
etsysLinkFlapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52))
etsysLinkFlapMIB.setRevisions(('2009-10-16 12:53', '2004-08-20 14:47',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysLinkFlapMIB.setRevisionsDescriptions(('Clarified the DESCRIPTION clause for the etsysLinkFlapIntfClearStats object.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysLinkFlapMIB.setLastUpdated('200910161253Z')
if mibBuilder.loadTexts: etsysLinkFlapMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysLinkFlapMIB.setContactInfo('Postal: Enterasys Networks 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysLinkFlapMIB.setDescription('This is the MIB module for Enterasys Link Flap Detection, a mechanism to automatically limit the effect of frequent link state transitions on Enterasys devices.')
class LinkFlapIntfAction(TextualConvention, Bits):
    description = "The possible actions that the Link Flap feature can take when link flap activity exceeds the associated action limits. disableInterface(0) - Operationally disable the interface, ifOperStatus for the interface MUST go into the 'down' state, and MUST remain in that state until the associated etsysLinkFlapIntfStatus is set to operational, the Link Flap feature is disabled, or the device is reset. generateSyslogEntry(1) - Generate the respective device log entry. generateNotification(2) - Generate the respective SNMP notification. The 'generateNotification(2)' will always be performed if it is a selected action, is globally enabled, and does not exceed the global rate limit for such notifications. It MUST be generated in such a way that the information in the notification indicates the condition on the interface after any other indicated action has been taken."
    status = 'current'
    namedValues = NamedValues(("disableInterface", 0), ("generateSyslogEntry", 1), ("generateNotification", 2))

etsysLinkFlapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1))
etsysLinkFlapSystemBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 1))
etsysLinkFlapInterfaceBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2))
etsysLinkFlapNotificationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 0))
etsysLinkFlapSystemState = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysLinkFlapSystemState.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapSystemState.setDescription("The current state of the active part of the Link Flap feature. enabled (1) - All supported aspects of Link Flap are operational. disabled (2) - Link Flap is configurable but no actions are taken. All statistical information is still gathered and available. When this object is set to disabled the Link Flap feature MUST release its control on all interfaces. Any interfaces which the Link Flap feature had operationally held in the 'down' state MUST be allowed to attain their currently correct operational state. Maintaining the value of this object across agent reboots is REQUIRED.")
etsysLinkFlapSystemSupportedActions = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 1, 2), LinkFlapIntfAction().clone(namedValues=NamedValues(("disableInterface", 0), ("generateSyslogEntry", 1), ("generateNotification", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysLinkFlapSystemSupportedActions.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapSystemSupportedActions.setDescription("The supported actions that the Link Flap feature can take when link flap activity exceeds the associated threshold on this interface. disableInterface(0) - Capability to set the interface operational status to 'down'. generateSyslogEntry(1) - Capability to create syslog messages. generateNotification(2) - Capability to generate SNMP notifications. Please see the LinkFlapIntfAction textual convention defined in this MIB.")
etsysLinkFlapSystemLinkFlapMaximum = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysLinkFlapSystemLinkFlapMaximum.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapSystemLinkFlapMaximum.setDescription('The greatest number of linkdown events which can occur per ten second interval. This is an implementation-specific parameter which will determine the allowable values of etsysLinkFlapIntfCountThreshold and etsysLinkFlapIntfTimeInterval. Setting either one of these such that the ratio of etsysLinkFlapIntfCountThreshold to etsysLinkFlapIntfTimeInterval would become greater than etsysLinkFlapSystemLinkFlapMaximum will result in the set operation failing with an inconsistentValue error.')
etsysLinkFlapInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1), )
if mibBuilder.loadTexts: etsysLinkFlapInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapInterfaceTable.setDescription('A table that provides for the configuration, status, and statistics related to, the Link Flap feature on a per interface basis.')
etsysLinkFlapInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etsysLinkFlapInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapInterfaceEntry.setDescription('The configuration, status, and statistics related to, the Link Flap feature for an individual interface.')
etsysLinkFlapIntfEnabledStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysLinkFlapIntfEnabledStatus.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapIntfEnabledStatus.setDescription("The enable state of Link Flap on this interface. Transitioning from enabled(1) to disabled(2) will disable the active part of the Link Flap feature as defined for the etsysLinkFlapSystemState object on this interface. In this event the agent MUST: 1) Release its control on this interface. If the interface had been operationally held in the 'down' state, then the interface MUST be allowed to attain its currently correct operational state. 2) etsysLinkFlapIntfOperStatus MUST be set to operational(1). 3) The objects etsysLinkFlapIntfLinkdownCountCurrent etsysLinkFlapIntfLinkdownCountTotal etsysLinkFlapIntfCurrentElapsed MUST continue to accrue value as events occur. In transitioning from disabled(2) to enabled(1) the objects: etsysLinkFlapIntfLinkdownCountCurrent etsysLinkFlapIntfCurrentElapsed MUST be initialized at 0 (zero) for this interface. Maintaining the value of this object across agent reboots is REQUIRED.")
etsysLinkFlapIntfAction = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 2), LinkFlapIntfAction().clone(namedValues=NamedValues(("generateSyslogEntry", 1), ("generateNotification", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysLinkFlapIntfAction.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapIntfAction.setDescription("The configured actions that the Link Flap feature can take when link flap activity exceeds the associated threshold on this interface. disableInterface(0) - Interface operational status set to 'down'. generateSyslogEntry(1) - Descriptive syslog message generated generateNotification(2) - SNMP notification generated. Maintaining the value of this object across agent reboots is REQUIRED.")
etsysLinkFlapIntfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("operational", 1), ("disabled", 2))).clone('operational')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysLinkFlapIntfOperStatus.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapIntfOperStatus.setDescription('The current status of the interface with respect to Link Flap detection. A read of operational(1) indicates that the Link Flap feature has not taken any action to operationally limit this interface. A read of disabled(2) indicates that the Link Flap feature has taken action to operationally disable this interface due to excessive link state transitions. Setting this object to operational(1) when it is disabled(2) will cause Link Flap to release its control which is keeping this interface operationally disabled. Any other write of this object will have no effect. Maintaining the value of this object across agent reboots is NOT RECOMMENDED.')
etsysLinkFlapIntfClearStats = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 4), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysLinkFlapIntfClearStats.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapIntfClearStats.setDescription('When set to true(1) the following objects: etsysLinkFlapIntfLinkdownCountCurrent etsysLinkFlapIntfLinkdownCountTotal etsysLinkFlapIntfLinkFlapViolations in this row of the etsysLinkFlapInterfaceTable MUST be set to 0 (zero). Setting this object to false(2) will have no effect. When read this object will always return false(2). Maintaining the value of this object across agent reboots is NOT RECOMMENDED.')
etsysLinkFlapIntfCountThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 5), Unsigned32().clone(5)).setUnits('link state transitions').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysLinkFlapIntfCountThreshold.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapIntfCountThreshold.setDescription('The threshold count of link state transitions, which if exceeded within time limit etsysLinkFlapIntfTimeInterval, necessitates actions specified in LinkFlapIntfAction. Setting etsysLinkFlapIntfCountThreshold such that the ratio of etsysLinkFlapIntfCountThreshold to etsysLinkFlapIntfTimeInterval would become greater than etsysLinkFlapSystemLinkFlapMaximum will result in the set operation failing with an inconsistentValue error. Maintaining the value of this object across agent reboots is REQUIRED')
etsysLinkFlapIntfTimeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )).clone(10)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysLinkFlapIntfTimeInterval.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapIntfTimeInterval.setDescription('The time period during which link state transitions accrue toward the threshold count etsysLinkFlapIntfCountThreshold. Setting etsysLinkFlapIntfTimeInterval such that the ratio of etsysLinkFlapIntfCountThreshold to etsysLinkFlapIntfTimeInterval would become greater than etsysLinkFlapSystemLinkFlapMaximum will result in the set operation failing with an inconsistentValue error. Note that one special value, 0 (zero) of the etsysLinkFlapIntfTimeInterval is used to specify that etsysLinkFlapIntfTimeInterval is unbounded. Maintaining the value of this object across agent reboots is REQUIRED')
etsysLinkFlapIntfDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysLinkFlapIntfDownTime.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapIntfDownTime.setDescription("The time period during which the violating interface operational status may be held to 'down' by the LinkFlap functionality. Note that one special value, 0 (zero) of the etsysLinkFlapIntfDownTime is used to specify that etsysLinkFlapIntfDownTime is unbounded. Maintaining the value of this object across agent reboots is REQUIRED")
etsysLinkFlapIntfLinkdownCountCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 8), Gauge32()).setUnits('link state transitions').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysLinkFlapIntfLinkdownCountCurrent.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapIntfLinkdownCountCurrent.setDescription('The current number of link state transitions accrued during the current monitor interval. This information is always available and current. Maintaining the value of this object across agent reboots is NOT RECOMMENDED.')
etsysLinkFlapIntfLinkdownCountTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 9), Gauge32()).setUnits('link state transitions').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysLinkFlapIntfLinkdownCountTotal.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapIntfLinkdownCountTotal.setDescription('The total number of link state transitions accrued on this interface. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. This information is always available and current. Maintaining the value of this object across agent reboots is NOT RECOMMENDED.')
etsysLinkFlapIntfCurrentElapsed = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 10), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysLinkFlapIntfCurrentElapsed.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapIntfCurrentElapsed.setDescription('The current number of completed system ticks accrued on this interface during the current monitor interval. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. This information is always available and current. Maintaining the value of this object across agent reboots is NOT RECOMMENDED.')
etsysLinkFlapIntfLinkFlapViolations = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 2, 1, 1, 11), Gauge32()).setUnits('violations').setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysLinkFlapIntfLinkFlapViolations.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapIntfLinkFlapViolations.setDescription('The total number of link flap violations accrued on this interface. Discontinuities in the value of this counter can occur at re-initialization of the management system, and at other times as indicated by the value of ifCounterDiscontinuityTime. This information is always available and current. Maintaining the value of this object across agent reboots is NOT RECOMMENDED.')
etsysLinkFlapViolation = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 1, 0, 1)).setObjects(("IF-MIB", "ifName"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfOperStatus"))
if mibBuilder.loadTexts: etsysLinkFlapViolation.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapViolation.setDescription('If the Link Flap feature is globally enabled and specifically enabled for this interface, then this trap is sent when a link state transition is detected which accrues to a sum of transitions exceeding the value etsysLinkFlapIntfCountThreshold over the time period etsysLinkFlapIntfTimeInterval.')
etsysLinkFlapConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2))
etsysLinkFlapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2, 1))
etsysLinkFlapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2, 2))
etsysLinkFlapSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2, 1, 1)).setObjects(("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapSystemState"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapSystemSupportedActions"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapSystemLinkFlapMaximum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysLinkFlapSystemGroup = etsysLinkFlapSystemGroup.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapSystemGroup.setDescription('A collection of objects providing global configuration and status for the Link Flap feature.')
etsysLinkFlapInterfaceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2, 1, 2)).setObjects(("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfEnabledStatus"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfAction"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfOperStatus"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfClearStats"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfCountThreshold"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfTimeInterval"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfDownTime"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfLinkdownCountCurrent"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfLinkdownCountTotal"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfCurrentElapsed"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapIntfLinkFlapViolations"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysLinkFlapInterfaceGroup = etsysLinkFlapInterfaceGroup.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapInterfaceGroup.setDescription('A collection of objects providing interface based configuration, status, and statistics of the Link Flap feature.')
etsysLinkFlapNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2, 1, 3)).setObjects(("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapViolation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysLinkFlapNotificationGroup = etsysLinkFlapNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapNotificationGroup.setDescription('A collection of notifications for violation of link state transition rates on individual interfaces.')
etsysLinkFlapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 52, 2, 2, 1)).setObjects(("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapSystemGroup"), ("ENTERASYS-LINK-FLAP-MIB", "etsysLinkFlapInterfaceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysLinkFlapCompliance = etsysLinkFlapCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysLinkFlapCompliance.setDescription('The compliance statement for devices that support Link Flap.')
mibBuilder.exportSymbols("ENTERASYS-LINK-FLAP-MIB", etsysLinkFlapViolation=etsysLinkFlapViolation, etsysLinkFlapSystemGroup=etsysLinkFlapSystemGroup, etsysLinkFlapSystemLinkFlapMaximum=etsysLinkFlapSystemLinkFlapMaximum, etsysLinkFlapIntfLinkFlapViolations=etsysLinkFlapIntfLinkFlapViolations, PYSNMP_MODULE_ID=etsysLinkFlapMIB, etsysLinkFlapSystemState=etsysLinkFlapSystemState, etsysLinkFlapIntfClearStats=etsysLinkFlapIntfClearStats, etsysLinkFlapInterfaceBranch=etsysLinkFlapInterfaceBranch, etsysLinkFlapNotificationBranch=etsysLinkFlapNotificationBranch, etsysLinkFlapInterfaceTable=etsysLinkFlapInterfaceTable, etsysLinkFlapIntfEnabledStatus=etsysLinkFlapIntfEnabledStatus, etsysLinkFlapIntfCurrentElapsed=etsysLinkFlapIntfCurrentElapsed, etsysLinkFlapGroups=etsysLinkFlapGroups, etsysLinkFlapSystemBranch=etsysLinkFlapSystemBranch, etsysLinkFlapObjects=etsysLinkFlapObjects, etsysLinkFlapConformance=etsysLinkFlapConformance, etsysLinkFlapNotificationGroup=etsysLinkFlapNotificationGroup, etsysLinkFlapSystemSupportedActions=etsysLinkFlapSystemSupportedActions, etsysLinkFlapIntfCountThreshold=etsysLinkFlapIntfCountThreshold, etsysLinkFlapMIB=etsysLinkFlapMIB, etsysLinkFlapIntfTimeInterval=etsysLinkFlapIntfTimeInterval, etsysLinkFlapIntfDownTime=etsysLinkFlapIntfDownTime, etsysLinkFlapInterfaceEntry=etsysLinkFlapInterfaceEntry, etsysLinkFlapCompliance=etsysLinkFlapCompliance, etsysLinkFlapIntfAction=etsysLinkFlapIntfAction, etsysLinkFlapIntfLinkdownCountTotal=etsysLinkFlapIntfLinkdownCountTotal, etsysLinkFlapCompliances=etsysLinkFlapCompliances, etsysLinkFlapIntfOperStatus=etsysLinkFlapIntfOperStatus, etsysLinkFlapInterfaceGroup=etsysLinkFlapInterfaceGroup, LinkFlapIntfAction=LinkFlapIntfAction, etsysLinkFlapIntfLinkdownCountCurrent=etsysLinkFlapIntfLinkdownCountCurrent)
