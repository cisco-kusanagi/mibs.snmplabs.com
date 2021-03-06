#
# PySNMP MIB module HH3C-VSI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-VSI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:15:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, ObjectIdentity, Unsigned32, Bits, IpAddress, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "IpAddress", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity", "TimeTicks", "Integer32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hh3cVsi = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 105))
hh3cVsi.setRevisions(('2009-08-08 10:00',))
if mibBuilder.loadTexts: hh3cVsi.setLastUpdated('200908081000Z')
if mibBuilder.loadTexts: hh3cVsi.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cVsiObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1))
hh3cVsiScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 1))
hh3cVsiNextAvailableVsiIndex = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cVsiNextAvailableVsiIndex.setStatus('current')
hh3cVsiTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2), )
if mibBuilder.loadTexts: hh3cVsiTable.setStatus('current')
hh3cVsiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1), ).setIndexNames((0, "HH3C-VSI-MIB", "hh3cVsiIndex"))
if mibBuilder.loadTexts: hh3cVsiEntry.setStatus('current')
hh3cVsiIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hh3cVsiIndex.setStatus('current')
hh3cVsiName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVsiName.setStatus('current')
hh3cVsiMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("martini", 1), ("minm", 2), ("martiniAndMinm", 3), ("kompella", 4), ("kompellaAndMinm", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVsiMode.setStatus('current')
hh3cMinmIsid = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cMinmIsid.setStatus('current')
hh3cVsiId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVsiId.setStatus('current')
hh3cVsiTransMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlan", 1), ("ethernet", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVsiTransMode.setStatus('current')
hh3cVsiEnableHubSpoke = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVsiEnableHubSpoke.setStatus('current')
hh3cVsiAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("adminUp", 1), ("adminDown", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVsiAdminState.setStatus('current')
hh3cVsiRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVsiRowStatus.setStatus('current')
hh3cVsiXconnectTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3), )
if mibBuilder.loadTexts: hh3cVsiXconnectTable.setStatus('current')
hh3cVsiXconnectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1), ).setIndexNames((0, "HH3C-VSI-MIB", "hh3cVsiXconnectIfIndex"), (0, "HH3C-VSI-MIB", "hh3cVsiXconnectEvcSrvInstId"))
if mibBuilder.loadTexts: hh3cVsiXconnectEntry.setStatus('current')
hh3cVsiXconnectIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hh3cVsiXconnectIfIndex.setStatus('current')
hh3cVsiXconnectEvcSrvInstId = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: hh3cVsiXconnectEvcSrvInstId.setStatus('current')
hh3cVsiXconnectVsiName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVsiXconnectVsiName.setStatus('current')
hh3cVsiXconnectAccessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("vlan", 1), ("ethernet", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVsiXconnectAccessMode.setStatus('current')
hh3cVsiXconnectHubSpoke = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("hub", 2), ("spoke", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVsiXconnectHubSpoke.setStatus('current')
hh3cVsiXconnectRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 105, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cVsiXconnectRowStatus.setStatus('current')
mibBuilder.exportSymbols("HH3C-VSI-MIB", hh3cVsiMode=hh3cVsiMode, hh3cMinmIsid=hh3cMinmIsid, hh3cVsi=hh3cVsi, hh3cVsiXconnectAccessMode=hh3cVsiXconnectAccessMode, hh3cVsiXconnectRowStatus=hh3cVsiXconnectRowStatus, hh3cVsiXconnectHubSpoke=hh3cVsiXconnectHubSpoke, hh3cVsiEntry=hh3cVsiEntry, hh3cVsiObjects=hh3cVsiObjects, hh3cVsiNextAvailableVsiIndex=hh3cVsiNextAvailableVsiIndex, hh3cVsiTransMode=hh3cVsiTransMode, hh3cVsiXconnectVsiName=hh3cVsiXconnectVsiName, hh3cVsiAdminState=hh3cVsiAdminState, hh3cVsiIndex=hh3cVsiIndex, hh3cVsiScalarGroup=hh3cVsiScalarGroup, hh3cVsiId=hh3cVsiId, hh3cVsiRowStatus=hh3cVsiRowStatus, PYSNMP_MODULE_ID=hh3cVsi, hh3cVsiName=hh3cVsiName, hh3cVsiEnableHubSpoke=hh3cVsiEnableHubSpoke, hh3cVsiTable=hh3cVsiTable, hh3cVsiXconnectEntry=hh3cVsiXconnectEntry, hh3cVsiXconnectEvcSrvInstId=hh3cVsiXconnectEvcSrvInstId, hh3cVsiXconnectIfIndex=hh3cVsiXconnectIfIndex, hh3cVsiXconnectTable=hh3cVsiXconnectTable)
