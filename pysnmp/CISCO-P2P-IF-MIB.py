#
# PySNMP MIB module CISCO-P2P-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-P2P-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:52:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, iso, MibIdentifier, ModuleIdentity, Counter64, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks, Integer32, IpAddress, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "MibIdentifier", "ModuleIdentity", "Counter64", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks", "Integer32", "IpAddress", "Gauge32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoP2PIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 668))
ciscoP2PIfMIB.setRevisions(('2008-08-12 00:00',))
if mibBuilder.loadTexts: ciscoP2PIfMIB.setLastUpdated('200808120000Z')
if mibBuilder.loadTexts: ciscoP2PIfMIB.setOrganization('Cisco Systems, Inc.')
ciscoP2PIfMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 0))
ciscoP2PIfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 1))
cp2pIfGeneralObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1))
class Cp2pIfCrcMode(TextualConvention, Integer32):
    reference = 'RFC-2615, PPP over SONET/SDH: Section 5. Configuration Details.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("crc16", 1), ("crc32", 2))

class Cp2pIfScramblingMode(TextualConvention, Integer32):
    reference = 'RFC-2615, PPP over SONET/SDH: Section 4. X**43 + 1 Scrambler Description.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

cp2pIfCfgTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1), )
if mibBuilder.loadTexts: cp2pIfCfgTable.setStatus('current')
cp2pIfCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cp2pIfCfgEntry.setStatus('current')
cp2pIfCfgCrcMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 1), Cp2pIfCrcMode().clone('crc32')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cp2pIfCfgCrcMode.setStatus('current')
cp2pIfCfgScramblingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 2), Cp2pIfScramblingMode().clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cp2pIfCfgScramblingMode.setStatus('current')
cp2pIfCfgTransmitDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 18000))).setUnits('microseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cp2pIfCfgTransmitDelay.setStatus('current')
cp2pIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2), )
if mibBuilder.loadTexts: cp2pIfStatsTable.setStatus('current')
cp2pIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2, 1), )
cp2pIfCfgEntry.registerAugmentions(("CISCO-P2P-IF-MIB", "cp2pIfStatsEntry"))
cp2pIfStatsEntry.setIndexNames(*cp2pIfCfgEntry.getIndexNames())
if mibBuilder.loadTexts: cp2pIfStatsEntry.setStatus('current')
cp2pIfStatsInCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 668, 1, 1, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cp2pIfStatsInCrcErrors.setStatus('current')
ciscoP2PIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 3))
ciscoP2PIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 1))
ciscoP2PIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 2))
ciscoP2PIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 1, 1)).setObjects(("CISCO-P2P-IF-MIB", "ciscoP2PIfMIBGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2PIfMIBCompliance = ciscoP2PIfMIBCompliance.setStatus('current')
ciscoP2PIfMIBGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 668, 3, 2, 1)).setObjects(("CISCO-P2P-IF-MIB", "cp2pIfCfgCrcMode"), ("CISCO-P2P-IF-MIB", "cp2pIfCfgScramblingMode"), ("CISCO-P2P-IF-MIB", "cp2pIfCfgTransmitDelay"), ("CISCO-P2P-IF-MIB", "cp2pIfStatsInCrcErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoP2PIfMIBGeneralGroup = ciscoP2PIfMIBGeneralGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-P2P-IF-MIB", cp2pIfStatsInCrcErrors=cp2pIfStatsInCrcErrors, cp2pIfCfgTable=cp2pIfCfgTable, cp2pIfStatsEntry=cp2pIfStatsEntry, ciscoP2PIfMIBCompliance=ciscoP2PIfMIBCompliance, cp2pIfCfgEntry=cp2pIfCfgEntry, cp2pIfStatsTable=cp2pIfStatsTable, ciscoP2PIfMIBNotifs=ciscoP2PIfMIBNotifs, ciscoP2PIfMIBConformance=ciscoP2PIfMIBConformance, Cp2pIfCrcMode=Cp2pIfCrcMode, PYSNMP_MODULE_ID=ciscoP2PIfMIB, ciscoP2PIfMIBGeneralGroup=ciscoP2PIfMIBGeneralGroup, cp2pIfGeneralObjects=cp2pIfGeneralObjects, ciscoP2PIfMIBObjects=ciscoP2PIfMIBObjects, cp2pIfCfgTransmitDelay=cp2pIfCfgTransmitDelay, cp2pIfCfgScramblingMode=cp2pIfCfgScramblingMode, cp2pIfCfgCrcMode=cp2pIfCfgCrcMode, ciscoP2PIfMIBGroups=ciscoP2PIfMIBGroups, ciscoP2PIfMIBCompliances=ciscoP2PIfMIBCompliances, ciscoP2PIfMIB=ciscoP2PIfMIB, Cp2pIfScramblingMode=Cp2pIfScramblingMode)
