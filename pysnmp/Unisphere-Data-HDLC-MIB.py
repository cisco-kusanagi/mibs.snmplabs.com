#
# PySNMP MIB module Unisphere-Data-HDLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-HDLC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:24:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, ObjectIdentity, MibIdentifier, Gauge32, TimeTicks, Integer32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "ObjectIdentity", "MibIdentifier", "Gauge32", "TimeTicks", "Integer32", "ModuleIdentity", "iso")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdNextIfIndex, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdNextIfIndex")
usdHdlcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9))
usdHdlcMIB.setRevisions(('2001-11-28 13:43', '2001-03-22 14:30', '2000-01-26 00:00', '1999-07-28 00:00', '1998-11-13 00:00',))
if mibBuilder.loadTexts: usdHdlcMIB.setLastUpdated('200111281343Z')
if mibBuilder.loadTexts: usdHdlcMIB.setOrganization('Unisphere Networks, Inc.')
usdHdlcObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1))
usdHdlcNextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 1), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdHdlcNextIfIndex.setStatus('current')
usdHdlcIfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2), )
if mibBuilder.loadTexts: usdHdlcIfTable.setStatus('current')
usdHdlcIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1), ).setIndexNames((0, "Unisphere-Data-HDLC-MIB", "usdHdlcIfIndex"))
if mibBuilder.loadTexts: usdHdlcIfEntry.setStatus('current')
usdHdlcIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdHdlcIfIndex.setStatus('current')
usdHdlcIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdHdlcIfRowStatus.setStatus('current')
usdHdlcIfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdHdlcIfLowerIfIndex.setStatus('current')
usdHdlcIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32763))).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdHdlcIfMtu.setStatus('current')
usdHdlcIfMru = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32763))).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdHdlcIfMru.setStatus('current')
usdHdlcIfCrcSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("crc16", 1), ("crc32", 2))).clone('crc16')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdHdlcIfCrcSize.setStatus('current')
usdHdlcIfDataPolarity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("inverted", 1))).clone('normal')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdHdlcIfDataPolarity.setStatus('current')
usdHdlcIfClockMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("hdlcClockUnsupported", 0), ("hdlcClockInternal", 1), ("hdlcClockLine", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdHdlcIfClockMode.setStatus('current')
usdHdlcIfClockRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("hdlcClockRateUnsupported", 0), ("hdlcClockRate34-368Mhz", 1), ("hdlcClockRate44-736Mhz", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdHdlcIfClockRate.setStatus('current')
usdHdlcIfForceDteAck = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("forceDteAckUnsupported", 0), ("forceDteAckNormal", 1), ("forceDteAckForced", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdHdlcIfForceDteAck.setStatus('current')
usdHdlcConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4))
usdHdlcCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1))
usdHdlcGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2))
usdHdlcCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 1)).setObjects(("Unisphere-Data-HDLC-MIB", "usdHdlcGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcCompliance = usdHdlcCompliance.setStatus('obsolete')
usdHdlcCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 2)).setObjects(("Unisphere-Data-HDLC-MIB", "usdHdlcGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcCompliance2 = usdHdlcCompliance2.setStatus('obsolete')
usdHdlcCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 1, 3)).setObjects(("Unisphere-Data-HDLC-MIB", "usdHdlcGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcCompliance3 = usdHdlcCompliance3.setStatus('current')
usdHdlcGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 1)).setObjects(("Unisphere-Data-HDLC-MIB", "usdHdlcNextIfIndex"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfRowStatus"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfLowerIfIndex"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfMtu"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfMru"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfCrcSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcGroup = usdHdlcGroup.setStatus('obsolete')
usdHdlcGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 2)).setObjects(("Unisphere-Data-HDLC-MIB", "usdHdlcNextIfIndex"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfRowStatus"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfLowerIfIndex"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfMtu"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfMru"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfCrcSize"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfDataPolarity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcGroup2 = usdHdlcGroup2.setStatus('obsolete')
usdHdlcGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 9, 4, 2, 3)).setObjects(("Unisphere-Data-HDLC-MIB", "usdHdlcNextIfIndex"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfRowStatus"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfLowerIfIndex"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfMtu"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfMru"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfCrcSize"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfDataPolarity"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfClockMode"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfClockRate"), ("Unisphere-Data-HDLC-MIB", "usdHdlcIfForceDteAck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdHdlcGroup3 = usdHdlcGroup3.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-HDLC-MIB", usdHdlcCompliance2=usdHdlcCompliance2, PYSNMP_MODULE_ID=usdHdlcMIB, usdHdlcGroup3=usdHdlcGroup3, usdHdlcIfDataPolarity=usdHdlcIfDataPolarity, usdHdlcIfClockMode=usdHdlcIfClockMode, usdHdlcIfMru=usdHdlcIfMru, usdHdlcCompliance3=usdHdlcCompliance3, usdHdlcIfClockRate=usdHdlcIfClockRate, usdHdlcGroup=usdHdlcGroup, usdHdlcIfTable=usdHdlcIfTable, usdHdlcIfIndex=usdHdlcIfIndex, usdHdlcIfForceDteAck=usdHdlcIfForceDteAck, usdHdlcIfCrcSize=usdHdlcIfCrcSize, usdHdlcCompliances=usdHdlcCompliances, usdHdlcNextIfIndex=usdHdlcNextIfIndex, usdHdlcIfMtu=usdHdlcIfMtu, usdHdlcIfLowerIfIndex=usdHdlcIfLowerIfIndex, usdHdlcConformance=usdHdlcConformance, usdHdlcMIB=usdHdlcMIB, usdHdlcCompliance=usdHdlcCompliance, usdHdlcIfEntry=usdHdlcIfEntry, usdHdlcGroup2=usdHdlcGroup2, usdHdlcIfRowStatus=usdHdlcIfRowStatus, usdHdlcObjects=usdHdlcObjects, usdHdlcGroups=usdHdlcGroups)
