#
# PySNMP MIB module CTRON-RATE-POLICING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-RATE-POLICING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:30:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
ctPriorityExt, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPriorityExt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, Counter32, Bits, ObjectIdentity, iso, NotificationType, IpAddress, Gauge32, TimeTicks, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "Counter32", "Bits", "ObjectIdentity", "iso", "NotificationType", "IpAddress", "Gauge32", "TimeTicks", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctRatePolicing = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7))
ctRatePolicing.setRevisions(('2003-04-10 15:18', '2003-03-11 15:53', '2000-11-28 15:51', '1999-06-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ctRatePolicing.setRevisionsDescriptions(('Added display hint to CtPriList.', 'Changed the definitions of the CtRatePolActionList and CtRatePolDirectionList textual conventions. The syntax was also changed from Integer32 to INTEGER with enumeration values that map to the prior bit positions.', 'Changed the CONTACT-INFO portion of the MODULE-IDENTITY to reflect the company name change to Enterasys Networks. Added ranges to the ctRatePolicingThreshHoldMin and ctRatePolicingThreshHold leaves.', 'The initial version of this MIB module',))
if mibBuilder.loadTexts: ctRatePolicing.setLastUpdated('200304101518Z')
if mibBuilder.loadTexts: ctRatePolicing.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: ctRatePolicing.setContactInfo('Postal: Enterasys Networks 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: ctRatePolicing.setDescription('The Enterasys Rate Policing MIB module allows the user to set maximum ingress rates on a per port, per priority basis.')
ctRatePolicingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1))
class CtPriList(TextualConvention, Integer32):
    description = "The least significant octet within this integer specifies a set of eight priorities. Within this octet, the most significant bit represents the highest priority(7), and the least significant bit represents the lowest priority(0). Thus, each priority is represented by a single bit within the value of this object. If that bit has a value of '1' then that priority is included in the set of priorities; the priority is not included if its bit has a value of '0'."
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class CtRatePolActionList(TextualConvention, Integer32):
    description = 'This value represents a list of rate policing actions.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("dropPacket", 1), ("flowCtrlPacketAndDrop", 2), ("dropPacketOrFlowCtrlAndDrop", 3))

class CtRatePolDirectionList(TextualConvention, Integer32):
    description = 'This value represents the possible traffic flow directions.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("none", 0), ("inbound", 1), ("outbound", 2), ("inboundAndOutbound", 3))

ctRatePolicingAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctRatePolicingAdminStatus.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingAdminStatus.setDescription('Allows the rate policing feature to be globally enabled/disabled. A value of disable(2), functionally supersedes the ctRatePolicingRuleStatus of individual entries in the ctRatePolicingConfigTable, but does not change their actual values.')
ctRatePolicingConfigLastChange = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctRatePolicingConfigLastChange.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingConfigLastChange.setDescription('The value of sysUpTime the last time anything in the ctRatePolicingConfigTable changed.')
ctRatePolicingConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3), )
if mibBuilder.loadTexts: ctRatePolicingConfigTable.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingConfigTable.setDescription('This table allows configuration of rate policing rules on this device. Their are a limited number of resources available for rate policing, and this directly limits the number of rate policing rules that may be configured on each port. As a result this table does not support dynamic row creation, rather, all possible rows exist in either an active or disabled state. A manager application should not, however, infer that this configuration is necessarily fixed during the lifetime of the managed entity. The allocation of resources could theoretically be shifted. For example port 20 could have 3 resources and at some point suddenly have 4 or 2. Any such change would of course cause the value of ctRatePolicingConfigLastChange to change. At this time their is no defined mechanism to move these resources and there very likely never will be. This is merely a warning that manager applications should not count on this.')
ctRatePolicingConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "CTRON-RATE-POLICING-MIB", "ctRatePolicingResourceIndex"))
if mibBuilder.loadTexts: ctRatePolicingConfigEntry.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingConfigEntry.setDescription('Describes a particular entry of ctRatePolicingConfigTable.')
ctRatePolicingResourceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ctRatePolicingResourceIndex.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingResourceIndex.setDescription('This specifies a unique resource available for configuring a rate policing rule on this port. Each port has a limited number of resources available for rate policing. This index simply provides a mechanism for uniquely addressing each of these resources.')
ctRatePolicingActionsAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 2), CtRatePolActionList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctRatePolicingActionsAllowed.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingActionsAllowed.setDescription('This specifies the valid policing actions that may be taken for this port upon exceeding the threshold specified in ctRatePolicingThreshHold.')
ctRatePolicingAction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 3), CtRatePolActionList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctRatePolicingAction.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingAction.setDescription('This is the action to be taken if the rate limit is exceeded. This value must be a valid action as specified by the corresponding ctRatePolicingActionsAllowed object. Also, no more than one action may be specified. Attempts to set this value outside of the aforementioned guidelines will fail.')
ctRatePolicingThreshHoldMin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('kilobytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ctRatePolicingThreshHoldMin.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingThreshHoldMin.setDescription('The minimum rate limit value for this entry in kB per second.')
ctRatePolicingThreshHold = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('kilobytes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctRatePolicingThreshHold.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingThreshHold.setDescription('The rate limit value for this entry in kB per second. If the rate is exceeded the defined action in ctRatePolicingAction will be enforced. This value may not be set below the minimum rate specified in ctRatePolicingThreshHoldMin.')
ctRatePolicingPriorityList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 6), CtPriList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctRatePolicingPriorityList.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingPriorityList.setDescription('This specifies the list of priorities to which this rule applies.')
ctRatePolicingRuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctRatePolicingRuleStatus.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingRuleStatus.setDescription('This object provides both control and status for the associated conceptual row in the table. The value of active(1) indicates that device is actively applying the rate policing rule defined by the other leaves in this row. All other read-write leaves in this row have an effective value of read-only while the row is in the active state. The value of disabled(2) indicates that this row is essentially an available resource which MAY be configured and activated.')
ctRatePolicingActionsTaken = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctRatePolicingActionsTaken.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingActionsTaken.setDescription('This object counts the number of times the ctRatePolicingAction has been enforced for this particular entry.')
ctRatePolicingDirectionsAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 9), CtRatePolDirectionList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctRatePolicingDirectionsAllowed.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingDirectionsAllowed.setDescription('This specifies the valid policing directions that may be taken for this port.')
ctRatePolicingDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 1, 3, 1, 10), CtRatePolDirectionList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctRatePolicingDirection.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingDirection.setDescription('This specifies the direction of the traffic flow that will be limited.')
ctRatePolicingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2))
ctRatePolicingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2, 1))
ctRatePolicingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2, 2))
ctRatePolicingConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2, 1, 1)).setObjects(("CTRON-RATE-POLICING-MIB", "ctRatePolicingAdminStatus"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingConfigLastChange"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingActionsAllowed"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingAction"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingThreshHold"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingPriorityList"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingRuleStatus"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingActionsTaken"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingDirectionsAllowed"), ("CTRON-RATE-POLICING-MIB", "ctRatePolicingDirection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctRatePolicingConfigGroup = ctRatePolicingConfigGroup.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingConfigGroup.setDescription('A collection of objects providing device level control and status information for rate policing.')
ctRatePolicingCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 7, 2, 2, 1)).setObjects(("CTRON-RATE-POLICING-MIB", "ctRatePolicingConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctRatePolicingCompliance = ctRatePolicingCompliance.setStatus('current')
if mibBuilder.loadTexts: ctRatePolicingCompliance.setDescription('The compliance statement for devices that support rate policing.')
mibBuilder.exportSymbols("CTRON-RATE-POLICING-MIB", ctRatePolicingObjects=ctRatePolicingObjects, CtRatePolActionList=CtRatePolActionList, ctRatePolicingConfigEntry=ctRatePolicingConfigEntry, ctRatePolicingResourceIndex=ctRatePolicingResourceIndex, ctRatePolicingActionsAllowed=ctRatePolicingActionsAllowed, ctRatePolicingConformance=ctRatePolicingConformance, ctRatePolicingConfigTable=ctRatePolicingConfigTable, ctRatePolicingConfigLastChange=ctRatePolicingConfigLastChange, ctRatePolicingDirectionsAllowed=ctRatePolicingDirectionsAllowed, ctRatePolicingCompliance=ctRatePolicingCompliance, ctRatePolicingPriorityList=ctRatePolicingPriorityList, ctRatePolicingRuleStatus=ctRatePolicingRuleStatus, ctRatePolicingCompliances=ctRatePolicingCompliances, CtPriList=CtPriList, PYSNMP_MODULE_ID=ctRatePolicing, ctRatePolicingConfigGroup=ctRatePolicingConfigGroup, ctRatePolicingDirection=ctRatePolicingDirection, CtRatePolDirectionList=CtRatePolDirectionList, ctRatePolicingGroups=ctRatePolicingGroups, ctRatePolicing=ctRatePolicing, ctRatePolicingThreshHold=ctRatePolicingThreshHold, ctRatePolicingActionsTaken=ctRatePolicingActionsTaken, ctRatePolicingThreshHoldMin=ctRatePolicingThreshHoldMin, ctRatePolicingAdminStatus=ctRatePolicingAdminStatus, ctRatePolicingAction=ctRatePolicingAction)
