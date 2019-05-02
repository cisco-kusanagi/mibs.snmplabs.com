#
# PySNMP MIB module Wellfleet-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-IF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:40:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, NotificationType, ModuleIdentity, Unsigned32, ObjectIdentity, Gauge32, Integer32, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "NotificationType", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "Gauge32", "Integer32", "MibIdentifier", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfIfGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfIfGroup")
wfIf = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 1))
wfIfNumber = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfNumber.setDescription('Total number of possible active interfaces')
wfIfRegistrationMode = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("wellfleetstandard", 1), ("dialcircuitunique", 2))).clone('wellfleetstandard')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIfRegistrationMode.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfRegistrationMode.setDescription('Method of instance specification Wellfleet Standard defines ifEntry instances by their router internal circuit number. Dial Circuit Unique is similar, but adds a bias to dial circuit instances so that a dial backup interface will have an ifEntry instance distinct from the primary interface. Neither selection is RFC 1213 compliant.')
wfIfTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2), )
if mibBuilder.loadTexts: wfIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfTable.setDescription('A table containing active interfaces')
wfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1), ).setIndexNames((0, "Wellfleet-IF-MIB", "wfIfIndex"))
if mibBuilder.loadTexts: wfIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfEntry.setDescription('A particular interface')
wfIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfIndex.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfDescr.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfDescr.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfType.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfType.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfMtu.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfMtu.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfSpeed.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfPhysAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfPhysAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfPhysAddress.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfAdminStatus.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfOperStatus.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfLastChange.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfLastChange.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfInOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfInOctets.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfInUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfInUcastPkts.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfInUcastPkts.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfInNUCastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfInNUCastPkts.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfInNUCastPkts.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfInDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfInDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfInDiscards.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfInErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfInErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfInErrors.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfInUnknownProtos = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfInUnknownProtos.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfInUnknownProtos.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfOutOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfOutOctets.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfOutUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfOutUcastPkts.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfOutUcastPkts.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfOutNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfOutNUcastPkts.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfOutNUcastPkts.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfOutDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfOutDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfOutDiscards.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfOutErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfOutErrors.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfOutErrors.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfOutQLen = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 21), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfOutQLen.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfOutQLen.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 2, 1, 22), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfSpecific.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfSpecific.setDescription("Corresponds to same attribute of MIB-II's ifTable")
wfIfCfgTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 3), )
if mibBuilder.loadTexts: wfIfCfgTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfCfgTable.setDescription('A table used to configure the rfc-1573 subagent')
wfIfCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 3, 1), ).setIndexNames((0, "Wellfleet-IF-MIB", "wfIfCfgIndex"))
if mibBuilder.loadTexts: wfIfCfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfCfgEntry.setDescription('Single row used to configure rfc-1573 subagent for entire box')
wfIfCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfIfCfgIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfCfgIndex.setDescription('Unique index for configuration table')
wfIfCfgConformanceTesting = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIfCfgConformanceTesting.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfCfgConformanceTesting.setDescription("When enabled, this informs the system to ensure that all objects supported for rfc1573 in the box follow rfc1573's conformance guidelines. Objects that do not follow the guidelines will not be accessible.")
wfIfCfgSparseTableAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 3, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("allowed", 1), ("zerofill", 2))).clone('allowed')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfIfCfgSparseTableAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: wfIfCfgSparseTableAdminStatus.setDescription('When enabled, this informs the system of the method to use when dealing with sparse tables (i.e rows that contain columns that are not all supported ). allowed - the agent must do nothing when sparse tables are encountered. zerofill - the agent must return a zero value for unsupported columns')
mibBuilder.exportSymbols("Wellfleet-IF-MIB", wfIfRegistrationMode=wfIfRegistrationMode, wfIfInUcastPkts=wfIfInUcastPkts, wfIfCfgIndex=wfIfCfgIndex, wfIfCfgTable=wfIfCfgTable, wfIfTable=wfIfTable, wfIfCfgConformanceTesting=wfIfCfgConformanceTesting, wfIfSpeed=wfIfSpeed, wfIfOutOctets=wfIfOutOctets, wfIfMtu=wfIfMtu, wfIfNumber=wfIfNumber, wfIfInErrors=wfIfInErrors, wfIfCfgEntry=wfIfCfgEntry, wfIfAdminStatus=wfIfAdminStatus, wfIfInNUCastPkts=wfIfInNUCastPkts, wfIfCfgSparseTableAdminStatus=wfIfCfgSparseTableAdminStatus, wfIfSpecific=wfIfSpecific, wfIfInOctets=wfIfInOctets, wfIfOperStatus=wfIfOperStatus, wfIfOutNUcastPkts=wfIfOutNUcastPkts, wfIfOutDiscards=wfIfOutDiscards, wfIfInDiscards=wfIfInDiscards, wfIfPhysAddress=wfIfPhysAddress, wfIfOutUcastPkts=wfIfOutUcastPkts, wfIf=wfIf, wfIfOutQLen=wfIfOutQLen, wfIfType=wfIfType, wfIfLastChange=wfIfLastChange, wfIfEntry=wfIfEntry, wfIfIndex=wfIfIndex, wfIfOutErrors=wfIfOutErrors, wfIfInUnknownProtos=wfIfInUnknownProtos, wfIfDescr=wfIfDescr)
