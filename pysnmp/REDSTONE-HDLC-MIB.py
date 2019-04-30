#
# PySNMP MIB module REDSTONE-HDLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-HDLC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
RsNextIfIndex, = mibBuilder.importSymbols("REDSTONE-TC", "RsNextIfIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, MibIdentifier, ModuleIdentity, Gauge32, NotificationType, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, Unsigned32, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Gauge32", "NotificationType", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "Unsigned32", "IpAddress", "Counter64")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
rsHdlcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 9))
rsHdlcMIB.setRevisions(('1999-07-28 00:00', '1999-07-14 00:00', '1998-01-01 00:00',))
if mibBuilder.loadTexts: rsHdlcMIB.setLastUpdated('9907280000Z')
if mibBuilder.loadTexts: rsHdlcMIB.setOrganization('Redstone Communications, Inc.')
rsHdlcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 9, 1))
rsHdlcNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 1), RsNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsHdlcNextIfIndex.setStatus('current')
rsHdlcIfTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2), )
if mibBuilder.loadTexts: rsHdlcIfTable.setStatus('current')
rsHdlcIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1), ).setIndexNames((0, "REDSTONE-HDLC-MIB", "rsHdlcIfIndex"))
if mibBuilder.loadTexts: rsHdlcIfEntry.setStatus('current')
rsHdlcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rsHdlcIfIndex.setStatus('current')
rsHdlcIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsHdlcIfRowStatus.setStatus('current')
rsHdlcIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsHdlcIfLowerIfIndex.setStatus('current')
rsHdlcIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65533))).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsHdlcIfMtu.setStatus('current')
rsHdlcIfMru = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65533))).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsHdlcIfMru.setStatus('current')
rsHdlcIfCrcSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("crc16", 1), ("crc32", 2))).clone('crc16')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsHdlcIfCrcSize.setStatus('current')
rsHdlcIfDataPolarity = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 9, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("inverted", 1))).clone('normal')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsHdlcIfDataPolarity.setStatus('current')
rsHdlcConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 9, 4))
rsHdlcCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 9, 4, 1))
rsHdlcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 9, 4, 2))
rsHdlcCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 9, 4, 1, 1)).setObjects(("REDSTONE-HDLC-MIB", "rsHdlcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsHdlcCompliance = rsHdlcCompliance.setStatus('obsolete')
rsHdlcCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 9, 4, 1, 2)).setObjects(("REDSTONE-HDLC-MIB", "rsHdlcGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsHdlcCompliance2 = rsHdlcCompliance2.setStatus('current')
rsHdlcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 9, 4, 2, 1)).setObjects(("REDSTONE-HDLC-MIB", "rsHdlcNextIfIndex"), ("REDSTONE-HDLC-MIB", "rsHdlcIfRowStatus"), ("REDSTONE-HDLC-MIB", "rsHdlcIfLowerIfIndex"), ("REDSTONE-HDLC-MIB", "rsHdlcIfMtu"), ("REDSTONE-HDLC-MIB", "rsHdlcIfMru"), ("REDSTONE-HDLC-MIB", "rsHdlcIfCrcSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsHdlcGroup = rsHdlcGroup.setStatus('obsolete')
rsHdlcGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 9, 4, 2, 2)).setObjects(("REDSTONE-HDLC-MIB", "rsHdlcNextIfIndex"), ("REDSTONE-HDLC-MIB", "rsHdlcIfRowStatus"), ("REDSTONE-HDLC-MIB", "rsHdlcIfLowerIfIndex"), ("REDSTONE-HDLC-MIB", "rsHdlcIfMtu"), ("REDSTONE-HDLC-MIB", "rsHdlcIfMru"), ("REDSTONE-HDLC-MIB", "rsHdlcIfCrcSize"), ("REDSTONE-HDLC-MIB", "rsHdlcIfDataPolarity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsHdlcGroup2 = rsHdlcGroup2.setStatus('current')
mibBuilder.exportSymbols("REDSTONE-HDLC-MIB", rsHdlcIfEntry=rsHdlcIfEntry, rsHdlcIfMru=rsHdlcIfMru, PYSNMP_MODULE_ID=rsHdlcMIB, rsHdlcIfLowerIfIndex=rsHdlcIfLowerIfIndex, rsHdlcCompliance2=rsHdlcCompliance2, rsHdlcCompliances=rsHdlcCompliances, rsHdlcIfMtu=rsHdlcIfMtu, rsHdlcCompliance=rsHdlcCompliance, rsHdlcIfCrcSize=rsHdlcIfCrcSize, rsHdlcObjects=rsHdlcObjects, rsHdlcNextIfIndex=rsHdlcNextIfIndex, rsHdlcIfTable=rsHdlcIfTable, rsHdlcGroup=rsHdlcGroup, rsHdlcGroups=rsHdlcGroups, rsHdlcConformance=rsHdlcConformance, rsHdlcIfIndex=rsHdlcIfIndex, rsHdlcIfDataPolarity=rsHdlcIfDataPolarity, rsHdlcMIB=rsHdlcMIB, rsHdlcIfRowStatus=rsHdlcIfRowStatus, rsHdlcGroup2=rsHdlcGroup2)
