#
# PySNMP MIB module TIMETRA-IPSEC-STATIC-SA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIMETRA-IPSEC-STATIC-SA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:10:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, Counter32, NotificationType, Unsigned32, TimeTicks, ObjectIdentity, ModuleIdentity, Counter64, IpAddress, MibIdentifier, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "NotificationType", "Unsigned32", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Counter64", "IpAddress", "MibIdentifier", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, TimeStamp, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString", "RowStatus")
tmnxSRObjs, timetraSRMIBModules, tmnxSRConfs = mibBuilder.importSymbols("TIMETRA-GLOBAL-MIB", "tmnxSRObjs", "timetraSRMIBModules", "tmnxSRConfs")
TNamedItem, TNamedItemOrEmpty = mibBuilder.importSymbols("TIMETRA-TC-MIB", "TNamedItem", "TNamedItemOrEmpty")
timetraIPsecStaticSAMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 73))
timetraIPsecStaticSAMIBModule.setRevisions(('1909-12-14 00:00',))
if mibBuilder.loadTexts: timetraIPsecStaticSAMIBModule.setLastUpdated('0912140000Z')
if mibBuilder.loadTexts: timetraIPsecStaticSAMIBModule.setOrganization('Alcatel-Lucent')
tmnxIPsecStaticSAObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73))
tmnxIPsecStaticSAConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73))
class TmnxAuthAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("null", 1), ("md5", 2), ("sha1", 3))

class TmnxIPsecDirection2(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inbound", 1), ("outbound", 2), ("bidirectional", 3))

class TmnxIPsecProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ah", 1), ("esp", 2))

tmnxIPsecStaticSATableLastChange = MibScalar((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxIPsecStaticSATableLastChange.setStatus('current')
tmnxIPsecStaticSATable = MibTable((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2), )
if mibBuilder.loadTexts: tmnxIPsecStaticSATable.setStatus('current')
tmnxIPsecStaticSAEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1), ).setIndexNames((1, "TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAName"))
if mibBuilder.loadTexts: tmnxIPsecStaticSAEntry.setStatus('current')
tmnxIPsecStaticSAName = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 1), TNamedItem())
if mibBuilder.loadTexts: tmnxIPsecStaticSAName.setStatus('current')
tmnxIPsecStaticSARowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSARowStatus.setStatus('current')
tmnxIPsecStaticSALastChanged = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmnxIPsecStaticSALastChanged.setStatus('current')
tmnxIPsecStaticSADirection = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 4), TmnxIPsecDirection2().clone('bidirectional')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSADirection.setStatus('current')
tmnxIPsecStaticSAProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 5), TmnxIPsecProtocol().clone('esp')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSAProtocol.setStatus('current')
tmnxIPsecStaticSAAuthAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 6), TmnxAuthAlgorithm().clone('sha1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSAAuthAlgorithm.setStatus('current')
tmnxIPsecStaticSAAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSAAuthKey.setStatus('current')
tmnxIPsecStaticSASpi = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(256, 16383), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSASpi.setStatus('current')
tmnxIPsecStaticSADescription = MibTableColumn((1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 73, 2, 1, 9), TNamedItemOrEmpty()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: tmnxIPsecStaticSADescription.setStatus('current')
tmnxIPsecStaticSACompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 1))
tmnxIPsecStaticSAGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 2))
tmnxIPsecStaticSAV8v0Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 1, 1)).setObjects(("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxIPsecStaticSAV8v0Compliance = tmnxIPsecStaticSAV8v0Compliance.setStatus('current')
tmnxIPsecStaticSAGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 73, 2, 1)).setObjects(("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSATableLastChange"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSARowStatus"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSALastChanged"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSADirection"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAProtocol"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAAuthAlgorithm"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSAAuthKey"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSASpi"), ("TIMETRA-IPSEC-STATIC-SA-MIB", "tmnxIPsecStaticSADescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tmnxIPsecStaticSAGroup = tmnxIPsecStaticSAGroup.setStatus('current')
mibBuilder.exportSymbols("TIMETRA-IPSEC-STATIC-SA-MIB", tmnxIPsecStaticSALastChanged=tmnxIPsecStaticSALastChanged, tmnxIPsecStaticSADescription=tmnxIPsecStaticSADescription, TmnxAuthAlgorithm=TmnxAuthAlgorithm, TmnxIPsecProtocol=TmnxIPsecProtocol, timetraIPsecStaticSAMIBModule=timetraIPsecStaticSAMIBModule, tmnxIPsecStaticSATableLastChange=tmnxIPsecStaticSATableLastChange, tmnxIPsecStaticSAGroup=tmnxIPsecStaticSAGroup, tmnxIPsecStaticSADirection=tmnxIPsecStaticSADirection, tmnxIPsecStaticSAProtocol=tmnxIPsecStaticSAProtocol, tmnxIPsecStaticSAConformance=tmnxIPsecStaticSAConformance, tmnxIPsecStaticSAEntry=tmnxIPsecStaticSAEntry, tmnxIPsecStaticSAV8v0Compliance=tmnxIPsecStaticSAV8v0Compliance, PYSNMP_MODULE_ID=timetraIPsecStaticSAMIBModule, tmnxIPsecStaticSAGroups=tmnxIPsecStaticSAGroups, tmnxIPsecStaticSASpi=tmnxIPsecStaticSASpi, tmnxIPsecStaticSAAuthKey=tmnxIPsecStaticSAAuthKey, tmnxIPsecStaticSATable=tmnxIPsecStaticSATable, tmnxIPsecStaticSARowStatus=tmnxIPsecStaticSARowStatus, tmnxIPsecStaticSAName=tmnxIPsecStaticSAName, tmnxIPsecStaticSACompliances=tmnxIPsecStaticSACompliances, tmnxIPsecStaticSAAuthAlgorithm=tmnxIPsecStaticSAAuthAlgorithm, tmnxIPsecStaticSAObjects=tmnxIPsecStaticSAObjects, TmnxIPsecDirection2=TmnxIPsecDirection2)
