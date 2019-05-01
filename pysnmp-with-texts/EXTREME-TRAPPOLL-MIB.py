#
# PySNMP MIB module EXTREME-TRAPPOLL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:07:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
trapDestIndex, = mibBuilder.importSymbols("RMON2-MIB", "trapDestIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, Integer32, Gauge32, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ModuleIdentity, ObjectIdentity, TimeTicks, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Integer32", "Gauge32", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "Bits", "Unsigned32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
extremeTrapPoll = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 6))
if mibBuilder.loadTexts: extremeTrapPoll.setLastUpdated('9801090000Z')
if mibBuilder.loadTexts: extremeTrapPoll.setOrganization('Extreme Networks, Inc.')
if mibBuilder.loadTexts: extremeTrapPoll.setContactInfo('www.extremenetworks.com')
if mibBuilder.loadTexts: extremeTrapPoll.setDescription('Extreme SmartTraps trap-based-polling objects')
extremeSmartTrapRulesTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1), )
if mibBuilder.loadTexts: extremeSmartTrapRulesTable.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapRulesTable.setDescription('A table of rules that are used to generate extremeSmartTraps.')
extremeSmartTrapRulesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1), ).setIndexNames((0, "EXTREME-TRAPPOLL-MIB", "extremeSmartTrapRulesIndex"))
if mibBuilder.loadTexts: extremeSmartTrapRulesEntry.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapRulesEntry.setDescription('Each row in the table represents a rule.')
extremeSmartTrapRulesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapRulesIndex.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapRulesIndex.setDescription('An index into the extremeSmartTraps rules table. ')
extremeSmartTrapRulesRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeSmartTrapRulesRowStatus.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapRulesRowStatus.setDescription('Indicates the status of row. ')
extremeSmartTrapRulesDesiredOID = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 3), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeSmartTrapRulesDesiredOID.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapRulesDesiredOID.setDescription('The OID for which the rule is desired. When the OID specified by this object undergoes an operation specified by extremeSmartTrapRulesOperation, then an entry in the extremeSmartTrapInstanceTable is created.')
extremeSmartTrapRulesSupportedOID = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapRulesSupportedOID.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapRulesSupportedOID.setDescription('The OID for which this entry is created. This is based on the granularity supported by the agent corresponding to the extremeSmartTrapRulesDesiredOID that the management station desires. This object has a value that is a prefix of, or is equal to the value of ExtremeSmartTrapRulesDesiredOID. The agent specifes this value before setting the extremeSmartTrapRulesRowStatus to active.')
extremeSmartTrapRulesOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("add", 1), ("delete", 2), ("modify", 3), ("any", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeSmartTrapRulesOperation.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapRulesOperation.setDescription('The write operations on extremeSmartTrapRulesDesiredOID for which extremeSmartTrapsInstanceEntry should be created.')
extremeSmartTrapRulesTrapDestIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: extremeSmartTrapRulesTrapDestIndex.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapRulesTrapDestIndex.setDescription("A pointer to a row in RMON2's trapDestTable that was created by the management station that defined this rule. Any extremeSmartTraps generated by this agent due to this rule will be sent to the trapDestCommunity/ trapDestAddress and will include trapDestOwner specified by this trapDestTable entry. This also allows a manager to identify if the rule was defined by itself, or by another (possibly older) instance of the management server process. The manager should initiate a poll only for traps received which indicate its own rules. Subprocesses within a single manager might also uniquely create their own entries within trapDestTable using different trapDestOwner strings: when a trap is received, the manager can authenticate if the trap was generated due to one of its rules and route the notification to the appropriate subprocess.")
extremeSmartTrapInstanceTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2), )
if mibBuilder.loadTexts: extremeSmartTrapInstanceTable.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapInstanceTable.setDescription('A table representing containing information about which variables have changed according to the rules defined in extremeSmartTrapRulesTable.')
extremeSmartTrapInstanceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1), ).setIndexNames((0, "RMON2-MIB", "trapDestIndex"), (0, "EXTREME-TRAPPOLL-MIB", "extremeSmartTrapInstanceSubindex"))
if mibBuilder.loadTexts: extremeSmartTrapInstanceEntry.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapInstanceEntry.setDescription('An entry corresponding to a change in value of one of the OIDs defined in extremeSmartTrapRulesTable. Entries are indexed by a pointer to the relevant row in RMON2 trapDestTable that a manager created in order to receive trap notifications of these events. Entries are created in this table whenever the value of one of the OIDs defined by extremeSmartTrapRulesSupportedOID changes. Entries are deleted when a get or get-next operation is performed on that entry. A get operation for a non-existent entry returns a noSuchInstance error.')
extremeSmartTrapInstanceSubindex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapInstanceSubindex.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapInstanceSubindex.setDescription('An additional index into the table of extremeSmartTrap instance data. Each row which has the same OID for the same management station (i.e. same cookie) is assigned a unique value by the agent in order to differentiate between multiple instances.')
extremeSmartTrapInstanceRule = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapInstanceRule.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapInstanceRule.setDescription('The index of the rule from the extremeSmartTrapRulesTable for which this entry was created.')
extremeSmartTrapInstanceChangedOid = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapInstanceChangedOid.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapInstanceChangedOid.setDescription('The OID value that has changed.')
extremeSmartTrapInstanceActualOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("add", 1), ("delete", 2), ("modify", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapInstanceActualOperation.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapInstanceActualOperation.setDescription('The operation that was recently performed on this extremeSmartTrapInstanceChangedOid.')
extremeSmartTrapInstanceChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 6, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeSmartTrapInstanceChangeTime.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapInstanceChangeTime.setDescription('The sysUpTime when this entry was created.')
extremeSmartTrapFlushInstanceTableIndex = MibScalar((1, 3, 6, 1, 4, 1, 1916, 1, 6, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extremeSmartTrapFlushInstanceTableIndex.setStatus('current')
if mibBuilder.loadTexts: extremeSmartTrapFlushInstanceTableIndex.setDescription('When this object is set, the agent will delete all rows from the extremeSmartTrapInstanceTable which meet the following rules: 1. The InstanceTableIndex is equal to the value obtained by taking the two most significant bytes of this integer and right-shifting it by two bytes as an unsigned int. 2. The InstanceTableSubIndex is less than or equal to the value obtained by masking this object value with 0x0000FFFF. If the value obtained is zero, then all rows with the specified InstanceTableIndex should be deleted.')
mibBuilder.exportSymbols("EXTREME-TRAPPOLL-MIB", extremeSmartTrapInstanceEntry=extremeSmartTrapInstanceEntry, extremeSmartTrapInstanceSubindex=extremeSmartTrapInstanceSubindex, extremeSmartTrapFlushInstanceTableIndex=extremeSmartTrapFlushInstanceTableIndex, extremeTrapPoll=extremeTrapPoll, extremeSmartTrapInstanceChangeTime=extremeSmartTrapInstanceChangeTime, extremeSmartTrapRulesOperation=extremeSmartTrapRulesOperation, extremeSmartTrapInstanceChangedOid=extremeSmartTrapInstanceChangedOid, extremeSmartTrapInstanceActualOperation=extremeSmartTrapInstanceActualOperation, extremeSmartTrapRulesEntry=extremeSmartTrapRulesEntry, extremeSmartTrapRulesSupportedOID=extremeSmartTrapRulesSupportedOID, PYSNMP_MODULE_ID=extremeTrapPoll, extremeSmartTrapRulesDesiredOID=extremeSmartTrapRulesDesiredOID, extremeSmartTrapRulesTrapDestIndex=extremeSmartTrapRulesTrapDestIndex, extremeSmartTrapInstanceRule=extremeSmartTrapInstanceRule, extremeSmartTrapRulesTable=extremeSmartTrapRulesTable, extremeSmartTrapInstanceTable=extremeSmartTrapInstanceTable, extremeSmartTrapRulesRowStatus=extremeSmartTrapRulesRowStatus, extremeSmartTrapRulesIndex=extremeSmartTrapRulesIndex)